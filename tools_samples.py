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


def calculate_travel_cost(
    origin_city: str, destination_city: str
) -> Dict[str, Union[str, float]]:
    """
    Calculate estimated travel cost between two cities.
    Args:
        origin_city: Starting city name.
        destination_city: Destination city name.
    Returns:
        Dict containing:
            - origin_city: The starting city
            - destination_city: The destination city
            - estimated_cost_usd: Estimated travel cost in USD
    """
    # Sample distances between cities in miles (symmetric)
    distances = {
        ("Seattle", "San Francisco"): 807,
        ("New York", "Chicago"): 790,
        ("Boston", "Chicago"): 983,
        ("Miami", "Orlando"): 235,
        ("Denver", "Las Vegas"): 748,
    }
    # Normalize city names to title case for matching
    origin = origin_city.title()
    destination = destination_city.title()
    # Try to find distance in either order (origin->destination or destination->origin)
    distance = distances.get((origin, destination)) or distances.get(
        (destination, origin)
    )
    if distance is None:
        raise ValueError(f"Distance data not available for {origin} to {destination}")
    # Assume a fixed cost per mile (e.g., $0.5 per mile)
    cost_per_mile = 0.5
    estimated_cost = distance * cost_per_mile
    return {
        "origin_city": origin,
        "destination_city": destination,
        "estimated_cost_usd": round(estimated_cost, 2),
    }


def schedule_meeting(
    date: str, time: str, duration_minutes: int, attendee: str
) -> Dict[str, Union[str, int]]:
    """
    Schedule a meeting with specified details.
    Args:
        date: Date of the meeting (YYYY-MM-DD)
        time: Time of the meeting (HH:MM, 24-hour)
        duration_minutes: Duration in minutes
        attendee: Attendee name or username
    Returns:
        Dict containing:
            - date
            - time
            - duration_minutes
            - attendee
            - confirmation: Confirmation message
    """
    confirmation = f"Meeting scheduled on {date} at {time} for {duration_minutes} minutes with {attendee}."
    return {
        "date": date,
        "time": time,
        "duration_minutes": duration_minutes,
        "attendee": attendee,
        "confirmation": confirmation,
    }


def get_population(city_name: str) -> Dict[str, Union[str, int]]:
    """
    Returns the population of the specified city.

    Args:
        city_name: Name of the city (e.g., "Tokyo", "Paris")

    Returns:
        Dict with:
            - city_name: The city queried
            - population: The population of the city
    """
    sample_data = {
        "Tokyo": 13929286,
        "Paris": 2161000,
        "New York": 8419600,
        "Seattle": 733919,
        "Boston": 654776,
    }
    city = city_name.title()
    if city not in sample_data:
        raise ValueError(f"City not found: {city}")
    return {"city_name": city, "population": sample_data[city]}


def lookup_employee(username: str) -> Dict[str, str]:
    """
    Returns basic employee info for the given username.

    Args:
        username: The employee's username (e.g., "arybak", "jdoe")

    Returns:
        Dict with:
            - username
            - name
            - role
            - team
            - location
    """
    sample_employees = {
        "arybak": {
            "name": "Alexey Rybak",
            "role": "Junior Vibe Coder",
            "team": "AI Platform",
            "location": "Seattle",
        },
        "jdoe": {
            "name": "Jane Doe",
            "role": "Product Manager",
            "team": "LlamaX",
            "location": "London",
        },
        "csmith": {
            "name": "Chris Smith",
            "role": "Data Scientist",
            "team": "Analytics",
            "location": "New York",
        },
    }
    if username not in sample_employees:
        raise ValueError(f"Username not found: {username}")
    return {"username": username, **sample_employees[username]}


def get_stock_price(ticker: str) -> Dict[str, Union[str, float]]:
    """
    Returns the current stock price for the given ticker symbol.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL", "GOOG")

    Returns:
        Dict with:
            - ticker
            - price_usd
    """
    sample_prices = {"AAPL": 210.15, "GOOG": 2850.50, "META": 320.75, "TSLA": 720.10}
    symbol = ticker.upper()
    if symbol not in sample_prices:
        raise ValueError(f"Ticker not found: {symbol}")
    return {"ticker": symbol, "price_usd": sample_prices[symbol]}


def get_book_info(isbn: str) -> Dict[str, str]:
    """
    Returns details about the book for the given ISBN.

    Args:
        isbn: Book ISBN (e.g., "9780143127741")

    Returns:
        Dict with:
            - isbn
            - title
            - author
            - publication_year
            - summary
    """
    sample_books = {
        "9780143127741": {
            "title": "Sapiens: A Brief History of Humankind",
            "author": "Yuval Noah Harari",
            "publication_year": "2015",
            "summary": "A thought-provoking journey through the history and impact of Homo sapiens.",
        },
        "9780062316097": {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "publication_year": "2014",
            "summary": "A mystical story about following your dreams.",
        },
        "9780307271037": {
            "title": "The Road",
            "author": "Cormac McCarthy",
            "publication_year": "2006",
            "summary": "A bleak, beautiful tale of a father and son journeying through a post-apocalyptic world.",
        },
    }
    if isbn not in sample_books:
        raise ValueError(f"ISBN not found: {isbn}")
    return {"isbn": isbn, **sample_books[isbn]}
