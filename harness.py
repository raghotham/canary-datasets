#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "openai>=1.0.0",
#   "rich",
#   "pyyaml"
# ]
# ///

import datetime
import inspect
import json
import os
import sys
import yaml
from rich.pretty import pprint
from typing import Any, Dict, List, Literal, Type, Union, get_args, get_type_hints
import openai

class ToolExecutor:
    """Executes tool calls by mapping function names to registered functions."""
    
    def __init__(self, *functions):
        self._registered_tools = {}
        for func in functions:
            self.register(func.__name__, func)

    def register(self, name: str, func: callable):
        """Register a function with a name.
        
        Args:
            name: Name to register the function under
            func: The function to register
        """
        self._registered_tools[name] = func
    
    def execute(self, tool_calls: List) -> List[Dict]:
        """Execute a list of tool calls and return their responses.
        
        Args:
            tool_calls: List of tool call objects from responses API or chat completions API
            
        Returns:
            List of tool response dictionaries with results
        """
        tool_responses = []
        
        for tool_call in tool_calls:
            # Support both dict and Pydantic object for chat completions
            function_name = getattr(tool_call, 'name', None)
            if function_name is None and hasattr(tool_call, 'function'):
                function_name = getattr(tool_call.function, 'name', None)
            arguments = getattr(tool_call, 'arguments', None)
            if arguments is None and hasattr(tool_call, 'function'):
                arguments = getattr(tool_call.function, 'arguments', None)
            if isinstance(arguments, str):
                try:
                    arguments = json.loads(arguments)
                except Exception:
                    pass
            if function_name in self._registered_tools:
                try:
                    # Convert arguments to expected types
                    converted_args = self._convert_arguments(function_name, arguments)
                    result = self._registered_tools[function_name](**converted_args)
                    tool_responses.append({
                        "type": "function_call_output",
                        "call_id": getattr(tool_call, 'call_id', getattr(tool_call, 'id', None)),
                        "output": json.dumps(result)
                    })
                except Exception as e:
                    tool_responses.append({
                        "type": "function_call_output",
                        "call_id": getattr(tool_call, 'call_id', getattr(tool_call, 'id', None)),
                        "output": json.dumps(f"Error executing {function_name}: {str(e)}")
                    })
            else:
                tool_responses.append({
                    "type": "function_call_output",
                    "call_id": getattr(tool_call, 'call_id', getattr(tool_call, 'id', None)),
                    "output": json.dumps(f"Unknown function: {function_name}")
                })
                
        return tool_responses

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        """Generate OpenAI tool schema for the responses API."""
        tool_schemas = []
        for func in self._registered_tools.values():
            tool_schemas.append(self._generate_tool_schema(func, chat_format=False))
        return tool_schemas

    def get_chat_tool_schemas(self) -> List[Dict[str, Any]]:
        """Generate OpenAI tool schema for the chat completions API."""
        tool_schemas = []
        for func in self._registered_tools.values():
            tool_schemas.append(self._generate_tool_schema(func, chat_format=True))
        return tool_schemas

    def get_system_prompt(self) -> str:
        """Generate system prompt with tool definitions in JSON format."""
        tool_schemas = self.get_chat_tool_schemas()
        system_prompt = "You have access to the following tools:\n\n"
        for tool in tool_schemas:
            system_prompt += f"Tool: {tool['function']['name']}\n"
            system_prompt += f"Description: {tool['function']['description']}\n"
            system_prompt += f"Parameters: {json.dumps(tool['function']['parameters'], indent=2)}\n\n"
        system_prompt += "Use these tools when needed to answer user questions. Do not use tools if you don't have to. When using tools, make sure to specify them as json with the format: {\"name\": \"tool_name\", \"arguments\": {\"arg_name\": \"arg_value\"}}"
        return system_prompt

    def _generate_tool_schema(self, func, chat_format=False) -> Dict[str, Any]:
        """Generate OpenAI tool schema from a Python function's type hints and docstring."""
        hints = get_type_hints(func)
        sig = inspect.signature(func)
        doc = inspect.getdoc(func)
        
        # Parse docstring to get parameter descriptions
        param_desc = {}
        if doc:
            for line in doc.split('\n'):
                if ':' in line and 'Args:' in doc:
                    param = line.split(':')[0].strip()
                    desc = line.split(':')[1].strip()
                    param_desc[param] = desc

        # Build parameters object
        properties = {}
        required = []
        
        for param_name, param in sig.parameters.items():
            param_type = hints[param_name]
            
            # Handle Literal types
            if hasattr(param_type, "__origin__") and param_type.__origin__ is Literal:
                properties[param_name] = {
                    "type": "string",
                    "enum": list(get_args(param_type)),
                    "description": param_desc.get(param_name, "")
                }
            # Handle basic types
            else:
                type_map = {str: "string", int: "number", float: "number", bool: "boolean"}
                properties[param_name] = {
                    "type": type_map.get(param_type, "string"),
                    "description": param_desc.get(param_name, "")
                }
            
            # Check if parameter is required
            if param.default == inspect.Parameter.empty:
                required.append(param_name)
            elif param.default is not None:
                properties[param_name]["default"] = param.default

        if chat_format:
            return {
                "type": "function",
                "function": {
                    "name": func.__name__,
                    "description": doc.split('\n')[0] if doc else "",
                    "parameters": {
                        "type": "object",
                        "properties": properties,
                        "required": required
                    }
                }
            }
        else:
            return {
                "type": "function",
                "name": func.__name__,
                "description": doc.split('\n')[0] if doc else "",
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required
                }
            }

    
    def _convert_arguments(self, function_name: str, arguments: Dict) -> Dict:
        """Convert arguments to the expected types based on function type hints."""
        func = self._registered_tools[function_name]
        type_hints = get_type_hints(func)
        converted_args = {}
        
        for param_name, value in arguments.items():
            if param_name in type_hints:
                expected_type = type_hints[param_name]
                try:
                    converted_args[param_name] = self._convert_value(value, expected_type)
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Failed to convert parameter '{param_name}' with value '{value}' to type {expected_type}: {e}")
            else:
                # If no type hint, use the value as-is
                converted_args[param_name] = value
        
        return converted_args
    
    def _convert_value(self, value: Any, target_type: Type) -> Any:
        """Convert a value to the target type."""
        # Handle None values
        if value is None:
            return None
        
        # Handle Union types (e.g., Union[str, int])
        if hasattr(target_type, "__origin__") and target_type.__origin__ is Union:
            # Try each type in the union
            for union_type in get_args(target_type):
                if union_type is type(None):  # Skip NoneType
                    continue
                try:
                    return self._convert_value(value, union_type)
                except (ValueError, TypeError):
                    continue
            raise ValueError(f"Cannot convert '{value}' to any type in {target_type}")
        
        # Handle Literal types
        if hasattr(target_type, "__origin__") and target_type.__origin__ is Literal:
            if value in get_args(target_type):
                return value
            else:
                raise ValueError(f"Value '{value}' not in allowed values {get_args(target_type)}")
        
        # Handle basic types
        if target_type == str:
            return str(value)
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == bool:
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)
        elif target_type == list:
            if isinstance(value, str):
                # Try to parse as JSON if it's a string
                try:
                    return json.loads(value)
                except json.JSONDecodeError:
                    # If not JSON, split by comma
                    return [item.strip() for item in value.split(',')]
            return list(value)
        elif target_type == dict:
            if isinstance(value, str):
                try:
                    return json.loads(value)
                except json.JSONDecodeError:
                    raise ValueError(f"Cannot convert string '{value}' to dict")
            return dict(value)
        
        # For other types, try to construct them directly
        try:
            return target_type(value)
        except (ValueError, TypeError):
            raise ValueError(f"Cannot convert '{value}' to {target_type}")

