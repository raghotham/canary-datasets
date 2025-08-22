# Location Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def find_bathroom(
    center: Union[str, float], radius: float = 5, open_now: bool = False
) -> Dict[str, Union[str, float, bool, list]]:
    """Locate a public bathroom near a specified location.

    Args:
        center: Search center (accepts: address, intersection, latitude/longitude, or business name)
        radius: Radius of search in miles
        open_now: Filter for bathrooms currently open

    Returns:
        Dict containing:
            - center: The search center used
            - radius: The radius of the search
            - open_now: Whether the search was filtered for currently open bathrooms
            - bathrooms: List of nearby bathrooms with details
    """
    # Simulated data based on the hash of the center
    hash_value = hash(center) % 3
    sample_data = [
        {
            "name": "Central Park Restroom",
            "address": "Central Park, New York, NY",
            "open_now": True,
            "distance": 1.2,
        },
        {
            "name": "Union Square Public Toilet",
            "address": "Union Square, San Francisco, CA",
            "open_now": False,
            "distance": 3.5,
        },
        {
            "name": "City Hall Restroom",
            "address": "City Hall, Boston, MA",
            "open_now": True,
            "distance": 0.8,
        },
    ]

    bathrooms = [
        bathroom
        for bathroom in sample_data
        if bathroom["distance"] <= radius and (not open_now or bathroom["open_now"])
    ]

    if not bathrooms:
        raise ValueError("No bathrooms found within the specified parameters.")

    return {
        "center": center,
        "radius": radius,
        "open_now": open_now,
        "bathrooms": bathrooms,
    }


import hashlib
from typing import Dict, List, Optional, Union


