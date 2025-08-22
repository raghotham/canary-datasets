# Real Estate Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def details(id: int) -> Dict[str, Union[int, str, bool]]:
    """Get details of a given bathroom.

    Args:
        id: ID of the bathroom

    Returns:
        Dict containing:
            - id: ID of the bathroom
            - location: Location description of the bathroom
            - is_clean: Boolean indicating if the bathroom is clean
            - has_accessible_facilities: Boolean indicating if the bathroom has accessible facilities
    """

    sample_data = {
        1: {
            "location": "First Floor, Near Elevator",
            "is_clean": True,
            "has_accessible_facilities": True,
        },
        2: {
            "location": "Second Floor, Near Cafeteria",
            "is_clean": False,
            "has_accessible_facilities": False,
        },
        3: {
            "location": "Ground Floor, Near Reception",
            "is_clean": True,
            "has_accessible_facilities": True,
        },
    }

    if id not in sample_data:
        raise ValueError(f"Bathroom ID not found: {id}")

    bathroom_details = sample_data[id]
    return {
        "id": id,
        "location": bathroom_details["location"],
        "is_clean": bathroom_details["is_clean"],
        "has_accessible_facilities": bathroom_details["has_accessible_facilities"],
    }


import hashlib
from typing import Dict, List, Literal, Optional, Union


def find_contractors(
    service_type: str,
    location: Dict[str, str],
    date_window: Optional[Dict[str, str]] = None,
    certifications: Optional[List[str]] = None,
    budget_max: Optional[float] = None,
    emergency: bool = False,
    sort_by: Literal[
        "rating_desc", "price_asc", "soonest_availability"
    ] = "rating_desc",
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, bool]]]]]:
    """Discover qualified contractors near an address, filtered by service type, availability, and constraints.

    Args:
        service_type: Type of service, e.g., 'plumbing', 'electrical', 'HVAC', 'appliance_repair'.
        location: Service location details including city and optional address and postal code.
        date_window: Desired service date window with 'start_date' and 'end_date'.
        certifications: Required certifications/tags, e.g., ['licensed','bonded','EPA_608'].
        budget_max: Maximum estimated cost in local currency.
        emergency: Prioritize emergency-ready providers.
        sort_by: Sort order: 'rating_desc', 'price_asc', 'soonest_availability'.

    Returns:
        Dict containing:
            - service_type: The type of service requested.
            - contractors: List of contractors with details such as name, rating, price, availability, and emergency readiness.
    """

    # Mock data generation
    def generate_contractor_data(name_seed: str) -> Dict[str, Union[str, float, bool]]:
        hash_seed = hashlib.sha256(name_seed.encode()).hexdigest()
        return {
            "name": f"Contractor {hash_seed[:6]}",
            "rating": round((int(hash_seed[0], 16) / 15) * 5, 1),  # Rating out of 5
            "price": round(
                (int(hash_seed[1:3], 16) / 255) * 1000, 2
            ),  # Price in local currency
            "availability": f"2023-10-{int(hash_seed[3:5], 16) % 30 + 1:02d}",  # Random date in October 2023
            "emergency_ready": int(hash_seed[5], 16) % 2 == 0,
        }

    # Sample contractors
    contractors = [
        generate_contractor_data(f"{service_type}{location['city']}{i}")
        for i in range(5)
    ]

    # Filtering based on constraints
    if budget_max is not None:
        contractors = [c for c in contractors if c["price"] <= budget_max]
    if emergency:
        contractors = [c for c in contractors if c["emergency_ready"]]
    if date_window:
        contractors = [
            c
            for c in contractors
            if date_window["start_date"] <= c["availability"] <= date_window["end_date"]
        ]

    # Sorting
    if sort_by == "rating_desc":
        contractors.sort(key=lambda x: x["rating"], reverse=True)
    elif sort_by == "price_asc":
        contractors.sort(key=lambda x: x["price"])
    elif sort_by == "soonest_availability":
        contractors.sort(key=lambda x: x["availability"])

    return {"service_type": service_type, "contractors": contractors}


import hashlib
from datetime import datetime
from typing import Dict, Optional, Union