def log_turn(sample_id, turn_id, user_message, tool_calls, tool_outputs, assistant_message, messages=[], model_name=None, log_filename=None):
    """Log a complete turn with all its data."""
    # Convert messages to serializable format
    serializable_messages = []
    for msg in messages:
        if hasattr(msg, 'model_dump'):  # Pydantic model
            serializable_messages.append(msg.model_dump())
        elif isinstance(msg, dict):
            serializable_messages.append(msg)
        else:
            # Convert to dict manually
            serializable_messages.append({
                'role': getattr(msg, 'role', None),
                'content': getattr(msg, 'content', None),
                'tool_calls': [tc.model_dump() if hasattr(tc, 'model_dump') else tc for tc in getattr(msg, 'tool_calls', [])] if getattr(msg, 'tool_calls', None) else None,
                'tool_call_id': getattr(msg, 'tool_call_id', None)
            })
    
    # Create turn entry
    turn_entry = {
        "sample_id": sample_id,
        "turn_id": turn_id,
        "messages": serializable_messages,
        "user_message": user_message,
        "tool_calls": tool_calls,
        "tool_outputs": tool_outputs,
        "assistant_message": assistant_message
    }

    pprint(turn_entry)

    with open(log_filename, 'a') as f:
        f.write(json.dumps(turn_entry) + '\n')



