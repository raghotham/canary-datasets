from typing import Dict, Literal, Union, List


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
            "name": "Philip K. Dick",
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


def quadratic_roots(a: int, b: int, c: int) -> Dict[str, Union[float, str]]:
    """
    Find the roots of a quadratic equation ax^2 + bx + c = 0.
    Args:
        a: Coefficient of x^2.
        b: Coefficient of x.
        c: Constant term.
    Returns:
        Dict containing:
            - root1: First root (float or complex)
            - root2: Second root (float or complex)
    """
    import cmath

    discriminant = b**2 - 4 * a * c
    sqrt_disc = cmath.sqrt(discriminant)
    root1 = (-b + sqrt_disc) / (2 * a)
    root2 = (-b - sqrt_disc) / (2 * a)
    return {
        "root1": root1,
        "root2": root2,
    }


def calculate_area(
    base: int, height: int, unit: str = "cm"
) -> Dict[str, Union[int, str, float]]:
    """
    Calculate the area of a right-angled triangle given the lengths of its base and height.
    Args:
        base: The length of the base of the right-angled triangle.
        height: The height of the right-angled triangle.
        unit: The unit of measure used. Defaults to 'cm'.
    Returns:
        Dict containing:
            - base: The base length
            - height: The height length
            - unit: The unit of measure
            - area: The calculated area of the triangle
    """
    area = 0.5 * base * height
    return {
        "base": base,
        "height": height,
        "unit": unit,
        "area": area,
    }


def get_trains(from_city: str, to_city: str) -> Dict[str, Union[str, list]]:
    """
    Returns train routes for a given day from one city to another.

    Args:
        from_city: The city to depart from
        to_city: The destination city

    Returns:
        Dict containing:
            - from_city: Departure city
            - to_city: Destination city
            - routes: List of available train routes with times and train types
    """
    # Sample train routes data
    train_routes = {
        ("New York", "Boston"): [
            {"departure": "06:00", "arrival": "10:15", "train": "Acela Express"},
            {"departure": "09:30", "arrival": "13:45", "train": "Northeast Regional"},
            {"departure": "14:00", "arrival": "18:20", "train": "Northeast Regional"},
            {"departure": "18:00", "arrival": "22:15", "train": "Acela Express"},
        ],
        ("Chicago", "Milwaukee"): [
            {"departure": "07:15", "arrival": "08:45", "train": "Hiawatha"},
            {"departure": "12:00", "arrival": "13:30", "train": "Hiawatha"},
            {"departure": "17:30", "arrival": "19:00", "train": "Hiawatha"},
        ],
        ("San Francisco", "Los Angeles"): [
            {"departure": "08:00", "arrival": "20:30", "train": "Coast Starlight"},
        ],
        ("Seattle", "Portland"): [
            {"departure": "07:30", "arrival": "11:00", "train": "Cascades"},
            {"departure": "13:15", "arrival": "16:45", "train": "Cascades"},
            {"departure": "18:00", "arrival": "21:30", "train": "Cascades"},
        ],
        ("Paris", "London"): [
            {"departure": "07:13", "arrival": "08:39", "train": "Eurostar"},
            {"departure": "11:13", "arrival": "12:39", "train": "Eurostar"},
            {"departure": "17:13", "arrival": "18:39", "train": "Eurostar"},
        ],
        ("Berlin", "Munich"): [
            {"departure": "06:00", "arrival": "10:00", "train": "ICE"},
            {"departure": "10:00", "arrival": "14:00", "train": "ICE"},
            {"departure": "14:00", "arrival": "18:00", "train": "ICE"},
            {"departure": "18:00", "arrival": "22:00", "train": "ICE"},
        ],
        ("Berlin", "Prague"): [
            {"departure": "08:30", "arrival": "13:00", "train": "EuroCity"},
            {"departure": "14:30", "arrival": "19:00", "train": "EuroCity"},
        ],
        ("Budapest", "Vienna"): [
            {"departure": "07:40", "arrival": "10:18", "train": "Railjet"},
            {"departure": "11:40", "arrival": "14:18", "train": "Railjet"},
            {"departure": "15:40", "arrival": "18:18", "train": "Railjet"},
            {"departure": "19:40", "arrival": "22:18", "train": "Railjet"},
        ],
        ("Budapest", "Prague"): [
            {"departure": "09:25", "arrival": "16:28", "train": "EuroCity"},
            {"departure": "17:25", "arrival": "00:28", "train": "EuroCity"},
        ],
        ("Athens", "Thessaloniki"): [
            {"departure": "06:22", "arrival": "10:37", "train": "InterCity"},
            {"departure": "08:22", "arrival": "12:37", "train": "InterCity"},
            {"departure": "14:22", "arrival": "18:37", "train": "InterCity"},
            {"departure": "20:22", "arrival": "00:37", "train": "InterCity Express"},
        ],
        ("Athens", "Patras"): [
            {"departure": "07:00", "arrival": "10:30", "train": "Proastiakos"},
            {"departure": "12:00", "arrival": "15:30", "train": "Proastiakos"},
            {"departure": "17:00", "arrival": "20:30", "train": "Proastiakos"},
        ],
    }

    # Normalize city names to title case
    from_normalized = from_city.title()
    to_normalized = to_city.title()

    # Try both directions (from->to and to->from)
    routes = train_routes.get((from_normalized, to_normalized))
    if routes is None:
        # Try reverse direction
        routes = train_routes.get((to_normalized, from_normalized))
        if routes:
            # Swap arrival and departure times for reverse routes
            routes = [
                {
                    "departure": r["arrival"],
                    "arrival": r["departure"],
                    "train": r["train"],
                }
                for r in routes
            ]

    if routes is None:
        raise ValueError(
            f"No train routes found from {from_normalized} to {to_normalized}"
        )

    return {
        "from_city": from_normalized,
        "to_city": to_normalized,
        "routes": routes,
    }


