import hashlib

# Travel Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Literal, Optional, Union


def book_flight(
    departure_airport: str,
    arrival_airport: str,
    departure_date: str,
    passenger_name: str,
    seat_preference: Optional[Literal["aisle", "window", "middle"]] = None,
) -> Dict[str, Union[str, int]]:
    """Hold and ticket a specific one-way flight.

    Args:
        departure_airport: IATA code for the departure airport (e.g., 'JFK').
        arrival_airport: IATA code for the arrival airport (e.g., 'LAX').
        departure_date: Date of departure in 'YYYY-MM-DD' format.
        passenger_name: Full name of the passenger for the booking.
        seat_preference: Optional seat preference ('aisle', 'window', 'middle').

    Returns:
        Dict containing:
            - booking_reference: Unique booking reference code.
            - departure_airport: IATA code of the departure airport.
            - arrival_airport: IATA code of the arrival airport.
            - departure_date: Date of departure.
            - passenger_name: Name of the passenger.
            - seat_number: Assigned seat number.
    """
    if len(departure_airport) != 3 or len(arrival_airport) != 3:
        raise ValueError("Invalid IATA code format. Must be 3 characters.")

    # Generate a unique booking reference using a hash
    booking_reference = hashlib.md5(
        f"{departure_airport}{arrival_airport}{departure_date}{passenger_name}".encode()
    ).hexdigest()[:8]

    # Simulate seat assignment based on preference
    seat_map = {
        "aisle": "12C",
        "window": "12A",
        "middle": "12B",
    }
    seat_number = seat_map.get(
        seat_preference, "12C"
    )  # Default to aisle if not specified

    return {
        "booking_reference": booking_reference,
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
        "departure_date": departure_date,
        "passenger_name": passenger_name,
        "seat_number": seat_number,
    }


import hashlib
from typing import Dict, Literal, Union


def distance(
    latitude_start: str,
    longitude_start: str,
    latitude_destination: str,
    longitude_destination: str,
    method: Literal["walking", "driving"] = "walking",
) -> Dict[str, Union[float, str]]:
    """Get the distance between two latitude/longitude coordinates by walking or driving.

    Args:
        latitude_start: Latitude of the starting point
        longitude_start: Longitude of the starting point
        latitude_destination: Latitude of the destination
        longitude_destination: Longitude of the destination
        method: Method of transportation between 'walking' or 'driving'

    Returns:
        Dict containing:
            - method: Method of transportation used
            - distance: Distance in miles
            - duration: Estimated duration in minutes
    """
    if method not in ["walking", "driving"]:
        raise ValueError("Method must be either 'walking' or 'driving'")

    # Create a unique hash based on the input coordinates and method
    hash_input = (
        latitude_start
        + longitude_start
        + latitude_destination
        + longitude_destination
        + method
    ).encode()
    hash_value = hashlib.md5(hash_input).hexdigest()

    # Generate mock distance and duration based on the hash value
    distance_miles = (
        int(hash_value[:4], 16) % 100
    ) + 1  # Distance between 1 and 100 miles
    duration_minutes = distance_miles * (2 if method == "walking" else 1)

    return {
        "method": method,
        "distance": distance_miles,
        "duration": duration_minutes,
    }


def estimate_trip_cost(
    distance_miles: float, fuel_price_per_gallon: float, fuel_efficiency_mpg: float
) -> Dict[str, Union[float, str]]:
    """Estimate the cost of a road trip based on distance, fuel price, and fuel efficiency.

    Args:
        distance_miles: Total trip distance in miles
        fuel_price_per_gallon: Average fuel price per gallon
        fuel_efficiency_mpg: Fuel efficiency of the vehicle in miles per gallon

    Returns:
        Dict containing:
            - total_cost: Estimated total cost of the trip
            - currency: Currency of the estimated cost
    """
    if distance_miles <= 0:
        raise ValueError("Distance must be greater than zero.")
    if fuel_price_per_gallon <= 0:
        raise ValueError("Fuel price per gallon must be greater than zero.")
    if fuel_efficiency_mpg <= 0:
        raise ValueError("Fuel efficiency must be greater than zero.")

    gallons_needed = distance_miles / fuel_efficiency_mpg
    total_cost = gallons_needed * fuel_price_per_gallon

    return {"total_cost": round(total_cost, 2), "currency": "USD"}


from typing import Dict, Literal


