from typing import Dict, List, Union, Any
# Astronomy Tools
# Auto-generated implementations from cached categorization

from typing import Dict, Union
import hashlib


def find_planet_position(planet_name: str, location: str) -> Dict[str, Union[str, float]]:
    """Find the position of a planet in the current sky as observed from a US location.

    Args:
        planet_name: The name of the planet, e.g., 'Mars' or 'Jupiter'.
        location: The user's current location in the United States, given by 'CITY, STATE'.

    Returns:
        Dict containing:
            - planet_name: Name of the planet
            - location: User's location
            - altitude: Altitude of the planet in degrees
            - azimuth: Azimuth of the planet in degrees
            - visibility: Visibility condition of the planet
    """
    
    # Validate location format
    if ',' not in location or len(location.split(',')) != 2:
        raise ValueError("Location must be in the format 'CITY, STATE'")
    
    # Validate planet name
    valid_planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    if planet_name not in valid_planets:
        raise ValueError(f"Unsupported planet: {planet_name}")

    # Generate a consistent but varied position based on hash
    hash_input = f"{planet_name}-{location}".encode('utf-8')
    hash_value = hashlib.sha256(hash_input).hexdigest()
    altitude = int(hash_value[:2], 16) % 90  # Altitude between 0 and 89 degrees
    azimuth = int(hash_value[2:4], 16) % 360  # Azimuth between 0 and 359 degrees
    visibility_conditions = ["clear", "partly cloudy", "cloudy", "overcast"]
    visibility = visibility_conditions[int(hash_value[4], 16) % len(visibility_conditions)]

    return {
        "planet_name": planet_name,
        "location": location,
        "altitude": float(altitude),
        "azimuth": float(azimuth),
        "visibility": visibility,
    }

from typing import Dict, Union


def is_planet_visible(planet_name: str, location: str) -> Dict[str, Union[bool, str]]:
    """Determine if a planet is visible from a given location in the US.

    Args:
        planet_name: The name of the planet, e.g., 'Mars' or 'Jupiter'.
        location: The user's current location in the United States. Given by `CITY, STATE`.

    Returns:
        Dict containing:
            - planet_name: Name of the planet
            - location: User's location
            - visible: Boolean indicating if the planet is visible
    """
    
    # Sample data for visibility based on location and planet
    visibility_data = {
        "New York, NY": {"Mars": True, "Jupiter": False},
        "Los Angeles, CA": {"Mars": False, "Jupiter": True},
        "Chicago, IL": {"Mars": True, "Jupiter": True},
    }
    
    if location not in visibility_data:
        raise ValueError(f"Location not supported: {location}")
    
    if planet_name not in visibility_data[location]:
        raise ValueError(f"Planet not supported: {planet_name}")
    
    return {
        "planet_name": planet_name,
        "location": location,
        "visible": visibility_data[location][planet_name],
    }

