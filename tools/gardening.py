# Gardening Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def get_coverage(brand: str) -> Dict[str, Union[str, float]]:
    """Get the coverage of a given paint brand in m^2/L.

    Args:
        brand: Paint brand name to get coverage for (e.g. 'BrandA', 'BrandB')

    Returns:
        Dict containing:
            - brand: Paint brand name
            - coverage: Coverage in square meters per liter (m^2/L)

    Raises:
        ValueError: If the brand is not supported
    """

    sample_coverage = {
        "BrandA": 12.0,
        "BrandB": 10.5,
        "BrandC": 15.0,
    }

    if brand not in sample_coverage:
        raise ValueError(f"Brand not supported: {brand}")

    return {
        "brand": brand,
        "coverage": sample_coverage[brand],
    }


import hashlib
from typing import Dict, Union


def check_soil_moisture(sensor_id: str, date: str) -> Dict[str, Union[str, float]]:
    """Checks the soil moisture levels for a given sensor on a specific date.

    Args:
        sensor_id: Unique soil sensor ID
        date: Date the soil moisture is checked in YYYY-MM-DD format

    Returns:
        Dict containing:
            - sensor_id: The unique ID of the soil sensor
            - date: The date of the moisture check
            - moisture_level: The moisture level as a percentage
    """
    if not sensor_id or not date:
        raise ValueError("Both sensor_id and date are required")

    # Generate a consistent but varied moisture level based on sensor_id and date
    hash_input = f"{sensor_id}-{date}".encode()
    hash_value = hashlib.sha256(hash_input).hexdigest()
    moisture_level = int(hash_value[:2], 16) % 101  # Moisture level between 0 and 100

    return {
        "sensor_id": sensor_id,
        "date": date,
        "moisture_level": moisture_level,
    }


from typing import Dict, Literal, Union


def control_sprinklers(
    zone: Literal["front_lawn", "back_lawn", "garden", "all"],
    action: Literal["start", "stop"],
    duration: int = 15,
) -> Dict[str, Union[str, int]]:
    """Manage outdoor sprinkler system for lawn and garden watering.

    Args:
        zone: Sprinkler zone to control ('front_lawn', 'back_lawn', 'garden', or 'all')
        action: Sprinkler action to perform ('start' or 'stop')
        duration: Watering duration in minutes (only used with 'start' action)

    Returns:
        Dict containing:
            - zone: The zone being controlled
            - action: The action performed
            - duration: Duration of watering in minutes (0 if action is 'stop')
    """
    if action == "stop":
        duration = 0

    if zone not in {"front_lawn", "back_lawn", "garden", "all"}:
        raise ValueError(f"Unsupported zone: {zone}")

    if action not in {"start", "stop"}:
        raise ValueError(f"Unsupported action: {action}")

    return {"zone": zone, "action": action, "duration": duration}


from typing import Dict, List, Literal, Optional, Union