def find_accommodation(
    location: str, type: Literal["hotel", "motel", "campsite"] = "hotel"
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Suggests accommodations near a location.

    Args:
        location: Location where accommodation is needed (e.g. 'New York', 'Yosemite')
        type: Type of accommodation: hotel, motel, campsite, etc

    Returns:
        Dict containing:
            - location: Location where accommodation is suggested
            - accommodations: List of accommodations with details
                - name: Name of the accommodation
                - rating: Average rating of the accommodation
                - price_per_night: Price per night in USD
    """
    sample_data = {
        "New York": [
            {"name": "Grand Hotel", "rating": 4.5, "price_per_night": 250.0},
            {"name": "Budget Inn", "rating": 3.8, "price_per_night": 120.0},
        ],
        "Yosemite": [
            {"name": "Campground A", "rating": 4.7, "price_per_night": 35.0},
            {"name": "Mountain Lodge", "rating": 4.2, "price_per_night": 150.0},
        ],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    accommodations = sample_data[location]
    if type != "hotel":
        accommodations = [acc for acc in accommodations if type in acc["name"].lower()]

    return {
        "location": location,
        "accommodations": accommodations,
    }


from typing import Dict, List, Union


def get_route(
    start_location: str, destination: str, waypoints: List[str] = None
) -> Dict[str, Union[str, List[str], float]]:
    """Generates the optimal trip route based on start location, destination, and stops.

    Args:
        start_location: The starting point of the road trip
        destination: The final destination of the road trip
        waypoints: List of intermediate stops along the way

    Returns:
        Dict containing:
            - start_location: Starting point of the trip
            - destination: Final destination of the trip
            - waypoints: Ordered list of stops including start and destination
            - total_distance: Total distance of the trip in miles
    """
    if not start_location or not destination:
        raise ValueError("Both start_location and destination are required.")

    # Simulate a hash-based generation for consistent but varied sample data
    sample_distances = {
        ("New York", "Los Angeles"): 2790.0,
        ("San Francisco", "Las Vegas"): 570.0,
        ("Miami", "Orlando"): 230.0,
    }

    # Default waypoints to an empty list if not provided
    if waypoints is None:
        waypoints = []

    # Create a full route including start, waypoints, and destination
    full_route = [start_location] + waypoints + [destination]

    # Calculate a mock total distance based on the number of stops
    base_distance = sample_distances.get((start_location, destination), 100.0)
    total_distance = base_distance + len(waypoints) * 50.0

    return {
        "start_location": start_location,
        "destination": destination,
        "waypoints": full_route,
        "total_distance": total_distance,
    }


from datetime import datetime, timedelta
from typing import Dict, Union


def get_travel_time(
    origin_coordinates: str,
    destination_coordinates: str,
    departure_timestamp: Union[str, None] = None,
    arrival_timestamp: Union[str, None] = None,
) -> Dict[str, Union[str, float]]:
    """Determines the total travel time between two locations.

    Args:
        origin_coordinates: Co-ordinates of the starting location
        destination_coordinates: Co-ordinates of the ending location
        departure_timestamp: A timestamp representing the desired departure time
        arrival_timestamp: A timestamp representing the desired arrival time

    Returns:
        Dict containing:
            - origin: Origin coordinates
            - destination: Destination coordinates
            - travel_time: Estimated travel time in hours
            - departure_time: Actual departure time used
            - arrival_time: Estimated arrival time
    """
    if not origin_coordinates or not destination_coordinates:
        raise ValueError("Both origin and destination coordinates must be provided.")

    # Simulate travel time calculation based on hash of coordinates
    travel_time_hours = (
        abs(hash(origin_coordinates) - hash(destination_coordinates)) % 10 + 1
    )

    if departure_timestamp:
        departure_time = datetime.fromisoformat(departure_timestamp)
    else:
        departure_time = datetime.now()

    if arrival_timestamp:
        arrival_time = datetime.fromisoformat(arrival_timestamp)
        travel_time_hours = (arrival_time - departure_time).total_seconds() / 3600
    else:
        arrival_time = departure_time + timedelta(hours=travel_time_hours)

    return {
        "origin": origin_coordinates,
        "destination": destination_coordinates,
        "travel_time": travel_time_hours,
        "departure_time": departure_time.isoformat(),
        "arrival_time": arrival_time.isoformat(),
    }


import hashlib
from typing import Dict, Optional, Union


def authenticate_frequent_flyer(
    username: Optional[str] = None,
    password: Optional[str] = None,
    o_auth_token: Optional[str] = None,
    expiration_time: Optional[float] = None,
) -> Dict[str, Union[str, float]]:
    """Authenticate a frequent flyer account and return an authentication token.

    Args:
        username: Username for the frequent flyer account.
        password: Password for the frequent flyer account.
        o_auth_token: OAuth token which can be used to authenticate in place of username and password.
        expiration_time: A custom expiration time for the authentication token. Defaults to the account's setting.

    Returns:
        Dict containing:
            - token: Authentication token
            - expiration: Expiration time of the token in hours

    Raises:
        ValueError: If neither username/password nor o_auth_token is provided.
    """
    if not (username and password) and not o_auth_token:
        raise ValueError("Either username/password or o_auth_token must be provided.")

    # Simulate token generation using a hash for consistency
    if o_auth_token:
        base_string = o_auth_token
    else:
        base_string = f"{username}:{password}"

    token = hashlib.sha256(base_string.encode()).hexdigest()

    # Default expiration time logic
    default_expiration = 24.0  # Default to 24 hours
    expiration = expiration_time if expiration_time is not None else default_expiration

    return {
        "token": token,
        "expiration": expiration,
    }


import hashlib
from typing import Dict, Union


def book_city_tour(
    city: str, tour_name: str, date: str, participants: int
) -> Dict[str, Union[str, int, float]]:
    """Book a guided city tour.

    Args:
        city: City where the tour takes place
        tour_name: Name of the city tour
        date: Date of the tour in YYYY-MM-DD format
        participants: Number of people joining the tour

    Returns:
        Dict containing:
            - booking_id: Unique identifier for the booking
            - city: City where the tour is booked
            - tour_name: Name of the booked tour
            - date: Date of the tour
            - participants: Number of participants
            - total_cost: Total cost of the booking
    """
    if participants <= 0:
        raise ValueError("Number of participants must be greater than zero")

    # Generate a unique booking ID using a hash
    booking_id = hashlib.md5(
        f"{city}{tour_name}{date}{participants}".encode()
    ).hexdigest()[:8]

    # Mock cost calculation: $50 per participant
    total_cost = participants * 50.0

    return {
        "booking_id": booking_id,
        "city": city,
        "tour_name": tour_name,
        "date": date,
        "participants": participants,
        "total_cost": total_cost,
    }


from datetime import datetime
from typing import Dict, Union


def book_hotel(
    hotel_name: str, city: str, check_in: str, check_out: str, guests: int
) -> Dict[str, Union[str, int, float]]:
    """Book a hotel room.

    Args:
        hotel_name: Name of the hotel
        city: City where the hotel is located
        check_in: Check-in date in YYYY-MM-DD format
        check_out: Check-out date in YYYY-MM-DD format
        guests: Number of guests staying at the hotel

    Returns:
        Dict containing:
            - booking_id: Unique identifier for the booking
            - hotel_name: Name of the hotel
            - city: City where the hotel is located
            - check_in: Check-in date
            - check_out: Check-out date
            - guests: Number of guests
            - total_price: Total price for the stay
    """
    try:
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        if check_in_date >= check_out_date:
            raise ValueError("Check-out date must be after check-in date.")
    except ValueError as e:
        raise ValueError(f"Invalid date format or logic: {e}")

    if guests <= 0:
        raise ValueError("Number of guests must be at least 1.")

    # Simulate a booking ID using a hash
    booking_id = hash((hotel_name, city, check_in, check_out, guests)) & 0xFFFFFFFF

    # Simulate a total price based on a simple calculation
    nights = (check_out_date - check_in_date).days
    price_per_night = 100.0  # Mock price per night
    total_price = nights * price_per_night * guests

    return {
        "booking_id": booking_id,
        "hotel_name": hotel_name,
        "city": city,
        "check_in": check_in,
        "check_out": check_out,
        "guests": guests,
        "total_price": total_price,
    }


from typing import Dict, Union


def book_tour(
    location: str, tour_name: str, date: str, participants: int
) -> Dict[str, Union[str, int, float]]:
    """Book a local tour or activity.

    Args:
        location: Location of the tour
        tour_name: Name of the tour
        date: Date of the tour in YYYY-MM-DD format
        participants: Number of participants

    Returns:
        Dict containing:
            - confirmation_number: Unique confirmation number for the booking
            - location: Location of the tour
            - tour_name: Name of the tour
            - date: Date of the tour
            - participants: Number of participants
            - total_cost: Total cost of the booking
    """
    if participants <= 0:
        raise ValueError("Number of participants must be greater than zero.")

    # Simulated pricing logic
    base_price_per_person = 50.0
    location_multiplier = hash(location) % 5 + 1
    tour_multiplier = hash(tour_name) % 3 + 1
    total_cost = (
        base_price_per_person * participants * location_multiplier * tour_multiplier
    )

    confirmation_number = hash((location, tour_name, date, participants)) % 1000000

    return {
        "confirmation_number": confirmation_number,
        "location": location,
        "tour_name": tour_name,
        "date": date,
        "participants": participants,
        "total_cost": round(total_cost, 2),
    }


from typing import Dict, List


def breaks(
    route_distance: float,
    average_speed: float = 60,
    break_per_minutes_traveled: float = 180,
) -> Dict[str, List[float]]:
    """Generate places to take breaks from driving.

    Args:
        route_distance: Total trip distance in miles
        average_speed: Average expected speed in mph
        break_per_minutes_traveled: Suggest break every x number of miles

    Returns:
        Dict containing:
            - break_points: List of mile markers where breaks are suggested
    """
    if route_distance <= 0:
        raise ValueError("Route distance must be greater than zero.")
    if average_speed <= 0:
        raise ValueError("Average speed must be greater than zero.")
    if break_per_minutes_traveled <= 0:
        raise ValueError("Break per minutes traveled must be greater than zero.")

    break_points = []
    current_distance = break_per_minutes_traveled

    while current_distance < route_distance:
        break_points.append(current_distance)
        current_distance += break_per_minutes_traveled

    return {"break_points": break_points}


from typing import Dict


def cancel_flight(departure_airport: str, arrival_airport: str) -> Dict[str, str]:
    """Cancel a booked flight from departure airport to arrival airport.

    Args:
        departure_airport: Name of the departure airport
        arrival_airport: Name of the arrival airport

    Returns:
        Dict containing:
            - status: Status of the cancellation
            - message: Detailed message about the cancellation process
    """
    # Mock database of booked flights
    booked_flights = {
        ("JFK", "LAX"): True,
        ("LHR", "CDG"): True,
        ("SFO", "ORD"): True,
    }

    if (departure_airport, arrival_airport) not in booked_flights:
        return {
            "status": "failed",
            "message": f"No booked flight found from {departure_airport} to {arrival_airport}.",
        }

    # Simulate cancellation process
    cancellation_success = hash(departure_airport + arrival_airport) % 2 == 0

    if cancellation_success:
        return {
            "status": "success",
            "message": f"Flight from {departure_airport} to {arrival_airport} has been successfully cancelled.",
        }
    else:
        return {
            "status": "failed",
            "message": f"Failed to cancel the flight from {departure_airport} to {arrival_airport}. Please try again later.",
        }


from typing import Dict


def cancel_reservation(reservation_id: str) -> Dict[str, str]:
    """Cancel a previously created reservation.

    Args:
        reservation_id: ID returned by reserve_instrument.

    Returns:
        Dict containing:
            - reservation_id: The ID of the canceled reservation
            - status: The status of the cancellation
    """
    # Simulate a database of reservations
    reservations_db = {
        "res123": "active",
        "res456": "active",
        "res789": "canceled",
    }

    if reservation_id not in reservations_db:
        raise ValueError(f"Reservation ID not found: {reservation_id}")

    if reservations_db[reservation_id] == "canceled":
        return {
            "reservation_id": reservation_id,
            "status": "already canceled",
        }

    # Cancel the reservation
    reservations_db[reservation_id] = "canceled"

    return {
        "reservation_id": reservation_id,
        "status": "canceled",
    }


from typing import Dict


def change_class(seating_class: str) -> Dict[str, str]:
    """Change the seating class for a booking.

    Args:
        seating_class: The name of the seating class to change to (e.g. 'Economy', 'Business', 'First')

    Returns:
        Dict containing:
            - booking_id: Unique identifier for the booking
            - new_class: The new seating class for the booking
            - confirmation: Confirmation message of the class change
    """
    valid_classes = {"Economy", "Business", "First"}
    if seating_class not in valid_classes:
        raise ValueError(f"Invalid seating class: {seating_class}")

    # Simulate a booking ID using a hash of the seating class for consistency
    booking_id = f"BK-{hash(seating_class) % 10000:04d}"

    return {
        "booking_id": booking_id,
        "new_class": seating_class,
        "confirmation": f"Seating class changed to {seating_class} successfully.",
    }


from typing import Dict, Union


def check_flight_status(flight_code: str) -> Dict[str, Union[str, bool]]:
    """Check the status of a flight given its flight code.

    Args:
        flight_code: The code of the flight whose status is being checked (e.g. 'AA123', 'BA456')

    Returns:
        Dict containing:
            - flight_code: The flight code
            - status: The current status of the flight (e.g. 'on time', 'delayed', 'cancelled')
            - gate_open: Boolean indicating if the gate is open for boarding
    """

    sample_statuses = {
        "AA123": {"status": "on time", "gate_open": True},
        "BA456": {"status": "delayed", "gate_open": False},
        "DL789": {"status": "cancelled", "gate_open": False},
    }

    if flight_code not in sample_statuses:
        raise ValueError(f"Flight code not recognized: {flight_code}")

    flight_info = sample_statuses[flight_code]
    return {
        "flight_code": flight_code,
        "status": flight_info["status"],
        "gate_open": flight_info["gate_open"],
    }


import hashlib
from typing import Dict, List, Literal, Union


def create_traveling_frame(
    team_name: str,
    age_group: Literal["U8", "U10", "U12", "U14", "U16", "U18", "Adult"],
    gender: Literal["Male", "Female"],
    players: List[Dict[str, Union[str, int, List[str]]]],
    match_date: str = None,
    notes: str = "",
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, List[str]]]]]]:
    """Create a traveling frame for a specific match or tournament.

    Args:
        team_name: Name or identifier for this traveling frame
        age_group: Age group for this traveling frame
        gender: Gender for this traveling frame
        players: List of players in the traveling frame with their assigned roles
        match_date: Date of the match or tournament in YYYY-MM-DD format
        notes: Additional notes about this traveling frame

    Returns:
        Dict containing:
            - team_name: Name of the team
            - age_group: Age group of the team
            - gender: Gender category of the team
            - match_date: Date of the match or tournament
            - notes: Additional notes
            - players: List of players with their roles and positions
    """
    if not players:
        raise ValueError("Players list cannot be empty")

    # Generate a consistent but varied sample data for players
    for player in players:
        player_info = player.get("player", {})
        name = player_info.get("name", "")
        dob = player_info.get("date_of_birth", "")
        if not name or not dob:
            raise ValueError("Each player must have a name and date of birth")

        # Generate a hash-based jersey number if not provided
        if "jersey_number" not in player or player["jersey_number"] is None:
            hash_input = f"{name}{dob}".encode()
            player["jersey_number"] = (
                int(hashlib.md5(hash_input).hexdigest(), 16) % 99 + 1
            )

        # Ensure secondary_positions is a list
        if "secondary_positions" not in player:
            player["secondary_positions"] = []

    return {
        "team_name": team_name,
        "age_group": age_group,
        "gender": gender,
        "match_date": match_date or "TBD",
        "notes": notes,
        "players": players,
    }


from datetime import datetime
from typing import Dict, List, Union


def filter_flight_info(
    departure_airport: str,
    arrival_airport: str,
    departure_time_before: Union[str, None] = None,
    arrival_time_before: Union[str, None] = None,
    departure_time_after: Union[str, None] = None,
    arrival_time_after: Union[str, None] = None,
    airline: Union[str, None] = None,
    aircraft_type: Union[str, None] = None,
) -> List[Dict[str, Union[str, datetime]]]:
    """Retrieve available flights for specified departure, arrival city (airport), and time.

    Args:
        departure_airport: The IATA code for the major airport of the departure city.
        arrival_airport: The IATA code for the major airport of the arrival city.
        departure_time_before: The scheduled departure time before a specified value.
        arrival_time_before: The scheduled arrival time before a specified value.
        departure_time_after: The scheduled departure time after a specified value.
        arrival_time_after: The scheduled arrival time after a specified value.
        airline: The name or code of the airline operating the flight.
        aircraft_type: The model of the aircraft.

    Returns:
        List of dictionaries containing:
            - flight_number: The flight number
            - departure_airport: The IATA code of the departure airport
            - arrival_airport: The IATA code of the arrival airport
            - departure_time: The scheduled departure time
            - arrival_time: The scheduled arrival time
            - airline: The airline operating the flight
            - aircraft_type: The model of the aircraft
    """
    sample_flights = [
        {
            "flight_number": "UA123",
            "departure_airport": "JFK",
            "arrival_airport": "LAX",
            "departure_time": datetime(2023, 10, 10, 8, 0),
            "arrival_time": datetime(2023, 10, 10, 11, 0),
            "airline": "United Airlines",
            "aircraft_type": "Boeing 737",
        },
        {
            "flight_number": "AA456",
            "departure_airport": "JFK",
            "arrival_airport": "LAX",
            "departure_time": datetime(2023, 10, 10, 9, 0),
            "arrival_time": datetime(2023, 10, 10, 12, 0),
            "airline": "American Airlines",
            "aircraft_type": "Airbus A320",
        },
        {
            "flight_number": "DL789",
            "departure_airport": "JFK",
            "arrival_airport": "SFO",
            "departure_time": datetime(2023, 10, 10, 10, 0),
            "arrival_time": datetime(2023, 10, 10, 13, 0),
            "airline": "Delta Airlines",
            "aircraft_type": "Boeing 757",
        },
    ]

    def time_filter(
        flight_time: datetime, before: Union[str, None], after: Union[str, None]
    ) -> bool:
        if before and flight_time >= datetime.fromisoformat(before):
            return False
        if after and flight_time <= datetime.fromisoformat(after):
            return False
        return True

    filtered_flights = [
        flight
        for flight in sample_flights
        if flight["departure_airport"] == departure_airport
        and flight["arrival_airport"] == arrival_airport
        and time_filter(
            flight["departure_time"], departure_time_before, departure_time_after
        )
        and time_filter(flight["arrival_time"], arrival_time_before, arrival_time_after)
        and (airline is None or flight["airline"] == airline)
        and (aircraft_type is None or flight["aircraft_type"] == aircraft_type)
    ]

    return filtered_flights


from typing import Dict, List, Union


def find_airports(
    city: str, state: Union[str, None] = None, country: str = None
) -> Dict[str, Union[str, List[str]]]:
    """Find all airports located in a specified city.

    Args:
        city: The name of the city to search for airports.
        state: The state where the city is located (for disambiguation).
        country: The name of the country where the city is located (for disambiguation).

    Returns:
        Dict containing:
            - city: City name
            - airports: List of airport names in the specified city
    """
    if not city or not country:
        raise ValueError("Both 'city' and 'country' parameters are required.")

    # Sample data for demonstration purposes
    sample_data = {
        ("New York", "USA"): [
            "John F. Kennedy International Airport",
            "LaGuardia Airport",
            "Newark Liberty International Airport",
        ],
        ("Los Angeles", "USA"): [
            "Los Angeles International Airport",
            "Hollywood Burbank Airport",
        ],
        ("London", "UK"): [
            "Heathrow Airport",
            "Gatwick Airport",
            "London City Airport",
        ],
    }

    key = (city, country)
    if key not in sample_data:
        raise ValueError(f"No airports found for city: {city}, country: {country}")

    return {
        "city": city,
        "airports": sample_data[key],
    }


from typing import Dict, List, Union


def find_flights(
    departure_city: str,
    arrival_city: str,
    departure_date: str,
    return_date: Union[str, None] = None,
    is_round_trip: bool = False,
    is_nonstop: bool = False,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find available flights given a departure city, arrival city, and trip type.

    Args:
        departure_city: City where the first flight will depart from in 'City, State' format.
        arrival_city: City where the first flight will arrive at in 'City, State' format.
        departure_date: Date of the first departure flight.
        return_date: Date of the return flight if round trip.
        is_round_trip: If the search is looking for round trips.
        is_nonstop: If the query should only show nonstop flights.

    Returns:
        Dict containing:
            - departure_city: Departure city
            - arrival_city: Arrival city
            - flights: List of available flights with details
    """
    if not departure_city or not arrival_city or not departure_date:
        raise ValueError("Missing required flight search parameters.")

    sample_flights = [
        {
            "flight_number": "AA123",
            "airline": "American Airlines",
            "departure_time": "08:00 AM",
            "arrival_time": "11:00 AM",
            "price": 250.00,
            "nonstop": True,
        },
        {
            "flight_number": "DL456",
            "airline": "Delta Airlines",
            "departure_time": "09:30 AM",
            "arrival_time": "12:30 PM",
            "price": 200.00,
            "nonstop": False,
        },
        {
            "flight_number": "UA789",
            "airline": "United Airlines",
            "departure_time": "07:00 AM",
            "arrival_time": "10:00 AM",
            "price": 300.00,
            "nonstop": True,
        },
    ]

    # Filter flights based on nonstop preference
    if is_nonstop:
        sample_flights = [flight for flight in sample_flights if flight["nonstop"]]

    # Mock return flights if round trip is requested
    if is_round_trip and return_date:
        return_flights = [
            {
                "flight_number": "AA321",
                "airline": "American Airlines",
                "departure_time": "04:00 PM",
                "arrival_time": "07:00 PM",
                "price": 250.00,
                "nonstop": True,
            },
            {
                "flight_number": "DL654",
                "airline": "Delta Airlines",
                "departure_time": "05:30 PM",
                "arrival_time": "08:30 PM",
                "price": 200.00,
                "nonstop": False,
            },
        ]
        if is_nonstop:
            return_flights = [flight for flight in return_flights if flight["nonstop"]]
        sample_flights.extend(return_flights)

    return {
        "departure_city": departure_city,
        "arrival_city": arrival_city,
        "flights": sample_flights,
    }


from typing import Dict, List


def find_flights_by_route(
    origin_airport_code: str, destination_airport_code: str, date: str
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find available flights between two airports on a given date.

    Args:
        origin_airport_code: The IATA code for the origin airport, e.g., 'JFK'.
        destination_airport_code: The IATA code for the destination airport, e.g., 'LAX'.
        date: The date to search for flights in YYYY-MM-DD format.

    Returns:
        Dict containing:
            - origin: Origin airport code
            - destination: Destination airport code
            - date: Date of the flights
            - flights: List of available flights with details
    """

    # Sample data generation based on hash of input parameters
    sample_flights = [
        {
            "flight_number": f"FL{hash((origin_airport_code, destination_airport_code, date, i)) % 1000:03}",
            "departure_time": f"{10 + i}:00",
            "arrival_time": f"{13 + i}:00",
            "price": round(
                200
                + (
                    hash((origin_airport_code, destination_airport_code, date, i)) % 100
                ),
                2,
            ),
        }
        for i in range(3)
    ]

    if not origin_airport_code or not destination_airport_code or not date:
        raise ValueError("All parameters must be provided and valid.")

    return {
        "origin": origin_airport_code,
        "destination": destination_airport_code,
        "date": date,
        "flights": sample_flights,
    }


from typing import Dict, List


def find_hotel(
    location: str, is_open: bool = False
) -> Dict[str, List[Dict[str, Union[str, bool]]]]:
    """Find hotels near a given location.

    Args:
        location: City or address to search around.
        is_open: Get only hotels that are currently open.

    Returns:
        Dict containing:
            - hotels: List of hotels with details such as name, address, and open status.
    """
    sample_hotels = {
        "New York": [
            {"name": "Hotel Central", "address": "123 Main St", "is_open": True},
            {"name": "Luxury Stay", "address": "456 Broadway", "is_open": False},
        ],
        "San Francisco": [
            {"name": "Bay View Inn", "address": "789 Ocean Ave", "is_open": True},
            {"name": "Golden Gate Hotel", "address": "101 Bridge Rd", "is_open": True},
        ],
        "London": [
            {"name": "Royal Palace Hotel", "address": "11 Queen St", "is_open": False},
            {"name": "City Center Lodge", "address": "22 King St", "is_open": True},
        ],
    }

    if location not in sample_hotels:
        raise ValueError(f"Location not supported: {location}")

    hotels = sample_hotels[location]
    if is_open:
        hotels = [hotel for hotel in hotels if hotel["is_open"]]

    return {"hotels": hotels}


import hashlib
from typing import Dict, List, Union


def find_hotels(
    city: str, check_in: str, check_out: str, guests: int
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find available hotels in a given city for specific dates.

    Args:
        city: City to search for hotels in
        check_in: Check-in date in YYYY-MM-DD format
        check_out: Check-out date in YYYY-MM-DD format
        guests: Number of guests

    Returns:
        Dict containing:
            - city: City name
            - hotels: List of available hotels with details
                - name: Hotel name
                - price_per_night: Price per night in USD
                - rating: Hotel rating out of 5
    """
    if guests <= 0:
        raise ValueError("Number of guests must be at least 1")

    # Generate a consistent but varied list of hotels based on city name
    hash_seed = hashlib.md5(city.encode()).hexdigest()
    hotel_names = [
        "Grand Plaza",
        "City Inn",
        "Comfort Stay",
        "Luxury Suites",
        "Budget Lodge",
    ]
    hotels = []
    for i in range(3):  # Simulate finding 3 hotels
        hotel_name = hotel_names[int(hash_seed[i], 16) % len(hotel_names)]
        price_per_night = 100 + (int(hash_seed[i + 1], 16) % 100)
        rating = 3 + (int(hash_seed[i + 2], 16) % 3) + 0.5
        hotels.append(
            {"name": hotel_name, "price_per_night": price_per_night, "rating": rating}
        )

    return {"city": city, "hotels": hotels}


from typing import Dict, List, Union


def find_rest_stops(
    route: str, radius_miles: float = 10
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find rest stops along a specified route within a given radius.

    Args:
        route: The route or location to find rest stops along (e.g. 'I-95', 'Route 66')
        radius_miles: The search radius in miles around the route or location

    Returns:
        Dict containing:
            - route: The specified route
            - radius_miles: The search radius used
            - rest_stops: List of rest stops with details including name, distance from route, and amenities
    """

    # Sample data based on hash of the route to ensure consistent but varied results
    sample_data = {
        "I-95": [
            {
                "name": "Rest Stop A",
                "distance_miles": 5.0,
                "amenities": ["restrooms", "food", "fuel"],
            },
            {
                "name": "Rest Stop B",
                "distance_miles": 8.5,
                "amenities": ["restrooms", "picnic area"],
            },
        ],
        "Route 66": [
            {
                "name": "Rest Stop C",
                "distance_miles": 3.2,
                "amenities": ["restrooms", "food"],
            },
            {
                "name": "Rest Stop D",
                "distance_miles": 9.0,
                "amenities": ["restrooms", "fuel"],
            },
        ],
    }

    if route not in sample_data:
        raise ValueError(f"Route not supported: {route}")

    rest_stops = [
        stop for stop in sample_data[route] if stop["distance_miles"] <= radius_miles
    ]

    return {
        "route": route,
        "radius_miles": radius_miles,
        "rest_stops": rest_stops,
    }


from typing import Dict, List, Literal, Union


def generate_budget(
    locations: List[str],
    length_days: int,
    comfort: Literal["Low", "Medium", "High"],
    activities: List[
        Literal["Skiing", "Beach", "Hiking", "Museums", "Restaurants"]
    ] = [],
) -> Dict[str, Union[float, Dict[str, float]]]:
    """Generate a daily budget for a trip based on locations, length, comfort, and activities.

    Args:
        locations: List of cities to visit (e.g., ['London', 'Edinburgh', 'Cardiff'])
        length_days: Length of trip in days
        comfort: Comfort level of trip, allowed values: Low (hostels), Medium (2-3 star hotels), High (4-5 star hotels)
        activities: List of categories of activities to be completed, allowed: Skiing, Beach, Hiking, Museums, Restaurants

    Returns:
        Dict containing:
            - total_budget: Total budget for the trip
            - daily_budget: Daily budget breakdown by category
    """
    if not locations or length_days <= 0:
        raise ValueError(
            "Locations must be provided and length_days must be greater than 0."
        )

    comfort_costs = {"Low": 50, "Medium": 100, "High": 200}

    activity_costs = {
        "Skiing": 150,
        "Beach": 50,
        "Hiking": 30,
        "Museums": 20,
        "Restaurants": 70,
        "road trip": 80,
    }

    location_costs = {
        "Nuremburg": 85,
        "Berlin": 95,
        "Munich": 110,
    }

    # Parse locations and activities from comma-separated strings
    locations_list = [loc.strip() for loc in locations.split(",")]
    activities_list = [act.strip() for act in activities.split(",")]

    base_cost_per_day = comfort_costs[comfort]
    activity_cost_per_day = sum(
        activity_costs.get(activity, 0) for activity in activities_list
    )

    # Handle multiple locations - calculate average location cost
    location_costs_sum = sum(
        location_costs.get(location, 0) for location in locations_list
    )
    location_cost_per_day = location_costs_sum / len(locations_list)

    daily_budget = base_cost_per_day + activity_cost_per_day + location_cost_per_day
    total_budget = daily_budget * length_days

    return {
        "total_budget": total_budget,
        "daily_budget": {
            "accommodation": base_cost_per_day,
            "activities": activity_cost_per_day,
            "total": daily_budget,
        },
    }


from typing import Dict, List, Union


def get_attractions(
    location: str, radius_miles: float = 15
) -> Dict[str, Union[str, float, List[str]]]:
    """Recommends popular tourist attractions or points of interest along a route or near a location.

    Args:
        location: Location or route to find attractions along.
        radius_miles: Search radius in miles around the location or route.

    Returns:
        Dict containing:
            - location: The location or route provided
            - radius_miles: The search radius used
            - attractions: List of popular attractions or points of interest
    """

    sample_data = {
        "New York": ["Statue of Liberty", "Central Park", "Metropolitan Museum of Art"],
        "San Francisco": ["Golden Gate Bridge", "Alcatraz Island", "Fisherman's Wharf"],
        "London": ["British Museum", "Tower of London", "Buckingham Palace"],
        "Carlisle": ["International House of Potato"],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    attractions = sample_data.get(location, [])
    return {
        "location": location,
        "radius_miles": radius_miles,
        "attractions": attractions,
    }


from datetime import datetime
from typing import Dict, List, Optional, Union


def get_campaign_travel(
    candidate_name: str, date_range: Optional[Dict[str, Optional[str]]] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, datetime]]]]]:
    """Retrieve public campaign travel information, including cities visited and dates.

    Args:
        candidate_name: Name of the candidate whose travel records are being requested.
        date_range: Optional date range to filter travel records, with 'start_date' and 'end_date' in YYYY-MM-DD format.

    Returns:
        Dict containing:
            - candidate_name: Name of the candidate
            - travel_records: List of dictionaries with 'city' and 'date' of visit
    """

    # Sample travel data for demonstration purposes
    sample_data = {
        "John Doe": [
            {"city": "New York", "date": datetime(2023, 9, 15)},
            {"city": "Los Angeles", "date": datetime(2023, 9, 20)},
            {"city": "Chicago", "date": datetime(2023, 9, 25)},
        ],
        "Jane Smith": [
            {"city": "Miami", "date": datetime(2023, 9, 10)},
            {"city": "Houston", "date": datetime(2023, 9, 18)},
            {"city": "Seattle", "date": datetime(2023, 9, 22)},
        ],
    }

    if candidate_name not in sample_data:
        raise ValueError(f"Candidate not found: {candidate_name}")

    travel_records = sample_data[candidate_name]

    if date_range:
        start_date = datetime.strptime(
            date_range.get("start_date", "1900-01-01"), "%Y-%m-%d"
        )
        end_date = datetime.strptime(
            date_range.get("end_date", "2100-01-01"), "%Y-%m-%d"
        )
        travel_records = [
            record
            for record in travel_records
            if start_date <= record["date"] <= end_date
        ]

    return {
        "candidate_name": candidate_name,
        "travel_records": travel_records,
    }


from typing import Dict, List, Union


def get_campgrounds(
    parkCode: str = "", stateCode: str = "", limit: int = 50
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Get campground-related data based on park and state codes.

    Args:
        parkCode: A comma delimited list of park codes (each 4-10 characters in length).
        stateCode: A comma delimited list of 2 character state codes.
        limit: Number of results to return per request.

    Returns:
        Dict containing:
            - parkCode: The park code(s) used in the query
            - stateCode: The state code(s) used in the query
            - campgrounds: List of campground data dictionaries, each containing:
                - name: Name of the campground
                - parkCode: Park code associated with the campground
                - stateCode: State code where the campground is located
                - availableSites: Number of available sites at the campground
    """
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")

    sample_campgrounds = [
        {
            "name": "Sunny Meadows",
            "parkCode": "YNP",
            "stateCode": "CA",
            "availableSites": 15,
        },
        {
            "name": "Lakeside Retreat",
            "parkCode": "GNP",
            "stateCode": "MT",
            "availableSites": 5,
        },
        {
            "name": "Mountain View",
            "parkCode": "ZNP",
            "stateCode": "UT",
            "availableSites": 10,
        },
        {
            "name": "Forest Haven",
            "parkCode": "YNP",
            "stateCode": "WY",
            "availableSites": 8,
        },
        {
            "name": "Desert Oasis",
            "parkCode": "DNP",
            "stateCode": "AZ",
            "availableSites": 12,
        },
    ]

    filtered_campgrounds = [
        campground
        for campground in sample_campgrounds
        if (not parkCode or campground["parkCode"] in parkCode.split(","))
        and (not stateCode or campground["stateCode"] in stateCode.split(","))
    ]

    return {
        "parkCode": parkCode,
        "stateCode": stateCode,
        "campgrounds": filtered_campgrounds[:limit],
    }


import hashlib
from typing import Dict, Optional, Union


def get_flight_info(
    departure_airport: str,
    arrival_airport: str,
    flight_number: Optional[str] = None,
    departure_time: Optional[str] = None,
    arrival_time: Optional[str] = None,
    airline: Optional[str] = None,
    aircraft_type: Optional[str] = None,
) -> Dict[str, Union[str, int, float]]:
    """Retrieve flights for specified departure city, arrival city, and time.

    Args:
        departure_airport: The IATA code for the major airport of the departure city.
        arrival_airport: The IATA code for the major airport of the arrival city.
        flight_number: Identifies a specific flight with an airline's two-letter IATA code and a numerical sequence.
        departure_time: The scheduled departure date and time.
        arrival_time: The scheduled arrival date and time.
        airline: The name or code of the airline operating the flight (e.g., 'United Airlines' or 'UA').
        aircraft_type: The model of the aircraft (e.g., 'Airbus A320').

    Returns:
        Dict containing:
            - departure_airport: IATA code of the departure airport
            - arrival_airport: IATA code of the arrival airport
            - flight_number: Flight number
            - departure_time: Scheduled departure time
            - arrival_time: Scheduled arrival time
            - airline: Airline operating the flight
            - aircraft_type: Model of the aircraft
            - duration: Estimated flight duration in hours
            - price: Estimated ticket price in USD
    """
    if not departure_airport or not arrival_airport:
        raise ValueError("Both departure_airport and arrival_airport are required.")

    # Generate consistent but varied sample data based on input hash
    seed = f"{departure_airport}-{arrival_airport}-{flight_number or ''}"
    hash_value = int(hashlib.md5(seed.encode()).hexdigest(), 16)

    sample_flights = [
        {
            "flight_number": "UA123",
            "departure_time": "2023-10-01T08:00:00",
            "arrival_time": "2023-10-01T12:00:00",
            "airline": "United Airlines",
            "aircraft_type": "Boeing 737",
            "duration": 4.0,
            "price": 350.0,
        },
        {
            "flight_number": "AA456",
            "departure_time": "2023-10-01T09:00:00",
            "arrival_time": "2023-10-01T13:30:00",
            "airline": "American Airlines",
            "aircraft_type": "Airbus A320",
            "duration": 4.5,
            "price": 400.0,
        },
    ]

    selected_flight = sample_flights[hash_value % len(sample_flights)]

    return {
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
        "flight_number": selected_flight["flight_number"],
        "departure_time": selected_flight["departure_time"],
        "arrival_time": selected_flight["arrival_time"],
        "airline": selected_flight["airline"],
        "aircraft_type": selected_flight["aircraft_type"],
        "duration": selected_flight["duration"],
        "price": selected_flight["price"],
    }


import hashlib
from typing import Dict, Union


def get_flight_status_by_flight_number(
    flight_number: str, date: str
) -> Dict[str, Union[str, Dict[str, str]]]:
    """Get the real-time status, including departure/arrival times and gate information, for a specific flight.

    Args:
        flight_number: The flight number to look up, e.g., 'UA245'.
        date: The date of the flight in YYYY-MM-DD format.

    Returns:
        Dict containing:
            - flight_number: The flight number
            - date: The date of the flight
            - status: The current status of the flight (e.g., 'On Time', 'Delayed')
            - departure: Dict containing:
                - time: Scheduled departure time
                - gate: Departure gate
            - arrival: Dict containing:
                - time: Scheduled arrival time
                - gate: Arrival gate
    """

    # Generate mock data based on flight number and date
    hash_input = f"{flight_number}-{date}".encode()
    hash_value = hashlib.md5(hash_input).hexdigest()

    # Simulate status based on hash value
    status_options = ["On Time", "Delayed", "Cancelled"]
    status = status_options[int(hash_value[0], 16) % len(status_options)]

    # Simulate departure and arrival times and gates
    departure_time = (
        f"{int(hash_value[1:3], 16) % 24:02}:{int(hash_value[3:5], 16) % 60:02}"
    )
    arrival_time = (
        f"{int(hash_value[5:7], 16) % 24:02}:{int(hash_value[7:9], 16) % 60:02}"
    )
    departure_gate = (
        f"{chr(65 + int(hash_value[9], 16) % 6)}{int(hash_value[10], 16) % 30 + 1}"
    )
    arrival_gate = (
        f"{chr(65 + int(hash_value[11], 16) % 6)}{int(hash_value[12], 16) % 30 + 1}"
    )

    return {
        "flight_number": flight_number,
        "date": date,
        "status": status,
        "departure": {
            "time": departure_time,
            "gate": departure_gate,
        },
        "arrival": {
            "time": arrival_time,
            "gate": arrival_gate,
        },
    }


from typing import Dict, List


def get_flight_times(
    departure_airport: str, arrival_airport: str, date: str
) -> Dict[str, List[Dict[str, str]]]:
    """Retrieves flight departure and arrival times between two airports for a given date.

    Args:
        departure_airport: The airport code where the flight departs from (IATA code).
        arrival_airport: The airport code where the flight arrives (IATA code).
        date: The date of travel in ISO 8601 format (YYYY-MM-DD).

    Returns:
        Dict containing:
            - flights: List of dictionaries with 'departure_time' and 'arrival_time' keys
    """
    # Sample data based on hash of the input parameters for consistent results
    sample_flights = {
        ("JFK", "LAX", "2023-10-01"): [
            {"departure_time": "08:00", "arrival_time": "11:00"},
            {"departure_time": "12:00", "arrival_time": "15:00"},
            {"departure_time": "16:00", "arrival_time": "19:00"},
        ],
        ("LHR", "CDG", "2023-10-01"): [
            {"departure_time": "09:00", "arrival_time": "11:15"},
            {"departure_time": "13:00", "arrival_time": "15:15"},
            {"departure_time": "17:00", "arrival_time": "19:15"},
        ],
        ("MAN", "BFS", "2023-10-17"): [
            {"departure_time": "07:30", "arrival_time": "08:45"},
            {"departure_time": "11:20", "arrival_time": "12:35"},
            {"departure_time": "15:45", "arrival_time": "17:00"},
            {"departure_time": "19:10", "arrival_time": "20:25"},
        ],
    }

    key = (departure_airport, arrival_airport, date)
    if key not in sample_flights:
        raise ValueError(f"No flights found for the given route and date: {key}")

    return {
        "flights": sample_flights[key],
    }


from typing import Dict, List


def get_flights(
    from_city: str, to_city: str
) -> Dict[str, List[Dict[str, Union[str, int]]]]:
    """Returns flight routes for a given day from one city to another.

    Args:
        from_city: The city to depart from
        to_city: The destination city

    Returns:
        Dict containing:
            - flights: List of flight details, each with:
                - flight_number: The flight number
                - departure_time: Scheduled departure time
                - arrival_time: Scheduled arrival time
                - duration: Duration of the flight in minutes
    """

    sample_routes = {
        ("New York", "London"): [
            {
                "flight_number": "NY100",
                "departure_time": "08:00",
                "arrival_time": "20:00",
                "duration": 480,
            },
            {
                "flight_number": "NY200",
                "departure_time": "16:00",
                "arrival_time": "04:00",
                "duration": 480,
            },
        ],
        ("Los Angeles", "Tokyo"): [
            {
                "flight_number": "LA300",
                "departure_time": "10:00",
                "arrival_time": "14:00",
                "duration": 720,
            },
            {
                "flight_number": "LA400",
                "departure_time": "22:00",
                "arrival_time": "02:00",
                "duration": 720,
            },
        ],
        ("Paris", "Rome"): [
            {
                "flight_number": "PR500",
                "departure_time": "09:00",
                "arrival_time": "11:00",
                "duration": 120,
            },
            {
                "flight_number": "PR600",
                "departure_time": "15:00",
                "arrival_time": "17:00",
                "duration": 120,
            },
        ],
    }

    if (from_city, to_city) not in sample_routes:
        raise ValueError(f"No flights available from {from_city} to {to_city}")

    return {"flights": sample_routes[(from_city, to_city)]}


from typing import Dict, Union


def get_frequent_flyer_miles(account_token: str) -> Dict[str, Union[str, int]]:
    """Gets the frequent flyer miles for an account.

    Args:
        account_token: Account token for the frequent flyer account

    Returns:
        Dict containing:
            - account_token: The account token provided
            - miles: The number of frequent flyer miles associated with the account
    """

    # Simulated hash-based generation for consistent sample data
    if not account_token:
        raise ValueError("Account token must be provided.")

    # Generate a pseudo-random number of miles based on the account token
    miles = sum(ord(char) for char in account_token) % 10000

    return {
        "account_token": account_token,
        "miles": miles,
    }


from typing import Dict, List, Union


def get_hiking_trails(
    city: str, max_length: Union[float, None] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Returns a list of hiking trails based on a given city.

    Args:
        city: The city from which the hiking trails should be accessible.
        max_length: The maximum length of the hiking trails returned in miles. If omitted, there will be no limit.

    Returns:
        Dict containing:
            - city: City name
            - trails: List of trails with each trail containing:
                - name: Name of the trail
                - length: Length of the trail in miles
                - difficulty: Difficulty level of the trail
    """

    sample_trails = {
        "Denver": [
            {"name": "Mount Falcon", "length": 2.7, "difficulty": "easy"},
            {"name": "Red Rocks Trail", "length": 6.0, "difficulty": "moderate"},
            {"name": "Chautauqua Trail", "length": 3.6, "difficulty": "moderate"},
        ],
        "Seattle": [
            {"name": "Rattlesnake Ledge", "length": 4.0, "difficulty": "moderate"},
            {"name": "Mount Si", "length": 8.0, "difficulty": "hard"},
            {"name": "Discovery Park Loop", "length": 2.8, "difficulty": "easy"},
        ],
        "San Francisco": [
            {"name": "Lands End Trail", "length": 3.4, "difficulty": "easy"},
            {"name": "Dipsea Trail", "length": 9.5, "difficulty": "hard"},
            {"name": "Muir Woods Trail", "length": 6.0, "difficulty": "moderate"},
        ],
    }

    if city not in sample_trails:
        raise ValueError(f"City not supported: {city}")

    trails = sample_trails[city]
    if max_length is not None:
        trails = [trail for trail in trails if trail["length"] <= max_length]

    return {
        "city": city,
        "trails": trails,
    }


from typing import Dict, List, Optional


def get_holiday_destinations(origin: Optional[str] = None) -> Dict[str, List[str]]:
    """Returns a list of holiday destinations.

    Args:
        origin: Origin location name (optional).

    Returns:
        Dict containing:
            - origin: Origin location name if provided, otherwise 'Worldwide'
            - destinations: List of recommended holiday destinations
    """

    destinations_by_origin = {
        "New York": ["Miami", "Los Angeles", "Las Vegas"],
        "London": ["Paris", "Barcelona", "Rome"],
        "Tokyo": ["Kyoto", "Osaka", "Hokkaido"],
    }

    default_destinations = ["Bali", "Maldives", "Santorini"]

    if origin and origin not in destinations_by_origin:
        raise ValueError(f"Origin not supported: {origin}")

    return {
        "origin": origin if origin else "Worldwide",
        "destinations": destinations_by_origin.get(origin, default_destinations),
    }


from typing import Dict, List, Union


def get_parks(
    parkCode: str = "", stateCode: str = "", limit: int = 50
) -> Dict[str, Union[List[Dict[str, Union[str, int]]], str]]:
    """Retrieve basic information about national parks.

    Args:
        parkCode: A comma delimited list of park codes (each 4-10 characters in length).
        stateCode: A comma delimited list of 2 character state codes.
        limit: Number of results to return per request.

    Returns:
        Dict containing:
            - parks: List of dictionaries with park information
            - message: Status message
    """

    sample_parks = {
        "YELL": {
            "name": "Yellowstone",
            "state": "WY",
            "contact": "307-344-7381",
            "hours": "24/7",
            "fee": 35,
        },
        "YOSE": {
            "name": "Yosemite",
            "state": "CA",
            "contact": "209-372-0200",
            "hours": "24/7",
            "fee": 35,
        },
        "GRCA": {
            "name": "Grand Canyon",
            "state": "AZ",
            "contact": "928-638-7888",
            "hours": "24/7",
            "fee": 35,
        },
        "ZION": {
            "name": "Zion",
            "state": "UT",
            "contact": "435-772-3256",
            "hours": "24/7",
            "fee": 35,
        },
    }

    park_codes = parkCode.split(",") if parkCode else sample_parks.keys()
    state_codes = stateCode.split(",") if stateCode else []

    parks = []
    for code in park_codes:
        if code in sample_parks:
            park = sample_parks[code]
            if not state_codes or park["state"] in state_codes:
                parks.append(
                    {
                        "code": code,
                        "name": park["name"],
                        "state": park["state"],
                        "contact": park["contact"],
                        "hours": park["hours"],
                        "fee": park["fee"],
                    }
                )
        if len(parks) >= limit:
            break

    if not parks:
        return {"parks": [], "message": "No parks found matching the criteria."}

    return {"parks": parks, "message": "Parks retrieved successfully."}


import hashlib
from typing import Dict, Optional, Union


def get_ticket_prices(
    origin: str,
    destination: str,
    date: str,
    return_date: Optional[str] = None,
    adults: int = 1,
    currency: str = "USD",
) -> Dict[str, Union[str, float, int]]:
    """Returns ticket prices for travel from an origin to a destination.

    Args:
        origin: Origin location name.
        destination: Destination location name.
        date: Departure date (YYYY-MM-DD).
        return_date: Return date (YYYY-MM-DD) for round trips.
        adults: Number of adult passengers.
        currency: Desired currency code (e.g. 'USD', 'AUD').

    Returns:
        Dict containing:
            - origin: Origin location name
            - destination: Destination location name
            - date: Departure date
            - return_date: Return date if applicable
            - adults: Number of adult passengers
            - currency: Currency code
            - price: Calculated ticket price
    """
    if origin == destination:
        raise ValueError("Origin and destination cannot be the same.")

    # Generate a consistent but varied price based on input parameters
    hash_input = f"{origin}-{destination}-{date}-{return_date}-{adults}-{currency}"
    hash_value = int(hashlib.sha256(hash_input.encode()).hexdigest(), 16)
    base_price = (hash_value % 1000) + 100  # Base price between 100 and 1099

    # Adjust price based on number of adults
    total_price = base_price * adults

    return {
        "origin": origin,
        "destination": destination,
        "date": date,
        "return_date": return_date,
        "adults": adults,
        "currency": currency,
        "price": total_price,
    }


from typing import Dict, Literal


def make_booking(
    booking_type: Literal[
        "Badminton Court",
        "Squash Court",
        "Climbing Wall",
        "Spin Session",
        "Astro Turf",
        "Tennis Court",
    ],
    time: str,
    name_of_booking: str,
    membership_type: Literal["None", "Off-peak", "Standard", "Gold", "Diamond"],
) -> Dict[str, str]:
    """Create a same-day area/event booking.

    Args:
        booking_type: Name of area/event being booked.
        time: Time for booking (HH:MM - HH:MM).
        name_of_booking: Booking name.
        membership_type: Membership type of booker.

    Returns:
        Dict containing:
            - booking_id: Unique identifier for the booking
            - booking_type: Confirmed booking type
            - time: Confirmed booking time
            - name_of_booking: Name under which the booking is made
            - membership_type: Membership type of the booker
            - status: Status of the booking
    """
    if not (booking_type and time and name_of_booking and membership_type):
        raise ValueError("All parameters are required.")

    # Simulate a booking ID generation
    booking_id = (
        f"{hash((booking_type, time, name_of_booking, membership_type)) % 10000:04}"
    )

    # Simulate a booking confirmation status
    status = (
        "Confirmed" if membership_type in ["Standard", "Gold", "Diamond"] else "Pending"
    )

    return {
        "booking_id": booking_id,
        "booking_type": booking_type,
        "time": time,
        "name_of_booking": name_of_booking,
        "membership_type": membership_type,
        "status": status,
    }


from typing import Dict, List, Optional


def route_plan(
    start_location: str, end_location: str, avoid: Optional[str] = None
) -> Dict[str, Union[str, List[str]]]:
    """Plan driving route from one destination to another.

    Args:
        start_location: Starting point (address)
        end_location: Ending point (address)
        avoid: Cities to avoid during the route

    Returns:
        Dict containing:
            - start: Starting location
            - end: Ending location
            - route: List of cities in the planned route
            - avoided: List of cities that were avoided
    """

    # Sample data for demonstration purposes
    sample_routes = {
        ("New York", "Los Angeles"): [
            "Philadelphia",
            "Columbus",
            "Denver",
            "Las Vegas",
        ],
        ("San Francisco", "Seattle"): ["Sacramento", "Portland"],
        ("Miami", "Chicago"): ["Atlanta", "Nashville", "Indianapolis"],
    }

    # Determine the route based on the start and end locations
    route_key = (start_location, end_location)
    if route_key not in sample_routes:
        raise ValueError(f"Route not supported: {start_location} to {end_location}")

    route = sample_routes[route_key]
    avoided = []

    # Handle the 'avoid' parameter
    if avoid:
        avoided_cities = avoid.split(", ")
        route = [city for city in route if city not in avoided_cities]
        avoided = [city for city in avoided_cities if city in sample_routes[route_key]]

    return {
        "start": start_location,
        "end": end_location,
        "route": route,
        "avoided": avoided,
    }


from typing import Dict, List, Union


def search_accommodation(
    country: str,
    city: str = None,
    date_range: Dict[str, str] = None,
    guests: int = 1,
    amenities: List[str] = None,
    price_range: Dict[str, float] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, List[str]]]]]]:
    """Search accommodation listings by city.

    Args:
        country: The destination country for the accommodation search.
        city: The destination city for the accommodation search.
        date_range: Check-in and check-out dates for the accommodation.
        guests: Total number of guests.
        amenities: List of required amenities (e.g., wifi, kitchen, pool).
        price_range: Minimum and maximum price range.

    Returns:
        Dict containing:
            - country: The country of the search
            - city: The city of the search
            - listings: List of accommodation listings with:
                - name: Name of the accommodation
                - price_per_night: Price per night
                - amenities: List of amenities available
    """
    if not country:
        raise ValueError("Country is required for accommodation search.")

    sample_listings = {
        "USA": [
            {
                "name": "Cozy Cottage",
                "price_per_night": 120,
                "amenities": ["wifi", "kitchen"],
            },
            {
                "name": "Luxury Villa",
                "price_per_night": 350,
                "amenities": ["pool", "wifi", "gym"],
            },
        ],
        "Japan": [
            {
                "name": "Tokyo Apartment",
                "price_per_night": 90,
                "amenities": ["wifi", "kitchen"],
            },
            {
                "name": "Kyoto Ryokan",
                "price_per_night": 200,
                "amenities": ["onsen", "wifi"],
            },
        ],
    }

    if country not in sample_listings:
        raise ValueError(f"No listings available for country: {country}")

    listings = sample_listings[country]

    if city:
        listings = [
            listing for listing in listings if city.lower() in listing["name"].lower()
        ]

    if price_range:
        listings = [
            listing
            for listing in listings
            if price_range["min"] <= listing["price_per_night"] <= price_range["max"]
        ]

    if amenities:
        listings = [
            listing
            for listing in listings
            if all(amenity in listing["amenities"] for amenity in amenities)
        ]

    return {
        "country": country,
        "city": city or "Any",
        "listings": listings,
    }


from typing import Dict, Optional, Union


def search_airfare(
    departure_airport: str,
    arrival_airport: str,
    departure_time: Optional[str] = None,
    arrival_time: Optional[str] = None,
    airline: Optional[str] = None,
    flight_number: Optional[str] = None,
    currency: Optional[str] = "USD",
) -> Dict[str, Union[str, float]]:
    """Retrieve flight ticket prices for specified departure and arrival city.

    Args:
        departure_airport: The IATA code for the major airport of the departure city.
        arrival_airport: The IATA code for the major airport of the arrival city.
        departure_time: The scheduled departure date and time.
        arrival_time: The scheduled arrival date and time.
        airline: The name or code of the airline operating the flight.
        flight_number: A unique code assigned to each flight.
        currency: Currency for the ticket price (default is USD).

    Returns:
        Dict containing:
            - departure_airport: IATA code of the departure airport
            - arrival_airport: IATA code of the arrival airport
            - airline: Airline name or code
            - flight_number: Flight number
            - price: Ticket price in specified currency
            - currency: Currency of the ticket price
    """
    if not departure_airport or not arrival_airport:
        raise ValueError("Both departure_airport and arrival_airport are required.")

    # Mocked sample data based on hash of input parameters for consistency
    base_price = (
        hash((departure_airport, arrival_airport, airline, flight_number)) % 500 + 100
    )
    currency_conversion = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "CAD": 1.25,
        "AUD": 1.35,
    }

    if currency not in currency_conversion:
        raise ValueError(f"Unsupported currency: {currency}")

    converted_price = base_price * currency_conversion[currency]

    return {
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
        "airline": airline or "Unknown Airline",
        "flight_number": flight_number or "N/A",
        "price": round(converted_price, 2),
        "currency": currency,
    }


import hashlib
from typing import Dict, List, Union


def search_available_flights(
    departure_location: str,
    destination_location: str,
    departure_date: str,
    return_date: Union[str, None] = None,
    number_of_passengers: int = 1,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search for available flights between two locations.

    Args:
        departure_location: Flight's departure location
        destination_location: Flight's destination location
        departure_date: Departure date in DD-MM-YYYY format
        return_date: Return date in DD-MM-YYYY format for round trips
        number_of_passengers: Number of passengers traveling

    Returns:
        Dict containing:
            - departure_location: Departure city name
            - destination_location: Destination city name
            - flights: List of available flights with:
                - flight_number: Unique flight identifier
                - airline: Airline operating the flight
                - price: Price per passenger in USD
                - departure_time: Scheduled departure time
                - arrival_time: Scheduled arrival time
    """
    if not departure_location or not destination_location or not departure_date:
        raise ValueError("Missing required flight search parameters")

    # Generate a consistent but varied list of flights using hash-based generation
    hash_input = f"{departure_location}-{destination_location}-{departure_date}"
    hash_seed = int(hashlib.sha256(hash_input.encode()).hexdigest(), 16)

    airlines = ["Airways A", "Airways B", "Airways C"]
    flight_numbers = [f"FL{hash_seed % 1000 + i}" for i in range(3)]
    prices = [round((hash_seed % 500 + i * 50) / 10, 2) for i in range(3)]
    departure_times = ["08:00", "12:00", "18:00"]
    arrival_times = ["10:00", "14:00", "20:00"]

    flights = [
        {
            "flight_number": flight_numbers[i],
            "airline": airlines[i % len(airlines)],
            "price": prices[i],
            "departure_time": departure_times[i],
            "arrival_time": arrival_times[i],
        }
        for i in range(3)
    ]

    return {
        "departure_location": departure_location,
        "destination_location": destination_location,
        "flights": flights,
    }


from typing import Dict, List, Union


def search_available_hotels(
    city: str,
    checkin_date: str,
    checkout_date: str,
    number_of_guests: int,
    currency: str = "USD",
    max_price: Union[float, None] = None,
    number_of_beds: int = 1,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, int]]]]]:
    """Search for available hotels in a specific city.

    Args:
        city: City to search for hotels
        checkin_date: Check-in date in DD-MM-YYYY format
        checkout_date: Check-out date in DD-MM-YYYY format
        number_of_guests: Number of guests
        currency: Currency code for maximum price per night
        max_price: Maximum price per night in specified currency
        number_of_beds: Total number of beds

    Returns:
        Dict containing:
            - city: City where the search was conducted
            - hotels: List of available hotels with details
    """
    if not city:
        raise ValueError("City is required")
    if not checkin_date or not checkout_date:
        raise ValueError("Both check-in and check-out dates are required")
    if number_of_guests <= 0:
        raise ValueError("Number of guests must be at least 1")

    # Simulated hotel data
    sample_hotels = {
        "New York": [
            {"name": "Hotel Central", "price_per_night": 150, "beds": 2},
            {"name": "Budget Inn", "price_per_night": 80, "beds": 1},
        ],
        "Paris": [
            {"name": "Eiffel Stay", "price_per_night": 200, "beds": 2},
            {"name": "Louvre Lodge", "price_per_night": 120, "beds": 1},
        ],
    }

    if city not in sample_hotels:
        raise ValueError(f"No hotel data available for city: {city}")

    available_hotels = []
    for hotel in sample_hotels[city]:
        if hotel["beds"] >= number_of_beds and (
            max_price is None or hotel["price_per_night"] <= max_price
        ):
            available_hotels.append(hotel)

    return {
        "city": city,
        "hotels": available_hotels,
    }