def find_nearby_activities(
    location: str,
    activity_type: Optional[str] = None,
    date: Optional[str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find activities near a location of a given type.

    Args:
        location: City or address to search near
        activity_type: Activity type to search for (e.g. 'hiking', 'museum')
        date: Date to search for activities on (format: 'YYYY-MM-DD')

    Returns:
        Dict containing:
            - location: The location searched
            - activities: List of activities with details such as name, type, and distance
    """
    if not location:
        raise ValueError("Location is required")

    # Generate a consistent but varied list of activities based on the location
    hash_seed = f"{location}-{activity_type}-{date}".encode()
    hash_value = int(hashlib.sha256(hash_seed).hexdigest(), 16)

    sample_activities = [
        {"name": "Central Park Walk", "type": "hiking", "distance": 1.2},
        {"name": "Modern Art Museum", "type": "museum", "distance": 3.5},
        {"name": "City Zoo Visit", "type": "zoo", "distance": 2.8},
        {"name": "Historic Downtown Tour", "type": "tour", "distance": 0.5},
        {"name": "River Kayaking", "type": "water sports", "distance": 4.0},
    ]

    # Filter activities by type if specified
    if activity_type:
        sample_activities = [
            activity
            for activity in sample_activities
            if activity["type"] == activity_type
        ]

    # Select a subset of activities based on the hash value
    selected_activities = [
        sample_activities[i % len(sample_activities)] for i in range(hash_value % 3 + 1)
    ]

    return {
        "location": location,
        "activities": selected_activities,
    }


from typing import Dict


def get_coords(city: str) -> Dict[str, float]:
    """Get the latitude and longitude of a given city.

    Args:
        city: The name of the city to get coordinates for (e.g. 'London', 'New York')

    Returns:
        Dict containing:
            - latitude: Latitude of the city
            - longitude: Longitude of the city
    """
    sample_coords = {
        "New York": (40.7128, -74.0060),
        "London": (51.5074, -0.1278),
        "Tokyo": (35.6895, 139.6917),
        "Paris": (48.8566, 2.3522),
        "Sydney": (-33.8688, 151.2093),
        "San Francisco": (37.7749, -122.4194),
        "Salt Lake City": (40.7608, -111.8910),
    }
    if city not in sample_coords:
        raise ValueError(f"City not supported: {city}")

    latitude, longitude = sample_coords[city]
    return {
        "latitude": latitude,
        "longitude": longitude,
    }


from typing import Dict, Literal, Optional


def get_home_team(
    location: str, league: Optional[Literal["mlb", "nfl", "nba", "mls"]] = None
) -> Dict[str, str]:
    """Gets the professional sports team in your area.

    Args:
        location: The city, state, or zipcode to find the team for
        league: The professional sports league ('mlb', 'nfl', 'nba', 'mls')

    Returns:
        Dict containing:
            - location: The input location
            - team: The name of the home team
            - league: The league of the home team
    """

    teams_data = {
        "New York": {
            "mlb": "New York Yankees",
            "nfl": "New York Giants",
            "nba": "New York Knicks",
            "mls": "New York City FC",
        },
        "Los Angeles": {
            "mlb": "Los Angeles Dodgers",
            "nfl": "Los Angeles Rams",
            "nba": "Los Angeles Lakers",
            "mls": "LA Galaxy",
        },
        "Chicago": {
            "mlb": "Chicago Cubs",
            "nfl": "Chicago Bears",
            "nba": "Chicago Bulls",
            "mls": "Chicago Fire",
        },
        "Boston": {
            "mlb": "Boston Red Sox",
            "nfl": "New England Patriots",
            "nba": "Boston Celtics",
            "mls": "New England Revolution",
        },
        "Phoenix": {
            "mlb": "Arizona Diamondbacks",
            "nfl": "Arizona Cardinals",
            "nba": "Phoenix Suns",
            "mls": "Phoenix Rising",
        },
    }

    if location not in teams_data:
        raise ValueError(f"Location not supported: {location}")

    if league:
        if league not in teams_data[location]:
            raise ValueError(f"League not supported in location: {location}")
        return {
            "location": location,
            "team": teams_data[location][league],
            "league": league,
        }

    # Default to MLB if no league is specified
    return {"location": location, "team": teams_data[location]["mlb"], "league": "mlb"}


from typing import Dict, Union


def get_latlong(address: str) -> Dict[str, Union[str, float]]:
    """Get the latitude and longitude of a street address.

    Args:
        address: Street address to get co-ordinates for

    Returns:
        Dict containing:
            - address: The input street address
            - latitude: Latitude of the address
            - longitude: Longitude of the address
    """
    # Simulated hash-based generation for consistent sample data
    sample_data = {
        "1600 Amphitheatre Parkway, Mountain View, CA": (37.4221, -122.0841),
        "1 Infinite Loop, Cupertino, CA": (37.3318, -122.0312),
        "350 Fifth Avenue, New York, NY": (40.7484, -73.9857),
    }

    if address not in sample_data:
        raise ValueError(f"Address not supported: {address}")

    latitude, longitude = sample_data[address]
    return {
        "address": address,
        "latitude": latitude,
        "longitude": longitude,
    }


from typing import Dict, Optional, Union


def get_location(
    location: str, origin: Optional[str] = None
) -> Dict[str, Union[str, Dict[str, Union[str, int]]]]:
    """Get details of a location and directions to the location if origin is provided.

    Args:
        location: Location to get details about.
        origin: Origin from which to get directions to location.

    Returns:
        Dict containing:
            - location_details: Dict with location name and a brief description
            - directions (optional): Dict with origin, destination, and estimated travel time in minutes
    """

    location_details_sample = {
        "Eiffel Tower": {
            "name": "Eiffel Tower",
            "description": "An iconic symbol of Paris, France.",
        },
        "Statue of Liberty": {
            "name": "Statue of Liberty",
            "description": "A colossal neoclassical sculpture on Liberty Island in New York Harbor.",
        },
        "Great Wall of China": {
            "name": "Great Wall of China",
            "description": "A series of fortifications made of stone, brick, tamped earth, wood, and other materials.",
        },
    }

    if location not in location_details_sample:
        raise ValueError(f"Location not supported: {location}")

    directions_sample = {
        ("New York", "Statue of Liberty"): {
            "origin": "New York",
            "destination": "Statue of Liberty",
            "travel_time": 30,
        },
        ("Paris", "Eiffel Tower"): {
            "origin": "Paris",
            "destination": "Eiffel Tower",
            "travel_time": 15,
        },
        ("Beijing", "Great Wall of China"): {
            "origin": "Beijing",
            "destination": "Great Wall of China",
            "travel_time": 60,
        },
    }

    result = {"location_details": location_details_sample[location]}

    if origin:
        directions_key = (origin, location)
        if directions_key not in directions_sample:
            raise ValueError(f"Directions not available from {origin} to {location}")
        result["directions"] = directions_sample[directions_key]

    return result


from typing import Dict


def get_user_location(user_id: str) -> Dict[str, Union[str, float]]:
    """Retrieves the user's current geographic location.

    Args:
        user_id: The unique identifier of the user whose location is to be retrieved.

    Returns:
        Dict containing:
            - latitude: Current latitude of the user
            - longitude: Current longitude of the user
            - city: Name of the city where the user is located
    """

    # Simulate user location data based on a hash of the user_id
    hash_value = hash(user_id)
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    latitudes = [40.7128, 34.0522, 41.8781, 29.7604, 33.4484]
    longitudes = [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740]

    index = hash_value % len(cities)

    return {
        "latitude": latitudes[index],
        "longitude": longitudes[index],
        "city": cities[index],
    }


from typing import Dict, List, Union


def search_venues(
    city_or_postcode: str,
    date_range: Dict[str, str],
    capacity_min: int = 1,
    amenities: List[str] = [],
    indoor_only: bool = True,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, List[str]]]]]]:
    """Find studios or locations for a shoot based on specified criteria.

    Args:
        city_or_postcode: City or UK postcode to search for venues.
        date_range: Dictionary with 'from' and 'to' keys indicating the date range for the shoot.
        capacity_min: Minimum number of people the venue should accommodate.
        amenities: List of required facilities (e.g., 'changing_room', 'makeup_area').
        indoor_only: Whether to search only for indoor venues.

    Returns:
        Dict containing:
            - location: The city or postcode searched.
            - venues: List of venues matching the criteria, each with:
                - name: Name of the venue
                - capacity: Maximum capacity of the venue
                - amenities: List of amenities available at the venue
                - indoor: Boolean indicating if the venue is indoor
    """
    sample_venues = {
        "London": [
            {
                "name": "Studio One",
                "capacity": 50,
                "amenities": ["changing_room", "makeup_area"],
                "indoor": True,
            },
            {
                "name": "Open Air Venue",
                "capacity": 200,
                "amenities": ["parking"],
                "indoor": False,
            },
        ],
        "Manchester": [
            {
                "name": "Northern Lights Studio",
                "capacity": 30,
                "amenities": ["natural_light", "kitchenette"],
                "indoor": True,
            },
            {
                "name": "City Center Loft",
                "capacity": 100,
                "amenities": ["blackout", "shower"],
                "indoor": True,
            },
        ],
    }

    if city_or_postcode not in sample_venues:
        raise ValueError(f"Location not supported: {city_or_postcode}")

    venues = sample_venues[city_or_postcode]
    filtered_venues = [
        venue
        for venue in venues
        if venue["capacity"] >= capacity_min
        and all(amenity in venue["amenities"] for amenity in amenities)
        and (not indoor_only or venue["indoor"])
    ]

    return {"location": city_or_postcode, "venues": filtered_venues}


from typing import Dict, List, Union


def find_nearby_library(
    location: str, open_now: bool = False
) -> Dict[str, Union[str, List[Dict[str, Union[str, bool]]]]]:
    """Find libraries near a given location.

    Args:
        location: City or address to search around (e.g. 'San Francisco', '123 Main St, Springfield')
        open_now: Filter results to places that are currently open

    Returns:
        Dict containing:
            - location: The search location
            - libraries: List of dictionaries with library details
                - name: Name of the library
                - address: Address of the library
                - open_now: Boolean indicating if the library is currently open
    """

    sample_libraries = {
        "San Francisco": [
            {
                "name": "San Francisco Public Library",
                "address": "100 Larkin St, San Francisco, CA",
                "open_now": True,
            },
            {
                "name": "Mission Bay Library",
                "address": "960 4th St, San Francisco, CA",
                "open_now": False,
            },
        ],
        "New York": [
            {
                "name": "New York Public Library",
                "address": "476 5th Ave, New York, NY",
                "open_now": True,
            },
            {
                "name": "Brooklyn Public Library",
                "address": "10 Grand Army Plaza, Brooklyn, NY",
                "open_now": True,
            },
        ],
    }

    if location not in sample_libraries:
        raise ValueError(f"Location not supported: {location}")

    libraries = sample_libraries[location]
    if open_now:
        libraries = [lib for lib in libraries if lib["open_now"]]

    return {
        "location": location,
        "libraries": libraries,
    }


from typing import Dict, List, Union


def find_places(
    search_query: str,
    country: str,
    city: Union[str, None] = None,
    open_now: Union[bool, None] = None,
    max_distance: float = 50,
) -> List[Dict[str, Union[str, float, bool]]]:
    """Returns a list of places based on search criteria.

    Args:
        search_query: The type of place to search for (e.g., 'cinema', 'restaurant').
        country: The country where the place is located.
        city: The city where the place is located (optional).
        open_now: True if the place is open currently, false otherwise (optional).
        max_distance: Maximum distance from the user to the place in km (default is 50).

    Returns:
        List of dictionaries, each containing:
            - name: Name of the place
            - address: Address of the place
            - distance: Distance from the user in km
            - open_now: Boolean indicating if the place is currently open
    """
    # Mock data for demonstration purposes
    sample_data = [
        {
            "name": "Cinema Paradiso",
            "address": "123 Movie St",
            "distance": 10.5,
            "open_now": True,
        },
        {
            "name": "Gourmet Restaurant",
            "address": "456 Food Ave",
            "distance": 5.2,
            "open_now": False,
        },
        {
            "name": "City Gym",
            "address": "789 Fitness Blvd",
            "distance": 3.8,
            "open_now": True,
        },
    ]

    # Filter based on search_query
    filtered_places = [
        place for place in sample_data if search_query.lower() in place["name"].lower()
    ]

    # Filter based on open_now if specified
    if open_now is not None:
        filtered_places = [
            place for place in filtered_places if place["open_now"] == open_now
        ]

    # Filter based on max_distance
    filtered_places = [
        place for place in filtered_places if place["distance"] <= max_distance
    ]

    # Simulate city and country filtering (mocked, as no real data is available)
    if city:
        filtered_places = [
            place
            for place in filtered_places
            if city.lower() in place["address"].lower()
        ]
    if country != "US":
        raise ValueError(f"Country not supported: {country}")

    return filtered_places


from typing import Dict


def get_city(latitude: float, longitude: float) -> Dict[str, str]:
    """Get the name of the city at a given latitude and longitude.

    Args:
        latitude: The latitude (use negative numbers for S)
        longitude: The longitude (use negative numbers for W)

    Returns:
        Dict containing:
            - city: Name of the city at the given coordinates
    """
    # Mock data simulating a hash-based lookup for city names
    sample_data = {
        (42.3601, -71.0589): "Boston",
        (35.6895, 139.6917): "Tokyo",
        (48.8566, 2.3522): "Paris",
        (-33.8688, 151.2093): "Sydney",
        (51.5074, -0.1278): "London",
    }

    # Rounding to 4 decimal places to simulate realistic coordinate matching
    rounded_coords = (round(latitude, 4), round(longitude, 4))

    if rounded_coords not in sample_data:
        raise ValueError(f"Coordinates not supported: {rounded_coords}")

    return {
        "city": sample_data[rounded_coords],
    }


from typing import Dict, Optional, Tuple


def get_coordinates(
    address: Optional[str] = None,
) -> Dict[str, Union[str, Tuple[float, float]]]:
    """Retrieve coordinates based on an address or return current location coordinates.

    Args:
        address: The full street address of the location to retrieve the coordinates for.

    Returns:
        Dict containing:
            - address: Provided address or 'Current Location'
            - coordinates: Tuple of latitude and longitude
    """

    sample_addresses = {
        "1600 Amphitheatre Parkway, Mountain View, CA": (37.4221, -122.0841),
        "1 Infinite Loop, Cupertino, CA": (37.3318, -122.0312),
        "350 Fifth Avenue, New York, NY": (40.7484, -73.9857),
        "790 7th Ave, New York, NY": (40.7790, -73.9827),
    }

    if address:
        if address not in sample_addresses:
            raise ValueError(f"Address not supported: {address}")
        return {
            "address": address,
            "coordinates": sample_addresses[address],
        }
    else:
        # Mock current location coordinates
        return {
            "address": "Current Location",
            "coordinates": (34.0522, -118.2437),  # Example: Los Angeles, CA
        }


from typing import Dict, Union


def get_current_location() -> Dict[str, Union[float, str]]:
    """Get the device's current GPS coordinates.

    Returns:
        Dict containing:
            - latitude: Latitude in decimal degrees
            - longitude: Longitude in decimal degrees
    """

    # Simulated GPS coordinates for demonstration purposes
    sample_coordinates = {
        "latitude": 37.7749,  # Example: San Francisco
        "longitude": -122.4194,
    }

    return sample_coordinates


import hashlib
from typing import Dict, Union


def get_distance(point_A: str, point_B: str) -> Dict[str, Union[str, float]]:
    """Get the distance between two locations.

    Args:
        point_A: The first location input
        point_B: The second location input

    Returns:
        Dict containing:
            - point_A: Name of the first location
            - point_B: Name of the second location
            - distance: Distance between the two locations in miles
    """

    if not point_A or not point_B:
        raise ValueError("Both point_A and point_B must be provided")

    # Simulate distance calculation using hash-based pseudo-random generation
    combined = f"{point_A}-{point_B}".encode("utf-8")
    hash_value = hashlib.md5(combined).hexdigest()
    # Convert hash to a float between 10 and 500 miles
    distance = 10 + (int(hash_value, 16) % 491)

    return {
        "point_A": point_A,
        "point_B": point_B,
        "distance": float(distance),
    }


from typing import Dict, List, Union


def get_lat_long(
    location_name: str, location_city: str = None, location_country: str = None
) -> List[Dict[str, Union[str, float]]]:
    """Gets the latitude and longitude of a given location name.

    Args:
        location_name: The name of the location.
        location_city: The name of the city the location is in.
        location_country: The name of the country the location is in.

    Returns:
        List of dictionaries, each containing:
            - location_name: Name of the location
            - latitude: Latitude of the location
            - longitude: Longitude of the location
    """

    # Sample data for demonstration purposes
    sample_data = {
        ("Eiffel Tower", "Paris", "France"): (48.8584, 2.2945),
        ("Statue of Liberty", "New York", "USA"): (40.6892, -74.0445),
        ("Colosseum", "Rome", "Italy"): (41.8902, 12.4922),
        ("Wollaton Park", "Nottingham", "UK"): (52.9492, -1.1512),
        ("Wollaton Park", "Nottingham", "United Kingdom"): (52.9492, -1.1512),
        ("Nottingham", "None", "UK"): (52.9492, -1.1512),
        # Add entries for location-only lookups
        ("Wollaton Park", None, None): (52.9492, -1.1512),
        ("Eiffel Tower", None, None): (48.8584, 2.2945),
        ("Statue of Liberty", None, None): (40.6892, -74.0445),
        ("Colosseum", None, None): (41.8902, 12.4922),
        ("Nottingham", None, None): (52.9492, -1.1512),
    }

    def find_matching_location(
        location_name, location_city, location_country, available_keys
    ):
        """Find matching location with flexible matching logic."""
        # First try exact match
        exact_key = (location_name, location_city, location_country)
        if exact_key in available_keys:
            return exact_key

        # Try location name only if city/country are None
        if location_city is None and location_country is None:
            name_only_key = (location_name, None, None)
            if name_only_key in available_keys:
                return name_only_key

        # Try to find any match with the same location name
        for key in available_keys:
            if key[0] == location_name:
                # If we find a match with the same location name, use it
                return key

        # Try partial matches if city is provided but country is None
        if location_city is not None and location_country is None:
            for key in available_keys:
                if key[0] == location_name and key[1] == location_city:
                    return key

        # Try partial matches if country is provided but city is None
        if location_country is not None and location_city is None:
            for key in available_keys:
                if key[0] == location_name and key[2] == location_country:
                    return key

        return None

    # Find matching location using flexible matching
    matching_key = find_matching_location(
        location_name, location_city, location_country, sample_data.keys()
    )

    if matching_key is None:
        raise ValueError(
            f"Location not supported: {location_name}, {location_city}, {location_country}"
        )

    latitude, longitude = sample_data[matching_key]

    return [
        {"location_name": location_name, "latitude": latitude, "longitude": longitude}
    ]


from typing import Dict, List, Optional


def get_nearby_activities(
    location_name: str,
    location_city: Optional[str] = None,
    location_country: Optional[str] = None,
    activity_type: Optional[str] = None,
) -> Dict[str, List[str]]:
    """Returns a list of activities near the specified location.

    Args:
        location_name: The name of the location.
        location_city: The name of the city the location is in.
        location_country: The name of the country the location is in.
        activity_type: The type of activity to be looked up.

    Returns:
        Dict containing:
            - activities: List of activities near the specified location.
    """

    # Sample data based on location_name
    sample_activities = {
        "Central Park": ["Jogging", "Picnic", "Bird Watching"],
        "Eiffel Tower": ["Photography", "Sightseeing", "Dining"],
        "Sydney Opera House": ["Concert", "Tour", "Dining"],
        "Wollaton Park": ["Jogging", "Picnic", "Bird Watching"],
    }

    if location_name not in sample_activities:
        raise ValueError(f"Location not supported: {location_name}")

    activities = sample_activities[location_name]

    if activity_type:
        activities = [
            activity
            for activity in activities
            if activity_type.lower() in activity.lower()
        ]
        if not activities:
            raise ValueError(f"No activities found for type: {activity_type}")

    return {"activities": activities}


from typing import Dict, Union


def get_point_elevation(
    coordinates: Union[Dict[str, float], None]
) -> Dict[str, Union[float, str]]:
    """Retrieve elevation for a given point.

    Args:
        coordinates: A dictionary containing 'lat' and 'lng' keys representing the latitude and longitude of the point.

    Returns:
        Dict containing:
            - elevation: Elevation of the point in meters
            - unit: Unit of the elevation
    """
    if coordinates is None:
        raise ValueError("Coordinates must be provided")

    lat = coordinates.get("lat")
    lng = coordinates.get("lng")

    if lat is None or lng is None:
        raise ValueError("Both latitude and longitude must be provided")

    # Simulate elevation data based on latitude and longitude
    elevation = (hash((lat, lng)) % 1000) + 100  # Elevation in meters

    return {
        "elevation": elevation,
        "unit": "meters",
    }


from datetime import datetime
from typing import Dict, Union


def get_user_location_datetime() -> Dict[str, Union[str, str]]:
    """Returns the user's current location, timezone, and local date/time.

    Returns:
        Dict containing:
            - location: User's current city
            - timezone: User's current timezone
            - local_datetime: User's local date and time as string
    """

    # Sample data for demonstration purposes
    locations = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney",
        "Mumbai": "Asia/Kolkata",
    }

    # Mock location selection based on hash for consistency
    location_list = list(locations.keys())
    location = location_list[hash("user") % len(location_list)]
    timezone = locations[location]

    # Mock current time as string
    mock_datetime = "2025-08-22 14:30:00"

    return {"location": location, "timezone": timezone, "local_datetime": mock_datetime}


from typing import Dict, List, Union


def place_details(
    place_id: str, fields: List[str] = None
) -> Dict[str, Union[str, Dict[str, Union[str, float]], List[str]]]:
    """Retrieves detailed information about a specific place.

    Args:
        place_id: Unique identifier for the place, such as a Google Places ID.
        fields: Optional list of specific fields to return, e.g., ['name', 'address', 'coordinates', 'opening_hours', 'phone_number'].

    Returns:
        Dict containing requested fields with sample data:
            - name: Name of the place
            - address: Address of the place
            - coordinates: Dict with 'latitude' and 'longitude'
            - opening_hours: List of opening hours for each day
            - phone_number: Contact phone number
    """
    # Sample data based on hash of place_id for consistency
    sample_data = {
        "name": "Sample Place",
        "address": "123 Sample St, Sample City, SC 12345",
        "coordinates": {"latitude": 40.7128, "longitude": -74.0060},
        "opening_hours": [
            "Monday: 9 AM - 5 PM",
            "Tuesday: 9 AM - 5 PM",
            "Wednesday: 9 AM - 5 PM",
            "Thursday: 9 AM - 5 PM",
            "Friday: 9 AM - 5 PM",
            "Saturday: 10 AM - 4 PM",
            "Sunday: Closed",
        ],
        "phone_number": "+1 555-123-4567",
    }

    if not place_id:
        raise ValueError("place_id is required")

    # If fields are specified, filter the sample data
    if fields:
        return {field: sample_data[field] for field in fields if field in sample_data}

    return sample_data


from typing import Dict, Union


def postcode_convert(postcode: str) -> Dict[str, Union[str, float]]:
    """Convert UK/US postcodes/zipcodes into location data.

    Args:
        postcode: The postcode or zipcode to be located

    Returns:
        Dict containing:
            - postcode: The original postcode or zipcode
            - city: The city name associated with the postcode
            - latitude: The latitude of the location
            - longitude: The longitude of the location
    """

    # Sample data for demonstration purposes
    sample_data = {
        "SW1A 1AA": {"city": "London", "latitude": 51.5014, "longitude": -0.1419},
        "90210": {"city": "Beverly Hills", "latitude": 34.0901, "longitude": -118.4065},
        "10001": {"city": "New York", "latitude": 40.7128, "longitude": -74.0060},
        "SW19": {"city": "London", "latitude": 51.4214, "longitude": -0.2053},
    }

    if postcode not in sample_data:
        raise ValueError(f"Postcode not supported: {postcode}")

    location_data = sample_data[postcode]
    return {
        "postcode": postcode,
        "city": location_data["city"],
        "latitude": location_data["latitude"],
        "longitude": location_data["longitude"],
    }
