import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Literal, Optional, Union


def update_patient_records(
    medical_number: str, update_notes: str, updated_by: str
) -> Dict[str, str]:
    """Update the patient's medical records with treatment details.

    Args:
        medical_number: Unique medical number assigned to the patient
        update_notes: Details of the treatment or prescription update
        updated_by: Name of the medical professional updating the records

    Returns:
        Dict containing:
            - medical_number: The patient's medical number
            - status: Status of the update operation
            - last_updated_by: Name of the medical professional who last updated the record
    """
    if not medical_number or not update_notes or not updated_by:
        raise ValueError("All parameters must be provided and non-empty.")

    # Simulate a database update operation
    # In a real-world scenario, this would involve database access code
    # Here, we mock the operation with a simple hash-based check for demonstration
    if hash(medical_number) % 2 == 0:
        status = "success"
    else:
        status = "failure"

    return {
        "medical_number": medical_number,
        "status": status,
        "last_updated_by": updated_by,
    }


def get_runs(
    username: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, int]]]]]:
    """Get a list of user running sessions.

    Args:
        username: Username for which to get the list of their running sessions

    Returns:
        Dict containing:
            - username: The username whose running sessions were retrieved
            - running_sessions: List of running sessions with their details
    """
    if not username:
        raise ValueError("Username must be provided")

    # Sample running sessions data
    sample_sessions = {
        "Joey": [
            {
                "session_id": "joey_001",
                "date": "2025-01-15",
                "distance_km": 5.2,
                "time_minutes": 24,
                "pace_min_per_km": 4.6,
            },
            {
                "session_id": "joey_002",
                "date": "2025-01-18",
                "distance_km": 8.1,
                "time_minutes": 38,
                "pace_min_per_km": 4.7,
            },
            {
                "session_id": "joey_003",
                "date": "2025-01-20",
                "distance_km": 3.5,
                "time_minutes": 16,
                "pace_min_per_km": 4.6,
            },
        ],
        "Sarah": [
            {
                "session_id": "sarah_001",
                "date": "2025-01-16",
                "distance_km": 4.8,
                "time_minutes": 28,
                "pace_min_per_km": 5.8,
            },
            {
                "session_id": "sarah_002",
                "date": "2025-01-19",
                "distance_km": 6.2,
                "time_minutes": 35,
                "pace_min_per_km": 5.6,
            },
        ],
        "Mike": [
            {
                "session_id": "mike_001",
                "date": "2025-01-14",
                "distance_km": 10.5,
                "time_minutes": 48,
                "pace_min_per_km": 4.6,
            },
            {
                "session_id": "mike_002",
                "date": "2025-01-17",
                "distance_km": 7.8,
                "time_minutes": 36,
                "pace_min_per_km": 4.6,
            },
        ],
    }

    if username not in sample_sessions:
        return {"username": username, "running_sessions": []}

    return {"username": username, "running_sessions": sample_sessions[username]}


def get_time(running_session_id: str) -> Dict[str, Union[str, float, int]]:
    """Get time information for a running session.

    Args:
        running_session_id: Running session id

    Returns:
        Dict containing:
            - running_session_id: The session ID
            - total_time_minutes: Total running time in minutes
            - average_pace_min_per_km: Average pace in minutes per kilometer
            - split_times: Split times for each kilometer
    """
    if not running_session_id:
        raise ValueError("Running session ID must be provided")

    # Sample time data for different sessions
    time_data = {
        "joey_001": {
            "total_time_minutes": 24.2,
            "average_pace_min_per_km": 4.65,
            "split_times": [4.5, 4.7, 4.6, 4.8, 4.6],
        },
        "joey_002": {
            "total_time_minutes": 38.1,
            "average_pace_min_per_km": 4.70,
            "split_times": [4.6, 4.7, 4.8, 4.7, 4.6, 4.8, 4.7, 4.6],
        },
        "joey_003": {
            "total_time_minutes": 16.1,
            "average_pace_min_per_km": 4.60,
            "split_times": [4.5, 4.7, 4.6],
        },
        "sarah_001": {
            "total_time_minutes": 27.8,
            "average_pace_min_per_km": 5.79,
            "split_times": [5.8, 5.9, 5.7, 5.8],
        },
        "sarah_002": {
            "total_time_minutes": 34.7,
            "average_pace_min_per_km": 5.60,
            "split_times": [5.5, 5.6, 5.7, 5.6, 5.5, 5.8],
        },
        "mike_001": {
            "total_time_minutes": 48.3,
            "average_pace_min_per_km": 4.60,
            "split_times": [4.5, 4.6, 4.7, 4.6, 4.5, 4.6, 4.7, 4.5, 4.6, 4.7],
        },
        "mike_002": {
            "total_time_minutes": 35.9,
            "average_pace_min_per_km": 4.60,
            "split_times": [4.5, 4.6, 4.7, 4.6, 4.5, 4.6, 4.8, 4.6],
        },
    }

    if running_session_id not in time_data:
        raise ValueError(f"Running session not found: {running_session_id}")

    session_data = time_data[running_session_id]
    return {
        "running_session_id": running_session_id,
        "total_time_minutes": session_data["total_time_minutes"],
        "average_pace_min_per_km": session_data["average_pace_min_per_km"],
        "split_times": session_data["split_times"],
    }


def call_doctor(schedule_appointment: bool = False) -> Dict[str, str]:
    """Call the doctor for help, optionally scheduling an appointment.

    Args:
        schedule_appointment: Whether to schedule an appointment (default is False)

    Returns:
        Dict containing:
            - status: The status of the call (e.g., 'connected', 'busy')
            - appointment: Details about the appointment if scheduled
    """
    import hashlib

    # Simulate a call status based on a hash of the input
    hash_input = f"{schedule_appointment}".encode()
    hash_value = hashlib.sha256(hash_input).hexdigest()

    if hash_value[0] in "0123456789abcdef":
        status = "connected"
    else:
        status = "busy"

    appointment_details = "No appointment scheduled"
    if schedule_appointment and status == "connected":
        appointment_details = "Appointment scheduled for tomorrow at 10 AM"

    return {
        "status": status,
        "appointment": appointment_details,
    }


from typing import Dict, List, Union