def execute_turn(client, model, executor, previous_id, user_message, sample_id, turn_id):
    inputs = [{
        "type": "message",
        "role": "user", 
        "content": [{"type": "input_text", "text": user_message}]
    }]
    
    all_tool_calls = []
    all_tool_outputs = []
    
    while True:
        # Only include previous_response_id if it's not None
        request_params = {
            "model": model,
            "input": inputs,
            "tools": executor.get_tool_schemas(),
            "stream": False
        }
        if previous_id is not None:
            request_params["previous_response_id"] = previous_id
            
        resp = client.responses.create(**request_params)
        #pprint(resp)

        # If model gives text, output and finish
        if all(item.type != "function_call" for item in resp.output):
            # Handle different output types
            for item in resp.output:
                if hasattr(item, 'content'):  # Regular message
                    content_blocks = item.content
                    text = next(block.text for block in content_blocks if block.type == "output_text")
                    return text, resp.id, all_tool_calls, all_tool_outputs
                elif hasattr(item, 'text'):  # Reasoning item
                    return item.text, resp.id, all_tool_calls, all_tool_outputs
                elif hasattr(item, 'output_text'):  # Direct text output
                    return item.output_text, resp.id, all_tool_calls, all_tool_outputs
            
            # Fallback: try to get any text from the response
            for item in resp.output:
                if hasattr(item, 'text'):
                    return item.text, resp.id, all_tool_calls, all_tool_outputs
            
            return "No text response found", resp.id, all_tool_calls, all_tool_outputs

        # Otherwise run tools, feed outputs back
        tool_calls = [item for item in resp.output if item.type == "function_call"]
        for tool_call in tool_calls:
            all_tool_calls.append({
                "call_id": tool_call.call_id,
                "name": tool_call.name,
                "arguments": tool_call.arguments
            })
        tool_outputs = executor.execute(tool_calls)
        for tool_output in tool_outputs:
            all_tool_outputs.append({
                "call_id": tool_output['call_id'],
                "output": tool_output['output']
            })
        previous_id = resp.id
        inputs = inputs + tool_outputs

def assistant_conversation(client, model, executor, user_messages, sample_id, log_filename):
    previous_id = None
    for turn_id, user_message in enumerate(user_messages, 1):
        response, previous_id, tool_calls, tool_outputs = execute_turn(client, model, executor, previous_id, user_message, sample_id, turn_id)
        log_turn(sample_id, turn_id, user_message, tool_calls, tool_outputs, response, [], model, log_filename)

def execute_chat_turn(client, model, executor, messages, user_message, use_system_prompt):
    # Add new user message to conversation
    messages.append({"role": "user", "content": user_message})
    
    all_tool_calls = []
    all_tool_outputs = []
    
    while True:
        # Prepare request parameters
        request_params = {
            "model": model,
            "messages": messages,
            "stream": False
        }
        
        if use_system_prompt:
            # Add system prompt with tool schemas instead of tools parameter
            system_prompt = executor.get_system_prompt()
            
            # Add system message at the beginning if not already present
            if not messages or messages[0]["role"] != "system":
                messages.insert(0, {"role": "system", "content": system_prompt})
        else:
            # Use tools parameter as before
            request_params["tools"] = executor.get_chat_tool_schemas()
        
        # Make chat completion request
        #pprint(request_params)
        resp = client.chat.completions.create(**request_params)
        #pprint(resp)
        assistant_message = resp.choices[0].message
        messages.append(assistant_message)

        # If no tool calls, return the response
        if not assistant_message.tool_calls:
            return assistant_message.content, messages, all_tool_calls, all_tool_outputs

        # Handle tool calls
        tool_calls = assistant_message.tool_calls
        for tool_call in tool_calls:
            all_tool_calls.append({
                "call_id": tool_call.id,
                "name": tool_call.function.name,
                "arguments": tool_call.function.arguments
            })
            
        tool_outputs = executor.execute(tool_calls)
        for tool_output in tool_outputs:
            all_tool_outputs.append({
                "call_id": tool_output['call_id'],
                "output": tool_output['output']
            })
            messages.append({
                "role": "tool",
                "tool_call_id": tool_output['call_id'],
                "content": str(tool_output['output'])
            })

