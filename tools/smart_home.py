from typing import Dict, List, Union, Any
# Smart Home Tools
# Auto-generated implementations from cached categorization

from typing import Dict, Literal, Union


def check_cameras(
    camera: Literal["front_door", "backyard", "driveway", "all"],
    view_type: Literal["live", "recordings"] = "live"
) -> Dict[str, Union[str, List[str]]]:
    """View live feed or recordings from security cameras.

    Args:
        camera: Camera location ('front_door', 'backyard', 'driveway', or 'all')
        view_type: Type of view ('live' or 'recordings')

    Returns:
        Dict containing:
            - camera: Camera location
            - view_type: Type of view
            - feeds: List of feed URLs or recording file names
    """
    feeds_sample = {
        "front_door": {
            "live": ["http://camera-feed/front_door/live"],
            "recordings": ["front_door_20231001.mp4", "front_door_20231002.mp4"]
        },
        "backyard": {
            "live": ["http://camera-feed/backyard/live"],
            "recordings": ["backyard_20231001.mp4", "backyard_20231002.mp4"]
        },
        "driveway": {
            "live": ["http://camera-feed/driveway/live"],
            "recordings": ["driveway_20231001.mp4", "driveway_20231002.mp4"]
        }
    }

    if camera == "all":
        feeds = []
        for cam in feeds_sample:
            feeds.extend(feeds_sample[cam][view_type])
    elif camera in feeds_sample:
        feeds = feeds_sample[camera][view_type]
    else:
        raise ValueError(f"Camera location not supported: {camera}")

    return {
        "camera": camera,
        "view_type": view_type,
        "feeds": feeds
    }

from typing import Dict, Literal, Union


def control_lights(
    light: str,
    action: Literal["on", "off", "toggle"],
    brightness: Union[int, None] = None
) -> Dict[str, Union[str, int, bool]]:
    """Control the lights in or around the home.

    Args:
        light: The ID or description of the light or group of lights (e.g., 'living room', 'porch').
        action: The action to perform ('on', 'off', or 'toggle').
        brightness: Optional brightness level (0-100) if turning on.

    Returns:
        Dict containing:
            - light: The ID or description of the light
            - action: The action performed
            - status: The new status of the light ('on' or 'off')
            - brightness: The brightness level if applicable
    """
    if action not in ["on", "off", "toggle"]:
        raise ValueError(f"Unsupported action: {action}")

    if action == "on" and brightness is not None and not (0 <= brightness <= 100):
        raise ValueError("Brightness must be between 0 and 100")

    # Simulate current state of the light
    current_state = {
        "living room": {"status": "off", "brightness": 0},
        "porch": {"status": "on", "brightness": 75},
    }

    if light not in current_state:
        raise ValueError(f"Light not found: {light}")

    current_status = current_state[light]["status"]
    current_brightness = current_state[light]["brightness"]

    if action == "toggle":
        new_status = "off" if current_status == "on" else "on"
    else:
        new_status = action

    new_brightness = brightness if new_status == "on" and brightness is not None else current_brightness

    return {
        "light": light,
        "action": action,
        "status": new_status,
        "brightness": new_brightness if new_status == "on" else 0,
    }

from typing import Dict, Literal


def lock_doors(
    door: Literal["front", "back", "garage", "all"],
    action: Literal["lock", "unlock"]
) -> Dict[str, str]:
    """Lock or unlock specific doors in the home.

    Args:
        door: Door identifier ('front', 'back', 'garage', or 'all')
        action: Lock action ('lock' or 'unlock')

    Returns:
        Dict containing:
            - door: The door identifier
            - status: The new status of the door ('locked' or 'unlocked')
    """
    valid_doors = ["front", "back", "garage", "all"]
    if door not in valid_doors:
        raise ValueError(f"Invalid door specified: {door}")

    if action not in ["lock", "unlock"]:
        raise ValueError(f"Invalid action specified: {action}")

    status = "locked" if action == "lock" else "unlocked"

    # Simulate the action on all doors if 'all' is specified
    if door == "all":
        return {d: status for d in valid_doors if d != "all"}

    return {door: status}

from typing import Dict, Literal, Union
import time


def set_security_alarm(
    mode: Literal["arm_home", "arm_away", "disarm"],
    delay: int = 30
) -> Dict[str, Union[str, int]]:
    """Arm or disarm the home security system.

    Args:
        mode: Security mode to set ('arm_home', 'arm_away', or 'disarm')
        delay: Delay in seconds before activation (default is 30 seconds)

    Returns:
        Dict containing:
            - status: Confirmation message of the action taken
            - mode: The mode the system is set to
            - delay: The delay before the mode is activated
    """
    if mode not in {"arm_home", "arm_away", "disarm"}:
        raise ValueError(f"Unsupported mode: {mode}")

    # Simulate delay
    time.sleep(delay)

    status_messages = {
        "arm_home": "Security system armed in home mode.",
        "arm_away": "Security system armed in away mode.",
        "disarm": "Security system disarmed."
    }

    return {
        "status": status_messages[mode],
        "mode": mode,
        "delay": delay
    }

from typing import Dict


