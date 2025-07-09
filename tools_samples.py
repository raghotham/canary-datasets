from typing import Dict, Literal, Union


def get_weather(location: str) -> Dict[str, Union[str, float, list]]:
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
        "Tokyo": 88,
        "Paris": 75,
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
    to_unit: Literal["celsius", "fahrenheit"],
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


def convert_currency(
    amount: float, from_currency: str, to_currency: str
) -> Dict[str, Union[float, str]]:
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
        "AUD": 1.52,
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
        "converted_amount": round(converted_amount, 2),
    }


def get_fruit_info(fruit: str) -> Dict[str, Union[str, float, Dict[str, float]]]:
    """
    Get typical color and average weight of a fruit in grams and ounces.
    Args:
        fruit: Name of the fruit (e.g. 'apple', 'banana', 'mango')
    Returns:
        Dict containing:
            - fruit: Fruit name
            - color: Typical color of the fruit
            - average_weight: Dict with weight in grams and ounces
    """
    sample_data = {
        "apple": {"color": "red or green", "average_weight_grams": 182.0},
        "banana": {"color": "yellow", "average_weight_grams": 118.0},
        "mango": {"color": "orange or green", "average_weight_grams": 200.0},
    }
    if fruit.lower() not in sample_data:
        raise ValueError(f"Fruit not supported: {fruit}")
    weight_g = sample_data[fruit.lower()]["average_weight_grams"]
    weight_oz = weight_g * 0.03527396  # grams to ounces conversion
    return {
        "fruit": fruit,
        "color": sample_data[fruit.lower()]["color"],
        "average_weight": {
            "grams": weight_g,
            "ounces": round(weight_oz, 2),
        },
    }


def convert_weight_units(
    value: float,
    from_unit: Literal["grams", "ounces"],
    to_unit: Literal["grams", "ounces"],
) -> Dict[str, Union[float, str]]:
    """
    Convert weight between grams and ounces.
    Args:
        value: The weight value to convert
        from_unit: The unit to convert from ('grams' or 'ounces')
        to_unit: The unit to convert to ('grams' or 'ounces')
    Returns:
        Dict containing:
            - value: Converted weight value
            - unit: Unit of the converted weight
    """
    if from_unit == to_unit:
        return {"value": value, "unit": to_unit}
    if (from_unit, to_unit) == ("grams", "ounces"):
        return {"value": round(value * 0.03527396, 2), "unit": "ounces"}
    if (from_unit, to_unit) == ("ounces", "grams"):
        return {"value": round(value / 0.03527396, 2), "unit": "grams"}
    raise ValueError("unsupported units")