def assistant_chat_conversation(client, model, executor, user_messages, sample_id, use_system_prompt, log_filename):
    messages = []  # Track full conversation history
    for turn_id, user_message in enumerate(user_messages, 1):
        response, messages, tool_calls, tool_outputs = execute_chat_turn(
            client, model, executor, messages, user_message, use_system_prompt
        )   
        log_turn(sample_id, turn_id, user_message, tool_calls, tool_outputs, response, messages, model, log_filename)

def load_conversations_from_yaml(filename):
    """Load conversation samples from YAML file."""
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data['conversations']


def get_weather(
    location: str
) -> Dict[str, Union[str, float, list]]:
    """Get the current weather conditions for a location.
    
    Args:
        location: The city name to get weather for (e.g. 'London', 'New York')
        
    Returns:
        Dict containing:
            - location: City name
            - temperature: Current temperature in Fahrenheit
            - conditions: List of current weather conditions
    """

    sample = {
        "Boston": 72,
        "Tokyo":  88,
        "Paris":  75,
    }
    if location not in sample:
        raise ValueError(f"Location not supported: {location}")
    
    return {
        "location": location,
        "temperature": sample.get(location),
        "forecast": ["sunny", "windy"],
    }

def convert_units(
    value: float,
    from_unit: Literal["celsius", "fahrenheit"],
    to_unit: Literal["celsius", "fahrenheit"]
) -> Dict[str, Union[float, str]]:
    """Convert a temperature value between Celsius and Fahrenheit.
    
    Args:
        value: The temperature value to convert
        from_unit: The unit to convert from ('celsius' or 'fahrenheit')
        to_unit: The unit to convert to ('celsius' or 'fahrenheit')
        
    Returns:
        Dict containing:
            - value: Converted temperature value
            - unit: Unit of the converted temperature
    """
    if from_unit == to_unit:
        return {"value": value, "unit": to_unit}
    if (from_unit, to_unit) == ("fahrenheit", "celsius"):
        return {"value": (value - 32) * 5 / 9, "unit": "celsius"}
    if (from_unit, to_unit) == ("celsius", "fahrenheit"):
        return {"value": value * 9 / 5 + 32, "unit": "fahrenheit"}
    raise ValueError("unsupported units")

def convert_currency(amount: float, from_currency: str, to_currency: str) -> Dict[str, Union[float, str]]:
    """Convert an amount from one currency to another.
    
    Args:
        amount: The amount of money to convert
        from_currency: The currency code to convert from (e.g., USD, EUR, GBP)
        to_currency: The currency code to convert to (e.g., USD, EUR, GBP)
    """
    # Dictionary of exchange rates (relative to USD)
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.93,
        "GBP": 0.79,
        "JPY": 153.2,
        "CAD": 1.37,
        "AUD": 1.52
    }
    # Normalize currency codes to uppercase
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
  
    # Check if currencies are supported
    if from_currency not in exchange_rates:
        raise ValueError(f"Currency not supported: {from_currency}")
    if to_currency not in exchange_rates:
        raise ValueError(f"Currency not supported: {to_currency}")
  
    # Convert to USD first, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
  
    return {
       "original_amount": amount,
       "from_currency": from_currency,
       "to_currency": to_currency,
       "converted_amount": round(converted_amount, 2)
    }

executor = ToolExecutor(get_weather, convert_currency, convert_units)

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL", "https://api.openai.com/v1")
client = openai.OpenAI(api_key=api_key, base_url=base_url)

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python responses-tools.py <conversations.yaml> <model_name> [--use-system-prompt]")
    sys.exit(1)

conversations_file = sys.argv[1]
model = sys.argv[2]
use_system_prompt = "--use-system-prompt" in sys.argv

print(f"Loading conversations from {conversations_file}")
conversations = load_conversations_from_yaml(conversations_file)

# Write directly to conversation log file with model name
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
log_filename = f"conversation_logs_{model}_{timestamp}.jsonl"

# sample_id = 0
# for conversation in conversations:
#     sample_id += 1
#     print(f"\n=== Running conversation: {conversation['name']} (sample_id={sample_id}) ===\n")
#     assistant_conversation(client, model, executor, conversation['messages'], sample_id)

sample_id = 0
for conversation in conversations:
    sample_id += 1
    print(f"\n=== Running conversation: {conversation['name']} (sample_id={sample_id}) ===\n")
    assistant_chat_conversation(client, model, executor, conversation['messages'], sample_id, use_system_prompt, log_filename)