import hashlib
from typing import Dict, List, Literal, Union


def search_flights(
    departure: str,
    arrival: str,
    departure_date: str,
    return_date: Union[str, None] = None,
    cabin: Literal["economy", "premium_economy", "business", "first"] = "economy",
    nonstop: bool = False,
    red_eye: bool = False,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search scheduled flights between two places on a target date.

    Args:
        departure: City or IATA code for departure (e.g., 'NYC' or 'JFK').
        arrival: City or IATA code for arrival (e.g., 'LON' or 'LHR').
        departure_date: Date of departure in YYYY-MM-DD format.
        return_date: Date of return in YYYY-MM-DD format (optional).
        cabin: Cabin class ('economy', 'premium_economy', 'business', 'first').
        nonstop: Only search for nonstop flights if true.
        red_eye: Only search for red-eye flights if true.

    Returns:
        Dict containing:
            - departure: Departure city or IATA code
            - arrival: Arrival city or IATA code
            - flights: List of available flights with details
    """

    # Simulate flight data generation using hash-based method for consistency
    def generate_flight_id(departure, arrival, date, index):
        hash_input = f"{departure}{arrival}{date}{index}".encode()
        return hashlib.md5(hash_input).hexdigest()[:8]

    # Sample flight data
    flights = []
    for i in range(3):  # Simulate 3 flight options
        flight_id = generate_flight_id(departure, arrival, departure_date, i)
        flights.append(
            {
                "flight_id": flight_id,
                "airline": f"Airline {i + 1}",
                "departure_time": f"{10 + i}:00",
                "arrival_time": f"{14 + i}:00",
                "duration": 4.0 + i * 0.5,  # Duration in hours
                "cabin": cabin,
                "nonstop": nonstop,
                "red_eye": red_eye,
                "price": 200.0 + i * 50.0,  # Price in USD
            }
        )

    return {"departure": departure, "arrival": arrival, "flights": flights}


import hashlib
from typing import Dict, List, Literal, Union


def stops_along_route_find(
    start_location: str,
    end_location: str,
    categories: List[
        Literal["gas", "food", "electric_charger", "coffee", "bathroom"]
    ] = ["gas"],
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Suggest places to take a break from driving along a route.

    Args:
        start_location: Starting point (address)
        end_location: Ending point (address)
        categories: Types of stops to look for (e.g., 'gas', 'food')

    Returns:
        Dict containing:
            - route: Description of the route
            - stops: List of suggested stops with details
    """

    def generate_sample_data(
        location: str, category: str
    ) -> Dict[str, Union[str, float]]:
        """Generate sample data for a stop based on location and category."""
        hash_input = f"{location}-{category}".encode()
        hash_value = hashlib.md5(hash_input).hexdigest()
        name = f"{category.capitalize()} Stop {hash_value[:5]}"
        latitude = int(hash_value[:2], 16) / 100.0 + 40.0  # Mock latitude
        longitude = int(hash_value[2:4], 16) / 100.0 - 100.0  # Mock longitude
        return {
            "name": name,
            "category": category,
            "latitude": latitude,
            "longitude": longitude,
        }

    if not start_location or not end_location:
        raise ValueError("Both start_location and end_location are required.")

    stops = []
    for category in categories:
        stops.append(generate_sample_data(start_location, category))
        stops.append(generate_sample_data(end_location, category))

    return {"route": f"From {start_location} to {end_location}", "stops": stops}


from typing import Dict, Literal, Union


def trip_cost_est(
    start_location: str,
    end_location: str,
    detour_miles: float = 0,
    miles_per_gallon: float = 30,
    lodging: Literal["car", "hotel", "motel", "campground"] = "motel",
) -> Dict[str, Union[float, str]]:
    """Estimate the total cost of a trip including fuel and lodging.

    Args:
        start_location: Starting point (address)
        end_location: Ending point (address)
        detour_miles: Amount of miles estimated to go off route
        miles_per_gallon: Amount of miles one gallon of gas their car gets
        lodging: Type of sleeping location ('car', 'hotel', 'motel', 'campground')

    Returns:
        Dict containing:
            - total_cost: Estimated total cost of the trip
            - fuel_cost: Estimated fuel cost
            - lodging_cost: Estimated lodging cost
            - total_miles: Total miles including detours
    """
    # Mock distance calculation between start and end location
    distance_sample = {
        ("New York", "Los Angeles"): 2800,
        ("San Francisco", "Las Vegas"): 570,
        ("Chicago", "Houston"): 1080,
    }
    distance = distance_sample.get((start_location, end_location))
    if distance is None:
        raise ValueError(f"Route not supported: {start_location} to {end_location}")

    # Calculate total miles
    total_miles = distance + detour_miles

    # Mock fuel price per gallon
    fuel_price_per_gallon = 3.5  # USD

    # Calculate fuel cost
    fuel_cost = (total_miles / miles_per_gallon) * fuel_price_per_gallon

    # Mock lodging cost per night
    lodging_cost_per_night = {
        "car": 0,
        "hotel": 150,
        "motel": 80,
        "campground": 30,
    }

    # Estimate number of nights based on distance
    nights = max(1, total_miles // 400)

    # Calculate lodging cost
    lodging_cost = nights * lodging_cost_per_night.get(lodging, 0)

    # Calculate total cost
    total_cost = fuel_cost + lodging_cost

    return {
        "total_cost": total_cost,
        "fuel_cost": fuel_cost,
        "lodging_cost": lodging_cost,
        "total_miles": total_miles,
    }
