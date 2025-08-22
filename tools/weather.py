# Weather Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def get_weather(
    location: str, forecast_days: int = 1
) -> Dict[str, Union[str, float, List[Dict[str, Union[str, float]]]]]:
    """Provides current and forecasted weather for a location.

    Args:
        location: The location for weather information (e.g. 'London', 'New York')
        forecast_days: Number of days to forecast the weather

    Returns:
        Dict containing:
            - location: Location name
            - current_temperature: Current temperature in Fahrenheit
            - forecast: List of dictionaries with forecasted weather conditions for each day
    """

    # Sample data for current temperature
    current_weather_sample = {
        "New York": 68.0,
        "London": 60.0,
        "Sydney": 75.0,
        "Mumbai": 85.0,
        "Tokyo": 70.0,
        "Boston": 65.0,
        "Paris": 62.0,
        "Las Vegas": 88.0,
        "San Francisco": 66.0,
    }

    # Sample data for forecasted weather
    forecast_sample = {
        "New York": [
            {"day": "Monday", "temperature": 70.0, "condition": "sunny"},
            {"day": "Tuesday", "temperature": 72.0, "condition": "cloudy"},
        ],
        "Sydney": [
            {"day": "Monday", "temperature": 77.0, "condition": "sunny"},
            {"day": "Tuesday", "temperature": 78.0, "condition": "windy"},
        ],
        "Mumbai": [
            {"day": "Monday", "temperature": 87.0, "condition": "humid"},
            {"day": "Tuesday", "temperature": 88.0, "condition": "sunny"},
        ],
        "Tokyo": [
            {"day": "Monday", "temperature": 72.0, "condition": "cloudy"},
            {"day": "Tuesday", "temperature": 74.0, "condition": "rainy"},
        ],
        "Boston": [
            {"day": "Monday", "temperature": 67.0, "condition": "cloudy"},
            {"day": "Tuesday", "temperature": 69.0, "condition": "sunny"},
        ],
        "Paris": [
            {"day": "Monday", "temperature": 64.0, "condition": "overcast"},
            {"day": "Tuesday", "temperature": 66.0, "condition": "rainy"},
        ],
        "Las Vegas": [
            {"day": "Monday", "temperature": 90.0, "condition": "sunny"},
            {"day": "Tuesday", "temperature": 92.0, "condition": "clear"},
        ],
        "San Francisco": [
            {"day": "Monday", "temperature": 68.0, "condition": "foggy"},
            {"day": "Tuesday", "temperature": 70.0, "condition": "partly cloudy"},
        ],
        "Venice": [
            {"day": "Monday", "temperature": 68.0, "condition": "foggy"},
            {"day": "Tuesday", "temperature": 70.0, "condition": "partly cloudy"},
        ],
        "Milan": [
            {"day": "Monday", "temperature": 67.0, "condition": "cloudy"},
            {"day": "Tuesday", "temperature": 69.0, "condition": "sunny"},
        ],
    }

    if location not in current_weather_sample:
        raise ValueError(f"Location not supported: {location}")

    # Limit the number of forecast days to the available sample data
    forecast_days = min(forecast_days, len(forecast_sample[location]))

    return {
        "location": location,
        "current_temperature": current_weather_sample[location],
        "forecast": forecast_sample[location][:forecast_days],
    }


import hashlib
from typing import Dict, Union


def get_local_weather(location: str) -> Dict[str, Union[str, float, list]]:
    """Get the local weather report for a given location.

    Args:
        location: City or address to search near

    Returns:
        Dict containing:
            - location: City name
            - temperature: Current temperature in Fahrenheit
            - conditions: List of current weather conditions
    """

    # Simulate weather data generation using a hash of the location
    hash_value = int(hashlib.md5(location.encode()).hexdigest(), 16)
    temperature = (hash_value % 55) + 30  # Generate a temperature between 30 and 85
    conditions_options = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    conditions = [conditions_options[hash_value % len(conditions_options)]]

    if not location:
        raise ValueError("Location must be provided")

    return {
        "location": location,
        "temperature": temperature,
        "conditions": conditions,
    }


from typing import Dict, List, Union