def get_build_age(
    build_addr: Optional[str] = None, coordinates: Optional[Dict[str, float]] = None
) -> Dict[str, Union[str, int]]:
    """Retrieve the age of a given building, in months.

    Args:
        build_addr: The full address of the building to look up.
        coordinates: The geolocation of the building to look up, with 'lat' and 'lng'.

    Returns:
        Dict containing:
            - identifier: A unique identifier for the building
            - age_months: The age of the building in months

    Raises:
        ValueError: If neither build_addr nor coordinates are provided.
    """
    if not build_addr and not coordinates:
        raise ValueError("Either 'build_addr' or 'coordinates' must be provided.")

    # Generate a unique identifier based on input
    if build_addr:
        identifier = hashlib.md5(build_addr.encode()).hexdigest()
    else:
        coord_str = f"{coordinates['lat']},{coordinates['lng']}"
        identifier = hashlib.md5(coord_str.encode()).hexdigest()

    # Simulate building age calculation
    # Using hash to generate a consistent but varied age in months
    age_seed = int(identifier[:8], 16)
    age_months = (age_seed % 1200) + 1  # Random age between 1 and 1200 months

    return {
        "identifier": identifier,
        "age_months": age_months,
    }


from typing import Dict, Optional, Union


def get_build_fire(
    build_addr: Optional[str] = None, coordinates: Optional[Dict[str, float]] = None
) -> Dict[str, Union[str, int]]:
    """Retrieve the number of fire escapes in a given building.

    Args:
        build_addr: The full address of the building to look up.
        coordinates: The geolocation of the building to look up.

    Returns:
        Dict containing:
            - identifier: A unique identifier for the building (address or coordinates)
            - fire_escapes: Number of fire escapes in the building
    """

    if not build_addr and not coordinates:
        raise ValueError("Either 'build_addr' or 'coordinates' must be provided.")

    if build_addr:
        identifier = build_addr
    else:
        identifier = f"{coordinates['lat']},{coordinates['lng']}"

    # Simulate a hash-based generation for consistent but varied sample data
    hash_value = hash(identifier) % 5 + 1  # Generates a number between 1 and 5

    return {
        "identifier": identifier,
        "fire_escapes": hash_value,
    }


from typing import Dict, Optional, Union


def get_build_height(
    build_addr: Optional[str] = None, coordinates: Optional[Dict[str, float]] = None
) -> Dict[str, Union[str, float]]:
    """Retrieve the height information for a given building.

    Args:
        build_addr: The full address of the building to look up.
        coordinates: The geolocation of the building to look up, containing 'lat' and 'lng'.

    Returns:
        Dict containing:
            - address: The address of the building
            - max_height: Maximum height from ground to top in meters
            - foundation_depth: Depth of the foundation from ground level in meters (if available)
    """

    if not build_addr and not coordinates:
        raise ValueError("Either 'build_addr' or 'coordinates' must be provided.")

    if build_addr:
        # Simulate a hash-based generation for consistent sample data
        hash_value = hash(build_addr) % 100
        address = build_addr
    else:
        # Simulate a hash-based generation for consistent sample data
        hash_value = hash((coordinates["lat"], coordinates["lng"])) % 100
        address = f"Building at ({coordinates['lat']}, {coordinates['lng']})"

    # Generate sample data based on the hash value
    max_height = 50 + (hash_value % 50)  # Random height between 50 and 100 meters
    foundation_depth = (
        (hash_value % 20) if hash_value % 2 == 0 else None
    )  # Random depth or None

    return {
        "address": address,
        "max_height": max_height,
        "foundation_depth": foundation_depth,
    }


import hashlib
from typing import Dict, List, Optional, Union


def get_build_history(
    build_addr: Optional[str] = None, coordinates: Optional[Dict[str, float]] = None
) -> Dict[str, Union[str, List[str]]]:
    """Retrieve historic records for a given building.

    Args:
        build_addr: The full address of the building to look up.
        coordinates: The geolocation of the building to look up.

    Returns:
        Dict containing:
            - address: The address of the building.
            - deeds: List of deed change records.
            - occupancy: List of occupancy history.
            - media_mentions: List of news and media mentions.
    """

    if not build_addr and not coordinates:
        raise ValueError("Either 'build_addr' or 'coordinates' must be provided.")

    if build_addr:
        key = build_addr
    else:
        key = f"{coordinates['lat']},{coordinates['lng']}"

    # Generate a consistent hash for the key to simulate data retrieval
    hash_key = hashlib.md5(key.encode()).hexdigest()

    # Mock data generation based on the hash
    deeds = [f"Deed change {i} for {hash_key[:8]}" for i in range(1, 4)]
    occupancy = [f"Occupancy record {i} for {hash_key[8:16]}" for i in range(1, 3)]
    media_mentions = [f"Media mention {i} for {hash_key[16:24]}" for i in range(1, 5)]

    return {
        "address": build_addr
        or f"Coordinates: {coordinates['lat']}, {coordinates['lng']}",
        "deeds": deeds,
        "occupancy": occupancy,
        "media_mentions": media_mentions,
    }


from typing import Dict, List, Optional, Union