def change_light_color(light_name: str, color: str) -> Dict[str, str]:
    """Change the color of a smart light.

    Args:
        light_name: Name of the light.
        color: New color (e.g., 'blue', 'warm white').

    Returns:
        Dict containing:
            - light_name: Name of the light
            - color: New color of the light
            - status: Status message indicating success or failure
    """
    supported_lights = {"Living Room Light", "Bedroom Light", "Kitchen Light"}
    supported_colors = {"red", "green", "blue", "warm white", "cool white"}

    if light_name not in supported_lights:
        raise ValueError(f"Light not supported: {light_name}")

    if color not in supported_colors:
        raise ValueError(f"Color not supported: {color}")

    # Simulate changing the light color
    return {
        "light_name": light_name,
        "color": color,
        "status": f"The color of '{light_name}' has been changed to '{color}'."
    }

from typing import Dict


def lock_door(door_name: str) -> Dict[str, str]:
    """Lock a specified smart door.

    Args:
        door_name: Name of the door to lock.

    Returns:
        Dict containing:
            - door_name: Name of the door
            - status: Lock status of the door
    """
    sample_doors = {
        "Front Door": "locked",
        "Back Door": "unlocked",
        "Garage Door": "locked",
    }

    if door_name not in sample_doors:
        raise ValueError(f"Door not found: {door_name}")

    # Simulate locking the door
    sample_doors[door_name] = "locked"

    return {
        "door_name": door_name,
        "status": sample_doors[door_name],
    }

def set_thermostat(temperature: float) -> Dict[str, Union[float, str]]:
    """Adjust the thermostat to a desired temperature.

    Args:
        temperature: Target temperature in Celsius.

    Returns:
        Dict containing:
            - status: Status message indicating success or failure
            - set_temperature: The temperature that was set
    """
    if not (10 <= temperature <= 30):
        raise ValueError("Temperature must be between 10 and 30 Celsius.")

    # Simulate setting the thermostat
    success = True  # Assume the operation is successful

    if success:
        return {
            "status": "Thermostat set successfully",
            "set_temperature": temperature,
        }
    else:
        return {
            "status": "Failed to set thermostat",
            "set_temperature": None,
        }

from typing import Dict


def turn_on_device(device_name: str) -> Dict[str, str]:
    """Turn on a specific smart home device.

    Args:
        device_name: The name of the device to turn on.

    Returns:
        Dict containing:
            - device_name: The name of the device
            - status: The status of the device after the operation
    """
    
    supported_devices = {
        "Living Room Light": "off",
        "Kitchen Light": "off",
        "Thermostat": "off",
        "Smart TV": "off",
    }

    if device_name not in supported_devices:
        raise ValueError(f"Device not supported: {device_name}")

    # Simulate turning on the device
    supported_devices[device_name] = "on"

    return {
        "device_name": device_name,
        "status": supported_devices[device_name],
    }

from typing import Dict, Literal, Union


def adjust_thermostat(
    temperature: float, mode: Literal["heat", "cool", "auto", "off"] = "auto"
) -> Dict[str, Union[float, str]]:
    """Change the temperature setting on the home thermostat.

    Args:
        temperature: Target temperature in Celsius
        mode: Heating/cooling mode: 'heat', 'cool', 'auto', or 'off'

    Returns:
        Dict containing:
            - temperature: Set temperature in Celsius
            - mode: Current mode of the thermostat
            - status: Confirmation message of the adjustment
    """
    if not (10 <= temperature <= 30):
        raise ValueError("Temperature must be between 10 and 30 Celsius.")

    if mode not in {"heat", "cool", "auto", "off"}:
        raise ValueError("Mode must be one of 'heat', 'cool', 'auto', or 'off'.")

    # Simulate thermostat adjustment
    status_message = f"Thermostat set to {temperature}°C in {mode} mode."

    return {
        "temperature": temperature,
        "mode": mode,
        "status": status_message,
    }

from typing import Dict, Literal


def control_door_lock(
    door: str, action: Literal["lock", "unlock"]
) -> Dict[str, str]:
    """Locks or unlocks a door in the home.

    Args:
        door: The ID or description of the door or doors (e.g., 'front door', 'garage door', 'all doors').
        action: The action to perform ('lock' or 'unlock').

    Returns:
        Dict containing:
            - door: The door that was acted upon
            - status: The new status of the door ('locked' or 'unlocked')
    """
    valid_doors = ["front door", "garage door", "back door", "all doors"]
    if door not in valid_doors:
        raise ValueError(f"Door not recognized: {door}")

    if action not in ["lock", "unlock"]:
        raise ValueError(f"Invalid action: {action}")

    # Simulate door action
    status = "locked" if action == "lock" else "unlocked"

    return {
        "door": door,
        "status": status,
    }

from typing import Dict, Optional


def device_activation(dev: str, ins: Optional[str] = None) -> Dict[str, str]:
    """Activates a device in a smart home network with a possible command.

    Args:
        dev: A name or description of the device which we want to use. Does not have to be exact.
        ins: An instruction, command, or request for the device. Does not have to be exact.

    Returns:
        Dict containing:
            - device: The name of the device
            - status: Activation status of the device
            - command: The command executed on the device
    """
    # Mock device database
    devices = {
        "light": "Living Room Light",
        "thermostat": "Main Thermostat",
        "speaker": "Kitchen Speaker",
    }

    # Find the closest matching device
    device_name = devices.get(dev.lower())
    if not device_name:
        raise ValueError(f"Device not found: {dev}")

    # Mock command execution
    if ins:
        command = f"Executing '{ins}' on {device_name}"
    else:
        command = f"Activating {device_name} with default settings"

    return {
        "device": device_name,
        "status": "activated",
        "command": command,
    }