def filter_species_by_region(
    region: Literal[
        "Pacific Northwest",
        "Iberia",
        "Japan",
        "Great Plains",
        "Southeast US",
        "Mediterranean",
    ],
    hardiness_zone: Optional[str] = None,
    is_native: Optional[bool] = None,
    habitat: Optional[
        Union[
            Literal["coastal", "wetland", "woodland", "urban", "alpine", "desert"], str
        ]
    ] = None,
) -> List[Dict[str, Union[str, bool]]]:
    """Filter plant species by geographic macro-region and habitat traits.

    Args:
        region: Macro-region to filter species by.
        hardiness_zone: USDA or RHS hardiness zone.
        is_native: Whether the species is native to the region.
        habitat: Habitat type of the species.

    Returns:
        List of dictionaries, each containing:
            - species_name: Name of the plant species
            - is_native: Whether the species is native to the region
            - habitat: Habitat type of the species
            - hardiness_zone: Hardiness zone of the species
    """
    # Convert habitat parameter to handle alternative forms
    if isinstance(habitat, str):
        habitat_mappings = {
            "coastal exposure": "coastal",
            "coastal area": "coastal",
            "coastal zone": "coastal",
            "wetland area": "wetland",
            "marsh": "wetland",
            "forest": "woodland",
            "wooded area": "woodland",
            "urban area": "urban",
            "city": "urban",
            "mountain": "alpine",
            "mountainous": "alpine",
            "desert area": "desert",
            "arid": "desert",
        }

        # Check if it's an alternative form and convert
        habitat_lower = habitat.lower()
        for key, value in habitat_mappings.items():
            if habitat_lower == key or habitat_lower in key or key in habitat_lower:
                habitat = value
                break

        # Check if it's a valid literal after conversion
        valid_habitats = {"coastal", "wetland", "woodland", "urban", "alpine", "desert"}
        if habitat not in valid_habitats:
            raise ValueError(
                f"Invalid habitat: {habitat}. Must be one of {valid_habitats}"
            )
    # Sample data for demonstration purposes
    species_data = [
        {
            "species_name": "Douglas Fir",
            "is_native": True,
            "habitat": "woodland",
            "hardiness_zone": "6a",
        },
        {
            "species_name": "Mediterranean Cypress",
            "is_native": True,
            "habitat": "coastal",
            "hardiness_zone": "9b",
        },
        {
            "species_name": "Japanese Maple",
            "is_native": False,
            "habitat": "urban",
            "hardiness_zone": "5b",
        },
        {
            "species_name": "Prairie Dropseed",
            "is_native": True,
            "habitat": "grassland",
            "hardiness_zone": "4a",
        },
        {
            "species_name": "Saw Palmetto",
            "is_native": True,
            "habitat": "wetland",
            "hardiness_zone": "8b",
        },
    ]

    # Filter the species based on the provided criteria
    filtered_species = []
    for species in species_data:
        if region == "Pacific Northwest" and species["species_name"] == "Douglas Fir":
            matches = True
        elif (
            region == "Mediterranean"
            and species["species_name"] == "Mediterranean Cypress"
        ):
            matches = True
        elif region == "Japan" and species["species_name"] == "Japanese Maple":
            matches = True
        elif region == "Great Plains" and species["species_name"] == "Prairie Dropseed":
            matches = True
        elif region == "Southeast US" and species["species_name"] == "Saw Palmetto":
            matches = True
        else:
            matches = False

        if hardiness_zone and species["hardiness_zone"] != hardiness_zone:
            matches = False
        if is_native is not None and species["is_native"] != is_native:
            matches = False
        if habitat and species["habitat"] != habitat:
            matches = False

        if matches:
            filtered_species.append(species)

    return filtered_species


from typing import Dict, List, Optional


def order_gardening_supplies(
    items: List[str],
    order_date: Optional[str] = None,
    delivery_date: Optional[str] = None,
) -> Dict[str, Union[str, List[str]]]:
    """Orders gardening supplies from a store.

    Args:
        items: List of items to order from the store.
        order_date: Date that the items should be ordered, in YYYY-MM-DD format.
        delivery_date: Preferred date for the items to arrive, in YYYY-MM-DD format.

    Returns:
        Dict containing:
            - order_id: Unique identifier for the order.
            - items: List of items ordered.
            - order_date: Date the order was placed.
            - delivery_date: Expected delivery date.
    """
    if not items:
        raise ValueError("At least one item must be ordered.")

    import datetime
    import hashlib

    # Generate a unique order ID using a hash of the items and order date
    order_id = hashlib.sha256((str(items) + (order_date or "")).encode()).hexdigest()[
        :10
    ]

    # Use current date if order_date is not provided
    order_date = order_date or datetime.date.today().isoformat()

    # Simulate a delivery date if not provided
    if not delivery_date:
        delivery_date = (
            (
                datetime.datetime.strptime(order_date, "%Y-%m-%d")
                + datetime.timedelta(days=7)
            )
            .date()
            .isoformat()
        )

    return {
        "order_id": order_id,
        "items": items,
        "order_date": order_date,
        "delivery_date": delivery_date,
    }


from datetime import datetime, timedelta
from typing import Dict, Union


def schedule_garden_watering(
    date: str, time: str, duration_minutes: int = 15
) -> Dict[str, Union[str, int]]:
    """Schedule the automatic garden watering system.

    Args:
        date: Date to start the watering system in YYYY-MM-DD format
        time: Time to start the watering system in HH:MM format
        duration_minutes: How long the watering system should run for (default is 15)

    Returns:
        Dict containing:
            - start_time: The scheduled start time in ISO 8601 format
            - end_time: The scheduled end time in ISO 8601 format
            - duration: Duration in minutes the system will run
    """
    try:
        start_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Invalid date or time format. Expected YYYY-MM-DD and HH:MM.")

    end_datetime = start_datetime + timedelta(minutes=duration_minutes)

    return {
        "start_time": start_datetime.isoformat(),
        "end_time": end_datetime.isoformat(),
        "duration": duration_minutes,
    }


from typing import Dict, Literal, Optional, Union