def request_quote(
    contractor_id: str,
    problem_description: str,
    photos: Optional[List[str]] = None,
    preferred_time_window: Optional[Dict[str, str]] = None,
    address: Optional[str] = None,
    contact_name: Optional[str] = None,
    contact_phone: Optional[str] = None,
) -> Dict[str, Union[str, List[str], Dict[str, str]]]:
    """Request a detailed quote from a contractor for a described issue.

    Args:
        contractor_id: Target contractor ID
        problem_description: Free-text description of the issue
        photos: Optional image file IDs to illustrate the problem
        preferred_time_window: Preferred arrival window (ISO 8601)
        address: Service address
        contact_name: Point of contact name
        contact_phone: Point of contact phone

    Returns:
        Dict containing:
            - contractor_id: The ID of the contractor
            - quote_id: Generated quote ID
            - status: Status of the quote request
            - details: Details of the request including problem description
            - photos: List of photo IDs if provided
            - preferred_time_window: Preferred time window if provided
            - address: Service address if provided
            - contact_info: Contact name and phone if provided
    """
    if not contractor_id or not problem_description:
        raise ValueError("contractor_id and problem_description are required fields")

    # Simulate quote ID generation
    quote_id = f"Q-{hash(contractor_id + problem_description) % 10000:04}"

    # Simulate status
    status = "pending"

    # Build the response
    response = {
        "contractor_id": contractor_id,
        "quote_id": quote_id,
        "status": status,
        "details": problem_description,
    }

    if photos:
        response["photos"] = photos

    if preferred_time_window:
        response["preferred_time_window"] = preferred_time_window

    if address:
        response["address"] = address

    if contact_name or contact_phone:
        response["contact_info"] = {
            "name": contact_name,
            "phone": contact_phone,
        }

    return response


from typing import Dict, List, Union


def search_properties(
    city: str,
    check_in: str,
    check_out: str,
    adults: int,
    children: int = 0,
    pets: int = 0,
    price_min: Union[int, None] = None,
    price_max: Union[int, None] = None,
    currency: str = "USD",
    superhost: Union[bool, None] = None,
    min_rating: Union[float, None] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, int, bool]]]]]:
    """Retrieve Airbnb listings that meet the specified criteria.

    Args:
        city: The city to search for listings in.
        check_in: Check-in date in ISO format (YYYY-MM-DD).
        check_out: Check-out date in ISO format (YYYY-MM-DD).
        adults: Number of adult guests (age 13+).
        children: Number of children (ages 2–12).
        pets: Number of pets.
        price_min: Minimum price-per-night in the specified currency.
        price_max: Maximum price-per-night in the specified currency.
        currency: ISO currency code (e.g., 'USD', 'AUD').
        superhost: Filter for listings hosted by Superhosts.
        min_rating: Minimum average rating (1.0–5.0).

    Returns:
        Dict containing:
            - city: The city of the listings
            - listings: List of listings with details such as:
                - name: Name of the listing
                - price_per_night: Price per night in the specified currency
                - rating: Average rating of the listing
                - superhost: Boolean indicating if the host is a Superhost
                - accommodates: Number of people the listing accommodates
    """

    # Sample data generation based on city hash
    sample_data = {
        "New York": [
            {
                "name": "Cozy Apartment in Manhattan",
                "price_per_night": 150,
                "rating": 4.8,
                "superhost": True,
                "accommodates": 3,
            },
            {
                "name": "Brooklyn Loft",
                "price_per_night": 120,
                "rating": 4.5,
                "superhost": False,
                "accommodates": 4,
            },
        ],
        "San Francisco": [
            {
                "name": "Modern Studio in SF",
                "price_per_night": 200,
                "rating": 4.9,
                "superhost": True,
                "accommodates": 2,
            },
            {
                "name": "Charming Victorian",
                "price_per_night": 180,
                "rating": 4.7,
                "superhost": False,
                "accommodates": 5,
            },
        ],
        "Bangkok": [
            {
                "name": "Modern Condo in Sukhumvit",
                "price_per_night": 80,
                "rating": 4.6,
                "superhost": True,
                "accommodates": 4,
            },
            {
                "name": "Traditional Thai House",
                "price_per_night": 60,
                "rating": 4.4,
                "superhost": False,
                "accommodates": 6,
            },
        ],
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    listings = sample_data[city]

    # Filter listings based on criteria
    filtered_listings = [
        listing
        for listing in listings
        if (price_min is None or listing["price_per_night"] >= price_min)
        and (price_max is None or listing["price_per_night"] <= price_max)
        and (superhost is None or listing["superhost"] == superhost)
        and (min_rating is None or listing["rating"] >= min_rating)
        and listing["accommodates"] >= (adults + children)
    ]

    return {
        "city": city,
        "listings": filtered_listings,
    }