def get_alerts(
    parkCode: str = "", stateCode: str = "", limit: int = 50
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Retrieve alerts for national parks based on park code or state code.

    Args:
        parkCode: A comma delimited list of park codes (each 4-10 characters in length).
        stateCode: A comma delimited list of 2 character state codes.
        limit: Number of results to return per request.

    Returns:
        Dict containing:
            - query: The query parameters used
            - alerts: List of alerts with details such as title, description, and severity
    """
    # Sample data for demonstration purposes
    sample_alerts = {
        "YELL": [
            {
                "title": "Bear Activity",
                "description": "Increased bear activity in the area.",
                "severity": "High",
            },
            {
                "title": "Trail Closure",
                "description": "Trail closed due to maintenance.",
                "severity": "Medium",
            },
        ],
        "YOSE": [
            {
                "title": "Fire Alert",
                "description": "Wildfire in the northern region.",
                "severity": "Critical",
            },
        ],
        "CA": [
            {
                "title": "Flood Warning",
                "description": "Heavy rains expected, risk of flooding.",
                "severity": "High",
            },
        ],
    }

    # Generate alerts based on parkCode or stateCode
    alerts = []
    if parkCode:
        for code in parkCode.split(","):
            code = code.strip().upper()
            if code in sample_alerts:
                alerts.extend(sample_alerts[code])
    elif stateCode:
        for code in stateCode.split(","):
            code = code.strip().upper()
            if code in sample_alerts:
                alerts.extend(sample_alerts[code])

    # Limit the number of alerts returned
    alerts = alerts[:limit]

    return {
        "query": {
            "parkCode": parkCode,
            "stateCode": stateCode,
            "limit": limit,
        },
        "alerts": alerts,
    }


import hashlib
from typing import Dict, Union


def get_cloud_cover(city: str, date: str) -> Dict[str, Union[str, int]]:
    """Retrieve the expected cloud cover percentage for a city on a given date.

    Args:
        city: City to check cloud cover for (e.g. 'London', 'New York')
        date: Date to check cloud cover (format 'YYYY-MM-DD')

    Returns:
        Dict containing:
            - city: City name
            - date: Date for the cloud cover forecast
            - cloud_cover: Expected cloud cover percentage

    Raises:
        ValueError: If the city or date format is invalid
    """
    if not city or not isinstance(city, str):
        raise ValueError("Invalid city provided")
    if not date or not isinstance(date, str):
        raise ValueError("Invalid date format provided")

    # Generate a pseudo-random cloud cover percentage based on city and date
    hash_input = f"{city.lower()}_{date}"
    hash_value = hashlib.md5(hash_input.encode()).hexdigest()
    cloud_cover_percentage = int(hash_value[:2], 16) % 101  # 0 to 100

    return {
        "city": city,
        "date": date,
        "cloud_cover": cloud_cover_percentage,
    }


from typing import Dict, Union


def get_hiking_trail_weather(hiking_trail: str) -> Dict[str, Union[str, float, list]]:
    """Returns the weather based on a given hiking trail.

    Args:
        hiking_trail: The name of the hiking trail.

    Returns:
        Dict containing:
            - trail: Name of the hiking trail
            - temperature: Current temperature in Fahrenheit
            - conditions: List of current weather conditions
    """

    trail_weather_data = {
        "Appalachian Trail": {
            "temperature": 68,
            "conditions": ["partly cloudy", "breezy"],
        },
        "Pacific Crest Trail": {"temperature": 75, "conditions": ["sunny", "dry"]},
        "John Muir Trail": {"temperature": 62, "conditions": ["overcast", "cool"]},
    }

    if hiking_trail not in trail_weather_data:
        raise ValueError(f"Hiking trail not supported: {hiking_trail}")

    weather_info = trail_weather_data[hiking_trail]
    return {
        "trail": hiking_trail,
        "temperature": weather_info["temperature"],
        "conditions": weather_info["conditions"],
    }


from datetime import datetime, timedelta
from typing import Dict, Union


def get_sunrise_sunset(city: str, date: str) -> Dict[str, Union[str, Dict[str, str]]]:
    """Get sunrise and sunset times for a city on a specific date.

    Args:
        city: City to get times for (e.g., 'New York', 'Los Angeles')
        date: Date to retrieve sunrise and sunset (format 'YYYY-MM-DD')

    Returns:
        Dict containing:
            - city: City name
            - date: Date for which the times are provided
            - times: Dict with 'sunrise' and 'sunset' times in 'HH:MM' format
    """
    # Sample data based on city hash
    city_hash = hash(city) % 24
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    sunrise_time = (
        datetime(date_obj.year, date_obj.month, date_obj.day, 6)
        + timedelta(hours=city_hash % 3)
    ).strftime("%H:%M")
    sunset_time = (
        datetime(date_obj.year, date_obj.month, date_obj.day, 18)
        + timedelta(hours=city_hash % 3)
    ).strftime("%H:%M")

    if city not in ["New York", "Los Angeles", "Chicago"]:
        raise ValueError(f"City not supported: {city}")

    return {
        "city": city,
        "date": date,
        "times": {
            "sunrise": sunrise_time,
            "sunset": sunset_time,
        },
    }


import hashlib
from typing import Dict, Union


def get_uv_index(city: str, date: str) -> Dict[str, Union[str, int]]:
    """Retrieve the UV index forecast for a particular date and city.

    Args:
        city: City to check UV index of
        date: Date of the UV index forecast

    Returns:
        Dict containing:
            - city: City name
            - date: Date of the forecast
            - uv_index: UV index value for the given date and city
    """

    supported_cities = ["Los Angeles", "New York", "Miami", "London", "Sydney"]
    if city not in supported_cities:
        raise ValueError(f"City not supported: {city}")

    # Generate a consistent but varied UV index based on city and date
    hash_input = f"{city}-{date}".encode()
    hash_value = hashlib.sha256(hash_input).hexdigest()
    uv_index = int(hash_value, 16) % 11  # UV index ranges from 0 to 10

    return {
        "city": city,
        "date": date,
        "uv_index": uv_index,
    }


import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Union


def get_weather_at_lat_long(
    latitude: float,
    longitude: float,
    start_date: Union[str, None] = None,
    end_date: Union[str, None] = None,
) -> List[Dict[str, Union[str, float, List[str]]]]:
    """Returns the weather on the specified dates, at the given latitude and longitude.

    Args:
        latitude: The latitude of the location to be looked up.
        longitude: The longitude of the location to be looked up.
        start_date: Forecast start date (YYYY-MM-DD). Defaults to current date if not provided.
        end_date: Forecast end date (YYYY-MM-DD). Defaults to start_date if not provided.

    Returns:
        List of dictionaries, each containing:
            - date: The date of the forecast
            - temperature: Forecasted temperature in Fahrenheit
            - conditions: List of forecasted weather conditions
    """

    def generate_weather_data(date: str) -> Dict[str, Union[str, float, List[str]]]:
        # Create a hash-based pseudo-random temperature and conditions
        hash_input = f"{latitude},{longitude},{date}".encode()
        hash_digest = hashlib.sha256(hash_input).hexdigest()
        temperature = (
            60 + int(hash_digest[:2], 16) % 40
        )  # Temperature between 60 and 100
        conditions_options = ["sunny", "rainy", "cloudy", "windy", "stormy"]
        conditions = [
            conditions_options[
                int(hash_digest[i : i + 2], 16) % len(conditions_options)
            ]
            for i in range(2, 10, 2)
        ]
        return {"date": date, "temperature": temperature, "conditions": conditions}

    # Determine the date range
    if start_date is None:
        start_date = datetime.now().strftime("%Y-%m-%d")
    if end_date is None:
        end_date = start_date

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if start > end:
        raise ValueError("start_date cannot be after end_date")

    # Generate weather data for each day in the range
    weather_data = []
    current_date = start
    while current_date <= end:
        date_str = current_date.strftime("%Y-%m-%d")
        weather_data.append(generate_weather_data(date_str))
        current_date += timedelta(days=1)

    return weather_data


import hashlib
from typing import Dict, List, Union


def get_weather_forecast(location: str) -> Dict[str, Union[str, List[str]]]:
    """Gets the weather forecast for a given location.

    Args:
        location: The location to get the forecast for.

    Returns:
        Dict containing:
            - location: The location name
            - forecast: List of weather conditions for the next 3 days
    """
    if not location:
        raise ValueError("Location must be provided")

    # Generate a hash-based pseudo-random forecast
    hash_value = int(hashlib.sha256(location.encode()).hexdigest(), 16)
    conditions = ["sunny", "cloudy", "rainy", "stormy", "snowy", "windy"]

    forecast = [conditions[(hash_value >> (i * 8)) % len(conditions)] for i in range(3)]

    return {
        "location": location,
        "forecast": forecast,
    }


from typing import Dict, Union


def ski_resort_current_condition(resort: str) -> Dict[str, Union[str, int, float]]:
    """Retrieve the current snow conditions for a ski resort.

    Args:
        resort: Resort to get conditions for

    Returns:
        Dict containing:
            - resort: Resort name
            - snow_depth: Current snow depth in inches
            - temperature: Current temperature in Fahrenheit
            - conditions: Current snow conditions (e.g., 'powder', 'packed')
    """

    sample_conditions = {
        "Aspen": {"snow_depth": 24, "temperature": 30, "conditions": "powder"},
        "Whistler": {"snow_depth": 36, "temperature": 28, "conditions": "packed"},
        "Vail": {"snow_depth": 20, "temperature": 32, "conditions": "icy"},
    }

    if resort not in sample_conditions:
        raise ValueError(f"Resort not supported: {resort}")

    resort_conditions = sample_conditions[resort]

    return {
        "resort": resort,
        "snow_depth": resort_conditions["snow_depth"],
        "temperature": resort_conditions["temperature"],
        "conditions": resort_conditions["conditions"],
    }


from typing import Dict, List


def ski_resort_forecast(
    resort: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Retrieve the snowfall forecast for a ski resort.

    Args:
        resort: Resort to get snow forecast for

    Returns:
        Dict containing:
            - resort: Name of the ski resort
            - forecast: List of dictionaries with daily snowfall forecast
                - day: Day of the forecast
                - snowfall: Expected snowfall in inches
    """

    sample_forecasts = {
        "Aspen": [
            {"day": "Monday", "snowfall": 5.0},
            {"day": "Tuesday", "snowfall": 2.5},
            {"day": "Wednesday", "snowfall": 0.0},
        ],
        "Whistler": [
            {"day": "Monday", "snowfall": 8.0},
            {"day": "Tuesday", "snowfall": 4.0},
            {"day": "Wednesday", "snowfall": 1.0},
        ],
        "Chamonix": [
            {"day": "Monday", "snowfall": 3.0},
            {"day": "Tuesday", "snowfall": 6.0},
            {"day": "Wednesday", "snowfall": 2.0},
        ],
    }

    if resort not in sample_forecasts:
        raise ValueError(f"Resort not supported: {resort}")

    return {
        "resort": resort,
        "forecast": sample_forecasts[resort],
    }


from typing import Dict, List, Union


def suggest_clothes_for_weather(
    location: str, date: str
) -> Dict[str, Union[str, List[str]]]:
    """Suggest appropriate clothes based on the weather for a specific date and location.

    Args:
        location: City or address to get weather for (e.g. 'London', 'New York')
        date: Forecast date in the format YYYY-MM-DD

    Returns:
        Dict containing:
            - location: City name
            - date: Forecast date
            - suggested_clothes: List of suggested clothing items
    """

    # Mock weather data based on location hash
    weather_conditions = {
        "sunny": ["t-shirt", "shorts", "sunglasses"],
        "rainy": ["raincoat", "umbrella", "waterproof boots"],
        "snowy": ["winter coat", "gloves", "scarf"],
        "windy": ["windbreaker", "jeans", "hat"],
        "cloudy": ["light jacket", "jeans", "sneakers"],
    }

    # Generate a pseudo-random weather condition based on the location and date
    hash_value = hash(location + date) % len(weather_conditions)
    condition = list(weather_conditions.keys())[hash_value]

    return {
        "location": location,
        "date": date,
        "suggested_clothes": weather_conditions[condition],
    }


from typing import Dict, List, Optional, Union


def tornado_lookup(
    location: Optional[Dict[str, Union[str, Dict[str, float]]]] = None,
    tornado_name: Optional[str] = None,
    EF_rating: Optional[int] = None,
    tornado_category: Optional[str] = None,
    tornado_damage: Optional[str] = None,
    damage_indicators: Optional[List[str]] = None,
) -> Dict[str, Union[str, int, List[str], Dict[str, Union[str, float]]]]:
    """Find tornado reports that match given parameters.

    Args:
        location: Dictionary containing country, state, city, and coordinates of the tornado.
        tornado_name: Name of the tornado event.
        EF_rating: Enhanced Fujita scale rating from 0-5.
        tornado_category: F category of the tornado.
        tornado_damage: Amount of damage from the tornado (e.g., 'light', 'moderate').
        damage_indicators: List of damage indicators involved in the tornado.

    Returns:
        Dict containing:
            - tornado_name: Name of the tornado event.
            - EF_rating: Enhanced Fujita scale rating.
            - location: Dictionary with country, state, city, and coordinates.
            - tornado_category: F category of the tornado.
            - tornado_damage: Amount of damage from the tornado.
            - damage_indicators: List of damage indicators.
    """

    sample_data = {
        "tornado_name": "Twister 2023",
        "EF_rating": 3,
        "location": {
            "country": "USA",
            "state": "Oklahoma",
            "city": "Norman",
            "coordinates": {"latitude": 35.2226, "longitude": -97.4395},
        },
        "tornado_category": "F3",
        "tornado_damage": "considerable",
        "damage_indicators": [
            "trees uprooted",
            "roofs torn off",
            "vehicles overturned",
        ],
    }

    # Simulate a simple matching mechanism
    if location and location.get("city") != sample_data["location"]["city"]:
        raise ValueError("No tornado reports found for the specified location.")
    if tornado_name and tornado_name != sample_data["tornado_name"]:
        raise ValueError("No tornado reports found with the specified name.")
    if EF_rating is not None and EF_rating != sample_data["EF_rating"]:
        raise ValueError("No tornado reports found with the specified EF rating.")
    if tornado_category and tornado_category != sample_data["tornado_category"]:
        raise ValueError("No tornado reports found with the specified category.")
    if tornado_damage and tornado_damage != sample_data["tornado_damage"]:
        raise ValueError("No tornado reports found with the specified damage level.")
    if damage_indicators and not set(damage_indicators).issubset(
        set(sample_data["damage_indicators"])
    ):
        raise ValueError(
            "No tornado reports found with the specified damage indicators."
        )

    return sample_data