from typing import Dict, Literal


def estimate_washing_cycle_length(
    cycle: Literal["normal", "delicates", "quick", "heavy-duty", "bedding", "rinse"],
    load_size: int
) -> Dict[str, Union[int, str]]:
    """Estimate the length of a washing cycle based on cycle type and load size.

    Args:
        cycle: The cycle type to use ('normal', 'delicates', 'quick', 'heavy-duty', 'bedding', 'rinse').
        load_size: The approximate load size in kg (rounded up).

    Returns:
        Dict containing:
            - cycle: The cycle type used
            - load_size: The load size in kg
            - estimated_time: Estimated cycle time in minutes
    """
    if load_size <= 0:
        raise ValueError("Load size must be a positive integer")

    base_times = {
        "normal": 60,
        "delicates": 45,
        "quick": 30,
        "heavy-duty": 90,
        "bedding": 75,
        "rinse": 20,
    }

    if cycle not in base_times:
        raise ValueError(f"Unsupported cycle type: {cycle}")

    # Simulate a simple load size impact on time
    estimated_time = base_times[cycle] + (load_size - 1) * 5

    return {
        "cycle": cycle,
        "load_size": load_size,
        "estimated_time": estimated_time,
    }

from typing import Dict, List, Literal, Optional, Union
import hashlib