def get_flights(from_city: str, to_city: str) -> Dict[str, Union[str, list]]:
    """
    Returns flight routes for a given day from one city to another.

    Args:
        from_city: The city to depart from
        to_city: The destination city

    Returns:
        Dict containing:
            - from_city: Departure city
            - to_city: Destination city
            - flights: List of available flights with times and airlines
    """
    # Sample flight routes data
    flight_routes = {
        ("New York", "Los Angeles"): [
            {
                "departure": "06:00",
                "arrival": "09:15",
                "airline": "American Airlines",
                "flight": "AA100",
            },
            {
                "departure": "09:30",
                "arrival": "12:45",
                "airline": "United",
                "flight": "UA250",
            },
            {
                "departure": "14:00",
                "arrival": "17:15",
                "airline": "JetBlue",
                "flight": "B6523",
            },
            {
                "departure": "19:00",
                "arrival": "22:15",
                "airline": "Delta",
                "flight": "DL410",
            },
        ],
        ("Chicago", "Miami"): [
            {
                "departure": "07:00",
                "arrival": "11:30",
                "airline": "United",
                "flight": "UA1234",
            },
            {
                "departure": "13:00",
                "arrival": "17:30",
                "airline": "American Airlines",
                "flight": "AA567",
            },
            {
                "departure": "18:30",
                "arrival": "23:00",
                "airline": "Southwest",
                "flight": "WN890",
            },
        ],
        ("San Francisco", "Seattle"): [
            {
                "departure": "07:00",
                "arrival": "09:15",
                "airline": "Alaska",
                "flight": "AS301",
            },
            {
                "departure": "11:30",
                "arrival": "13:45",
                "airline": "United",
                "flight": "UA788",
            },
            {
                "departure": "16:00",
                "arrival": "18:15",
                "airline": "Alaska",
                "flight": "AS455",
            },
            {
                "departure": "20:00",
                "arrival": "22:15",
                "airline": "Southwest",
                "flight": "WN999",
            },
        ],
        ("London", "Paris"): [
            {
                "departure": "06:30",
                "arrival": "08:45",
                "airline": "British Airways",
                "flight": "BA304",
            },
            {
                "departure": "10:00",
                "arrival": "12:15",
                "airline": "Air France",
                "flight": "AF1081",
            },
            {
                "departure": "15:30",
                "arrival": "17:45",
                "airline": "EasyJet",
                "flight": "U28323",
            },
            {
                "departure": "19:00",
                "arrival": "21:15",
                "airline": "British Airways",
                "flight": "BA318",
            },
        ],
        ("Tokyo", "Seoul"): [
            {
                "departure": "08:00",
                "arrival": "10:30",
                "airline": "ANA",
                "flight": "NH861",
            },
            {
                "departure": "13:00",
                "arrival": "15:30",
                "airline": "Korean Air",
                "flight": "KE704",
            },
            {
                "departure": "18:00",
                "arrival": "20:30",
                "airline": "Asiana",
                "flight": "OZ105",
            },
        ],
        ("Berlin", "Frankfurt"): [
            {
                "departure": "07:00",
                "arrival": "08:15",
                "airline": "Lufthansa",
                "flight": "LH172",
            },
            {
                "departure": "10:00",
                "arrival": "11:15",
                "airline": "Lufthansa",
                "flight": "LH176",
            },
            {
                "departure": "14:00",
                "arrival": "15:15",
                "airline": "Lufthansa",
                "flight": "LH180",
            },
            {
                "departure": "18:00",
                "arrival": "19:15",
                "airline": "Lufthansa",
                "flight": "LH184",
            },
        ],
        ("Berlin", "Amsterdam"): [
            {
                "departure": "06:45",
                "arrival": "08:10",
                "airline": "KLM",
                "flight": "KL1822",
            },
            {
                "departure": "11:30",
                "arrival": "12:55",
                "airline": "EasyJet",
                "flight": "U25673",
            },
            {
                "departure": "17:00",
                "arrival": "18:25",
                "airline": "KLM",
                "flight": "KL1826",
            },
        ],
        ("Budapest", "Rome"): [
            {
                "departure": "06:00",
                "arrival": "07:45",
                "airline": "Ryanair",
                "flight": "FR8412",
            },
            {
                "departure": "11:30",
                "arrival": "13:15",
                "airline": "Wizz Air",
                "flight": "W62311",
            },
            {
                "departure": "18:45",
                "arrival": "20:30",
                "airline": "Alitalia",
                "flight": "AZ481",
            },
        ],
        ("Budapest", "Berlin"): [
            {
                "departure": "07:20",
                "arrival": "08:50",
                "airline": "EasyJet",
                "flight": "U24892",
            },
            {
                "departure": "13:15",
                "arrival": "14:45",
                "airline": "Ryanair",
                "flight": "FR2516",
            },
            {
                "departure": "19:00",
                "arrival": "20:30",
                "airline": "Wizz Air",
                "flight": "W62468",
            },
        ],
        ("Tahiti", "Bora Bora"): [
            {
                "departure": "07:00",
                "arrival": "07:50",
                "airline": "Air Tahiti",
                "flight": "VT272",
            },
            {
                "departure": "10:30",
                "arrival": "11:20",
                "airline": "Air Tahiti",
                "flight": "VT274",
            },
            {
                "departure": "15:00",
                "arrival": "15:50",
                "airline": "Air Tahiti",
                "flight": "VT276",
            },
            {
                "departure": "17:30",
                "arrival": "18:20",
                "airline": "Air Tahiti",
                "flight": "VT278",
            },
        ],
        ("Los Angeles", "Bora Bora"): [
            {
                "departure": "23:00",
                "arrival": "06:45+1",
                "airline": "Air Tahiti Nui",
                "flight": "TN102",
            },
        ],
        ("Athens", "Rome"): [
            {
                "departure": "07:45",
                "arrival": "09:00",
                "airline": "Aegean Airlines",
                "flight": "A3650",
            },
            {
                "departure": "13:30",
                "arrival": "14:45",
                "airline": "ITA Airways",
                "flight": "AZ717",
            },
            {
                "departure": "19:15",
                "arrival": "20:30",
                "airline": "Aegean Airlines",
                "flight": "A3654",
            },
        ],
        ("Athens", "Istanbul"): [
            {
                "departure": "06:00",
                "arrival": "09:30",
                "airline": "Turkish Airlines",
                "flight": "TK1842",
            },
            {
                "departure": "11:45",
                "arrival": "15:15",
                "airline": "Aegean Airlines",
                "flight": "A3992",
            },
            {
                "departure": "18:30",
                "arrival": "22:00",
                "airline": "Turkish Airlines",
                "flight": "TK1846",
            },
        ],
        ("Athens", "London"): [
            {
                "departure": "06:00",
                "arrival": "08:05",
                "airline": "British Airways",
                "flight": "BA632",
            },
            {
                "departure": "11:15",
                "arrival": "13:20",
                "airline": "Aegean Airlines",
                "flight": "A3600",
            },
            {
                "departure": "15:40",
                "arrival": "17:45",
                "airline": "EasyJet",
                "flight": "U28082",
            },
        ],
    }

    # Normalize city names to title case
    from_normalized = from_city.title()
    to_normalized = to_city.title()

    # Try to find flights
    flights = flight_routes.get((from_normalized, to_normalized))
    if flights is None:
        # Try reverse direction (some routes might be bidirectional)
        flights = flight_routes.get((to_normalized, from_normalized))
        if flights:
            # For reverse routes, swap times and adjust flight numbers
            flights = [
                {
                    "departure": f["arrival"],
                    "arrival": f["departure"],
                    "airline": f["airline"],
                    "flight": f["flight"] + "R",  # Add R for return flight
                }
                for f in flights
            ]

    if flights is None:
        raise ValueError(f"No flights found from {from_normalized} to {to_normalized}")

    return {
        "from_city": from_normalized,
        "to_city": to_normalized,
        "flights": flights,
    }