def search_plant_species_by_flower(
    color: Literal[
        "white",
        "yellow",
        "orange",
        "red",
        "pink",
        "purple",
        "violet",
        "blue",
        "green",
        "brown",
    ],
    shape: Literal["tubular", "bell", "composite", "star", "irregular"],
    petal_count: Optional[int] = None,
    fragrant: Optional[bool] = None,
) -> Dict[str, Union[str, int, bool]]:
    """Retrieves plant species matching given flower characteristics.

    Args:
        color: Basic color term of the flower.
        shape: Flower shape (choose exactly one).
        petal_count: Approximate integer petal count.
        fragrant: Whether the flower has a noticeable fragrance.

    Returns:
        Dict containing:
            - species_name: Name of the plant species.
            - color: Color of the flower.
            - shape: Shape of the flower.
            - petal_count: Number of petals.
            - fragrant: Whether the flower is fragrant.
    """
    # Sample data based on hash of input parameters for consistent results
    sample_data = {
        ("white", "tubular"): {
            "species_name": "White Trumpet",
            "petal_count": 5,
            "fragrant": True,
        },
        ("yellow", "bell"): {
            "species_name": "Golden Bells",
            "petal_count": 6,
            "fragrant": False,
        },
        ("red", "composite"): {
            "species_name": "Scarlet Composite",
            "petal_count": 8,
            "fragrant": True,
        },
        ("pink", "star"): {
            "species_name": "Pink Starflower",
            "petal_count": 5,
            "fragrant": False,
        },
        ("purple", "irregular"): {
            "species_name": "Purple Orchid",
            "petal_count": 3,
            "fragrant": True,
        },
        ("violet", "tubular"): {
            "species_name": "Purple Orchid",
            "petal_count": 3,
            "fragrant": True,
        },
    }

    key = (color, shape)
    if key not in sample_data:
        raise ValueError(f"No species found for color '{color}' and shape '{shape}'")

    result = sample_data[key]
    if petal_count is not None and result["petal_count"] != petal_count:
        raise ValueError(
            f"No species found with {petal_count} petals for color '{color}' and shape '{shape}'"
        )
    if fragrant is not None and result["fragrant"] != fragrant:
        raise ValueError(
            f"No species found with fragrance '{fragrant}' for color '{color}' and shape '{shape}'"
        )

    return {
        "species_name": result["species_name"],
        "color": color,
        "shape": shape,
        "petal_count": result["petal_count"],
        "fragrant": result["fragrant"],
    }


from typing import Dict, List, Literal, Optional


def search_plant_species_by_leaf(
    color: Literal["green", "blue-gray", "gray", "purple", "variegated"],
    shape: Optional[
        Literal["ovate", "lanceolate", "linear", "cordate", "palmate", "needle"]
    ] = None,
    is_succulent: Optional[bool] = None,
    texture: Optional[Literal["waxy", "hairy", "glabrous", "leathery"]] = None,
) -> Dict[str, List[str]]:
    """Retrieve a list of plant species matching the given leaf characteristics.

    Args:
        color: Basic color term of the leaf.
        shape: Leaf shape (optional).
        is_succulent: Whether or not the leaf is a succulent leaf (optional).
        texture: Surface texture (optional).

    Returns:
        Dict containing:
            - species: List of plant species matching the criteria.
    """

    # Sample data representing a mock database of plant species
    plant_database = {
        "green": {
            "ovate": ["Ficus elastica", "Camellia japonica"],
            "lanceolate": ["Eucalyptus globulus"],
            "linear": ["Hordeum vulgare"],
            "cordate": ["Cercis canadensis"],
            "palmate": ["Acer palmatum"],
            "needle": ["Pinus sylvestris"],
        },
        "blue-gray": {
            "ovate": ["Eucalyptus cinerea"],
            "lanceolate": ["Agave americana"],
            "linear": ["Festuca glauca"],
        },
        "gray": {
            "ovate": ["Salvia apiana"],
            "lanceolate": ["Lavandula angustifolia"],
        },
        "purple": {
            "ovate": ["Tradescantia pallida"],
            "lanceolate": ["Perilla frutescens"],
        },
        "variegated": {
            "ovate": ["Hosta 'Patriot'"],
            "lanceolate": ["Aucuba japonica"],
        },
    }

    # Filter results based on the provided characteristics
    species_list = plant_database.get(color, {}).get(shape, [])

    # Simulate additional filtering based on is_succulent and texture
    if is_succulent is not None:
        species_list = [
            species
            for species in species_list
            if hash(species) % 2 == int(is_succulent)
        ]

    if texture:
        species_list = [
            species for species in species_list if hash(species) % 4 == len(texture) % 4
        ]

    return {"species": species_list}