def get_camera_summary(
    time_range: str = "last 24 hours",
    priority_level: Optional[Literal["high", "medium", "low"]] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Retrieves a summary of recent events detected on the home security camera feeds.

    Args:
        time_range: The time range for filtering events (e.g., 'last 24 hours', 'last week').
        priority_level: Filters events by priority ('high', 'medium', 'low').

    Returns:
        Dict containing:
            - time_range: The time range for the events
            - events: List of events with details such as timestamp, description, and priority
    """
    
    # Sample event data based on time_range and priority_level
    sample_events = [
        {"timestamp": "2023-10-01T14:23:00", "description": "Motion detected in the backyard", "priority": "high"},
        {"timestamp": "2023-10-01T15:45:00", "description": "Person detected at the front door", "priority": "medium"},
        {"timestamp": "2023-10-01T16:00:00", "description": "Package delivered", "priority": "low"},
    ]

    # Filter events based on priority_level if provided
    if priority_level:
        sample_events = [event for event in sample_events if event["priority"] == priority_level]

    # Generate a hash to simulate varied but consistent sample data
    hash_input = f"{time_range}-{priority_level}".encode()
    hash_value = hashlib.sha256(hash_input).hexdigest()
    num_events = int(hash_value, 16) % len(sample_events) + 1

    return {
        "time_range": time_range,
        "events": sample_events[:num_events],
    }

from typing import Dict, Optional


def register_device(id: int, use_case: Optional[str] = None) -> Dict[str, Union[int, str]]:
    """Register a device with a smart home network.

    Args:
        id: An identification number for a device such as a MAC address or IMEI for use in registration.
        use_case: The function or use of the device. What the device is responsible for.

    Returns:
        Dict containing:
            - id: The identification number of the registered device
            - status: Registration status message
            - use_case: The function or use of the device if provided
    """
    if id <= 0:
        raise ValueError("Device ID must be a positive integer.")

    # Simulate a registration process with a hash-based status generation
    status = "registered" if hash(id) % 2 == 0 else "pending"

    result = {
        "id": id,
        "status": status,
    }

    if use_case:
        result["use_case"] = use_case

    return result

from typing import Dict


def remote_authentication(log_in_id: str, secret: str) -> Dict[str, str]:
    """Authenticate access to a smart home network when away from home.

    Args:
        log_in_id: The username or login id used for the smart home network.
        secret: The password for the userid which will be validated.

    Returns:
        Dict containing:
            - status: Authentication status ('success' or 'failure')
            - message: Detailed message about the authentication result
    """
    # Mock user database
    user_db = {
        "user123": "password123",
        "john_doe": "securePass!",
        "alice": "aliceSecret"
    }

    if log_in_id not in user_db:
        return {
            "status": "failure",
            "message": "Login ID not found."
        }

    if user_db[log_in_id] == secret:
        return {
            "status": "success",
            "message": "Authentication successful. Access granted."
        }
    else:
        return {
            "status": "failure",
            "message": "Incorrect password. Access denied."
        }

from typing import Dict


def remove_device(id: int) -> Dict[str, str]:
    """Remove a device from a smart home network.

    Args:
        id: An identification number for a device such as a MAC address or IMEI for use in registration.

    Returns:
        Dict containing:
            - status: Result of the removal operation ('success' or 'failure')
            - message: Additional information about the operation
    """
    # Simulated device database
    devices = {
        101: "Thermostat",
        202: "Smart Light",
        303: "Security Camera",
    }

    if id not in devices:
        return {
            "status": "failure",
            "message": f"Device with ID {id} not found in the network.",
        }

    # Simulate removal operation
    removed_device = devices.pop(id)
    return {
        "status": "success",
        "message": f"Device '{removed_device}' with ID {id} has been removed from the network.",
    }

from typing import Dict, Literal


def set_security_mode(mode: Literal["away", "home", "night", "off"]) -> Dict[str, str]:
    """Change the overall security mode of the home.

    Args:
        mode: The security mode to activate ('away', 'home', 'night', 'off')

    Returns:
        Dict containing:
            - mode: The activated security mode
            - status: Confirmation message of the mode change
    """
    valid_modes = {"away", "home", "night", "off"}
    if mode not in valid_modes:
        raise ValueError(f"Invalid mode: {mode}. Valid modes are: {valid_modes}")

    # Simulate setting the security mode
    return {
        "mode": mode,
        "status": f"Security mode set to '{mode}' successfully."
    }

from typing import Dict


def shutdown_network(save_states: bool = True) -> Dict[str, str]:
    """Instruct the smart home network to turn off all devices and deactivate itself.

    Args:
        save_states: A flag indicating whether the smart home network should save state data for the devices to resume tasks.

    Returns:
        Dict containing:
            - status: The status of the shutdown process
            - message: A message detailing the shutdown operation
    """
    
    # Simulate the process of shutting down devices
    devices = ["lights", "thermostat", "security_system", "entertainment_system"]
    shutdown_log = []

    for device in devices:
        if save_states:
            shutdown_log.append(f"{device} state saved and turned off.")
        else:
            shutdown_log.append(f"{device} turned off without saving state.")

    # Simulate network deactivation
    network_status = "deactivated"
    shutdown_log.append("Network deactivated.")

    return {
        "status": network_status,
        "message": " | ".join(shutdown_log)
    }

from typing import Dict, Literal, Optional, Union


def start_washing_cycle(
    cycle: Literal["normal", "delicates", "quick", "heavy-duty", "bedding", "rinse"],
    temperature: Literal["cold", "warm", "hot"] = "warm",
    delay: Optional[int] = None,
) -> Dict[str, Union[str, int]]:
    """Remotely start the washing cycle with specified settings.

    Args:
        cycle: The cycle type to use ('normal', 'delicates', 'quick', 'heavy-duty', 'bedding', 'rinse').
        temperature: Water temperature for the cycle ('cold', 'warm', 'hot'). Defaults to 'warm'.
        delay: Delay for the start in hours. Max 12. Defaults to None.

    Returns:
        Dict containing:
            - status: Status of the washing machine start command
            - cycle: The cycle type used
            - temperature: The water temperature used
            - delay: The delay in hours before starting

    Raises:
        ValueError: If delay is not between 0 and 12 inclusive.
    """
    if delay is not None and (delay < 0 or delay > 12):
        raise ValueError("Delay must be between 0 and 12 hours.")

    # Simulate starting the washing cycle
    status = "started" if delay is None else f"scheduled in {delay} hours"

    return {
        "status": status,
        "cycle": cycle,
        "temperature": temperature,
        "delay": delay if delay is not None else 0,
    }

from typing import Dict, Union


def washing_cycle_status() -> Dict[str, Union[str, int]]:
    """Get the current status of the washing cycle.

    Returns:
        Dict containing:
            - status: Current status of the washing cycle (e.g., 'washing', 'rinsing', 'spinning', 'completed')
            - time_remaining: Estimated time remaining in minutes
    """

    # Simulated washing cycle data
    cycle_stages = ["washing", "rinsing", "spinning", "completed"]
    time_remaining_samples = {
        "washing": 25,
        "rinsing": 15,
        "spinning": 5,
        "completed": 0,
    }

    # Simulate a hash-based cycle stage selection
    import hashlib
    import time

    # Use current time to simulate different stages
    current_time = int(time.time())
    stage_index = current_time % len(cycle_stages)
    current_stage = cycle_stages[stage_index]

    return {
        "status": current_stage,
        "time_remaining": time_remaining_samples[current_stage],
    }

from typing import Dict, Literal


def brew_coffee(
    strength: Literal["light", "medium", "strong"] = "medium",
    cups: int = 1
) -> Dict[str, str]:
    """Start brewing coffee with specific settings.

    Args:
        strength: Coffee strength: 'light', 'medium', or 'strong'.
        cups: Number of cups to brew.

    Returns:
        Dict containing:
            - message: Confirmation message of the brewing process
            - strength: The strength of the coffee being brewed
            - cups: Number of cups being brewed
    """
    if cups < 1:
        raise ValueError("Number of cups must be at least 1")

    strength_options = {"light", "medium", "strong"}
    if strength not in strength_options:
        raise ValueError(f"Invalid strength option: {strength}")

    return {
        "message": f"Brewing {cups} cup(s) of {strength} coffee.",
        "strength": strength,
        "cups": str(cups),
    }

from typing import Dict, List, Literal, Union
from datetime import datetime


def diagnose_issue(
    appliance_type: str,
    symptoms: List[str],
    urgency: Literal["low", "normal", "emergency"] = "normal",
    home_age_years: Union[int, None] = None,
    last_service_date: Union[str, None] = None,
) -> Dict[str, Union[str, List[str]]]:
    """Triage a home maintenance problem from symptoms to suggest likely causes and recommended next steps.

    Args:
        appliance_type: Appliance or system, e.g., 'HVAC', 'water_heater', 'dishwasher', 'electrical', 'plumbing'
        symptoms: List of observed symptoms or error codes, e.g., ['leaking near base','E24']
        urgency: How urgent the issue is: 'low', 'normal', or 'emergency'
        home_age_years: Approximate age of the home in years
        last_service_date: Last service date (YYYY-MM-DD), if known

    Returns:
        Dict containing:
            - likely_causes: List of possible causes for the issue
            - recommended_steps: List of recommended next steps to resolve the issue
    """
    if not appliance_type or not symptoms:
        raise ValueError("Both 'appliance_type' and 'symptoms' are required.")

    # Mocked data for demonstration purposes
    cause_samples = {
        "HVAC": ["dirty filter", "thermostat malfunction"],
        "water_heater": ["sediment build-up", "faulty thermostat"],
        "dishwasher": ["clogged drain", "faulty pump"],
        "electrical": ["tripped breaker", "faulty wiring"],
        "plumbing": ["leak in pipe", "clogged drain"],
    }

    step_samples = {
        "HVAC": ["Replace filter", "Check thermostat settings"],
        "water_heater": ["Flush tank", "Inspect thermostat"],
        "dishwasher": ["Clean drain", "Inspect pump"],
        "electrical": ["Reset breaker", "Inspect wiring"],
        "plumbing": ["Tighten fittings", "Clear drain"],
    }

    likely_causes = cause_samples.get(appliance_type, ["unknown issue"])
    recommended_steps = step_samples.get(appliance_type, ["consult a professional"])

    # Adjust recommendations based on urgency
    if urgency == "emergency":
        recommended_steps.append("Contact emergency services immediately")

    # Consider home age and last service date for additional context
    if home_age_years and home_age_years > 20:
        likely_causes.append("age-related wear and tear")
    if last_service_date:
        try:
            last_service = datetime.strptime(last_service_date, "%Y-%m-%d")
            if (datetime.now() - last_service).days > 365:
                recommended_steps.append("Schedule a routine maintenance check")
        except ValueError:
            raise ValueError("Invalid date format for 'last_service_date'. Use YYYY-MM-DD.")

    return {
        "likely_causes": likely_causes,
        "recommended_steps": recommended_steps,
    }

from typing import Dict, List, Literal


def drapes_status(room: List[str]) -> Dict[str, Literal["open", "closed"]]:
    """Returns the closed or open status of drapes in a given room or set of rooms.

    Args:
        room: List of rooms to check the drapes status for.

    Returns:
        Dict where keys are room names and values are 'open' or 'closed' indicating the drapes status.
    """

    sample_status = {
        "Living Room": "open",
        "Bedroom": "closed",
        "Kitchen": "open",
        "Bathroom": "closed",
        "Office": "open",
    }

    result = {}
    for r in room:
        if r not in sample_status:
            raise ValueError(f"Room not supported: {r}")
        result[r] = sample_status[r]

    return result

from typing import Dict, List, Union


def get_device_properties(device: Union[str, List[str]]) -> Dict[str, Union[str, List[Dict[str, Union[str, bool]]]]]:
    """Return on/off state and device type for one or more devices.

    Args:
        device: Device ID or array of device IDs

    Returns:
        Dict containing:
            - device_ids: List of device IDs
            - properties: List of dictionaries with:
                - id: Device ID
                - type: Type of the device (e.g., 'light', 'thermostat')
                - state: On/off state of the device
    """
    if isinstance(device, str):
        device = [device]

    sample_devices = {
        "device1": {"type": "light", "state": True},
        "device2": {"type": "thermostat", "state": False},
        "device3": {"type": "camera", "state": True},
    }

    properties = []
    for dev_id in device:
        if dev_id not in sample_devices:
            raise ValueError(f"Device ID not supported: {dev_id}")
        device_info = sample_devices[dev_id]
        properties.append({
            "id": dev_id,
            "type": device_info["type"],
            "state": device_info["state"],
        })

    return {
        "device_ids": device,
        "properties": properties,
    }

from typing import Dict, List


def get_home_devices() -> Dict[str, List[str]]:
    """Returns a list of smart devices in the user's home.

    Returns:
        Dict containing:
            - devices: List of smart device names
    """

    sample_devices = [
        "Smart Thermostat",
        "Smart Light Bulb",
        "Smart Speaker",
        "Smart Lock",
        "Smart Camera",
    ]

    return {
        "devices": sample_devices,
    }

from typing import Dict, List, Union


def heat(room: List[str], temperature: Union[float, None] = None) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Adjust the heating setpoint for a given room or set of rooms.

    Args:
        room: List of rooms whose heating setpoint to adjust.
        temperature: Target temperature setpoint in Celsius (optional, defaults to 22).

    Returns:
        Dict containing:
            - status: Status of the operation
            - details: List of dictionaries with room name and set temperature
    """
    if temperature is not None and (temperature < 5 or temperature > 30):
        raise ValueError("Temperature must be between 5 and 30 Celsius.")

    default_temperature = 22.0
    set_temperature = temperature if temperature is not None else default_temperature

    sample_rooms = {
        "Living Room": 21.5,
        "Bedroom": 19.0,
        "Kitchen": 20.0,
        "Bathroom": 23.0,
    }

    adjusted_rooms = []
    for r in room:
        if r not in sample_rooms:
            raise ValueError(f"Room not recognized: {r}")
        adjusted_rooms.append({"room": r, "set_temperature": set_temperature})

    return {
        "status": "success",
        "details": adjusted_rooms,
    }

from typing import Dict, List, Literal


def lights(room: List[str]) -> Dict[str, Literal["on", "off"]]:
    """Returns the on/off status of lights in a given room or set of rooms.

    Args:
        room: List of rooms to check the light status for

    Returns:
        Dict containing:
            - room_name: The name of the room
            - status: 'on' if the light is on, 'off' if the light is off
    """
    sample_status = {
        "Living Room": "on",
        "Kitchen": "off",
        "Bedroom": "on",
        "Bathroom": "off",
        "Garage": "on",
    }
    
    result = {}
    for r in room:
        if r not in sample_status:
            raise ValueError(f"Room not found: {r}")
        result[r] = sample_status[r]
    
    return result

from typing import Dict, Literal, Optional, Union


def play_music(
    room: Literal["living room", "kitchen", "bedroom", "all"],
    action: Literal["play", "pause", "stop", "skip"],
    genre: Optional[str] = None,
    volume: int = 50,
) -> Dict[str, Union[str, int]]:
    """Control music playback on smart speakers throughout the home.

    Args:
        room: Room for music playback ('living room', 'kitchen', 'bedroom', or 'all')
        action: Music action ('play', 'pause', 'stop', or 'skip')
        genre: Music genre or playlist name
        volume: Volume level from 0-100

    Returns:
        Dict containing:
            - room: Room where the action was applied
            - action: Action performed
            - genre: Genre or playlist name being played (if applicable)
            - volume: Volume level set
    """
    if not (0 <= volume <= 100):
        raise ValueError("Volume must be between 0 and 100")

    # Simulated response based on input parameters
    response = {
        "room": room,
        "action": action,
        "genre": genre if genre else "default playlist",
        "volume": volume,
    }

    return response

def preheat_oven(temperature_celsius: float) -> Dict[str, Union[str, float]]:
    """Preheat the oven to a specified temperature.

    Args:
        temperature_celsius: Oven temperature in Celsius.

    Returns:
        Dict containing:
            - status: Status of the preheating process
            - temperature: Target temperature in Celsius
    """
    if temperature_celsius < 0 or temperature_celsius > 300:
        raise ValueError("Temperature must be between 0 and 300 Celsius.")

    # Simulating the preheating process
    current_temperature = 20  # Assume room temperature
    time_to_preheat = (temperature_celsius - current_temperature) * 0.5  # Minutes

    # Simulate a successful preheat
    return {
        "status": "Preheating complete",
        "temperature": temperature_celsius,
    }

from typing import Dict, List, Literal


def schedule_cleaning(
    rooms: List[str],
    time: str,
    intensity: Literal["quiet", "standard", "turbo"] = "standard"
) -> Dict[str, Union[str, List[str]]]:
    """Program the robotic vacuum to clean specific areas.

    Args:
        rooms: List of rooms to clean (e.g. ['kitchen', 'living room'])
        time: Scheduled cleaning time in HH:MM format (e.g. '14:30')
        intensity: Cleaning intensity: 'quiet', 'standard', or 'turbo'

    Returns:
        Dict containing:
            - scheduled_rooms: List of rooms scheduled for cleaning
            - scheduled_time: Scheduled cleaning time
            - cleaning_intensity: Intensity level of the cleaning
    """
    if not rooms:
        raise ValueError("At least one room must be specified for cleaning.")
    if not isinstance(time, str) or len(time) != 5 or time[2] != ':':
        raise ValueError("Time must be in HH:MM format.")

    # Simulating a hash-based generation for consistent sample data
    scheduled_rooms = [room.capitalize() for room in rooms]
    scheduled_time = time
    cleaning_intensity = intensity

    return {
        "scheduled_rooms": scheduled_rooms,
        "scheduled_time": scheduled_time,
        "cleaning_intensity": cleaning_intensity,
    }

from typing import Dict, Literal, Union


def schedule_home_service(
    service_type: Literal[
        "plumbing", "electric", "hvac", "appliance", "cleaning", "pest_control", "internet"
    ],
    address: str,
    date: str,
    time_window: Dict[str, str],
    access_instructions: str = "",
    pet_on_premises: bool = False,
) -> Dict[str, Union[str, bool, Dict[str, str]]]:
    """Book a home service appointment with a time window.

    Args:
        service_type: Type of service to be scheduled (e.g., 'plumbing', 'electric')
        address: Service address
        date: Preferred date for the service in 'YYYY-MM-DD' format
        time_window: Preferred arrival window with 'start' and 'end' in 'HH:MM' 24h format
        access_instructions: Optional instructions for accessing the premises
        pet_on_premises: Whether pets will be present during the service

    Returns:
        Dict containing:
            - confirmation_id: Unique ID for the scheduled service
            - service_type: Type of service scheduled
            - address: Service address
            - date: Scheduled date
            - time_window: Scheduled time window
            - access_instructions: Provided access instructions
            - pet_on_premises: Whether pets will be present
    """
    import hashlib

    # Generate a unique confirmation ID based on input parameters
    hash_input = f"{service_type}{address}{date}{time_window['start']}{time_window['end']}"
    confirmation_id = hashlib.md5(hash_input.encode()).hexdigest()[:8]

    return {
        "confirmation_id": confirmation_id,
        "service_type": service_type,
        "address": address,
        "date": date,
        "time_window": time_window,
        "access_instructions": access_instructions,
        "pet_on_premises": pet_on_premises,
    }

from typing import Dict, List


def search_chromecast_devices(
    discovery_port: int = 1900,
    capability_video_out: bool = True,
    capability_audio_out: bool = True,
) -> Dict[str, List[str]]:
    """Retrieve the list of Chromecast-compatible device IDs on the local network.

    Args:
        discovery_port: Chromecast device's discovery UDP port
        capability_video_out: Whether the device must have video output capabilities
        capability_audio_out: Whether the device must have audio output capabilities

    Returns:
        Dict containing:
            - devices: List of device IDs that match the given capabilities
    """
    # Mock data simulating discovered devices
    mock_devices = {
        "device_1": {"video_out": True, "audio_out": True},
        "device_2": {"video_out": False, "audio_out": True},
        "device_3": {"video_out": True, "audio_out": False},
        "device_4": {"video_out": True, "audio_out": True},
    }

    # Filter devices based on capabilities
    matching_devices = [
        device_id
        for device_id, capabilities in mock_devices.items()
        if (capability_video_out == capabilities["video_out"] and
            capability_audio_out == capabilities["audio_out"])
    ]

    return {"devices": matching_devices}

from typing import Dict


def set_blind_position(blind_name: str, position: float) -> Dict[str, Union[str, float]]:
    """Set the position of the specified blinds.

    Args:
        blind_name: The name of the blinds to adjust.
        position: The desired position of the blinds from 0 (fully closed) to 100 (fully open).

    Returns:
        Dict containing:
            - blind_name: The name of the blinds
            - position: The new position of the blinds
            - status: Confirmation message of the action taken
    """
    if not (0 <= position <= 100):
        raise ValueError("Position must be between 0 and 100")

    # Simulate setting the blinds position
    status = f"Blinds '{blind_name}' set to position {position}%."

    return {
        "blind_name": blind_name,
        "position": position,
        "status": status,
    }

from typing import Dict, Literal, Optional, Union


def set_light_state(
    light_name: str,
    state: Literal["on", "off"],
    brightness: Optional[int] = None,
    color: Optional[str] = None
) -> Dict[str, Union[str, int, None]]:
    """Control the state of a light, including turning it on/off and adjusting brightness or color.

    Args:
        light_name: The name of the light to control.
        state: The desired state of the light ('on' or 'off').
        brightness: Brightness level from 0 to 100.
        color: Color of the light in hex (e.g., '#FF0000') or named color.

    Returns:
        Dict containing:
            - light_name: Name of the light
            - state: Current state of the light
            - brightness: Current brightness level
            - color: Current color of the light
    """
    if not (0 <= brightness <= 100) if brightness is not None else True:
        raise ValueError("Brightness must be between 0 and 100")

    # Simulated light states
    light_states = {
        "Living Room Light": {"state": "off", "brightness": 50, "color": "#FFFFFF"},
        "Bedroom Light": {"state": "on", "brightness": 75, "color": "#FFDD00"},
    }

    if light_name not in light_states:
        raise ValueError(f"Light not found: {light_name}")

    # Update the light state
    light_states[light_name]["state"] = state
    if brightness is not None:
        light_states[light_name]["brightness"] = brightness
    if color is not None:
        light_states[light_name]["color"] = color

    return {
        "light_name": light_name,
        "state": light_states[light_name]["state"],
        "brightness": light_states[light_name]["brightness"],
        "color": light_states[light_name]["color"],
    }

from typing import Dict, Literal


def set_lock_state(lock_name: str, state: Literal["lock", "unlock"]) -> Dict[str, str]:
    """Locks or unlocks a smart lock.

    Args:
        lock_name: The name of the lock.
        state: The desired state of the lock ('lock' or 'unlock').

    Returns:
        Dict containing:
            - lock_name: The name of the lock
            - state: The new state of the lock
            - message: Confirmation message of the action performed
    """
    
    valid_locks = {"FrontDoor", "BackDoor", "Garage"}
    if lock_name not in valid_locks:
        raise ValueError(f"Lock not recognized: {lock_name}")

    action_messages = {
        "lock": f"{lock_name} has been locked.",
        "unlock": f"{lock_name} has been unlocked."
    }
    
    return {
        "lock_name": lock_name,
        "state": state,
        "message": action_messages[state]
    }

from typing import Dict, List, Tuple, Union


def set_routine(
    frequency: int,
    time: str,
    day: int = 1,
    commands: List[Tuple[str, str]] = None
) -> Dict[str, Union[str, int, List[Tuple[str, str]]]]:
    """Creates a reoccurring routine of commands for devices on the home network.

    Args:
        frequency: A number which represents a choice of frequency. 0 for daily, 1 for weekly, 2 for monthly, and 3 for yearly.
        time: A time formatted string for the time of day the routine should be executed.
        day: Either a day of the month from 1-31 or a day of the week 1-7. This input should be adapted depending on the frequency flag.
        commands: An array or list of tuples which pair device ID's and commands.

    Returns:
        Dict containing:
            - frequency: The frequency of the routine
            - time: The time the routine is set to run
            - day: The day the routine is set to run
            - commands: The list of device ID and command pairs
    """
    if commands is None:
        raise ValueError("Commands list cannot be None")

    if frequency not in {0, 1, 2, 3}:
        raise ValueError("Invalid frequency value. Must be 0, 1, 2, or 3.")

    if frequency == 0 and not (1 <= day <= 7):
        raise ValueError("For daily routines, 'day' must be between 1 and 7.")
    if frequency in {1, 2, 3} and not (1 <= day <= 31):
        raise ValueError("For weekly, monthly, or yearly routines, 'day' must be between 1 and 31.")

    sample_commands = [
        ("device_1", "turn_on"),
        ("device_2", "turn_off"),
        ("device_3", "set_temperature"),
    ]

    return {
        "frequency": frequency,
        "time": time,
        "day": day,
        "commands": commands or sample_commands,
    }

def set_thermostat(temperature: float) -> Dict[str, Union[float, str]]:
    """Set the thermostat to the desired temperature.

    Args:
        temperature: Desired temperature in Celsius.

    Returns:
        Dict containing:
            - status: Confirmation message of the thermostat setting
            - set_temperature: The temperature that has been set
    """
    if not isinstance(temperature, (int, float)):
        raise ValueError("Temperature must be a number.")

    if temperature < 5 or temperature > 35:
        raise ValueError("Temperature must be between 5 and 35 Celsius.")

    return {
        "status": "Thermostat set successfully",
        "set_temperature": temperature
    }

def set_window_position(window_name: str, position: float) -> Dict[str, Union[str, int]]:
    """Set the position of a window to a specified level.

    Args:
        window_name: The name of the window.
        position: Position of the window from 0 (fully closed) to 100 (fully open).

    Returns:
        Dict containing:
            - window_name: Name of the window
            - position: Current position of the window
            - status: Status message indicating success or failure
    """
    if not (0 <= position <= 100):
        raise ValueError("Position must be between 0 and 100")

    # Simulate a hash-based generation for consistent but varied sample data
    window_status = {
        "Living Room": 75,
        "Bedroom": 50,
        "Kitchen": 25,
    }

    if window_name not in window_status:
        raise ValueError(f"Window not supported: {window_name}")

    # Simulate setting the window position
    window_status[window_name] = position

    return {
        "window_name": window_name,
        "position": window_status[window_name],
        "status": "Window position set successfully"
    }

from typing import Dict, Literal, Optional


def space(
    room: Literal["bedroom", "livingroom", "kitchen"],
    drapes: Optional[Literal["open", "close"]] = None,
    lights: Optional[Literal["on", "off"]] = None,
) -> Dict[str, str]:
    """Modify items in a specific room depending on their current status.

    Args:
        room: The room whose drapes/lights to modify ('bedroom', 'livingroom', 'kitchen').
        drapes: Action to perform on the drapes ('open' or 'close').
        lights: Action to perform on the lights ('on' or 'off').

    Returns:
        Dict containing:
            - room: The room where modifications were made
            - drapes_status: The new status of the drapes
            - lights_status: The new status of the lights

    Raises:
        ValueError: If neither drapes nor lights are specified.
    """
    if drapes is None and lights is None:
        raise ValueError("At least one of 'drapes' or 'lights' must be specified.")

    # Sample current states for demonstration purposes
    current_states = {
        "bedroom": {"drapes": "closed", "lights": "off"},
        "livingroom": {"drapes": "open", "lights": "on"},
        "kitchen": {"drapes": "closed", "lights": "off"},
    }

    # Modify the states based on input
    if drapes:
        current_states[room]["drapes"] = drapes
    if lights:
        current_states[room]["lights"] = lights

    return {
        "room": room,
        "drapes_status": current_states[room]["drapes"],
        "lights_status": current_states[room]["lights"],
    }

from typing import Dict, Literal


def start_dishwasher(mode: Literal["eco", "heavy", "quick"]) -> Dict[str, str]:
    """Start the dishwasher with a selected mode.

    Args:
        mode: Wash mode, e.g., 'eco', 'heavy', 'quick'.

    Returns:
        Dict containing:
            - status: Status of the dishwasher start process
            - mode: The mode in which the dishwasher is running
    """
    available_modes = {"eco", "heavy", "quick"}
    if mode not in available_modes:
        raise ValueError(f"Unsupported mode: {mode}")

    # Simulate starting the dishwasher
    return {
        "status": "Dishwasher started successfully",
        "mode": mode,
    }

from typing import Dict, Literal


def start_stove(burner: str, heat_level: Literal["low", "medium", "high"]) -> Dict[str, str]:
    """Turn on the stove and set a burner to a specific heat level.

    Args:
        burner: Identifier of the burner (e.g., 'front left', 'rear right').
        heat_level: Heat level setting (e.g., 'low', 'medium', 'high').

    Returns:
        Dict containing:
            - burner: Identifier of the burner
            - heat_level: Set heat level
            - status: Confirmation message of the action
    """
    valid_burners = {"front left", "front right", "rear left", "rear right"}
    if burner not in valid_burners:
        raise ValueError(f"Invalid burner specified: {burner}")

    return {
        "burner": burner,
        "heat_level": heat_level,
        "status": f"The {burner} burner is now set to {heat_level} heat."
    }

from typing import Dict, Optional


def update_device(device_id: str, version_number: Optional[str] = "latest") -> Dict[str, str]:
    """Update the specified device to a given version number.

    Args:
        device_id: ID number linked to the device.
        version_number: Version number to update to (default is 'latest').

    Returns:
        Dict containing:
            - device_id: The ID of the updated device
            - version_number: The version number the device was updated to
            - status: Status of the update operation
    """
    
    # Simulated device database
    devices = {
        "device_001": "1.0.0",
        "device_002": "1.2.3",
        "device_003": "2.0.1",
    }
    
    # Check if the device exists
    if device_id not in devices:
        raise ValueError(f"Device ID not found: {device_id}")
    
    # Simulate updating the device
    if version_number == "latest":
        version_number = "3.0.0"  # Assume 'latest' is version 3.0.0 for all devices
    
    # Update the device version
    devices[device_id] = version_number
    
    return {
        "device_id": device_id,
        "version_number": version_number,
        "status": "success",
    }