def compare_energy_drinks(
    drinks: Union[List[Dict[str, str]], str]
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Compare energy drinks based on nutrition, caffeine content, and price.

    Args:
        drinks: List of drinks to compare or a comma-separated string of drink names. Each drink should have brand and flavor information.

    Returns:
        Dict containing:
            - comparison: List of drinks with their nutrition, caffeine content, and price
    """
    if not drinks:
        raise ValueError("No drinks provided for comparison.")

    # Convert string to list of drinks if needed
    if isinstance(drinks, str):
        # Handle string input (comma-separated list of drink names)
        drink_names = [name.strip() for name in drinks.split(",")]
        processed_drinks = []
        for name in drink_names:
            # Try to extract brand and flavor from the name
            parts = name.split(" ", 1)
            if len(parts) > 1:
                processed_drinks.append({"brand": parts[0], "flavor": parts[1]})
            else:
                processed_drinks.append({"brand": name, "flavor": "Original"})
        drinks = processed_drinks

    # Sample data for mock comparison
    sample_data = {
        ("BrandA", "Original"): {"calories": 110, "caffeine_mg": 80, "price_usd": 2.5},
        ("BrandB", "Berry"): {"calories": 120, "caffeine_mg": 90, "price_usd": 2.8},
        ("BrandC", "Citrus"): {"calories": 100, "caffeine_mg": 85, "price_usd": 2.3},
    }

    comparison_results = []
    for drink in drinks:
        key = (drink.get("brand"), drink.get("flavor"))
        if key not in sample_data:
            raise ValueError(f"Drink not supported: {key}")

        drink_data = sample_data[key]
        comparison_results.append(
            {
                "brand": drink.get("brand"),
                "flavor": drink.get("flavor"),
                "calories": drink_data["calories"],
                "caffeine_mg": drink_data["caffeine_mg"],
                "price_usd": drink_data["price_usd"],
            }
        )

    return {"comparison": comparison_results}


from typing import Dict


def confirm_prescription(
    patient_name: str, medical_number: str, drug_name: str, confirmation: bool
) -> Dict[str, str]:
    """Confirm the prescription details before administering drugs to a patient.

    Args:
        patient_name: Full name of the patient
        medical_number: Unique medical number assigned to the patient
        drug_name: Name of the prescribed drug
        confirmation: Whether the prescription is confirmed for administration

    Returns:
        Dict containing:
            - status: Confirmation status message
            - patient_name: Full name of the patient
            - medical_number: Unique medical number of the patient
            - drug_name: Name of the prescribed drug
    """
    if not confirmation:
        raise ValueError("Prescription confirmation is required before administration.")

    # Simulate a confirmation process
    confirmation_status = "confirmed" if confirmation else "not confirmed"

    return {
        "status": f"Prescription {confirmation_status} for administration.",
        "patient_name": patient_name,
        "medical_number": medical_number,
        "drug_name": drug_name,
    }


from typing import Dict, Union


def get_caffeine_warning(
    brand_name: Union[str, None] = None, caffeine_mg: float = None
) -> Dict[str, Union[str, float, bool]]:
    """Checks if the caffeine amount in a drink exceeds recommended limits.

    Args:
        brand_name: The brand name of the drink.
        caffeine_mg: The amount of caffeine in milligrams.

    Returns:
        Dict containing:
            - brand_name: The brand name of the drink, if provided
            - caffeine_mg: The amount of caffeine in milligrams
            - exceeds_limit: Boolean indicating if the caffeine amount exceeds the recommended limit
            - warning_message: A warning message if the limit is exceeded
    """
    if caffeine_mg is None:
        raise ValueError("caffeine_mg is a required parameter")

    recommended_limit_mg = 400  # Recommended daily limit for an average adult
    exceeds_limit = caffeine_mg > recommended_limit_mg

    warning_message = (
        f"Warning: This drink exceeds the recommended caffeine limit of {recommended_limit_mg} mg."
        if exceeds_limit
        else "Caffeine amount is within the recommended limit."
    )

    return {
        "brand_name": brand_name if brand_name else "Unknown",
        "caffeine_mg": caffeine_mg,
        "exceeds_limit": exceeds_limit,
        "warning_message": warning_message,
    }


from typing import Dict, Union


def get_calories_burned(
    exercise_name: str, duration: float, weight: float = 60
) -> Dict[str, Union[str, float]]:
    """Calculate the number of calories burned during a cardio exercise.

    Args:
        exercise_name: The name of the exercise being performed.
        duration: How long to perform the exercise for in minutes.
        weight: The weight of the user in kg. Defaults to 60kg if not provided.

    Returns:
        Dict containing:
            - exercise_name: Name of the exercise
            - duration: Duration of the exercise in minutes
            - weight: Weight of the user in kg
            - calories_burned: Estimated calories burned
    """

    # Sample MET values for different exercises
    met_values = {
        "running": 9.8,
        "cycling": 7.5,
        "swimming": 8.0,
        "walking": 3.8,
    }

    if exercise_name not in met_values:
        raise ValueError(f"Exercise not supported: {exercise_name}")

    met = met_values[exercise_name]
    calories_burned = (met * weight * duration) / 60

    return {
        "exercise_name": exercise_name,
        "duration": duration,
        "weight": weight,
        "calories_burned": round(calories_burned, 2),
    }


from typing import Dict, List, Optional


def get_drug_side_effects(
    drug_name: str, dosage: Optional[str] = None
) -> Dict[str, Union[str, List[str]]]:
    """Retrieve side effects for a specified drug, optionally considering the dosage.

    Args:
        drug_name: Name of the drug
        dosage: Dosage of the drug (optional)

    Returns:
        Dict containing:
            - drug_name: Name of the drug
            - dosage: Dosage of the drug (if provided)
            - side_effects: List of potential side effects
    """

    # Sample data for demonstration purposes
    side_effects_data = {
        "Aspirin": {
            None: ["nausea", "vomiting", "stomach pain"],
            "100mg": ["mild headache", "dizziness"],
            "500mg": ["severe headache", "ringing in ears"],
        },
        "Ibuprofen": {
            None: ["upset stomach", "mild heartburn"],
            "200mg": ["drowsiness", "blurred vision"],
            "400mg": ["high blood pressure", "rash"],
        },
    }

    if drug_name not in side_effects_data:
        raise ValueError(f"Drug not supported: {drug_name}")

    # Retrieve side effects based on drug name and dosage
    drug_side_effects = side_effects_data[drug_name]
    side_effects = drug_side_effects.get(dosage, drug_side_effects[None])

    return {"drug_name": drug_name, "dosage": dosage, "side_effects": side_effects}


from typing import Dict, List, Union


def get_exercises(
    primary_muscles: str, equipment_required: bool = True
) -> List[Dict[str, Union[str, List[str], bool]]]:
    """Returns data on exercises that match the body part specified by the primary_muscles parameter.

    Args:
        primary_muscles: The primary muscle to be targeted by the exercise.
        equipment_required: Filter exercises depending on whether equipment is required.

    Returns:
        List of dictionaries, each containing:
            - description: Description of the exercise
            - difficulty_level: Difficulty level of the exercise
            - equipment_required: Boolean indicating if equipment is required
            - primary_muscles: List of primary muscles targeted
            - secondary_muscles: List of secondary muscles targeted
    """

    sample_exercises = [
        {
            "description": "Push-up",
            "difficulty_level": "Intermediate",
            "equipment_required": False,
            "primary_muscles": ["chest"],
            "secondary_muscles": ["triceps", "shoulders"],
        },
        {
            "description": "Barbell Bench Press",
            "difficulty_level": "Advanced",
            "equipment_required": True,
            "primary_muscles": ["chest"],
            "secondary_muscles": ["triceps", "shoulders"],
        },
        {
            "description": "Squat",
            "difficulty_level": "Intermediate",
            "equipment_required": False,
            "primary_muscles": ["legs"],
            "secondary_muscles": ["glutes", "lower back"],
        },
        {
            "description": "Deadlift",
            "difficulty_level": "Advanced",
            "equipment_required": True,
            "primary_muscles": ["back"],
            "secondary_muscles": ["legs", "core"],
        },
    ]

    if not primary_muscles:
        raise ValueError("Primary muscles parameter is required.")

    filtered_exercises = [
        exercise
        for exercise in sample_exercises
        if primary_muscles.lower() in exercise["primary_muscles"]
        and (exercise["equipment_required"] == equipment_required)
    ]

    return filtered_exercises


from typing import Dict, Union


def get_patient_details(
    name: str, medical_number: str
) -> Dict[str, Union[str, int, list]]:
    """Retrieve patient details based on their name and medical number.

    Args:
        name: Full name of the patient
        medical_number: Unique medical number assigned to the patient

    Returns:
        Dict containing:
            - name: Full name of the patient
            - medical_number: Unique medical number
            - age: Age of the patient
            - conditions: List of medical conditions
    """
    # Simulated patient database
    patients = {
        "John Doe": {
            "medical_number": "123456",
            "age": 45,
            "conditions": ["hypertension", "diabetes"],
        },
        "Jane Smith": {"medical_number": "654321", "age": 37, "conditions": ["asthma"]},
        "Henry Martin": {
            "medical_number": "GGTH472",
            "age": 25,
            "conditions": ["allergies"],
        },
        "Mark Martin": {
            "medical_number": "GGTH552",
            "age": 52,
            "conditions": ["allergies"],
        },
        # Legacy entries for backward compatibility
        "Henry Martin (Legacy)": {
            "medical_number": "111222",
            "age": 25,
            "conditions": ["allergies"],
        },
        "Mark Martin (Legacy)": {
            "medical_number": "111223",
            "age": 52,
            "conditions": ["allergies"],
        },
    }

    # Check if the patient exists in the database
    if name not in patients or patients[name]["medical_number"] != medical_number:
        raise ValueError(f"Patient not found or medical number mismatch for: {name}")

    patient = patients[name]
    return {
        "name": name,
        "medical_number": medical_number,
        "age": patient["age"],
        "conditions": patient["conditions"],
    }


from typing import Dict, List


def get_pet_medication_schedule(
    pet_name: str, medication_name: str
) -> Dict[str, Union[str, List[str]]]:
    """Retrieve the medication schedule for a pet.

    Args:
        pet_name: The pet's name
        medication_name: Name of the medication

    Returns:
        Dict containing:
            - pet_name: The name of the pet
            - medication_name: The name of the medication
            - schedule: List of times the medication should be administered
    """

    sample_data = {
        ("Buddy", "Heartworm"): ["8:00 AM", "8:00 PM"],
        ("Whiskers", "Flea Prevention"): ["9:00 AM"],
        ("Rex", "Pain Relief"): ["7:00 AM", "7:00 PM"],
    }

    key = (pet_name, medication_name)
    if key not in sample_data:
        raise ValueError(
            f"Medication schedule not found for pet: {pet_name} with medication: {medication_name}"
        )

    return {
        "pet_name": pet_name,
        "medication_name": medication_name,
        "schedule": sample_data[key],
    }


from datetime import datetime, timedelta
from typing import Dict, List, Union


def get_pet_vaccination_schedule(
    pet_name: str, species: str, birth_date: str
) -> Dict[str, Union[str, List[Dict[str, Union[str, datetime]]]]]:
    """Retrieve the upcoming vaccination schedule for a specific pet.

    Args:
        pet_name: The pet's name
        species: Species of the pet (e.g., dog, cat, rabbit)
        birth_date: The pet's date of birth in YYYY-MM-DD format

    Returns:
        Dict containing:
            - pet_name: The pet's name
            - species: The species of the pet
            - upcoming_vaccinations: List of upcoming vaccinations with details
    """

    def fuzzy_match_species(search_species: str, available_species: List[str]) -> str:
        """Find the best matching species using fuzzy matching"""
        search_lower = search_species.lower().strip()

        # Direct exact match
        for spec in available_species:
            if spec.lower() == search_lower:
                return spec

        # Species variations and mappings
        species_mappings = {
            "dog": ["dog", "puppy", "canine"],
            "cat": ["cat", "kitten", "feline"],
            "rabbit": ["rabbit", "bunny"],
            "reptile": [
                "reptile",
                "snake",
                "python",
                "ball python",
                "royal python",
                "gecko",
                "lizard",
                "iguana",
                "turtle",
                "tortoise",
            ],
            "bird": ["bird", "parrot", "cockatiel", "budgie", "canary", "finch"],
            "hamster": ["hamster", "gerbil", "guinea pig", "mouse", "rat"],
            "ferret": ["ferret"],
            "horse": ["horse", "pony", "equine"],
        }

        # Find matching category
        for base_species, variants in species_mappings.items():
            if search_lower in variants:
                return base_species

        # Partial match - search species contains available species or vice versa
        for spec in available_species:
            spec_lower = spec.lower()
            if search_lower in spec_lower or spec_lower in search_lower:
                return spec

        # Return the first available species as fallback
        return available_species[0] if available_species else "dog"

    try:
        birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    # Expanded vaccination schedules based on species categories
    vaccination_schedules = {
        "dog": [
            {"vaccine": "Rabies", "age_weeks": 12},
            {"vaccine": "Distemper", "age_weeks": 8},
            {"vaccine": "Parvovirus", "age_weeks": 16},
        ],
        "cat": [
            {"vaccine": "Feline Leukemia", "age_weeks": 9},
            {"vaccine": "Rabies", "age_weeks": 12},
            {"vaccine": "FVRCP", "age_weeks": 8},
        ],
        "rabbit": [
            {"vaccine": "Myxomatosis", "age_weeks": 6},
            {"vaccine": "Rabbit Hemorrhagic Disease", "age_weeks": 10},
        ],
        "reptile": [
            {"vaccine": "Reptile Health Check", "age_weeks": 4},
            {"vaccine": "Parasite Prevention", "age_weeks": 8},
        ],
        "bird": [
            {"vaccine": "Polyomavirus", "age_weeks": 6},
            {"vaccine": "Newcastle Disease", "age_weeks": 10},
            {"vaccine": "Avian Health Screening", "age_weeks": 12},
        ],
        "hamster": [
            {"vaccine": "Small Mammal Health Check", "age_weeks": 4},
            {"vaccine": "Respiratory Health Screen", "age_weeks": 8},
        ],
        "ferret": [
            {"vaccine": "Distemper", "age_weeks": 8},
            {"vaccine": "Rabies", "age_weeks": 12},
            {"vaccine": "Adrenal Disease Screen", "age_weeks": 52},
        ],
        "horse": [
            {"vaccine": "Tetanus", "age_weeks": 16},
            {"vaccine": "Eastern/Western Encephalitis", "age_weeks": 20},
            {"vaccine": "Rabies", "age_weeks": 24},
            {"vaccine": "West Nile Virus", "age_weeks": 28},
        ],
    }

    # Find matching species using fuzzy matching
    available_species = list(vaccination_schedules.keys())
    matched_species = fuzzy_match_species(species, available_species)

    if matched_species not in vaccination_schedules:
        # Generate basic vaccination schedule for unknown species
        vaccination_schedules[matched_species] = [
            {"vaccine": "General Health Check", "age_weeks": 4},
            {"vaccine": "Species-Specific Health Screen", "age_weeks": 8},
        ]

    today = datetime.today()
    upcoming_vaccinations = []

    for vaccine_info in vaccination_schedules[matched_species]:
        vaccine_date = birth_date_obj + timedelta(weeks=vaccine_info["age_weeks"])
        if vaccine_date > today:
            upcoming_vaccinations.append(
                {
                    "vaccine": vaccine_info["vaccine"],
                    "scheduled_date": vaccine_date,
                }
            )

    return {
        "pet_name": pet_name,
        "species": matched_species,
        "upcoming_vaccinations": upcoming_vaccinations,
    }


from typing import Dict, Union


def track_energy_drink_consumption(
    brand_name: str,
    caffeine_mg: float,
    flavor: Union[str, None] = None,
    sugar_g: Union[float, None] = None,
) -> Dict[str, Union[str, float, None]]:
    """Logs and tracks the user's daily energy drink intake.

    Args:
        brand_name: The brand name of the consumed drink.
        caffeine_mg: The amount of caffeine consumed in milligrams.
        flavor: The flavor variant consumed (optional).
        sugar_g: The amount of sugar consumed in grams (optional).

    Returns:
        Dict containing:
            - brand_name: The brand name of the consumed drink.
            - caffeine_mg: The amount of caffeine consumed in milligrams.
            - flavor: The flavor variant consumed.
            - sugar_g: The amount of sugar consumed in grams.
            - daily_total_caffeine: Total caffeine consumed today in milligrams.
            - daily_total_sugar: Total sugar consumed today in grams.
    """
    if caffeine_mg <= 0:
        raise ValueError("Caffeine amount must be greater than zero.")

    # Simulated daily totals using hash-based generation for consistency
    daily_total_caffeine = hash(brand_name) % 400 + caffeine_mg
    daily_total_sugar = (hash(flavor) % 100 + sugar_g) if sugar_g is not None else None

    return {
        "brand_name": brand_name,
        "caffeine_mg": caffeine_mg,
        "flavor": flavor,
        "sugar_g": sugar_g,
        "daily_total_caffeine": daily_total_caffeine,
        "daily_total_sugar": daily_total_sugar,
    }


from typing import Dict, Optional


def book_appointment(
    provider_name: str,
    appointment_type: str,
    preferred_date: Optional[str] = None,
    preferred_time: Optional[str] = None,
    insurance_provider: Optional[str] = None,
) -> Dict[str, str]:
    """Schedule an appointment with a healthcare provider.

    Args:
        provider_name: Name of the healthcare provider or practice
        appointment_type: Type of appointment (checkup, consultation, follow-up, urgent)
        preferred_date: Preferred date for appointment (YYYY-MM-DD)
        preferred_time: Preferred time slot (morning, afternoon, evening)
        insurance_provider: Patient's insurance provider name

    Returns:
        Dict containing:
            - confirmation_id: Unique confirmation ID for the appointment
            - provider_name: Name of the healthcare provider
            - appointment_type: Type of appointment scheduled
            - scheduled_date: Scheduled date for the appointment
            - scheduled_time: Scheduled time for the appointment
            - insurance_provider: Insurance provider used for the appointment
    """
    if not provider_name or not appointment_type:
        raise ValueError("Provider name and appointment type are required.")

    # Simulate a hash-based generation for consistent sample data
    confirmation_id = f"{hash(provider_name + appointment_type) % 10000:04d}"

    # Mocked scheduling logic
    scheduled_date = preferred_date if preferred_date else "2023-11-01"
    scheduled_time = preferred_time if preferred_time else "morning"

    return {
        "confirmation_id": confirmation_id,
        "provider_name": provider_name,
        "appointment_type": appointment_type,
        "scheduled_date": scheduled_date,
        "scheduled_time": scheduled_time,
        "insurance_provider": insurance_provider or "Not provided",
    }


import hashlib
from datetime import datetime
from typing import Dict, Union


def book_doctor_appointment(
    hospital_id: int,
    date_time: str,
    patient_name: str,
    patient_birthday: str,
    doctor_name: Union[str, None] = None,
    specialty: str = "General practice",
) -> Dict[str, Union[str, int]]:
    """Books an appointment with a doctor at a specified hospital.

    Args:
        hospital_id: The unique id of the hospital for the appointment.
        date_time: Desired date and time for the appointment in ISO 8601 format.
        patient_name: The last name of the patient for booking purposes.
        patient_birthday: The date of birth of the patient for booking purposes.
        doctor_name: The name of the doctor for the appointment. Optional if booking with any available doctor.
        specialty: Medical specialty if a specific doctor is not provided.

    Returns:
        Dict containing:
            - appointment_id: Unique identifier for the booked appointment
            - hospital_id: The hospital id where the appointment is booked
            - doctor_name: Name of the doctor for the appointment
            - specialty: Medical specialty of the doctor
            - date_time: Confirmed date and time of the appointment
            - patient_name: Name of the patient
    """
    try:
        # Validate date_time format
        datetime.fromisoformat(date_time)
    except ValueError:
        raise ValueError("Invalid date_time format. Must be ISO 8601.")

    # Simulate doctor selection
    if not doctor_name:
        doctor_name = (
            "Dr. Smith"
            if specialty == "General practice"
            else f"Dr. {specialty} Specialist"
        )

    # Generate a unique appointment_id using a hash
    appointment_id = (
        int(
            hashlib.sha256(
                f"{hospital_id}{date_time}{patient_name}".encode()
            ).hexdigest(),
            16,
        )
        % 10**8
    )

    return {
        "appointment_id": appointment_id,
        "hospital_id": hospital_id,
        "doctor_name": doctor_name,
        "specialty": specialty,
        "date_time": date_time,
        "patient_name": patient_name,
    }


from typing import Dict


def call_veterinarian(
    schedule_appointment: bool = False, is_medical_emergency: bool = False
) -> Dict[str, str]:
    """Call the veterinarian for help.

    Args:
        schedule_appointment: Whether to schedule an appointment
        is_medical_emergency: Whether there is a medical emergency

    Returns:
        Dict containing:
            - action: The action taken by the veterinarian
            - message: A message detailing the next steps
    """

    if is_medical_emergency:
        return {
            "action": "emergency_response",
            "message": "An emergency team is dispatched to your location immediately.",
        }

    if schedule_appointment:
        return {
            "action": "appointment_scheduled",
            "message": "An appointment has been scheduled for the next available slot.",
        }

    return {
        "action": "general_inquiry",
        "message": "Please call during business hours for non-emergency inquiries.",
    }


import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Literal, Union


def check_provider_availability(
    provider_name: str,
    date_range: Literal["this_week", "next_week", "next_month"] = "next_week",
    appointment_duration: int = 30,
) -> Dict[str, Union[str, List[str]]]:
    """Check available time slots for a healthcare provider.

    Args:
        provider_name: Name of the healthcare provider to check
        date_range: Date range to check ('this_week', 'next_week', 'next_month')
        appointment_duration: Expected appointment duration in minutes

    Returns:
        Dict containing:
            - provider_name: Name of the healthcare provider
            - available_slots: List of available time slots as strings
    """

    # Simulate available slots based on provider name and date range
    def generate_slots(provider: str, days: int) -> List[str]:
        slots = []
        base_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        for day in range(days):
            for hour in range(9, 17):  # 9 AM to 5 PM
                slot_time = base_time + timedelta(days=day, hours=hour)
                # Generate a hash-based decision for slot availability
                slot_hash = hashlib.md5(f"{provider}{slot_time}".encode()).hexdigest()
                if int(slot_hash, 16) % 2 == 0:  # Simulate 50% availability
                    slots.append(slot_time.strftime("%Y-%m-%d %H:%M"))
        return slots

    if date_range == "this_week":
        days_to_check = 7
    elif date_range == "next_week":
        days_to_check = 7
    elif date_range == "next_month":
        days_to_check = 30
    else:
        raise ValueError(f"Unsupported date range: {date_range}")

    available_slots = generate_slots(provider_name, days_to_check)

    return {
        "provider_name": provider_name,
        "available_slots": available_slots,
    }


from typing import Dict, Union


def create_food_item(
    name: str,
    portion_size: int = 0,
    energy_kj: int = 0,
    energy_kcal: int = 0,
    fat_total: int = 0,
    fat_saturates: int = 0,
    carb_total: int = 0,
    carb_sugars: int = 0,
    fibre: int = 0,
    protein: int = 0,
    salt: int = 0,
) -> Dict[str, Union[str, int]]:
    """Sets up a new food item in the daily nutrition tracker.

    Args:
        name: Name of the food item
        portion_size: Weight of a standard portion of the food item in grams
        energy_kj: Energy per 100g in kJ
        energy_kcal: Energy per 100g in kcal
        fat_total: Total fat grams per 100g
        fat_saturates: Saturated fat grams per 100g. Must be less than fat_total
        carb_total: Carbohydrate grams per 100g
        carb_sugars: Sugar carbohydrate grams per 100g. Must be less than carb_total
        fibre: Fibre grams per 100g
        protein: Protein grams per 100g
        salt: Salt grams per 100g

    Returns:
        Dict containing:
            - name: Name of the food item
            - portion_size: Portion size in grams
            - energy_kj: Energy in kJ per 100g
            - energy_kcal: Energy in kcal per 100g
            - fat_total: Total fat in grams per 100g
            - fat_saturates: Saturated fat in grams per 100g
            - carb_total: Total carbohydrates in grams per 100g
            - carb_sugars: Sugars in grams per 100g
            - fibre: Fibre in grams per 100g
            - protein: Protein in grams per 100g
            - salt: Salt in grams per 100g
    """
    if fat_saturates > fat_total:
        raise ValueError("Saturated fat cannot exceed total fat")
    if carb_sugars > carb_total:
        raise ValueError("Sugar carbohydrates cannot exceed total carbohydrates")

    return {
        "name": name,
        "portion_size": portion_size,
        "energy_kj": energy_kj,
        "energy_kcal": energy_kcal,
        "fat_total": fat_total,
        "fat_saturates": fat_saturates,
        "carb_total": carb_total,
        "carb_sugars": carb_sugars,
        "fibre": fibre,
        "protein": protein,
        "salt": salt,
    }


import hashlib
from typing import Dict, Literal, Union


def create_membership(
    new_member_name: str,
    date_of_birth: str,
    email: str,
    phone_number: str,
    membership_type: Literal["Off-peak", "Standard", "Gold", "Diamond"],
    flavoured_water_add_on: bool = False,
) -> Dict[str, Union[str, bool]]:
    """Create or register a new gym member.

    Args:
        new_member_name: First name and surname of the new member.
        date_of_birth: Member’s date of birth (YYYY-MM-DD).
        email: Member’s email address.
        phone_number: Member’s contact/phone number.
        membership_type: Desired membership type ('Off-peak', 'Standard', 'Gold', 'Diamond').
        flavoured_water_add_on: Include flavoured water package? Defaults to False.

    Returns:
        Dict containing:
            - member_id: Unique identifier for the new member
            - name: Full name of the member
            - membership_type: Type of membership chosen
            - flavoured_water_add_on: Whether the flavoured water package is included
            - registration_status: Status of the registration process
    """
    if (
        not new_member_name
        or not date_of_birth
        or not email
        or not phone_number
        or not membership_type
    ):
        raise ValueError("All required fields must be provided")

    # Generate a unique member ID using a hash of the email
    member_id = hashlib.sha256(email.encode()).hexdigest()[:10]

    # Simulate a successful registration process
    registration_status = "Success"

    return {
        "member_id": member_id,
        "name": new_member_name,
        "membership_type": membership_type,
        "flavoured_water_add_on": flavoured_water_add_on,
        "registration_status": registration_status,
    }


from typing import Dict, List, Union


def find_nearby_specialists(
    specialty: str,
    location: str,
    insurance_accepted: Union[str, None] = None,
    max_distance: int = 25,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Find specialist doctors near a location.

    Args:
        specialty: Medical specialty (e.g., 'cardiologist', 'dermatologist')
        location: City or zip code to search near
        insurance_accepted: Insurance plan that must be accepted
        max_distance: Maximum distance in miles

    Returns:
        Dict containing:
            - location: The location searched
            - specialists: List of specialists with details such as name, distance, and insurance accepted
    """

    def normalize_specialty(search_specialty: str) -> str:
        """Map specialty variations to standard specialty names."""
        specialty_mappings = {
            # Orthopedic variations
            "orthopedic": "orthopedic",
            "orthopedist": "orthopedic",
            "orthopedic surgeon": "orthopedic",
            "orthopedic surgery": "orthopedic",
            "ortho": "orthopedic",
            "bone doctor": "orthopedic",
            "joint doctor": "orthopedic",
            # Cardiology variations
            "cardiologist": "cardiologist",
            "cardiology": "cardiologist",
            "heart doctor": "cardiologist",
            # Dermatology variations
            "dermatologist": "dermatologist",
            "dermatology": "dermatologist",
            "skin doctor": "dermatologist",
            # Additional specialties
            "neurologist": "neurologist",
            "neurology": "neurologist",
            "brain doctor": "neurologist",
            "psychiatrist": "psychiatrist",
            "psychiatry": "psychiatrist",
            "mental health": "psychiatrist",
        }

        search_lower = search_specialty.lower().strip()

        # Direct match first
        if search_lower in specialty_mappings:
            return specialty_mappings[search_lower]

        # Partial matching for compound terms
        for variation, standard in specialty_mappings.items():
            if variation in search_lower or search_lower in variation:
                return standard

        # If no match found, return the original (will be handled by extended data)
        return search_lower

    def normalize_insurance(insurance_plan: str) -> str:
        """Map insurance variations to standard insurance names."""
        if not insurance_plan:
            return None

        insurance_mappings = {
            "blue cross": "Blue Cross",
            "bluecross": "Blue Cross",
            "blue cross blue shield": "Blue Cross",
            "bcbs": "Blue Cross",
            "healthplus": "HealthPlus",
            "health plus": "HealthPlus",
            "medicare": "MediCare",
            "medi care": "MediCare",
            "aetna": "Aetna",
            "cigna": "Cigna",
            "humana": "Humana",
            "united healthcare": "United Healthcare",
            "unitedhealth": "United Healthcare",
        }

        insurance_lower = insurance_plan.lower().strip()

        # Direct match first
        if insurance_lower in insurance_mappings:
            return insurance_mappings[insurance_lower]

        # Partial matching
        for variation, standard in insurance_mappings.items():
            if variation in insurance_lower or insurance_lower in variation:
                return standard

        # Return original if no match found
        return insurance_plan

    # Expanded sample data with more specialists and locations
    sample_specialists = {
        "cardiologist": [
            {
                "name": "Dr. Heart",
                "distance": 10,
                "insurance": "HealthPlus",
                "location": "Chicago",
            },
            {
                "name": "Dr. Cardio",
                "distance": 15,
                "insurance": "MediCare",
                "location": "Chicago",
            },
            {
                "name": "Dr. Rhythm",
                "distance": 12,
                "insurance": "Blue Cross",
                "location": "Chicago",
            },
        ],
        "dermatologist": [
            {
                "name": "Dr. Skin",
                "distance": 5,
                "insurance": "HealthPlus",
                "location": "Chicago",
            },
            {
                "name": "Dr. Derm",
                "distance": 20,
                "insurance": "MediCare",
                "location": "Chicago",
            },
            {
                "name": "Dr. Complexion",
                "distance": 8,
                "insurance": "Blue Cross",
                "location": "Chicago",
            },
        ],
        "orthopedic": [
            {
                "name": "Dr. Bone",
                "distance": 8,
                "insurance": "HealthPlus",
                "location": "Chicago",
            },
            {
                "name": "Dr. Joint",
                "distance": 18,
                "insurance": "MediCare",
                "location": "Chicago",
            },
            {
                "name": "Dr. Spine",
                "distance": 6,
                "insurance": "Blue Cross",
                "location": "Chicago",
            },
            {
                "name": "Dr. Ortho",
                "distance": 12,
                "insurance": "Blue Cross",
                "location": "Chicago",
            },
            {
                "name": "Dr. Fracture",
                "distance": 22,
                "insurance": "Aetna",
                "location": "Chicago",
            },
        ],
        "neurologist": [
            {
                "name": "Dr. Brain",
                "distance": 14,
                "insurance": "Blue Cross",
                "location": "Chicago",
            },
            {
                "name": "Dr. Neural",
                "distance": 19,
                "insurance": "HealthPlus",
                "location": "Chicago",
            },
        ],
        "psychiatrist": [
            {
                "name": "Dr. Mind",
                "distance": 7,
                "insurance": "Blue Cross",
                "location": "Chicago",
            },
            {
                "name": "Dr. Mental",
                "distance": 16,
                "insurance": "MediCare",
                "location": "Chicago",
            },
        ],
    }

    # Normalize the search parameters
    normalized_specialty = normalize_specialty(specialty)
    normalized_insurance = (
        normalize_insurance(insurance_accepted) if insurance_accepted else None
    )

    # Find specialists for the normalized specialty
    specialists_data = sample_specialists.get(normalized_specialty, [])

    # If no exact match, try fuzzy matching across all specialties
    if not specialists_data:
        for spec_key, spec_list in sample_specialists.items():
            if normalized_specialty in spec_key or spec_key in normalized_specialty:
                specialists_data = spec_list
                break

    if not specialists_data:
        raise ValueError(f"Specialty not supported: {specialty}")

    # Filter specialists based on max_distance and insurance_accepted
    specialists = []
    for specialist in specialists_data:
        # Distance filter
        if specialist["distance"] > max_distance:
            continue

        # Insurance filter - be flexible with insurance matching
        if normalized_insurance is not None:
            specialist_insurance = specialist["insurance"]
            # Map insurance variations to match better
            specialist_normalized = normalize_insurance(specialist_insurance)
            insurance_match = (
                normalized_insurance == specialist_insurance
                or normalized_insurance == specialist_normalized
                or specialist_normalized == normalized_insurance
                or normalized_insurance.lower() in specialist_insurance.lower()
                or specialist_insurance.lower() in normalized_insurance.lower()
                or "blue cross" in normalized_insurance.lower()
                and "blue cross" in specialist_insurance.lower()
            )
            if not insurance_match:
                continue

        specialists.append(specialist)

    return {"location": location, "specialists": specialists}


import hashlib
from typing import Dict, Optional, Union


def find_nearest_hospital(
    location: str, radius: float = 50, specialty: Optional[str] = None
) -> Dict[str, Union[str, float]]:
    """Find the nearest hospital to a given location.

    Args:
        location: The coordinates to search around (e.g., '40.7128,-74.0060').
        radius: The radius in km around the location to search.
        specialty: Optional medical specialty of the hospital (e.g., 'cardiology', 'psychiatry').

    Returns:
        Dict containing:
            - hospital_id: Unique identifier of the nearest hospital
            - name: Name of the hospital
            - distance: Distance to the hospital in km
            - specialty: Specialty of the hospital if specified
    """

    # Simulated hospital data
    hospitals = {
        "40.7128,-74.0060": [
            {
                "name": "New York General Hospital",
                "distance": 5.2,
                "specialty": "cardiology",
            },
            {
                "name": "Downtown Health Center",
                "distance": 3.8,
                "specialty": "psychiatry",
            },
        ],
        "34.0522,-118.2437": [
            {
                "name": "Los Angeles Medical Center",
                "distance": 10.1,
                "specialty": "cardiology",
            },
            {"name": "Westside Hospital", "distance": 7.5, "specialty": "orthopedics"},
        ],
    }

    if location not in hospitals:
        raise ValueError(f"Location not supported: {location}")

    # Filter hospitals by specialty if provided
    filtered_hospitals = [
        hospital
        for hospital in hospitals[location]
        if specialty is None or hospital["specialty"] == specialty
    ]

    if not filtered_hospitals:
        raise ValueError(f"No hospitals found with specialty: {specialty}")

    # Find the nearest hospital within the specified radius
    nearest_hospital = min(
        (hospital for hospital in filtered_hospitals if hospital["distance"] <= radius),
        key=lambda h: h["distance"],
        default=None,
    )

    if nearest_hospital is None:
        raise ValueError(f"No hospitals found within {radius} km radius")

    # Generate a unique hospital ID using a hash
    hospital_id = hashlib.sha256(
        f"{nearest_hospital['name']}{location}".encode()
    ).hexdigest()[:8]

    return {
        "hospital_id": hospital_id,
        "name": nearest_hospital["name"],
        "distance": nearest_hospital["distance"],
        "specialty": nearest_hospital["specialty"],
    }


from typing import Dict, Union


def get_autoclave_config() -> Dict[str, Union[float, int, bool, str]]:
    """Retrieve current autoclave configuration settings.

    Returns:
        Dict containing:
            - goalTemperature: Target temperature setting in Celsius
            - timerMinutes: Configured cycle duration in minutes
            - useVacuum: Whether vacuum is enabled for the cycle
            - cycle_complete: Boolean indicating if the current cycle is finished
            - time_remaining: Minutes remaining in current cycle (0 if complete)
    """
    import hashlib

    # Simulate configuration data with some variability
    config_hash = hashlib.md5("autoclave_config".encode()).hexdigest()

    goal_temperature = int(config_hash[:2], 16) % 50 + 121  # 121 to 170 Celsius
    timer_minutes = int(config_hash[2:4], 16) % 60 + 15  # 15 to 74 minutes
    use_vacuum = int(config_hash[4], 16) % 2 == 0  # Boolean

    # Simulate cycle completion status - key for the use case
    cycle_progress = int(config_hash[5:7], 16) % 100
    cycle_complete = cycle_progress > 85  # 85% chance cycle is complete
    time_remaining = 0 if cycle_complete else (cycle_progress % 30)

    return {
        "goalTemperature": float(goal_temperature),
        "timerMinutes": float(timer_minutes),
        "useVacuum": use_vacuum,
        "cycle_complete": cycle_complete,
        "time_remaining": float(time_remaining),
    }


def get_autoclave_status() -> Dict[str, Union[float, int, bool, str]]:
    """Retrieve current status of the autoclave including internal temperature, runtime, vacuum status, and whether it's running.

    Returns:
        Dict containing:
            - temperature: Current internal temperature in Celsius
            - runtime: Total runtime in minutes
            - vacuum_status: Status of the vacuum ('optimal', 'suboptimal', 'failed')
            - is_running: Boolean indicating if the autoclave is currently running
    """

    # Simulated sample data
    temperature = 121.5  # in Celsius
    runtime = 45  # in minutes
    vacuum_status = "optimal"
    is_running = True

    return {
        "temperature": temperature,
        "runtime": runtime,
        "vacuum_status": vacuum_status,
        "is_running": is_running,
    }


from datetime import datetime
from typing import Dict, List, Literal, Optional, Union


def get_activity(
    id: Optional[int] = 0,
    activity_type: Optional[str] = None,
    start_date_time: Optional[str] = None,
    end_date_time: Optional[str] = None,
) -> Dict[str, Union[int, str, List[Dict[str, Union[int, str]]]]]:
    """Retrieves the details of one or more fitness activities.

    Args:
        id: The ID of the activity to retrieve
        activity_type: The type of activities to retrieve. Can specify multiple with | separator
        start_date_time: Start date and time of activities to retrieve, in UTC format
        end_date_time: End date and time of activities to retrieve, in UTC format

    Returns:
        Dict containing:
            - id: The ID of the activity
            - activity_type: The type of the activity
            - start_date_time: Start date and time of the activity
            - end_date_time: End date and time of the activity
            - details: List of activities with their details
    """

    # Sample data for demonstration purposes
    sample_activities = [
        {
            "id": 1,
            "activity_type": "RUN",
            "start_date_time": "2025-08-12T09:00:00+01:00",
            "end_date_time": "2025-08-12T10:00:00+01:00",
        },
        {
            "id": 2,
            "activity_type": "CYCLE",
            "start_date_time": "2025-08-13T11:00:00+01:00",
            "end_date_time": "2025-08-13T12:30:00+01:00",
        },
        {
            "id": 3,
            "activity_type": "SWIM",
            "start_date_time": "2025-08-14T14:00:00+01:00",
            "end_date_time": "2025-08-14T15:00:00+01:00",
        },
    ]

    # Filter activities based on provided parameters
    filtered_activities = [
        activity
        for activity in sample_activities
        if (id == 0 or activity["id"] == id)
        and (
            activity_type is None
            or activity["activity_type"] in activity_type.split("|")
        )
        and (
            start_date_time is None
            or datetime.fromisoformat(activity["start_date_time"])
            >= datetime.fromisoformat(start_date_time)
        )
        and (
            end_date_time is None
            or datetime.fromisoformat(activity["end_date_time"])
            <= datetime.fromisoformat(end_date_time)
        )
    ]

    if not filtered_activities:
        raise ValueError("No activities found matching the criteria")

    return {
        "id": id,
        "activity_type": activity_type or "ALL",
        "start_date_time": start_date_time or "N/A",
        "end_date_time": end_date_time or "N/A",
        "details": filtered_activities,
    }


from typing import Dict


def get_current_steps() -> Dict[str, int]:
    """Returns the number of steps recorded so far today.

    Returns:
        Dict containing:
            - steps: Number of steps recorded today
    """
    # Simulate step count using a hash-based generation for consistency
    import datetime
    import hashlib

    # Use the current date to generate a consistent step count for today
    today = datetime.date.today().isoformat()
    hash_object = hashlib.sha256(today.encode())
    hash_digest = hash_object.hexdigest()

    # Convert the hash to an integer and scale it to a realistic step count
    step_count = int(hash_digest[:8], 16) % 20000  # Simulate up to 20,000 steps

    return {"steps": step_count}


from typing import Dict, Literal


def get_gene_sequence(
    gene_symbol: str, sequence_type: Literal["dna", "protein"]
) -> Dict[str, str]:
    """Returns the gene's sequence in the requested form.

    Args:
        gene_symbol: Official gene symbol.
        sequence_type: Type of sequence to fetch ('dna' or 'protein').

    Returns:
        Dict containing:
            - gene_symbol: The official gene symbol
            - sequence_type: The type of sequence requested
            - sequence: The gene sequence in the requested form
    """
    # Mock data for demonstration purposes
    dna_sequences = {
        "BRCA1": "ATGCGTACCTGACTGACCTG",
        "TP53": "ATGTTCCGAGGAGCCGCAGT",
        "EGFR": "ATGCGACCCTCCGGGACGGA",
        "HBA1": "ATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGG",
    }
    protein_sequences = {
        "BRCA1": "MRTDMT",
        "TP53": "MFRGSG",
        "EGFR": "MRPPRG",
        "HBA1": "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR",
    }

    if sequence_type == "dna":
        sequence = dna_sequences.get(gene_symbol)
    elif sequence_type == "protein":
        sequence = protein_sequences.get(gene_symbol)
    else:
        raise ValueError(f"Unsupported sequence type: {sequence_type}")

    if sequence is None:
        raise ValueError(f"Gene symbol not supported: {gene_symbol}")

    return {
        "gene_symbol": gene_symbol,
        "sequence_type": sequence_type,
        "sequence": sequence,
    }


from typing import Dict, Literal


def get_skin_exposure_risk(
    uv_index: int,
    skin_type: Literal["I", "II", "III", "IV", "V", "VI"],
    duration_minutes: int,
) -> Dict[str, Union[str, int]]:
    """Estimate skin exposure risk based on UV index, skin type, and duration.

    Args:
        uv_index: UV index value
        skin_type: Skin type of the user (e.g., I, II, III, IV, V, VI)
        duration_minutes: Time of sun exposure in minutes

    Returns:
        Dict containing:
            - risk_level: Estimated risk level ('low', 'moderate', 'high', 'very high', 'extreme')
            - recommended_protection: Suggested protection measures
    """
    if uv_index < 0 or uv_index > 11:
        raise ValueError("UV index must be between 0 and 11")

    skin_type_sensitivity = {
        "I": 1.0,
        "II": 0.8,
        "III": 0.6,
        "IV": 0.4,
        "V": 0.2,
        "VI": 0.1,
    }

    if skin_type not in skin_type_sensitivity:
        raise ValueError(f"Unsupported skin type: {skin_type}")

    # Calculate risk factor based on UV index, skin type sensitivity, and duration
    risk_factor = uv_index * skin_type_sensitivity[skin_type] * (duration_minutes / 60)

    if risk_factor < 2:
        risk_level = "low"
        recommended_protection = "No protection needed"
    elif risk_factor < 5:
        risk_level = "moderate"
        recommended_protection = "Wear sunglasses on bright days"
    elif risk_factor < 8:
        risk_level = "high"
        recommended_protection = "Use sunscreen SPF 30+ and wear a hat"
    elif risk_factor < 11:
        risk_level = "very high"
        recommended_protection = "Seek shade and wear protective clothing"
    else:
        risk_level = "extreme"
        recommended_protection = "Avoid sun exposure between 10 AM and 4 PM"

    return {
        "risk_level": risk_level,
        "recommended_protection": recommended_protection,
    }


from typing import Dict, Literal, Union


def get_species_toxicity(
    species_name: str, target: Literal["cats", "dogs", "humans", "livestock"]
) -> Dict[str, Union[str, bool, list]]:
    """Return toxicity information for a species for a specific target.

    Args:
        species_name: Botanical or common name of the species
        target: Who/what is exposed (cats, dogs, humans, livestock)

    Returns:
        Dict containing:
            - species_name: Name of the species
            - target: Target of exposure
            - is_toxic: Boolean indicating if the species is toxic to the target
            - symptoms: List of symptoms if toxic, empty if not toxic
    """

    # Mock data for toxicity information
    toxicity_data = {
        ("Lilium", "cats"): {
            "is_toxic": True,
            "symptoms": ["vomiting", "lethargy", "kidney failure"],
        },
        ("Lilium", "dogs"): {"is_toxic": False, "symptoms": []},
        ("Ricinus communis", "humans"): {
            "is_toxic": True,
            "symptoms": ["abdominal pain", "vomiting", "diarrhea"],
        },
        ("Ricinus communis", "livestock"): {
            "is_toxic": True,
            "symptoms": ["weakness", "tremors", "difficulty breathing"],
        },
        ("Aloe vera", "cats"): {"is_toxic": True, "symptoms": ["vomiting", "diarrhea"]},
        ("Aloe vera", "dogs"): {"is_toxic": True, "symptoms": ["vomiting", "diarrhea"]},
        ("Aloe vera", "humans"): {"is_toxic": False, "symptoms": []},
        ("Aloe vera", "livestock"): {"is_toxic": False, "symptoms": []},
    }

    key = (species_name, target)
    if key not in toxicity_data:
        raise ValueError(
            f"Toxicity information not available for species '{species_name}' and target '{target}'"
        )

    toxicity_info = toxicity_data[key]
    return {
        "species_name": species_name,
        "target": target,
        "is_toxic": toxicity_info["is_toxic"],
        "symptoms": toxicity_info["symptoms"],
    }


from typing import Dict


def get_step_count(date: str) -> Dict[str, int]:
    """Returns the number of steps recorded on a given day.

    Args:
        date: Date of requested day in day–month–year format (e.g. '01-01-2023')

    Returns:
        Dict containing:
            - date: The requested date
            - steps: Number of steps recorded on that date
    """

    # Simulate step count data using a hash-based approach for consistency
    import hashlib

    # Generate a pseudo-random number of steps based on the date
    hash_object = hashlib.md5(date.encode())
    hash_digest = hash_object.hexdigest()
    steps = int(hash_digest[:8], 16) % 20000  # Limit steps to a realistic range

    return {
        "date": date,
        "steps": steps,
    }


from datetime import datetime
from typing import Dict, Literal, Union


def log_activity(
    activity_type: Literal[
        "RUN",
        "TRAIL_RUN",
        "VIRTUAL_RUN",
        "WALK",
        "HIKE",
        "CYCLE",
        "SWIM",
        "YOGA",
        "WEIGHT_TRAINING",
    ],
    duration: int = 0,
    distance: float = 0.0,
    date_time: str = None,
) -> Dict[str, Union[str, int, float]]:
    """Record the details of a fitness activity.

    Args:
        activity_type: The type of activity to record.
        duration: Duration of activity in seconds.
        distance: Distance of activity in km. Not applicable to YOGA and WEIGHT_TRAINING.
        date_time: Start date and time of activity in UTC format.

    Returns:
        Dict containing:
            - activity_type: The type of activity recorded.
            - duration: Duration of the activity in seconds.
            - distance: Distance of the activity in km.
            - date_time: Start date and time of the activity in UTC format.
            - calories_burned: Estimated calories burned during the activity.
    """
    if date_time is None:
        raise ValueError("date_time is required and cannot be None")

    try:
        datetime.fromisoformat(date_time)
    except ValueError:
        raise ValueError(
            "Invalid date_time format. Expected format: YYYY-MM-DDTHH:MM:SS+HH:MM"
        )

    if activity_type in ["YOGA", "WEIGHT_TRAINING"] and distance != 0.0:
        raise ValueError(f"Distance should be 0 for {activity_type} activities")

    # Simulate calorie calculation based on activity type and duration
    calorie_factor = {
        "RUN": 0.1,
        "TRAIL_RUN": 0.12,
        "VIRTUAL_RUN": 0.09,
        "WALK": 0.05,
        "HIKE": 0.08,
        "CYCLE": 0.07,
        "SWIM": 0.13,
        "YOGA": 0.03,
        "WEIGHT_TRAINING": 0.06,
    }

    calories_burned = duration * calorie_factor.get(activity_type, 0)

    return {
        "activity_type": activity_type,
        "duration": duration,
        "distance": distance,
        "date_time": date_time,
        "calories_burned": round(calories_burned, 2),
    }


from typing import Dict, Union


def log_exercise(
    exercise_name: str, workout_id: str, weight: float, sets: int
) -> Dict[str, Union[str, float, int]]:
    """Saves a specific exercise to a workout log.

    Args:
        exercise_name: The name of the exercise performed.
        workout_id: The workout during which the exercise was performed.
        weight: The total amount of weight (kg) used across all reps and sets.
        sets: The number of sets performed.

    Returns:
        Dict containing:
            - exercise_name: Name of the exercise
            - workout_id: ID of the workout session
            - weight: Weight used in kg
            - sets: Number of sets performed
    """
    if not exercise_name:
        raise ValueError("Exercise name must be provided.")
    if not workout_id:
        raise ValueError("Workout ID must be provided.")
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    if sets <= 0:
        raise ValueError("Sets must be a positive integer.")

    # Simulating a log entry with hash-based generation for consistency
    log_entry = {
        "exercise_name": exercise_name,
        "workout_id": workout_id,
        "weight": weight,
        "sets": sets,
    }

    return log_entry


import hashlib
from typing import Dict, Union


def log_workout(
    date: str, time: str, workout_name: str, user_rating: float
) -> Dict[str, Union[str, int]]:
    """Saves an overview of workout data and returns a workout ID.

    Args:
        date: The date the workout was performed.
        time: The time the workout was performed.
        workout_name: The name of the workout (e.g., 'upper body').
        user_rating: The rating the user gave the workout, can be 1-5.

    Returns:
        Dict containing:
            - workout_id: A unique identifier for the workout log.
    """
    if not (1 <= user_rating <= 5):
        raise ValueError("user_rating must be between 1 and 5")

    workout_data = f"{date}-{time}-{workout_name}-{user_rating}"
    workout_id = int(hashlib.sha256(workout_data.encode()).hexdigest(), 16) % (10**8)

    return {"workout_id": workout_id}


from typing import Dict, Union


def recommend_sun_protection(
    uv_index: int, duration_minutes: int
) -> Dict[str, Union[str, List[str]]]:
    """Suggest sun protection measures based on UV index and exposure time.

    Args:
        uv_index: Current or forecasted UV index
        duration_minutes: Time of sun exposure in minutes

    Returns:
        Dict containing:
            - risk_level: The level of risk associated with the UV exposure
            - recommendations: List of recommended sun protection measures
    """
    if uv_index < 0 or duration_minutes < 0:
        raise ValueError("UV index and duration must be non-negative")

    if uv_index <= 2:
        risk_level = "Low"
        recommendations = ["Wear sunglasses on bright days"]
    elif 3 <= uv_index <= 5:
        risk_level = "Moderate"
        recommendations = [
            "Stay in shade near midday",
            "Wear sunglasses",
            "Use SPF 30+ sunscreen",
        ]
    elif 6 <= uv_index <= 7:
        risk_level = "High"
        recommendations = [
            "Reduce time in the sun between 10 a.m. and 4 p.m.",
            "Cover up with clothing and a wide-brimmed hat",
            "Use SPF 30+ sunscreen",
        ]
    elif 8 <= uv_index <= 10:
        risk_level = "Very High"
        recommendations = [
            "Minimize sun exposure between 10 a.m. and 4 p.m.",
            "Seek shade",
            "Wear protective clothing, a wide-brimmed hat, and sunglasses",
            "Use SPF 30+ sunscreen",
        ]
    else:
        risk_level = "Extreme"
        recommendations = [
            "Avoid sun exposure between 10 a.m. and 4 p.m.",
            "Seek shade",
            "Wear protective clothing, a wide-brimmed hat, and sunglasses",
            "Use SPF 50+ sunscreen",
        ]

    if duration_minutes > 60:
        recommendations.append("Reapply sunscreen every 2 hours")

    return {"risk_level": risk_level, "recommendations": recommendations}


from typing import Dict, Union


def record_food(
    name: str,
    weight: int = 0,
    count: Union[int, None] = None,
    portions: Union[int, None] = None,
) -> Dict[str, Union[str, int]]:
    """Records an item of food consumed in the daily nutrition tracker.

    Args:
        name: Name of the food item consumed
        weight: Weight of the food item consumed in grams where measured
        count: Number of the food items consumed where individual units
        portions: Number of portions of the food items consumed where standard portion known

    Returns:
        Dict containing:
            - name: Name of the food item
            - weight: Total weight in grams
            - count: Total count of items consumed
            - portions: Total portions consumed
    """
    if not name:
        raise ValueError("Food name must be provided")

    if weight < 0:
        raise ValueError("Weight cannot be negative")

    if count is not None and count < 0:
        raise ValueError("Count cannot be negative")

    if portions is not None and portions < 0:
        raise ValueError("Portions cannot be negative")

    # Simulate a realistic calculation of total weight based on count and portions
    standard_weight_per_item = 100  # Assume each item weighs 100 grams if not specified
    standard_weight_per_portion = (
        50  # Assume each portion weighs 50 grams if not specified
    )

    total_weight = weight
    if count is not None:
        total_weight += count * standard_weight_per_item
    if portions is not None:
        total_weight += portions * standard_weight_per_portion

    return {
        "name": name,
        "weight": total_weight,
        "count": count if count is not None else 0,
        "portions": portions if portions is not None else 0,
    }


def reset_autoclave() -> Dict[str, Union[str, bool]]:
    """Reset the autoclave to its default state and clear configuration.

    Returns:
        Dict containing:
            - status: Status message indicating the reset operation result
            - success: Boolean indicating if the reset was successful
    """
    # Simulate the reset operation
    reset_successful = True  # Assume the reset is always successful in this mock

    if not reset_successful:
        raise RuntimeError("Failed to reset the autoclave due to an internal error.")

    return {
        "status": "Autoclave reset to default state successfully.",
        "success": reset_successful,
    }


from typing import Dict, Union


def set_autoclave_config(
    goalTemperature: float,
    timerMinutes: Union[float, None] = None,
    useVacuum: bool = True,
) -> Dict[str, Union[float, bool, str]]:
    """Set the configuration for an autoclave cycle.

    Args:
        goalTemperature: Target temperature in degrees Celsius (120 to 170).
        timerMinutes: Duration in minutes for the autoclave cycle.
        useVacuum: Whether to use vacuum during the cycle.

    Returns:
        Dict containing:
            - status: Configuration status message
            - goalTemperature: Set target temperature
            - timerMinutes: Set duration in minutes
            - useVacuum: Vacuum usage preference
    """
    if not (120 <= goalTemperature <= 170):
        raise ValueError("goalTemperature must be between 120 and 170 degrees Celsius")

    if timerMinutes is not None and timerMinutes <= 0:
        raise ValueError("timerMinutes must be a positive number")

    return {
        "status": "Configuration set successfully",
        "goalTemperature": goalTemperature,
        "timerMinutes": timerMinutes if timerMinutes is not None else 60,
        "useVacuum": useVacuum,
    }


def start_autoclave() -> Dict[str, Union[str, int, bool]]:
    """Initiate autoclave cycle with current configuration.

    Returns:
        Dict containing:
            - status: Status of the autoclave cycle initiation
            - cycle_time: Estimated cycle time in minutes
            - temperature: Operating temperature in Celsius
            - pressure: Operating pressure in PSI
            - success: Boolean indicating if the cycle started successfully
    """
    import hashlib

    # Simulate a consistent but varied response using a hash-based approach
    config_hash = hashlib.md5("current_configuration".encode()).hexdigest()
    cycle_time = int(config_hash[:2], 16) % 60 + 30  # 30 to 89 minutes
    temperature = int(config_hash[2:4], 16) % 50 + 121  # 121 to 170 Celsius
    pressure = int(config_hash[4:6], 16) % 20 + 15  # 15 to 34 PSI

    # Assume the cycle starts successfully if the pressure is within a certain range
    success = 20 <= pressure <= 30

    return {
        "status": "Cycle initiated" if success else "Cycle failed to start",
        "cycle_time": cycle_time,
        "temperature": temperature,
        "pressure": pressure,
        "success": success,
    }


def stop_autoclave() -> Dict[str, Union[str, bool]]:
    """Stop the autoclave process immediately.

    Returns:
        Dict containing:
            - status: Status of the autoclave after attempting to stop
            - stopped: Boolean indicating if the autoclave was successfully stopped
    """
    # Simulating the process of stopping an autoclave
    # In a real-world scenario, this would involve hardware communication
    import random

    # Randomly decide if the autoclave was successfully stopped
    success = random.choice([True, False])

    if success:
        return {"status": "Autoclave stopped successfully", "stopped": True}
    else:
        return {"status": "Failed to stop the autoclave", "stopped": False}


from typing import Dict


def update_patient_records(
    medical_number: str, update_notes: str, updated_by: str
) -> Dict[str, str]:
    """Update the patient's medical records with treatment details.

    Args:
        medical_number: Unique medical number assigned to the patient
        update_notes: Details of the treatment or prescription update
        updated_by: Name of the medical professional updating the records

    Returns:
        Dict containing:
            - medical_number: The patient's medical number
            - status: Status of the update operation
            - last_updated_by: Name of the medical professional who last updated the record
    """
    if not medical_number or not update_notes or not updated_by:
        raise ValueError("All parameters must be provided and non-empty.")

    # Simulate a database update operation
    # In a real-world scenario, this would involve database access code
    # Here, we mock the operation with a simple hash-based check for demonstration
    if hash(medical_number) % 2 == 0:
        status = "success"
    else:
        status = "failure"

    return {
        "medical_number": medical_number,
        "status": status,
        "last_updated_by": updated_by,
    }
