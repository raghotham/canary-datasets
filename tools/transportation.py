# Transportation Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def check_traffic(
    start_location: str, destination: str
) -> Dict[str, Union[str, List[str]]]:
    """Retrieves current traffic conditions along a specified route.

    Args:
        start_location: The starting location of the route
        destination: The ending location of the route

    Returns:
        Dict containing:
            - start_location: Starting point of the route
            - destination: Ending point of the route
            - traffic_conditions: List of current traffic conditions
    """

    if not start_location or not destination:
        raise ValueError("Both start_location and destination must be provided.")

    # Simulated traffic data based on hash values for consistency
    traffic_data = {
        "heavy": ["accident", "construction"],
        "moderate": ["roadwork", "event"],
        "light": ["clear"],
    }

    # Generate a hash-based index to simulate traffic conditions
    index = (hash(start_location) + hash(destination)) % 3
    conditions = list(traffic_data.keys())[index]

    return {
        "start_location": start_location,
        "destination": destination,
        "traffic_conditions": traffic_data[conditions],
    }


from typing import Dict, List, Union


def get_gas_stations(
    location: str, radius_miles: float = 5
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find nearby gas stations at a specific location.

    Args:
        location: The location to search for gas stations
        radius_miles: Search radius in miles around the location

    Returns:
        Dict containing:
            - location: The location searched
            - radius_miles: The search radius in miles
            - gas_stations: List of nearby gas stations with details
    """

    sample_data = {
        "New York": [
            {"name": "Shell", "address": "123 Main St", "distance_miles": 1.2},
            {"name": "BP", "address": "456 Broadway", "distance_miles": 2.5},
        ],
        "Los Angeles": [
            {"name": "Chevron", "address": "789 Sunset Blvd", "distance_miles": 0.8},
            {"name": "Exxon", "address": "101 Hollywood Ave", "distance_miles": 3.1},
        ],
        "Chicago": [
            {"name": "Mobil", "address": "202 Michigan Ave", "distance_miles": 1.5},
            {"name": "Citgo", "address": "303 Lake Shore Dr", "distance_miles": 2.9},
        ],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    return {
        "location": location,
        "radius_miles": radius_miles,
        "gas_stations": sample_data[location],
    }


from typing import Dict, Union


def arrange_airport_transfer(
    pickup_location: str, dropoff_location: str, date: str, passengers: int
) -> Dict[str, Union[str, int, float]]:
    """Arrange a private or shared airport transfer.

    Args:
        pickup_location: Pickup location (hotel, address, or airport)
        dropoff_location: Drop-off location (hotel, address, or airport)
        date: Date of the transfer in YYYY-MM-DD format
        passengers: Number of passengers

    Returns:
        Dict containing:
            - pickup_location: Confirmed pickup location
            - dropoff_location: Confirmed drop-off location
            - date: Confirmed date of transfer
            - passengers: Number of passengers
            - vehicle_type: Type of vehicle assigned
            - estimated_cost: Estimated cost of the transfer
    """
    if passengers <= 0:
        raise ValueError("Number of passengers must be greater than zero")

    vehicle_type = "sedan" if passengers <= 3 else "minivan"
    base_cost = 50.0
    cost_per_passenger = 10.0
    estimated_cost = base_cost + (cost_per_passenger * passengers)

    return {
        "pickup_location": pickup_location,
        "dropoff_location": dropoff_location,
        "date": date,
        "passengers": passengers,
        "vehicle_type": vehicle_type,
        "estimated_cost": estimated_cost,
    }


from datetime import datetime, timedelta
from typing import Dict, Literal, Optional, Union


def arrange_transport(
    mode: Literal["rideshare", "transit", "parking"],
    dropoff_location: str,
    pickup_location: Optional[str] = None,
    departure_time: Optional[str] = None,
    arrival_time: Optional[str] = None,
    budget_max: Optional[float] = None,
    wheelchair_accessible: Optional[bool] = None,
    passengers: Optional[int] = None,
) -> Dict[str, Union[str, float, bool, int]]:
    """Plan transport to or from an event using rideshare, transit, or parking.

    Args:
        mode: Transport mode: 'rideshare', 'transit', or 'parking'
        dropoff_location: Destination address or place name
        pickup_location: Pickup address or place name (required for rideshare)
        departure_time: Desired departure time (ISO 8601)
        arrival_time: Desired arrival time (ISO 8601). If set, service will back-calc pickup.
        budget_max: Maximum spend in local currency
        wheelchair_accessible: Require accessible vehicle/route/parking
        passengers: Number of passengers (integer)

    Returns:
        Dict containing:
            - mode: Chosen transport mode
            - estimated_cost: Estimated cost of the transport
            - estimated_time: Estimated travel time in minutes
            - pickup_time: Calculated pickup time if arrival_time is provided
            - accessible: Whether the option is wheelchair accessible
            - passengers: Number of passengers accommodated
    """
    if mode == "rideshare" and not pickup_location:
        raise ValueError("pickup_location is required for rideshare mode")

    if arrival_time and departure_time:
        raise ValueError("Specify either departure_time or arrival_time, not both")

    # Mock data generation
    hash_value = hash(
        (mode, dropoff_location, pickup_location, departure_time, arrival_time)
    )
    estimated_cost = abs(hash_value) % 50 + 10  # Mock cost between 10 and 60
    estimated_time = abs(hash_value) % 60 + 15  # Mock time between 15 and 75 minutes

    if arrival_time:
        arrival_dt = datetime.fromisoformat(arrival_time)
        pickup_time = (arrival_dt - timedelta(minutes=estimated_time)).isoformat()
    else:
        pickup_time = departure_time

    return {
        "mode": mode,
        "estimated_cost": estimated_cost,
        "estimated_time": estimated_time,
        "pickup_time": pickup_time,
        "accessible": (
            wheelchair_accessible if wheelchair_accessible is not None else False
        ),
        "passengers": passengers if passengers is not None else 1,
    }


import hashlib
from typing import Dict, Union


def book_transport(
    pickup_location: str, dropoff_location: str, date: str, passengers: int
) -> Dict[str, Union[str, int, float]]:
    """Book transportation between two points.

    Args:
        pickup_location: Starting location for the transport
        dropoff_location: Destination location for the transport
        date: Date of the transport in YYYY-MM-DD format
        passengers: Number of passengers

    Returns:
        Dict containing:
            - booking_id: Unique identifier for the booking
            - pickup_location: Starting location for the transport
            - dropoff_location: Destination location for the transport
            - date: Date of the transport
            - passengers: Number of passengers
            - estimated_cost: Estimated cost of the transport in USD
    """
    if passengers <= 0:
        raise ValueError("Number of passengers must be greater than zero")

    # Generate a unique booking ID using a hash
    booking_id = hashlib.sha256(
        f"{pickup_location}{dropoff_location}{date}{passengers}".encode()
    ).hexdigest()[:10]

    # Mock estimated cost calculation
    base_cost = 50.0
    distance_factor = len(pickup_location) + len(dropoff_location)
    passenger_factor = passengers * 10.0
    estimated_cost = base_cost + distance_factor + passenger_factor

    return {
        "booking_id": booking_id,
        "pickup_location": pickup_location,
        "dropoff_location": dropoff_location,
        "date": date,
        "passengers": passengers,
        "estimated_cost": round(estimated_cost, 2),
    }


from typing import Dict


def check_car_price(
    make: str, model: str, year: int
) -> Dict[str, Union[str, int, float]]:
    """Returns an estimated price for a given car.

    Args:
        make: The make of the car (e.g., 'Toyota', 'Ford')
        model: The model of the car (e.g., 'Camry', 'Mustang')
        year: The production year of the car

    Returns:
        Dict containing:
            - make: The make of the car
            - model: The model of the car
            - year: The production year of the car
            - estimated_price: The estimated price of the car in USD
    """

    # Sample base prices for different makes and models
    base_prices = {
        ("Toyota", "Camry"): 24000,
        ("Ford", "Mustang"): 26000,
        ("Honda", "Civic"): 22000,
        ("Volvo", "S90"): 48000,
    }

    # Calculate depreciation based on the year
    current_year = 2023
    depreciation_rate = 0.05  # 5% depreciation per year

    if (make, model) not in base_prices:
        raise ValueError(f"Car make and model not supported: {make} {model}")

    base_price = base_prices[(make, model)]
    age = current_year - year

    if age < 0:
        raise ValueError("Year cannot be in the future")

    estimated_price = base_price * ((1 - depreciation_rate) ** age)

    return {
        "make": make,
        "model": model,
        "year": year,
        "estimated_price": round(estimated_price, 2),
    }


from typing import Dict, Literal, Optional, Union


def filter_cars(
    condition: Literal["new", "used"],
    use_case: Literal[
        "commuting",
        "work",
        "sport",
        "luxury",
        "industrial",
        "taxi",
        "family_mode_of_transport",
    ],
    make: Optional[str] = None,
    model: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    mileage_max: Optional[float] = None,
    mileage_min: Optional[float] = None,
    exclude_make: Optional[str] = None,
    exclude_model: Optional[str] = None,
    car_style: Optional[
        Literal["coupe", "sedan", "van", "truck", "hatchback", "convertible"]
    ] = None,
    drive_type: Optional[
        Literal["AWD/4WD", "Front wheel drive", "Rear wheel drive"]
    ] = None,
    transmission: Optional[Literal["Manual", "Automatic"]] = None,
) -> Dict[str, Union[str, int, float]]:
    """Returns the best car make, model year, and mileage for a person to buy given a set of criteria.

    Args:
        condition: Condition of a car ('new' or 'used').
        use_case: Use case for the car.
        make: Make of the car.
        model: Model of the car.
        price_min: Minimum price.
        price_max: Maximum price.
        mileage_max: Maximum mileage.
        mileage_min: Minimum mileage.
        exclude_make: Exclude certain makes of cars from the return list.
        exclude_model: Exclude certain models of cars from the return list.
        car_style: Style of the car.
        drive_type: Drive type of the car.
        transmission: Transmission type of the car.

    Returns:
        Dict containing:
            - make: Best car make
            - model: Best car model
            - year: Model year
            - mileage: Mileage of the car
            - price: Price of the car
    """

    def normalize_make(search_make: str) -> str:
        """Normalize car make for flexible matching"""
        if not search_make:
            return search_make
        
        make_mappings = {
            "toyota": ["toyota", "toyoda"],
            "ford": ["ford", "ford motor company"],
            "honda": ["honda", "honda motor company"], 
            "chevrolet": ["chevrolet", "chevy", "chev"],
            "gmc": ["gmc", "general motors"],
            "nissan": ["nissan", "datsun"],
            "ram": ["ram", "dodge ram"],
            "jeep": ["jeep", "chrysler jeep"],
        }
        
        search_lower = search_make.lower().strip()
        for standard, variants in make_mappings.items():
            if search_lower in variants:
                return standard
        return search_lower

    def normalize_drive_type(search_drive: str) -> str:
        """Normalize drive type for flexible matching"""
        if not search_drive:
            return search_drive
            
        drive_mappings = {
            "AWD/4WD": ["awd", "4wd", "all wheel drive", "four wheel drive", "awd/4wd", "4x4"],
            "Front wheel drive": ["fwd", "front wheel drive", "front-wheel drive", "front wheel", "front"],
            "Rear wheel drive": ["rwd", "rear wheel drive", "rear-wheel drive", "rear wheel", "rear"],
        }
        
        search_lower = search_drive.lower().strip()
        for standard, variants in drive_mappings.items():
            if search_lower in variants:
                return standard
        return search_drive

    # Expanded mock data with Toyota trucks and work vehicles
    sample_cars = [
        # Original cars
        {
            "make": "toyota",
            "model": "Camry",
            "year": 2020,
            "mileage": 15000,
            "price": 22000,
            "condition": "used",
            "style": "sedan",
            "drive": "Front wheel drive",
            "transmission": "Automatic",
            "use_cases": ["commuting", "family_mode_of_transport"],
        },
        {
            "make": "ford",
            "model": "F-150",
            "year": 2021,
            "mileage": 5000,
            "price": 35000,
            "condition": "new",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "industrial"],
        },
        {
            "make": "honda",
            "model": "Civic",
            "year": 2019,
            "mileage": 30000,
            "price": 18000,
            "condition": "used",
            "style": "sedan",
            "drive": "Front wheel drive",
            "transmission": "Manual",
            "use_cases": ["commuting", "sport"],
        },
        # Toyota trucks for work use case
        {
            "make": "toyota",
            "model": "Tacoma",
            "year": 2019,
            "mileage": 65000,
            "price": 32000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "sport"],
        },
        {
            "make": "toyota",
            "model": "Tundra",
            "year": 2020,
            "mileage": 45000,
            "price": 38000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "industrial"],
        },
        {
            "make": "toyota",
            "model": "Tacoma",
            "year": 2018,
            "mileage": 75000,
            "price": 29000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Manual",
            "use_cases": ["work", "sport"],
        },
        # More work trucks
        {
            "make": "chevrolet",
            "model": "Silverado 1500",
            "year": 2019,
            "mileage": 55000,
            "price": 34000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "industrial"],
        },
        {
            "make": "ford",
            "model": "F-150",
            "year": 2018,
            "mileage": 80000,
            "price": 31000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "industrial"],
        },
        {
            "make": "ram",
            "model": "1500",
            "year": 2019,
            "mileage": 70000,
            "price": 33000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "industrial"],
        },
        # More diverse vehicles
        {
            "make": "gmc",
            "model": "Sierra 1500",
            "year": 2020,
            "mileage": 50000,
            "price": 36000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "luxury"],
        },
        {
            "make": "nissan",
            "model": "Titan",
            "year": 2018,
            "mileage": 90000,
            "price": 28000,
            "condition": "used",
            "style": "truck",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["work", "industrial"],
        },
        # Family and commuter cars
        {
            "make": "honda",
            "model": "CR-V",
            "year": 2020,
            "mileage": 25000,
            "price": 26000,
            "condition": "used",
            "style": "van",
            "drive": "Front wheel drive",
            "transmission": "Automatic",
            "use_cases": ["family_mode_of_transport", "commuting"],
        },
        {
            "make": "toyota",
            "model": "Highlander",
            "year": 2019,
            "mileage": 40000,
            "price": 32000,
            "condition": "used",
            "style": "van",
            "drive": "AWD/4WD",
            "transmission": "Automatic",
            "use_cases": ["family_mode_of_transport"],
        },
        # Luxury cars
        {
            "make": "toyota",
            "model": "Lexus ES",
            "year": 2020,
            "mileage": 20000,
            "price": 38000,
            "condition": "used",
            "style": "sedan",
            "drive": "Front wheel drive",
            "transmission": "Automatic",
            "use_cases": ["luxury", "commuting"],
        },
        # Sport cars
        {
            "make": "toyota",
            "model": "86",
            "year": 2019,
            "mileage": 35000,
            "price": 25000,
            "condition": "used",
            "style": "coupe",
            "drive": "Rear wheel drive", 
            "transmission": "Manual",
            "use_cases": ["sport"],
        }
    ]

    # Normalize parameters for flexible matching
    normalized_make = normalize_make(make) if make else None
    normalized_drive_type = normalize_drive_type(drive_type) if drive_type else None

    # Filter cars based on criteria
    filtered_cars = []
    for car in sample_cars:
        # Check condition
        if car["condition"] != condition:
            continue
            
        # Check make with normalized matching
        if normalized_make and car["make"] != normalized_make:
            continue
            
        # Check model
        if model and car["model"] != model:
            continue
            
        # Check price range
        if price_min is not None and car["price"] < price_min:
            continue
        if price_max is not None and car["price"] > price_max:
            continue
            
        # Check mileage range
        if mileage_min is not None and car["mileage"] < mileage_min:
            continue
        if mileage_max is not None and car["mileage"] > mileage_max:
            continue
            
        # Check excluded make/model
        if exclude_make and car["make"] == normalize_make(exclude_make):
            continue
        if exclude_model and car["model"] == exclude_model:
            continue
            
        # Check car style
        if car_style and car["style"] != car_style:
            continue
            
        # Check drive type with normalized matching
        if normalized_drive_type and car["drive"] != normalized_drive_type:
            continue
            
        # Check transmission
        if transmission and car["transmission"] != transmission:
            continue
            
        # Check use case compatibility
        if use_case not in car["use_cases"]:
            continue
            
        filtered_cars.append(car)

    if not filtered_cars:
        raise ValueError("No cars match the given criteria")

    # Sort by best match (price within range, lower mileage preferred)
    def score_car(car):
        score = 0
        # Prefer lower mileage
        score -= car["mileage"] / 1000
        # Prefer newer years  
        score += car["year"] - 2000
        # Prefer mid-range pricing if price range specified
        if price_min and price_max:
            mid_price = (price_min + price_max) / 2
            score -= abs(car["price"] - mid_price) / 1000
        return score
    
    # Sort by score and return the best match
    best_car = max(filtered_cars, key=score_car)
    
    return {
        "make": best_car["make"].title(),  # Return capitalized make
        "model": best_car["model"],
        "year": best_car["year"],
        "mileage": best_car["mileage"],
        "price": best_car["price"],
    }


from typing import Dict, List, Literal, Union


def find_charge_stops(
    origin: str,
    destination: str,
    plug_type: str,
    open_now: bool,
    min_power_kW: float = 50,
    route_bias: Literal["fastest", "cheapest", "avoid_downtown"] = "fastest",
    top_k: int = 3,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, bool]]]]]:
    """Find high-power EV charging stations along a driving route.

    Args:
        origin: Starting point in human-readable form (e.g., 'San Francisco International Airport', 'SFO').
        destination: End point in human-readable form (e.g., 'Healdsburg, CA').
        plug_type: Connector standard to match (e.g., 'CCS', 'NACS', 'CHAdeMO').
        open_now: Filter to only stations that are currently available/open.
        min_power_kW: Minimum charger power in kW (default is 50).
        route_bias: Preference for routing tradeoffs: 'fastest', 'cheapest', or 'avoid_downtown' (default is 'fastest').
        top_k: Maximum number of candidate stops to return (default is 3).

    Returns:
        Dict containing:
            - origin: Starting point
            - destination: End point
            - charge_stops: List of charging stations with:
                - name: Station name
                - location: Station location
                - power_kW: Charger power in kW
                - open_now: Availability status
    """
    # Mock data for demonstration purposes
    sample_stations = [
        {
            "name": "ChargePoint Station A",
            "location": "123 Main St",
            "power_kW": 150,
            "open_now": True,
        },
        {
            "name": "EVgo Station B",
            "location": "456 Elm St",
            "power_kW": 200,
            "open_now": False,
        },
        {
            "name": "Tesla Supercharger C",
            "location": "789 Oak St",
            "power_kW": 250,
            "open_now": True,
        },
        {
            "name": "Blink Station D",
            "location": "321 Pine St",
            "power_kW": 100,
            "open_now": True,
        },
        {
            "name": "Electrify America E",
            "location": "654 Maple St",
            "power_kW": 350,
            "open_now": True,
        },
    ]

    # Filter based on plug type, power, and availability
    filtered_stations = [
        station
        for station in sample_stations
        if station["power_kW"] >= min_power_kW and (not open_now or station["open_now"])
    ]

    # Sort based on power and limit to top_k results
    sorted_stations = sorted(
        filtered_stations, key=lambda x: x["power_kW"], reverse=True
    )[:top_k]

    return {
        "origin": origin,
        "destination": destination,
        "charge_stops": sorted_stations,
    }


from typing import Dict, List, Union


def find_dealers(
    origin_location: Union[str, None] = None,
    required_vehicles: Union[List[str], str] = [],
    range: float = 0,
    brand_dealership: bool = False,
    new_vehicles_only: bool = False,
) -> Dict[str, Union[str, List[Dict[str, Union[str, List[str]]]]]]:
    """Find dealerships within a range of an initial location.

    Args:
        origin_location: The starting place for the search.
        required_vehicles: A list of specific vehicles required to be at a dealership to be considered.
        range: The range in miles that you want to search.
        brand_dealership: Should the dealerships that are listed be official brand dealerships?
        new_vehicles_only: Should only dealerships with new vehicles be listed?

    Returns:
        Dict containing:
            - origin_location: The starting place for the search.
            - dealerships: List of dealerships with details including name, location, and available vehicles.
    """
    if not origin_location:
        raise ValueError("Origin location must be provided.")

    # Convert required_vehicles parameter if provided as string
    if isinstance(required_vehicles, str):
        if required_vehicles.startswith("[") and required_vehicles.endswith("]"):
            # Handle string representation of list like "['GMC Truck']"
            try:
                import ast

                parsed_vehicles = ast.literal_eval(required_vehicles)
                if isinstance(parsed_vehicles, list):
                    required_vehicles = parsed_vehicles
                else:
                    raise ValueError(
                        "Invalid required_vehicles format. Expected a list."
                    )
            except (ValueError, SyntaxError):
                raise ValueError(
                    "Invalid required_vehicles format. Expected a valid list representation."
                )
        else:
            # Handle single vehicle string like "GMC Truck"
            required_vehicles = [required_vehicles]

    # Sample data for dealerships
    sample_dealerships = [
        {
            "name": "City Auto Mall",
            "location": "Downtown",
            "vehicles": ["Honda Civic", "Toyota Corolla", "Ford F-150"],
            "brand": True,
            "new_vehicles": True,
        },
        {
            "name": "Suburban Motors",
            "location": "Suburbia",
            "vehicles": ["Chevrolet Malibu", "Jeep Wrangler"],
            "brand": True,
            "new_vehicles": False,
        },
        {
            "name": "Budget Cars",
            "location": "Uptown",
            "vehicles": ["Nissan Sentra", "Hyundai Elantra"],
            "brand": False,
            "new_vehicles": True,
        },
    ]

    # Filter dealerships based on criteria
    filtered_dealerships = []
    for dealership in sample_dealerships:
        if brand_dealership and not dealership["brand"]:
            continue
        if new_vehicles_only and not dealership["new_vehicles"]:
            continue
        if required_vehicles and not any(
            vehicle in dealership["vehicles"] for vehicle in required_vehicles
        ):
            continue
        filtered_dealerships.append(dealership)

    return {"origin_location": origin_location, "dealerships": filtered_dealerships}


from typing import Dict, Literal, Union


def find_dealership_nearby(
    make: Literal[
        "Honda", "Toyota", "Jeep", "Hyundai", "Chevrolet", "Volvo", "volkswagen"
    ] = "Honda",
    zipcode: str = None,
    distance: Literal["25", "50", "75", "100"] = "25",
    coordinates: Dict[str, float] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search for car dealerships in a given location.

    Args:
        make: The dealership's brand of vehicle.
        zipcode: Zipcode of area to search within.
        distance: Maximum distance from area to search, in miles.
        coordinates: Coordinates of geographical area to search within. If provided, value inside zipcode will be ignored.

    Returns:
        Dict containing:
            - make: The brand of the dealership
            - dealerships: List of dealerships with their name, address, and distance from the search location
    """
    if not zipcode and not coordinates:
        raise ValueError("Either 'zipcode' or 'coordinates' must be provided.")

    sample_dealerships = {
        "Honda": [
            {"name": "Honda City", "address": "123 Main St, Anytown", "distance": 5.0},
            {
                "name": "Auto Honda",
                "address": "456 Elm St, Othertown",
                "distance": 20.0,
            },
        ],
        "Toyota": [
            {
                "name": "Toyota World",
                "address": "789 Maple Ave, Anytown",
                "distance": 10.0,
            },
            {
                "name": "City Toyota",
                "address": "321 Oak St, Othertown",
                "distance": 30.0,
            },
        ],
        "Jeep": [
            {
                "name": "Jeep Junction",
                "address": "654 Pine Rd, Anytown",
                "distance": 15.0,
            },
            {
                "name": "Offroad Jeep",
                "address": "987 Cedar Blvd, Othertown",
                "distance": 40.0,
            },
        ],
        # Add similar entries for other makes...
    }

    dealerships = sample_dealerships.get(make, [])
    filtered_dealerships = [d for d in dealerships if d["distance"] <= float(distance)]

    return {"make": make, "dealerships": filtered_dealerships}


from typing import Dict, List, Literal, Optional, Union


def find_similar(
    make: str,
    model: str,
    condition: Literal["new", "used"],
    price_min: Optional[str] = None,
    price_max: Optional[str] = None,
    exclude_make: Optional[str] = None,
    exclude_model: Optional[str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Returns most similar cars to the one being provided in a given price range.

    Args:
        make: Make of the original car.
        model: Model of the original car.
        condition: Condition of a car ('new' or 'used').
        price_min: Minimum price.
        price_max: Maximum price.
        exclude_make: Exclude certain makes of cars from the return list.
        exclude_model: Exclude certain models of cars from the return list.

    Returns:
        Dict containing:
            - original_car: Description of the original car
            - similar_cars: List of similar cars with their details
    """
    # Sample data for demonstration purposes
    sample_cars = [
        {"make": "Toyota", "model": "Camry", "condition": "used", "price": 15000},
        {"make": "Honda", "model": "Accord", "condition": "used", "price": 16000},
        {"make": "Ford", "model": "Focus", "condition": "new", "price": 20000},
        {"make": "Chevrolet", "model": "Malibu", "condition": "new", "price": 22000},
    ]

    def is_within_price_range(car_price: int) -> bool:
        if price_min is not None and car_price < int(price_min):
            return False
        if price_max is not None and car_price > int(price_max):
            return False
        return True

    similar_cars = [
        car
        for car in sample_cars
        if car["condition"] == condition
        and is_within_price_range(car["price"])
        and (exclude_make is None or car["make"] != exclude_make)
        and (exclude_model is None or car["model"] != exclude_model)
    ]

    return {
        "original_car": f"{make} {model} ({condition})",
        "similar_cars": similar_cars,
    }


from typing import Dict, List, Union


def find_similar_cars(
    search_input: str,
    type: Union[str, None] = None,
    price: Union[List[int], str, None] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Find similar vehicles based on make, model, type, and price range.

    Args:
        search_input: The make and/or model of a vehicle (e.g., 'Toyota Camry')
        type: The type of car requested (e.g., 'sedan', 'truck')
        price: The minimum and maximum price of a requested vehicle search [min_price, max_price]

    Returns:
        Dict containing:
            - search_input: The original search input
            - similar_vehicles: List of similar vehicles with details
    """
    def normalize_make_model(search_term: str):
        """Normalize car make and model for flexible matching"""
        make_model_mappings = {
            "gmc sierra denali": ["gmc", "sierra denali"],
            "gmc sierra": ["gmc", "sierra"],
            "gmc yukon denali": ["gmc", "yukon denali"],
            "gmc yukon": ["gmc", "yukon"],
            "chevrolet silverado": ["chevrolet", "silverado"],
            "chevy silverado": ["chevrolet", "silverado"],
            "ford f-150": ["ford", "f-150"],
            "ford f150": ["ford", "f-150"],
        }
        
        search_lower = search_term.lower().strip()
        return make_model_mappings.get(search_lower, [None, None])
        
    # Convert price parameter if provided as string
    if isinstance(price, str):
        if price.startswith("[") and price.endswith("]"):
            # Handle string representation of list like "[0, 80000]"
            try:
                import ast

                parsed_price = ast.literal_eval(price)
                if isinstance(parsed_price, list):
                    price = parsed_price
                else:
                    raise ValueError("Invalid price format. Expected a list.")
            except (ValueError, SyntaxError):
                raise ValueError(
                    "Invalid price format. Expected a valid list representation."
                )
        elif "," in price:
            # Handle comma-separated string like "0,80000"
            try:
                parts = price.split(",")
                if len(parts) == 2:
                    price = [int(parts[0].strip()), int(parts[1].strip())]
                else:
                    raise ValueError("Invalid price format. Expected format: 'min,max'")
            except ValueError:
                raise ValueError("Invalid price format. Could not convert to integers.")
        elif "-" in price:
            # Handle range format like "60000-85000"
            try:
                parts = price.split("-")
                if len(parts) == 2:
                    price = [int(parts[0].strip()), int(parts[1].strip())]
                else:
                    raise ValueError("Invalid price format. Expected format: 'min-max'")
            except ValueError:
                raise ValueError("Invalid price format. Could not convert to integers.")
        else:
            # Handle single price value like "80000" - treat as maximum price
            try:
                max_price = int(price)
                price = [0, max_price]  # Assume minimum is 0
            except ValueError:
                raise ValueError("Invalid price format. Could not convert to integer.")

    # Expanded sample data with luxury trucks
    sample_vehicles = [
        # Original vehicles
        {"make": "Toyota", "model": "Camry", "type": "sedan", "price": 24000},
        {"make": "Honda", "model": "Accord", "type": "sedan", "price": 23000},
        {"make": "Ford", "model": "F-150", "type": "truck", "price": 28000},
        {"make": "BMW", "model": "3 Series", "type": "luxury", "price": 35000},
        {"make": "Chevrolet", "model": "Silverado", "type": "truck", "price": 30000},
        # Premium and luxury trucks
        {"make": "GMC", "model": "Sierra Denali", "type": "truck", "price": 68000},
        {"make": "GMC", "model": "Yukon Denali", "type": "truck", "price": 72000},
        {"make": "Chevrolet", "model": "Silverado High Country", "type": "truck", "price": 65000},
        {"make": "Ford", "model": "F-150 Platinum", "type": "truck", "price": 62000},
        {"make": "Ford", "model": "F-150 Limited", "type": "truck", "price": 75000},
        {"make": "RAM", "model": "1500 Limited", "type": "truck", "price": 64000},
        {"make": "Toyota", "model": "Tundra TRD Pro", "type": "truck", "price": 55000},
        {"make": "Toyota", "model": "Tundra Capstone", "type": "truck", "price": 70000},
        {"make": "Nissan", "model": "Titan Platinum Reserve", "type": "truck", "price": 58000},
        # More trucks at various price points
        {"make": "Ford", "model": "F-150 XLT", "type": "truck", "price": 42000},
        {"make": "Chevrolet", "model": "Silverado LT", "type": "truck", "price": 45000},
        {"make": "RAM", "model": "1500 Big Horn", "type": "truck", "price": 46000},
        {"make": "GMC", "model": "Sierra", "type": "truck", "price": 48000},
        # Luxury sedans and SUVs
        {"make": "Mercedes-Benz", "model": "S-Class", "type": "luxury", "price": 95000},
        {"make": "BMW", "model": "X7", "type": "luxury", "price": 78000},
        {"make": "Audi", "model": "Q8", "type": "luxury", "price": 72000},
        {"make": "Lexus", "model": "LX", "type": "luxury", "price": 88000},
        {"make": "Cadillac", "model": "Escalade", "type": "luxury", "price": 82000},
    ]

    # Filter vehicles based on the search criteria
    def vehicle_matches(vehicle):
        # Handle "truck" as a general search term
        if search_input.lower() == "truck" and vehicle["type"] == "truck":
            matches_search_input = True
        else:
            # Try to match make and model (either directly or with normalized values)
            vehicle_full_name = f"{vehicle['make']} {vehicle['model']}".lower()
            matches_search_input = search_input.lower() in vehicle_full_name
            
            # If no direct match, try normalized matching for specific truck models
            if not matches_search_input:
                normalized_make, normalized_model = normalize_make_model(search_input)
                if normalized_make and normalized_model:
                    if (normalized_make.lower() in vehicle["make"].lower() and 
                        normalized_model.lower() in vehicle["model"].lower()):
                        matches_search_input = True
        
        # Type matching
        matches_type = type is None or vehicle["type"] == type
        
        # Price range matching
        matches_price = price is None or (price[0] <= vehicle["price"] <= price[1])
        
        return matches_search_input and matches_type and matches_price

    similar_vehicles = [
        vehicle for vehicle in sample_vehicles if vehicle_matches(vehicle)
    ]

    if not similar_vehicles:
        # Generate fallback vehicles based on the input if no matches found
        fallback_vehicles = []
        
        # For truck searches with no matches, return some trucks in the price range
        if type == "truck" or "truck" in search_input.lower():
            truck_vehicles = [v for v in sample_vehicles if v["type"] == "truck"]
            # Filter by price if specified
            if price:
                truck_vehicles = [v for v in truck_vehicles if price[0] <= v["price"] <= price[1]]
            # Take up to 3 trucks
            fallback_vehicles = truck_vehicles[:3] if truck_vehicles else []
            
        # For GMC or Denali searches, find the closest matches
        if "gmc" in search_input.lower() or "denali" in search_input.lower():
            gmc_vehicles = [v for v in sample_vehicles if "gmc" in v["make"].lower()]
            # Filter by price if specified
            if price:
                gmc_vehicles = [v for v in gmc_vehicles if price[0] <= v["price"] <= price[1]]
            # Add any GMC vehicles
            fallback_vehicles = gmc_vehicles if gmc_vehicles else fallback_vehicles
            
        # If we found fallbacks, use them instead of raising an error
        if fallback_vehicles:
            similar_vehicles = fallback_vehicles
        else:
            raise ValueError(f"No similar vehicles found for search input: {search_input}")

    return {
        "search_input": search_input,
        "similar_vehicles": similar_vehicles,
    }


from typing import Dict, List


def find_used_car_part_dealer(city: str) -> Dict[str, List[str]]:
    """Find dealers selling used car parts in the specified city.

    Args:
        city: The city to search for car part dealers.

    Returns:
        Dict containing:
            - city: The city name
            - dealers: List of dealer names selling used car parts
    """

    sample_data = {
        "New York": ["NYC Auto Parts", "Manhattan Motors", "Brooklyn Car Spares"],
        "Los Angeles": [
            "LA Parts Depot",
            "Hollywood Auto Salvage",
            "Westside Car Parts",
        ],
        "Chicago": [
            "Windy City Auto Parts",
            "Chicago Car Components",
            "Midwest Motors",
        ],
        "Houston": ["Houston Auto Hub", "Lone Star Car Parts", "Bayou City Spares"],
        "Phoenix": [
            "Desert Auto Parts",
            "Phoenix Car Salvage",
            "Valley Car Components",
        ],
        "Wellington": ["Radiator Springs Parts'n'More"],
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    return {
        "city": city,
        "dealers": sample_data[city],
    }


from typing import Dict, List, Union


def get_bus(
    loc: str,
    full: bool,
    cost: float,
    stops: List[str] = None,
    arr_time: List[str] = None,
) -> List[Dict[str, Union[str, float, bool, List[str]]]]:
    """Returns a list of available buses based on the given criteria.

    Args:
        loc: Initial location of the main bus stop.
        full: Filters whether the bus is full or not.
        cost: Cost of the bus ticket.
        stops: List of the bus stops along the way.
        arr_time: Timestamp of when the bus arrives at each stop.

    Returns:
        List of dictionaries, each containing:
            - bus_id: Unique identifier for the bus
            - loc: Initial location of the main bus stop
            - full: Whether the bus is full or not
            - cost: Cost of the bus ticket
            - stops: List of the bus stops along the way
            - arr_time: Timestamp of when the bus arrives at each stop
    """

    # Extended sample buses with more locations including Macroom
    sample_buses = [
        {
            "bus_id": "B123",
            "loc": "Downtown",
            "full": False,
            "cost": 2.5,
            "stops": ["Main St", "2nd Ave", "3rd Ave"],
            "arr_time": ["08:00", "08:15", "08:30"],
        },
        {
            "bus_id": "B456",
            "loc": "Uptown",
            "full": True,
            "cost": 3.0,
            "stops": ["1st Ave", "Central Park", "5th Ave"],
            "arr_time": ["09:00", "09:20", "09:40"],
        },
        {
            "bus_id": "B789",
            "loc": "Midtown",
            "full": False,
            "cost": 2.0,
            "stops": ["Broadway", "7th Ave", "8th Ave"],
            "arr_time": ["10:00", "10:15", "10:30"],
        },
        # Irish locations
        {
            "bus_id": "B801",
            "loc": "Macroom",
            "full": False,
            "cost": 3.5,
            "stops": ["Main Square", "Castle Street", "Barrack Hill"],
            "arr_time": ["07:30", "07:45", "08:00"],
        },
        {
            "bus_id": "B802",
            "loc": "Macroom",
            "full": True,
            "cost": 2.8,
            "stops": ["Cork Road", "New Street", "Millstreet Road"],
            "arr_time": ["09:15", "09:30", "09:45"],
        },
        {
            "bus_id": "B803",
            "loc": "Macroom",
            "full": False,
            "cost": 3.2,
            "stops": ["Church Street", "Market Square", "Dan Corkery Bridge"],
            "arr_time": ["11:00", "11:15", "11:30"],
        },
        # Additional international locations
        {
            "bus_id": "B901",
            "loc": "Dublin",
            "full": False,
            "cost": 2.4,
            "stops": ["O'Connell St", "Temple Bar", "Trinity College"],
            "arr_time": ["08:30", "08:45", "09:00"],
        },
        {
            "bus_id": "B902",
            "loc": "Cork",
            "full": False,
            "cost": 2.6,
            "stops": ["Patrick Street", "Grand Parade", "English Market"],
            "arr_time": ["10:00", "10:15", "10:30"],
        },
        {
            "bus_id": "B903",
            "loc": "London",
            "full": True,
            "cost": 4.5,
            "stops": ["Big Ben", "Westminster", "London Bridge"],
            "arr_time": ["07:00", "07:20", "07:40"],
        },
    ]

    def generate_fallback_buses(location: str):
        """Generate sample buses for unknown locations using hash-based generation."""
        import hashlib

        hash_seed = int(hashlib.sha256(location.encode()).hexdigest(), 16)

        fallback_buses = []
        for i in range(2):  # Generate 2 buses for unknown locations
            bus_id = (
                f"B{(hash_seed + i) % 9000 + 1000}"  # Generate ID between B1000-B9999
            )
            is_full = (hash_seed + i) % 2 == 0
            bus_cost = 2.0 + ((hash_seed + i) % 20) / 10  # Cost between 2.0 and 4.0

            # Generate stops based on location
            stops = [f"{location} Central", f"{location} Station", f"{location} Mall"]

            # Generate arrival times
            base_hour = 8 + (i * 2)
            arr_times = [
                f"{base_hour:02d}:00",
                f"{base_hour:02d}:15",
                f"{base_hour:02d}:30",
            ]

            fallback_buses.append(
                {
                    "bus_id": bus_id,
                    "loc": location,
                    "full": is_full,
                    "cost": round(bus_cost, 1),
                    "stops": stops,
                    "arr_time": arr_times,
                }
            )

        return fallback_buses

    # Find buses for the requested location
    location_buses = [bus for bus in sample_buses if bus["loc"] == loc]

    # If no buses found for location, generate fallback buses
    if not location_buses:
        location_buses = generate_fallback_buses(loc)

    # Apply filters
    filtered_buses = [
        bus for bus in location_buses if bus["full"] == full and bus["cost"] <= cost
    ]

    if stops:
        filtered_buses = [
            bus for bus in filtered_buses if set(stops).issubset(bus["stops"])
        ]

    if arr_time:
        filtered_buses = [
            bus for bus in filtered_buses if set(arr_time).issubset(bus["arr_time"])
        ]

    if not filtered_buses:
        raise ValueError("No buses available with the given criteria")

    return filtered_buses


from typing import Dict, List


def get_bus_times(
    departure_stop: str, arrival_stop: str, date: str
) -> Dict[str, List[Dict[str, str]]]:
    """Retrieves bus departure and arrival times between two bus stops for a given date.

    Args:
        departure_stop: The bus stop where the journey starts.
        arrival_stop: The bus stop where the journey ends.
        date: The date of travel in ISO 8601 format (YYYY-MM-DD).

    Returns:
        Dict containing:
            - times: List of dictionaries with 'departure' and 'arrival' times
    """
    if not departure_stop or not arrival_stop or not date:
        raise ValueError("All parameters must be provided and non-empty.")

    # Mock data generation based on hash of inputs for consistency
    hash_seed = hash((departure_stop, arrival_stop, date))
    base_hour = hash_seed % 24  # Ensure hour is within 0-23
    times = []

    for i in range(5):  # Generate 5 sample bus times
        departure_hour = (base_hour + i) % 24
        arrival_hour = (departure_hour + 1) % 24  # Assume 1 hour travel time
        times.append(
            {"departure": f"{departure_hour:02}:00", "arrival": f"{arrival_hour:02}:00"}
        )

    return {"times": times}


from typing import Dict, Union


def get_car_details(registration_number: str) -> Dict[str, Union[str, int]]:
    """Gets the make, model, and year of a car given the registration number.

    Args:
        registration_number: Registration number of the car to find.

    Returns:
        Dict containing:
            - make: Car make
            - model: Car model
            - year: Year of manufacture
    """

    # Sample data based on registration number hash
    sample_data = {
        "ABC123": {"make": "Toyota", "model": "Camry", "year": 2010},
        "XYZ789": {"make": "Ford", "model": "Mustang", "year": 2018},
        "LMN456": {"make": "Honda", "model": "Civic", "year": 2015},
    }

    # Hash-based generation for consistent but varied sample data
    if registration_number not in sample_data:
        raise ValueError(f"Registration number not found: {registration_number}")

    return sample_data[registration_number]


from typing import Dict, Union


def get_car_information(
    car_make: str, car_model: str
) -> Dict[str, Union[str, int, float]]:
    """Retrieve various information about a specific car model.

    Args:
        car_make: The make of the vehicle (e.g., 'Toyota', 'Ford')
        car_model: The model of the vehicle (e.g., 'Camry', 'Mustang')

    Returns:
        Dict containing:
            - make: The make of the vehicle
            - model: The model of the vehicle
            - year: The year the model was released
            - horsepower: The horsepower of the vehicle
            - price: The average price of the vehicle in USD
    """

    def fuzzy_match_car_info(
        search_make: str, search_model: str, car_data: dict
    ) -> tuple:
        """Find the best matching car make/model using fuzzy matching"""
        search_make_lower = search_make.lower().strip()
        search_model_lower = search_model.lower().strip()

        # Direct exact match first
        for make, model in car_data.keys():
            if (
                make.lower() == search_make_lower
                and model.lower() == search_model_lower
            ):
                return (make, model)

        # Fuzzy make matching
        make_variants = {
            "gmc": ["gmc", "general motors"],
            "chevrolet": ["chevrolet", "chevy"],
            "ford": ["ford"],
            "toyota": ["toyota"],
            "honda": ["honda"],
            "nissan": ["nissan"],
            "ram": ["ram", "dodge ram"],
            "cadillac": ["cadillac"],
        }

        # Model-specific fuzzy matching for trucks
        model_variants = {
            "denali": ["denali", "denalt", "denalli", "denaly"],
            "sierra": ["sierra", "sienna"],
            "silverado": ["silverado", "silvarado"],
            "yukon": ["yukon"],
            "escalade": ["escalade"],
            "f-150": ["f-150", "f150", "f 150"],
            "f-250": ["f-250", "f250", "f 250"],
            "f-350": ["f-350", "f350", "f 350"],
        }

        # Find matching make
        matched_make = None
        for base_make, variants in make_variants.items():
            if search_make_lower in variants:
                matched_make = base_make
                break

        # If no direct make match, try partial matching
        if not matched_make:
            for make, model in car_data.keys():
                if (
                    search_make_lower in make.lower()
                    or make.lower() in search_make_lower
                ):
                    matched_make = make.lower()
                    break

        # Find matching model
        matched_model = None
        for base_model, variants in model_variants.items():
            if search_model_lower in variants:
                matched_model = base_model
                break

        # If no direct model match, try partial matching
        if not matched_model:
            for make, model in car_data.keys():
                if (
                    search_model_lower in model.lower()
                    or model.lower() in search_model_lower
                ):
                    matched_model = model.lower()
                    break

        # Find best match in car_data
        for make, model in car_data.keys():
            make_match = matched_make and (
                matched_make == make.lower()
                or search_make_lower in make.lower()
                or make.lower() in search_make_lower
            )

            model_match = matched_model and (
                matched_model in model.lower()
                or search_model_lower in model.lower()
                or model.lower() in search_model_lower
            )

            if make_match and model_match:
                return (make, model)

        return None

    # Expanded sample data with trucks and luxury vehicles
    sample_data = {
        ("Toyota", "Camry"): {"year": 2020, "horsepower": 203, "price": 24425},
        ("Ford", "Mustang"): {"year": 2021, "horsepower": 450, "price": 55000},
        ("Honda", "Civic"): {"year": 2019, "horsepower": 158, "price": 20500},
        ("GMC", "Sierra Denali"): {"year": 2023, "horsepower": 420, "price": 75000},
        ("GMC", "Yukon Denali"): {"year": 2023, "horsepower": 420, "price": 82000},
        ("GMC", "Sierra 1500"): {"year": 2023, "horsepower": 355, "price": 65000},
        ("Chevrolet", "Silverado 1500"): {
            "year": 2023,
            "horsepower": 355,
            "price": 62000,
        },
        ("Ford", "F-150"): {"year": 2023, "horsepower": 400, "price": 68000},
        ("Ford", "F-250"): {"year": 2023, "horsepower": 475, "price": 78000},
        ("Ford", "F-350"): {"year": 2023, "horsepower": 475, "price": 85000},
        ("Ram", "1500"): {"year": 2023, "horsepower": 395, "price": 64000},
        ("Ram", "2500"): {"year": 2023, "horsepower": 410, "price": 76000},
        ("Cadillac", "Escalade"): {"year": 2023, "horsepower": 420, "price": 95000},
        ("Lincoln", "Navigator"): {"year": 2023, "horsepower": 440, "price": 88000},
        ("Toyota", "Tundra"): {"year": 2023, "horsepower": 389, "price": 58000},
        ("Nissan", "Titan"): {"year": 2023, "horsepower": 400, "price": 55000},
        ("Jeep", "Grand Cherokee"): {"year": 2023, "horsepower": 357, "price": 52000},
        ("BMW", "X7"): {"year": 2023, "horsepower": 523, "price": 92000},
        ("Mercedes-Benz", "GLS"): {"year": 2023, "horsepower": 483, "price": 89000},
        ("Audi", "Q8"): {"year": 2023, "horsepower": 335, "price": 79000},
    }

    # Try fuzzy matching first
    matched_key = fuzzy_match_car_info(car_make, car_model, sample_data)

    if matched_key:
        make, model = matched_key
        car_info = sample_data[(make, model)]
        return {
            "make": make,
            "model": model,
            "year": car_info["year"],
            "horsepower": car_info["horsepower"],
            "price": car_info["price"],
        }

    # If no fuzzy match, generate info based on inputs
    # Generate consistent but varied data based on hash
    hash_seed = hash(car_make.lower() + car_model.lower())

    # Determine vehicle type for appropriate specs
    is_truck = any(
        word in car_model.lower()
        for word in ["truck", "f-", "sierra", "silverado", "ram", "tundra", "titan"]
    )
    is_luxury = any(
        word in car_make.lower()
        for word in ["bmw", "mercedes", "audi", "cadillac", "lincoln", "lexus"]
    )

    if is_truck:
        base_hp = 300 + (hash_seed % 200)  # 300-500 HP for trucks
        base_price = 50000 + (hash_seed % 40000)  # $50k-$90k for trucks
    elif is_luxury:
        base_hp = 250 + (hash_seed % 300)  # 250-550 HP for luxury
        base_price = 40000 + (hash_seed % 60000)  # $40k-$100k for luxury
    else:
        base_hp = 150 + (hash_seed % 200)  # 150-350 HP for regular cars
        base_price = 20000 + (hash_seed % 30000)  # $20k-$50k for regular cars

    year = 2020 + (hash_seed % 4)  # 2020-2023

    return {
        "make": car_make,
        "model": car_model,
        "year": year,
        "horsepower": base_hp,
        "price": base_price,
    }


from typing import Dict, List


def get_car_reviews(search_input: str) -> Dict[str, Union[str, List[str]]]:
    """Returns a list of reviews of a specific vehicle model.

    Args:
        search_input: The make and or model of a vehicle (e.g. 'Toyota Camry', 'Ford F-150')

    Returns:
        Dict containing:
            - model: The make and model of the vehicle
            - reviews: List of reviews for the specified vehicle model
    """

    sample_reviews = {
        "Toyota Camry": [
            "Smooth ride and great fuel efficiency.",
            "Comfortable interior with plenty of space.",
            "Reliable and affordable maintenance.",
        ],
        "Ford F-150": [
            "Powerful engine with excellent towing capacity.",
            "Spacious cabin and advanced tech features.",
            "Rugged design, perfect for off-road adventures.",
        ],
        "Honda Civic": [
            "Sporty design with a comfortable ride.",
            "Excellent fuel economy and low emissions.",
            "High resale value and reliable performance.",
        ],
    }

    if search_input not in sample_reviews:
        raise ValueError(f"Vehicle model not supported: {search_input}")

    return {
        "model": search_input,
        "reviews": sample_reviews.get(search_input),
    }


from typing import Dict, Literal, Union


def get_car_value(
    make: str,
    model: str,
    condition: Literal["new", "used"],
    mileage: float,
    car_identification_type: Literal["vin", "license_plate"],
    car_identification: str,
) -> Dict[str, Union[str, float]]:
    """Returns current value of a vehicle based on retail prices and current trends.

    Args:
        make: Make of a car (e.g., 'Toyota', 'Ford')
        model: Model of a car (e.g., 'Camry', 'Mustang')
        condition: Condition of the vehicle ('new' or 'used')
        mileage: Car mileage
        car_identification_type: Type of the identification used for the search ('vin' or 'license_plate')
        car_identification: Car identification value

    Returns:
        Dict containing:
            - make: Make of the car
            - model: Model of the car
            - estimated_value: Estimated current value of the car in USD
    """

    # Sample base values for demonstration purposes
    base_values = {
        ("Toyota", "Camry"): 24000,
        ("Ford", "Mustang"): 26000,
        ("Honda", "Civic"): 22000,
    }

    # Calculate depreciation based on mileage and condition
    depreciation_rate = 0.2 if condition == "used" else 0.0
    mileage_factor = max(0, 1 - (mileage / 100000) * 0.1)

    # Generate a base value using make and model
    base_value = base_values.get(
        (make, model), 20000
    )  # Default base value if not found

    # Calculate the estimated value
    estimated_value = base_value * (1 - depreciation_rate) * mileage_factor

    # Simulate a hash-based adjustment for consistent variation
    hash_adjustment = hash(car_identification) % 1000 / 1000
    estimated_value *= 0.95 + hash_adjustment * 0.1

    return {
        "make": make,
        "model": model,
        "estimated_value": round(estimated_value, 2),
    }


import hashlib
from typing import Dict, Union


def get_fuel_price_by_city(
    city: str, date: str = "2025-01-01"
) -> Dict[str, Union[str, float]]:
    """Get the fuel price for a given city in the EU on a specific date.

    Args:
        city: The city name to get the fuel price for (e.g. 'Berlin', 'Madrid')
        date: The date to search the fuel price for in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - city: City name
            - date: Date of the fuel price
            - fuel_price: Fuel price in EUR per liter
    """

    supported_cities = [
        "Berlin",
        "Madrid",
        "Paris",
        "Rome",
        "Amsterdam",
        "Nuremburg",
        "Nuremberg",
        "Munich",
    ]
    if city not in supported_cities:
        raise ValueError(f"City not supported: {city}")

    # Generate a consistent but varied fuel price based on city and date
    hash_input = f"{city}-{date}".encode()
    hash_value = hashlib.sha256(hash_input).hexdigest()
    fuel_price = (
        int(hash_value[:8], 16) % 1000
    ) / 100 + 1.0  # Price between 1.00 and 10.00 EUR

    return {
        "city": city,
        "date": date,
        "fuel_price": fuel_price,
    }


from typing import Dict, List


def get_makes() -> Dict[str, List[str]]:
    """Retrieve a list of known vehicle makes.

    Returns:
        Dict containing:
            - makes: List of vehicle makes
    """

    makes_sample = [
        "Toyota",
        "Ford",
        "Chevrolet",
        "Honda",
        "Nissan",
        "BMW",
        "Mercedes-Benz",
        "Volkswagen",
        "Hyundai",
        "Audi",
    ]

    return {"makes": makes_sample}


from typing import Dict, Literal, Union


def get_maximum_tire_pressure(
    tin: str, units: Literal["psi", "bar"]
) -> Dict[str, Union[str, float]]:
    """Retrieve the maximum allowed pressure for a vehicle's tires.

    Args:
        tin: Tire Identification Number (TIN). A unique alphanumeric value following the 'DOT' code.
        units: Units of tire pressure ('psi' or 'bar').

    Returns:
        Dict containing:
            - tin: The provided Tire Identification Number
            - max_pressure: Maximum allowed tire pressure in the specified units
            - units: The units of the tire pressure
    """

    # Simulated database of TIN to maximum pressure in psi
    tin_to_pressure_psi = {
        "DOT123456": 35.0,
        "DOT654321": 40.0,
        "DOT111111": 32.0,
    }

    if tin not in tin_to_pressure_psi:
        raise ValueError(f"TIN not supported: {tin}")

    max_pressure_psi = tin_to_pressure_psi[tin]

    if units == "psi":
        max_pressure = max_pressure_psi
    elif units == "bar":
        max_pressure = max_pressure_psi * 0.0689476
    else:
        raise ValueError("Unsupported units")

    return {
        "tin": tin,
        "max_pressure": round(max_pressure, 2),
        "units": units,
    }


from typing import Dict, List


def get_models(make: str) -> Dict[str, List[str]]:
    """Retrieve a list of vehicle models for a specified make.

    Args:
        make: The vehicle make under which to search for vehicle models.

    Returns:
        Dict containing:
            - make: The vehicle make
            - models: List of vehicle models for the specified make
    """

    sample_data = {
        "Toyota": ["Camry", "Corolla", "Prius"],
        "Ford": ["F-150", "Mustang", "Explorer"],
        "Honda": ["Civic", "Accord", "CR-V"],
    }

    if make not in sample_data:
        raise ValueError(f"Make not supported: {make}")

    return {
        "make": make,
        "models": sample_data[make],
    }


from typing import Dict, Literal


def get_recommended_tire_pressure(
    make: str, model: str, year: int, option: str, units: Literal["psi", "bar"]
) -> Dict[str, Union[str, float]]:
    """Retrieve the recommended tire pressure for a vehicle.

    Args:
        make: Make of the vehicle.
        model: Model of the vehicle.
        year: Year of the vehicle.
        option: Vehicle option (e.g. 'Sedan EX').
        units: Units of tire pressure ('psi' or 'bar').

    Returns:
        Dict containing:
            - make: Make of the vehicle
            - model: Model of the vehicle
            - year: Year of the vehicle
            - option: Vehicle option
            - recommended_pressure: Recommended tire pressure in specified units
            - units: Units of the tire pressure
    """
    # Sample tire pressure data based on make, model, year, and option
    sample_data = {
        ("Toyota", "Camry", 2020, "Sedan LE"): 35,
        ("Honda", "Civic", 2019, "Sedan EX"): 32,
        ("Ford", "F-150", 2021, "Truck XLT"): 40,
    }

    key = (make, model, year, option)
    if key not in sample_data:
        raise ValueError(f"Vehicle configuration not supported: {key}")

    pressure_psi = sample_data[key]

    if units == "bar":
        recommended_pressure = pressure_psi * 0.0689476
    else:
        recommended_pressure = pressure_psi

    return {
        "make": make,
        "model": model,
        "year": year,
        "option": option,
        "recommended_pressure": round(recommended_pressure, 2),
        "units": units,
    }


from typing import Dict, List, Optional, Union


def get_taxi(
    range: float,
    availability: bool,
    cost: float,
    smoke: Optional[bool] = False,
    arr_time: Optional[str] = None,
) -> List[Dict[str, Union[str, float, bool]]]:
    """Returns a list of available taxis based on the given criteria.

    Args:
        range: Number of kilometres the taxi has to drive.
        availability: Filters whether the taxi is available or not.
        cost: Cost of the taxi per km.
        smoke: Filters whether the taxi allows smoking or not.
        arr_time: Timestamp of when the taxi arrives for pickup.

    Returns:
        List of dictionaries, each containing:
            - id: Unique identifier for the taxi
            - driver: Name of the taxi driver
            - range: Maximum range the taxi can drive
            - availability: Availability status of the taxi
            - cost: Cost per km
            - smoke: Smoking allowed status
            - arr_time: Arrival time for pickup
    """

    sample_taxis = [
        {
            "id": "TX001",
            "driver": "Alice",
            "range": 50,
            "availability": True,
            "cost": 1.5,
            "smoke": False,
            "arr_time": "2023-10-01T10:00:00",
        },
        {
            "id": "TX002",
            "driver": "Bob",
            "range": 100,
            "availability": False,
            "cost": 2.0,
            "smoke": True,
            "arr_time": "2023-10-01T11:00:00",
        },
        {
            "id": "TX003",
            "driver": "Charlie",
            "range": 75,
            "availability": True,
            "cost": 1.8,
            "smoke": False,
            "arr_time": "2023-10-01T12:00:00",
        },
    ]

    filtered_taxis = [
        taxi
        for taxi in sample_taxis
        if taxi["range"] >= range
        and taxi["availability"] == availability
        and taxi["cost"] <= cost
        and (smoke is None or taxi["smoke"] == smoke)
        and (arr_time is None or taxi["arr_time"] == arr_time)
    ]

    return filtered_taxis


from typing import Dict, List


def get_tires(make: str, model: str, year: int) -> Dict[str, Union[str, List[str]]]:
    """Retrieve OEM factory tire sizes for a specified vehicle make, model, and year.

    Args:
        make: The vehicle make under which to search for tire sizes (e.g. 'Toyota', 'Ford')
        model: The vehicle model under which to search for tire sizes (e.g. 'Camry', 'Mustang')
        year: The year of manufacture under which to search for tire sizes (e.g. 2020, 2021)

    Returns:
        Dict containing:
            - make: Vehicle make
            - model: Vehicle model
            - year: Year of manufacture
            - tire_sizes: List of OEM factory tire sizes
    """
    # Sample data for demonstration purposes
    sample_data = {
        ("Toyota", "Camry", 2020): ["205/65R16", "215/55R17"],
        ("Ford", "Mustang", 2021): ["235/50R18", "255/40R19"],
        ("Honda", "Civic", 2022): ["215/55R16", "225/45R17"],
    }

    key = (make, model, year)
    if key not in sample_data:
        raise ValueError(f"Tire sizes not available for {make} {model} {year}")

    return {
        "make": make,
        "model": model,
        "year": year,
        "tire_sizes": sample_data[key],
    }


from typing import Dict, Union


def get_traffic(street_name: str) -> Dict[str, Union[str, bool]]:
    """Get up-to-date information on if a street has heavy traffic or not.

    Args:
        street_name: Street name to get traffic status for.

    Returns:
        Dict containing:
            - street_name: Name of the street
            - heavy_traffic: Boolean indicating if there is heavy traffic
    """

    # Simulated traffic data based on street names
    traffic_data = {
        "Main Street": True,
        "Broadway": False,
        "Elm Street": True,
        "5th Avenue": False,
        "Sunset Boulevard": True,
    }

    if street_name not in traffic_data:
        raise ValueError(f"Street not supported: {street_name}")

    return {
        "street_name": street_name,
        "heavy_traffic": traffic_data.get(street_name),
    }


import hashlib
from typing import Dict, List, Union


def get_train_times(
    departure_station: str, arrival_station: str, date: str
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Retrieves train departure and arrival times between two stations for a given date.

    Args:
        departure_station: The station where the journey starts.
        arrival_station: The station where the journey ends.
        date: The date of travel in ISO 8601 format (YYYY-MM-DD).

    Returns:
        Dict containing:
            - departure_station: The station where the journey starts.
            - arrival_station: The station where the journey ends.
            - date: The date of travel.
            - schedule: List of dictionaries with 'departure_time' and 'arrival_time'.
    """

    if not departure_station or not arrival_station or not date:
        raise ValueError("All parameters must be provided and non-empty.")

    # Generate a consistent hash-based seed for reproducible sample data
    seed = int(
        hashlib.sha256(
            f"{departure_station}{arrival_station}{date}".encode()
        ).hexdigest(),
        16,
    )

    # Generate mock train times
    schedule = []
    for i in range(3):  # Assume 3 trains per day for simplicity
        departure_hour = (seed % 24 + i * 3) % 24
        arrival_hour = (departure_hour + 2) % 24
        schedule.append(
            {
                "departure_time": f"{departure_hour:02d}:00",
                "arrival_time": f"{arrival_hour:02d}:00",
            }
        )

    return {
        "departure_station": departure_station,
        "arrival_station": arrival_station,
        "date": date,
        "schedule": schedule,
    }


from typing import Dict, List


def get_trains(
    from_city: str, to_city: str
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Returns train routes for a given day from one city to another.

    Args:
        from_city: The city to depart from
        to_city: The destination city

    Returns:
        Dict containing:
            - from: Departure city name
            - to: Destination city name
            - routes: List of routes with train details
    """

    if not from_city or not to_city:
        raise ValueError("Both 'from_city' and 'to_city' must be provided")

    # Sample data simulating train routes
    sample_routes = {
        ("New York", "Boston"): [
            {
                "train": "Acela Express",
                "departure": "08:00 AM",
                "arrival": "11:00 AM",
                "duration": 180,
            },
            {
                "train": "Northeast Regional",
                "departure": "09:00 AM",
                "arrival": "12:30 PM",
                "duration": 210,
            },
        ],
        ("San Francisco", "Los Angeles"): [
            {
                "train": "Coast Starlight",
                "departure": "07:15 AM",
                "arrival": "01:30 PM",
                "duration": 375,
            },
            {
                "train": "Pacific Surfliner",
                "departure": "10:00 AM",
                "arrival": "04:00 PM",
                "duration": 360,
            },
        ],
    }

    routes = sample_routes.get((from_city, to_city))
    if routes is None:
        raise ValueError(f"No train routes available from {from_city} to {to_city}")

    return {
        "from": from_city,
        "to": to_city,
        "routes": routes,
    }


from typing import Dict


def order_cab(from_location: str, to_location: str) -> Dict[str, str]:
    """Book a cab from one location to another.

    Args:
        from_location: The starting point for the cab ride.
        to_location: The destination for the cab ride.

    Returns:
        Dict containing:
            - booking_id: Unique identifier for the cab booking
            - status: Current status of the booking
            - from_location: Starting point of the cab ride
            - to_location: Destination of the cab ride
    """
    if not from_location or not to_location:
        raise ValueError("Both from_location and to_location must be provided.")

    # Simulate a unique booking ID using a hash-based approach
    booking_id = f"BOOK-{hash(from_location + to_location) % 10000:04d}"

    return {
        "booking_id": booking_id,
        "status": "confirmed",
        "from_location": from_location,
        "to_location": to_location,
    }


import hashlib
from typing import Dict, Union


def rent_ev_adapter(
    adapter_type: str, pickup_location: str, date: str, duration_hours: float = 24
) -> Dict[str, Union[str, float]]:
    """Reserve a temporary EV adapter for pickup at a specified location.

    Args:
        adapter_type: Adapter type requested (e.g., 'CHAdeMO', 'NACS').
        pickup_location: Store or kiosk for pickup.
        date: Pickup date in YYYY-MM-DD format.
        duration_hours: Rental duration in hours (default is 24).

    Returns:
        Dict containing:
            - reservation_id: Unique identifier for the reservation
            - adapter_type: Type of adapter reserved
            - pickup_location: Location for pickup
            - date: Date of pickup
            - duration_hours: Duration of the rental in hours
            - status: Reservation status
    """
    if adapter_type not in ["CHAdeMO", "NACS"]:
        raise ValueError(f"Unsupported adapter type: {adapter_type}")

    if not pickup_location:
        raise ValueError("Pickup location must be specified")

    if not date:
        raise ValueError("Pickup date must be specified")

    # Generate a unique reservation ID using a hash
    reservation_id = hashlib.md5(
        f"{adapter_type}-{pickup_location}-{date}".encode()
    ).hexdigest()

    return {
        "reservation_id": reservation_id,
        "adapter_type": adapter_type,
        "pickup_location": pickup_location,
        "date": date,
        "duration_hours": duration_hours,
        "status": "reserved",
    }


from typing import Dict, List, Union


def report_station_issue(
    station_id: str, issue_type: str, notes: str = "", photo_urls: List[str] = []
) -> Dict[str, Union[str, List[str]]]:
    """File a report about a charger problem.

    Args:
        station_id: Provider's station identifier.
        issue_type: Short label for the issue (e.g., 'blocked', 'offline', 'payment_error').
        notes: Free-text description with any relevant details.
        photo_urls: Optional photos for evidence.

    Returns:
        Dict containing:
            - report_id: Unique identifier for the filed report
            - status: Status of the report submission
            - message: Confirmation message
            - submitted_photos: List of URLs of submitted photos
    """
    if not station_id or not issue_type:
        raise ValueError("station_id and issue_type are required fields")

    # Simulate report ID generation using a hash-based approach
    report_id = f"RPT-{hash((station_id, issue_type, notes)) % 10000:04d}"

    return {
        "report_id": report_id,
        "status": "submitted",
        "message": f"Issue '{issue_type}' reported successfully for station {station_id}.",
        "submitted_photos": photo_urls,
    }


from typing import Dict, Union


def reserve_parking(
    location: str,
    date: str,
    start_time: str,
    duration_minutes: int,
    covered: bool = False,
    max_price_per_hour: Union[float, None] = None,
    license_plate: Union[str, None] = None,
) -> Dict[str, Union[str, float, bool]]:
    """Reserve a garage or lot parking space for a given time window.

    Args:
        location: Address or POI near which to reserve parking.
        date: Reservation date in YYYY-MM-DD.
        start_time: Start time in 24h HH:MM local time.
        duration_minutes: Total duration for the reservation.
        covered: Require a covered spot.
        max_price_per_hour: Price ceiling in local currency.
        license_plate: Vehicle plate for the reservation (if required).

    Returns:
        Dict containing:
            - reservation_id: Unique identifier for the reservation
            - location: Location of the reserved parking
            - start_time: Start time of the reservation
            - end_time: End time of the reservation
            - covered: Whether the spot is covered
            - price: Total price for the reservation
    """
    if duration_minutes <= 0:
        raise ValueError("Duration must be greater than zero.")

    # Mock data generation using a simple hash-based approach
    reservation_id = hash((location, date, start_time, duration_minutes, covered))
    end_time = f"{int(start_time.split(':')[0]) + duration_minutes // 60}:{int(start_time.split(':')[1]) + duration_minutes % 60:02d}"
    price_per_hour = 5.0 if not covered else 7.0
    if max_price_per_hour is not None and price_per_hour > max_price_per_hour:
        raise ValueError("No available spots within the specified price range.")

    total_price = (duration_minutes / 60) * price_per_hour

    return {
        "reservation_id": str(reservation_id),
        "location": location,
        "start_time": start_time,
        "end_time": end_time,
        "covered": covered,
        "price": round(total_price, 2),
    }


from typing import Dict, List, Union


def ride_history(
    username: str, is_completed: bool = False
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Retrieve the ride history for a user.

    Args:
        username: The username of the ride app user
        is_completed: Boolean indicating if the trip is in the past (completed) or future (upcoming)

    Returns:
        Dict containing:
            - username: The username of the ride app user
            - trips: List of trips with details including:
                - date: Date of the trip
                - origin: Starting point of the trip
                - destination: Ending point of the trip
                - cost: Cost of the trip in USD
    """

    if not username:
        raise ValueError("Username must be provided")

    # Sample data based on username hash for consistency
    sample_data = {
        "completed": [
            {
                "date": "2023-01-15",
                "origin": "Downtown",
                "destination": "Airport",
                "cost": 35.50,
            },
            {
                "date": "2023-02-20",
                "origin": "Home",
                "destination": "Office",
                "cost": 12.75,
            },
        ],
        "upcoming": [
            {
                "date": "2023-12-01",
                "origin": "Office",
                "destination": "Gym",
                "cost": 8.00,
            },
            {
                "date": "2023-12-05",
                "origin": "Mall",
                "destination": "Home",
                "cost": 15.25,
            },
        ],
    }

    trips = sample_data["completed"] if is_completed else sample_data["upcoming"]

    return {
        "username": username,
        "trips": trips,
    }


from typing import Dict, Union


def ride_share_look_up(
    current_location: Union[Dict[str, Union[str, Dict[str, float]]], str],
    destination_location: Union[Dict[str, Union[str, Dict[str, float]]], str],
) -> Dict[str, Union[str, float]]:
    """Get the price of rides from ride share apps based on parameters.

    Args:
        current_location: The user's current location (string like 'Mesa, Colorado' or dictionary containing location details)
        destination_location: The destination location (string like 'Denver, CO' or dictionary containing location details)

    Returns:
        Dict containing:
            - service: Name of the ride share service
            - estimated_price: Estimated price for the ride in USD
            - currency: Currency of the estimated price
    """

    def convert_location_parameter(location):
        """Helper function to convert string location to expected dictionary format"""
        if isinstance(location, str):
            # Handle string representation of dictionary
            if location.startswith("{") and location.endswith("}"):
                try:
                    import ast

                    parsed_location = ast.literal_eval(location)
                    if isinstance(parsed_location, dict):
                        # Ensure we have coordinates even if not provided
                        if "coordinates" not in parsed_location:
                            parsed_location["coordinates"] = {
                                "latitude": 0.0,
                                "longitude": 0.0,
                            }
                        return parsed_location
                except (ValueError, SyntaxError):
                    pass

            # Handle plain string like "Mesa" or "Denver, Colorado"
            city = location.strip()
            # Generate mock coordinates based on hash for consistency
            coord_hash = hash(city) % 3600  # Generate values between 0-3600
            lat = (coord_hash % 180) - 90  # Latitude between -90 and 90
            lon = ((coord_hash * 2) % 360) - 180  # Longitude between -180 and 180

            return {"city": city, "coordinates": {"latitude": lat, "longitude": lon}}
        return location

    # Convert location parameters if they are strings
    current_location = convert_location_parameter(current_location)
    destination_location = convert_location_parameter(destination_location)

    # Mock data for ride share services and their base prices
    services = {
        "Uber": 1.5,
        "Lyft": 1.3,
        "Bolt": 1.4,
    }

    # Calculate a mock distance based on coordinates difference
    current_coords = current_location["coordinates"]
    destination_coords = destination_location["coordinates"]
    distance = (
        (destination_coords["latitude"] - current_coords["latitude"]) ** 2
        + (destination_coords["longitude"] - current_coords["longitude"]) ** 2
    ) ** 0.5

    if distance == 0:
        raise ValueError("Current location and destination cannot be the same.")

    # Generate a consistent but varied price estimate using hash-based generation
    base_price = services["Uber"]  # Default to Uber for simplicity
    estimated_price = round(base_price * distance * 10, 2)  # Mock calculation for price

    return {
        "service": "Uber",
        "estimated_price": estimated_price,
        "currency": "USD",
    }


from typing import Dict, List, Union


def search_dealerships(
    make: str, model: str, location: str, search_radius: float = 2
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Get car dealerships for a specific car make and model around a location.

    Args:
        make: Make of the original car.
        model: Model of the original car.
        location: Postcode, city or coordinates, around which the search ought to happen.
        search_radius: Search radius in miles.

    Returns:
        Dict containing:
            - location: The location around which the search was conducted
            - dealerships: List of dealerships with their name, address, and distance from the location
    """

    if not make or not model or not location:
        raise ValueError("Make, model, and location are required parameters.")

    # Sample data generation based on hash of inputs for consistency
    sample_dealerships = [
        {"name": "Auto World", "address": "123 Main St", "distance": 1.5},
        {"name": "Car Hub", "address": "456 Elm St", "distance": 0.8},
        {"name": "DriveTime", "address": "789 Oak St", "distance": 2.0},
    ]

    # Filter dealerships within the search radius
    filtered_dealerships = [
        dealership
        for dealership in sample_dealerships
        if dealership["distance"] <= search_radius
    ]

    return {"location": location, "dealerships": filtered_dealerships}


from typing import Dict, List


def search_for_car_model(search_input: str) -> Dict[str, List[str]]:
    """Search for possible car models based on a full or partial input.

    Args:
        search_input: The make and or model of a vehicle

    Returns:
        Dict containing:
            - matches: List of possible car models that match the input
    """

    def fuzzy_match_car_model(search_term: str, car_list: List[str]) -> List[str]:
        """Find matching car models using fuzzy matching"""
        search_lower = search_term.lower().strip()
        matches = []

        # Direct substring match first
        for car in car_list:
            if search_lower in car.lower():
                matches.append(car)

        # If no direct matches, try fuzzy matching for common misspellings
        if not matches:
            # Handle common truck name variations
            if any(
                variant in search_lower for variant in ["denalt", "denalli", "denaly"]
            ):
                matches.extend([car for car in car_list if "denali" in car.lower()])

            if any(
                variant in search_lower
                for variant in ["silverado", "silvarado", "chevrolet"]
            ):
                matches.extend([car for car in car_list if "silverado" in car.lower()])

            if any(variant in search_lower for variant in ["sierra", "gmc"]):
                matches.extend(
                    [
                        car
                        for car in car_list
                        if "sierra" in car.lower() or "gmc" in car.lower()
                    ]
                )

            # Word-based fuzzy matching
            search_words = set(search_lower.split())
            for car in car_list:
                car_words = set(car.lower().split())
                if search_words and car_words:
                    overlap = search_words.intersection(car_words)
                    if len(overlap) / max(len(search_words), len(car_words)) > 0.4:
                        if car not in matches:
                            matches.append(car)

        return matches

    # Expanded car models including trucks and luxury vehicles
    car_models = [
        "Toyota Camry",
        "Toyota Corolla",
        "Toyota Prius",
        "Toyota Tacoma",
        "Toyota Tundra",
        "Honda Accord",
        "Honda Civic",
        "Honda CR-V",
        "Honda Pilot",
        "Ford Mustang",
        "Ford Focus",
        "Ford F-150",
        "Ford F-250",
        "Ford F-350",
        "Ford Explorer",
        "Ford Expedition",
        "Chevrolet Impala",
        "Chevrolet Malibu",
        "Chevrolet Silverado 1500",
        "Chevrolet Silverado 2500",
        "Chevrolet Tahoe",
        "Chevrolet Suburban",
        "GMC Sierra 1500",
        "GMC Sierra 2500",
        "GMC Yukon",
        "GMC Yukon Denali",
        "GMC Sierra Denali",
        "Cadillac Escalade",
        "Nissan Altima",
        "Nissan Sentra",
        "Nissan Titan",
        "Nissan Armada",
        "Ram 1500",
        "Ram 2500",
        "Ram 3500",
        "BMW X5",
        "BMW X7",
        "Mercedes-Benz GLS",
        "Mercedes-Benz G-Class",
        "Audi Q7",
        "Audi Q8",
        "Lexus GX",
        "Lexus LX",
        "Lincoln Navigator",
        "Jeep Wrangler",
        "Jeep Grand Cherokee",
    ]

    if not search_input:
        raise ValueError("Search input cannot be empty")

    # Use fuzzy matching to find matches
    matches = fuzzy_match_car_model(search_input, car_models)

    # Remove duplicates while preserving order
    unique_matches = []
    for match in matches:
        if match not in unique_matches:
            unique_matches.append(match)

    return {"matches": unique_matches}


from typing import Dict, List, Union


def search_independent_garages(
    make: str, model: str, location: str, search_radius: float = 2
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Returns a list of independent garages that can work on your car in a given location.

    Args:
        make: Make of the original car.
        model: Model of the original car.
        location: Postcode, city or coordinates, around which the search ought to happen.
        search_radius: Search radius in miles.

    Returns:
        Dict containing:
            - location: The location where the search was conducted.
            - garages: List of garages with details such as name, address, and distance.
    """

    # Sample data based on hash of the location for consistency
    sample_garages = {
        "New York": [
            {"name": "Joe's Garage", "address": "123 Elm St", "distance": 1.5},
            {"name": "Auto Fix", "address": "456 Maple Ave", "distance": 2.0},
        ],
        "San Francisco": [
            {"name": "Bay Area Auto", "address": "789 Pine St", "distance": 1.0},
            {"name": "Golden Gate Garage", "address": "101 Market St", "distance": 1.8},
        ],
        "London": [
            {"name": "London Auto Repair", "address": "11 Downing St", "distance": 1.2},
            {"name": "West End Motors", "address": "221B Baker St", "distance": 1.9},
        ],
    }

    if location not in sample_garages:
        raise ValueError(f"Location not supported: {location}")

    return {
        "location": location,
        "garages": sample_garages[location],
    }


from typing import Dict, List


def search_train(
    from_station: str, to_station: str, date: str
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Search train schedules between two stations on a specific date.

    Args:
        from_station: Station to leave from
        to_station: Station to arrive at
        date: Date of journey in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - from: Departure station
            - to: Arrival station
            - date: Date of journey
            - schedules: List of train schedules with departure and arrival times
    """

    # Sample train schedules based on hash of the input parameters for consistency
    sample_schedules = {
        ("Nuremburg", "Berlin", "2024-08-22"): [
            {"departure": "06:30 AM", "arrival": "10:00 AM"},
            {"departure": "12:00 PM", "arrival": "03:30 PM"},
            {"departure": "06:00 PM", "arrival": "09:30 PM"},
        ],
        ("Berlin", "Munich", "2024-08-25"): [
            {"departure": "07:00 AM", "arrival": "11:30 AM"},
            {"departure": "01:00 PM", "arrival": "05:30 PM"},
            {"departure": "05:00 PM", "arrival": "09:30 PM"},
        ],
        ("Munich", "Nuremburg", "2025-08-27"): [
            {"departure": "08:00 AM", "arrival": "10:30 AM"},
            {"departure": "12:30 PM", "arrival": "03:00 PM"},
            {"departure": "05:00 PM", "arrival": "07:30 PM"},
        ],
        ("New York", "Boston", "2023-10-01"): [
            {"departure": "08:00 AM", "arrival": "11:00 AM"},
            {"departure": "01:00 PM", "arrival": "04:00 PM"},
        ],
        ("San Francisco", "Los Angeles", "2023-10-01"): [
            {"departure": "09:00 AM", "arrival": "01:00 PM"},
            {"departure": "03:00 PM", "arrival": "07:00 PM"},
        ],
    }

    key = (from_station, to_station, date)
    if key not in sample_schedules:
        raise ValueError(
            f"No train schedules available for the route from {from_station} to {to_station} on {date}"
        )

    return {
        "from": from_station,
        "to": to_station,
        "date": date,
        "schedules": sample_schedules[key],
    }


from typing import Dict, Union


def start_charging_session(
    station_id: str,
    kWh_limit: float,
    payment_method_id: str,
    stall_number: Union[str, None] = None,
) -> Dict[str, Union[str, float, bool]]:
    """Remotely start a charging session at a specific station stall.

    Args:
        station_id: Provider's station identifier.
        kWh_limit: Energy cap for the session in kWh.
        payment_method_id: Saved payment method token to bill.
        stall_number: Physical stall number or label within the station (optional).

    Returns:
        Dict containing:
            - station_id: The station identifier where the session was started.
            - stall_number: The stall number where the session was initiated.
            - kWh_limit: The energy cap set for the session.
            - session_active: Boolean indicating if the session was successfully started.
    """
    if not station_id or not kWh_limit or not payment_method_id:
        raise ValueError("station_id, kWh_limit, and payment_method_id are required.")

    # Simulated logic to start a charging session
    supported_stations = {"ST123", "ST456", "ST789"}
    if station_id not in supported_stations:
        raise ValueError(f"Station ID not supported: {station_id}")

    if kWh_limit <= 0:
        raise ValueError("kWh_limit must be a positive number.")

    # Simulate a successful session start
    session_active = True

    return {
        "station_id": station_id,
        "stall_number": stall_number or "default",
        "kWh_limit": kWh_limit,
        "session_active": session_active,
    }