def get_refreshments(city: str) -> Dict[str, Union[str, list]]:
    """
    Returns a list of venues in a given city that offer refreshments such as water or soda.

    Args:
        city: The city to search

    Returns:
        Dict containing:
            - city: The city searched
            - venues: List of venues offering refreshments with details
    """
    # Sample refreshment venues data
    refreshment_venues = {
        "New York": [
            {
                "name": "Central Park Cafe",
                "type": "Cafe",
                "address": "Central Park West",
                "specialties": ["coffee", "water", "soda", "sandwiches"],
            },
            {
                "name": "Times Square Refreshments",
                "type": "Kiosk",
                "address": "Times Square",
                "specialties": ["water", "soda", "snacks"],
            },
            {
                "name": "Brooklyn Bridge Beverages",
                "type": "Food Truck",
                "address": "Brooklyn Bridge Park",
                "specialties": ["water", "juice", "soda", "ice cream"],
            },
            {
                "name": "Grand Central Market",
                "type": "Market",
                "address": "Grand Central Terminal",
                "specialties": ["water", "soda", "coffee", "fresh juice"],
            },
        ],
        "San Francisco": [
            {
                "name": "Golden Gate Refreshments",
                "type": "Stand",
                "address": "Golden Gate Park",
                "specialties": ["water", "soda", "coffee"],
            },
            {
                "name": "Fisherman's Wharf Drinks",
                "type": "Kiosk",
                "address": "Fisherman's Wharf",
                "specialties": ["water", "soda", "local beverages"],
            },
            {
                "name": "Union Square Cafe",
                "type": "Cafe",
                "address": "Union Square",
                "specialties": ["coffee", "tea", "water", "pastries"],
            },
        ],
        "Chicago": [
            {
                "name": "Millennium Park Refreshments",
                "type": "Stand",
                "address": "Millennium Park",
                "specialties": ["water", "soda", "ice tea"],
            },
            {
                "name": "Navy Pier Beverages",
                "type": "Kiosk",
                "address": "Navy Pier",
                "specialties": ["water", "soda", "lemonade"],
            },
            {
                "name": "Loop Cafe",
                "type": "Cafe",
                "address": "The Loop",
                "specialties": ["coffee", "water", "juice", "sandwiches"],
            },
        ],
        "London": [
            {
                "name": "Hyde Park Corner Cafe",
                "type": "Cafe",
                "address": "Hyde Park",
                "specialties": ["tea", "water", "soda", "scones"],
            },
            {
                "name": "Covent Garden Refreshments",
                "type": "Stand",
                "address": "Covent Garden",
                "specialties": ["water", "soda", "fresh juice"],
            },
            {
                "name": "Thames Riverside Kiosk",
                "type": "Kiosk",
                "address": "Thames Path",
                "specialties": ["water", "soda", "ice cream"],
            },
        ],
        "Tokyo": [
            {
                "name": "Shibuya Station Drinks",
                "type": "Vending Area",
                "address": "Shibuya Station",
                "specialties": ["water", "tea", "soda", "coffee"],
            },
            {
                "name": "Ueno Park Refreshments",
                "type": "Stand",
                "address": "Ueno Park",
                "specialties": ["water", "green tea", "ramune"],
            },
            {
                "name": "Ginza Cafe",
                "type": "Cafe",
                "address": "Ginza District",
                "specialties": ["coffee", "tea", "water", "pastries"],
            },
        ],
        "Berlin": [
            {
                "name": "Brandenburg Gate Cafe",
                "type": "Cafe",
                "address": "Pariser Platz",
                "specialties": ["coffee", "water", "beer", "pretzels"],
            },
            {
                "name": "Tiergarten Refreshments",
                "type": "Stand",
                "address": "Tiergarten Park",
                "specialties": ["water", "soda", "ice cream"],
            },
            {
                "name": "Alexanderplatz Drinks",
                "type": "Kiosk",
                "address": "Alexanderplatz",
                "specialties": ["water", "soda", "coffee", "currywurst"],
            },
            {
                "name": "Checkpoint Charlie Cafe",
                "type": "Cafe",
                "address": "Friedrichstraße",
                "specialties": ["coffee", "tea", "water", "cake"],
            },
        ],
        "Budapest": [
            {
                "name": "Chain Bridge Refreshments",
                "type": "Stand",
                "address": "Chain Bridge",
                "specialties": ["water", "soda", "lemonade"],
            },
            {
                "name": "Central Market Hall Drinks",
                "type": "Market Stall",
                "address": "Central Market Hall",
                "specialties": ["water", "fruit juice", "local wines", "soft drinks"],
            },
            {
                "name": "Fisherman's Bastion Cafe",
                "type": "Cafe",
                "address": "Fisherman's Bastion",
                "specialties": ["coffee", "water", "wine", "pastries"],
            },
            {
                "name": "Thermal Bath Refreshments",
                "type": "Pool Bar",
                "address": "Széchenyi Thermal Bath",
                "specialties": ["water", "juice", "beer", "smoothies"],
            },
        ],
        "Bora Bora": [
            {
                "name": "Matira Beach Bar",
                "type": "Beach Bar",
                "address": "Matira Beach",
                "specialties": [
                    "water",
                    "coconut water",
                    "tropical juice",
                    "cocktails",
                ],
            },
            {
                "name": "Vaitape Village Refreshments",
                "type": "Stand",
                "address": "Vaitape",
                "specialties": ["water", "soda", "fresh fruit juice"],
            },
            {
                "name": "Lagoon Cafe",
                "type": "Waterfront Cafe",
                "address": "Bora Bora Lagoon",
                "specialties": [
                    "water",
                    "tropical smoothies",
                    "coffee",
                    "fresh coconut",
                ],
            },
            {
                "name": "Mount Otemanu Lookout",
                "type": "Refreshment Hut",
                "address": "Otemanu Trail",
                "specialties": ["water", "energy drinks", "fruit"],
            },
        ],
        "Athens": [
            {
                "name": "Acropolis Cafe",
                "type": "Cafe",
                "address": "Acropolis Museum",
                "specialties": ["coffee", "frappe", "water", "Greek pastries"],
            },
            {
                "name": "Plaka Refreshments",
                "type": "Traditional Kiosk",
                "address": "Plaka District",
                "specialties": ["water", "soda", "fresh orange juice", "loukoumades"],
            },
            {
                "name": "Syntagma Square Drinks",
                "type": "Stand",
                "address": "Syntagma Square",
                "specialties": ["water", "iced coffee", "lemonade"],
            },
            {
                "name": "National Garden Cafe",
                "type": "Garden Cafe",
                "address": "National Garden",
                "specialties": ["water", "juice", "Greek coffee", "ice cream"],
            },
            {
                "name": "Monastiraki Market Bar",
                "type": "Market Stall",
                "address": "Monastiraki Flea Market",
                "specialties": ["water", "ouzo", "beer", "mezze"],
            },
        ],
    }

    # Normalize city name to title case
    city_normalized = city.title()

    # Get venues for the city
    venues = refreshment_venues.get(city_normalized)

    if venues is None:
        # Try some common variations
        city_variations = {
            "Nyc": "New York",
            "Sf": "San Francisco",
            "La": "Los Angeles",
        }
        alternative = city_variations.get(city_normalized)
        if alternative:
            venues = refreshment_venues.get(alternative)
            city_normalized = alternative

    if venues is None:
        raise ValueError(f"No refreshment venues found for city: {city_normalized}")

    return {
        "city": city_normalized,
        "venues": venues,
    }


def file_search(query: str) -> Dict[str, Union[str, List[str]]]:
    """Search through uploaded files using vector search.

    Note: This is a placeholder function. The actual implementation
    will be dynamically created by create_file_search_function()
    and will replace this function in the ToolExecutor.

    Args:
        query: The search query to find relevant content in the files

    Returns:
        Dict containing:
            - query: The original search query
            - results: List of relevant text snippets from the files
            - sources: List of source file names where results were found
    """
    return {
        "query": query,
        "results": [
            "This function should be dynamically replaced by create_file_search_function"
        ],
        "sources": [],
    }
