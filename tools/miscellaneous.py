# Miscellaneous Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def employer_visa_status_requirements(
    employer_name: str, city: str
) -> Dict[str, Union[str, bool]]:
    """Check visa status requirements of an employer in the UK.

    Args:
        employer_name: Name of the employer
        city: Code of the city where the role is based

    Returns:
        Dict containing:
            - employer_name: Name of the employer
            - city: City code
            - visa_sponsorship_available: Boolean indicating if visa sponsorship is available
            - skilled_worker_visa: Boolean indicating if the employer can sponsor a Skilled Worker visa
    """

    def fuzzy_match_employer(search_employer: str, employer_list: List[str]) -> str:
        """Find the best matching employer using fuzzy matching"""
        search_lower = search_employer.lower().strip()

        # Direct exact match
        for employer in employer_list:
            if employer.lower() == search_lower:
                return employer

        # Partial match - search employer contains employer name or vice versa
        for employer in employer_list:
            employer_lower = employer.lower()
            if search_lower in employer_lower or employer_lower in search_lower:
                return employer

        # Tech company variations
        tech_variants = [
            "tech",
            "technology",
            "corp",
            "corporation",
            "ltd",
            "limited",
            "inc",
        ]
        if any(variant in search_lower for variant in tech_variants):
            for employer in employer_list:
                if any(variant in employer.lower() for variant in tech_variants):
                    return employer

        return None

    def fuzzy_match_city(search_city: str, city_list: List[str]) -> str:
        """Find the best matching city using fuzzy matching"""
        search_lower = search_city.lower().strip()

        # Direct exact match
        for city_code in city_list:
            if city_code.lower() == search_lower:
                return city_code

        # City code mappings
        city_mappings = {
            "london": "LDN",
            "manchester": "MAN",
            "birmingham": "BIR",
            "leeds": "LEE",
            "glasgow": "GLA",
            "edinburgh": "EDI",
            "bristol": "BRI",
            "liverpool": "LIV",
            "sheffield": "SHE",
            "cardiff": "CAR",
        }

        # Check if search term maps to a city code
        mapped_city = city_mappings.get(search_lower)
        if mapped_city and mapped_city in city_list:
            return mapped_city

        # Partial match
        for city_code in city_list:
            city_lower = city_code.lower()
            if search_lower in city_lower or city_lower in search_lower:
                return city_code

        return None

    # Expanded simulated data with more employers and cities
    sample_data = {
        ("TechCorp", "LDN"): {
            "visa_sponsorship_available": True,
            "skilled_worker_visa": True,
        },
        ("HealthPlus", "MAN"): {
            "visa_sponsorship_available": False,
            "skilled_worker_visa": False,
        },
        ("EduWorld", "BIR"): {
            "visa_sponsorship_available": True,
            "skilled_worker_visa": False,
        },
        ("SmithTech", "LDN"): {
            "visa_sponsorship_available": True,
            "skilled_worker_visa": True,
        },
        ("DataCorp", "LDN"): {
            "visa_sponsorship_available": True,
            "skilled_worker_visa": False,
        },
        ("FinanceGroup", "LDN"): {
            "visa_sponsorship_available": False,
            "skilled_worker_visa": False,
        },
        ("GlobalTech", "MAN"): {
            "visa_sponsorship_available": True,
            "skilled_worker_visa": True,
        },
        ("StartupLtd", "BIR"): {
            "visa_sponsorship_available": False,
            "skilled_worker_visa": True,
        },
    }

    # Get all available employers and cities
    all_employers = list(set(key[0] for key in sample_data.keys()))
    all_cities = list(set(key[1] for key in sample_data.keys()))

    # Try fuzzy matching
    matched_employer = fuzzy_match_employer(employer_name, all_employers)
    matched_city = fuzzy_match_city(city, all_cities)

    # Use original values if no fuzzy match found
    final_employer = matched_employer or employer_name
    final_city = matched_city or city

    key = (final_employer, final_city)
    if key in sample_data:
        return {
            "employer_name": final_employer,
            "city": final_city,
            **sample_data[key],
        }

    # Generate visa sponsorship data based on employer and city if no match
    # Use hash to make it consistent
    employer_hash = hash(final_employer.lower()) % 100
    city_hash = hash(final_city.lower()) % 100

    # Tech companies and London are more likely to sponsor visas
    tech_keywords = ["tech", "software", "data", "digital", "ai", "corp"]
    is_tech = any(keyword in final_employer.lower() for keyword in tech_keywords)
    is_london = "ldn" in final_city.lower() or "london" in final_city.lower()

    # Calculate probabilities
    visa_prob = 0.3  # Base 30% chance
    if is_tech:
        visa_prob += 0.4  # Tech companies +40%
    if is_london:
        visa_prob += 0.2  # London +20%

    skilled_prob = visa_prob * 0.8  # Skilled worker visa slightly less likely

    visa_sponsorship = (employer_hash + city_hash) % 100 < (visa_prob * 100)
    skilled_worker = (employer_hash + city_hash + 10) % 100 < (skilled_prob * 100)

    return {
        "employer_name": final_employer,
        "city": final_city,
        "visa_sponsorship_available": visa_sponsorship,
        "skilled_worker_visa": skilled_worker,
    }


from typing import Dict, Union


def evaluate_patron(patron_id: str) -> Dict[str, Union[str, bool]]:
    """Evaluate a patron for unlawful, disruptive, or overly drunk behavior.

    Args:
        patron_id: The ID number or barcode to verify.

    Returns:
        Dict containing:
            - patron_id: The ID of the patron
            - is_unlawful: Whether the patron is engaging in unlawful behavior
            - is_disruptive: Whether the patron is being disruptive
            - is_overly_drunk: Whether the patron is overly drunk
    """
    # Simulated hash-based evaluation for consistent results
    hash_value = hash(patron_id) % 100

    is_unlawful = hash_value < 10
    is_disruptive = 10 <= hash_value < 30
    is_overly_drunk = 30 <= hash_value < 50

    return {
        "patron_id": patron_id,
        "is_unlawful": is_unlawful,
        "is_disruptive": is_disruptive,
        "is_overly_drunk": is_overly_drunk,
    }


from typing import Dict


def get_church_service_preacher(
    church_name: str, city: str, street: str
) -> Dict[str, str]:
    """Get information about the preacher of the upcoming church service.

    Args:
        church_name: The name of the church
        city: The city where the church is located
        street: The street where the church is located

    Returns:
        Dict containing:
            - preacher_name: Name of the preacher
            - sermon_title: Title of the upcoming sermon
            - service_time: Time of the upcoming service
    """

    # Generate a hash-based index to simulate varied sample data
    index = hash((church_name, city, street)) % 3

    sample_data = [
        {
            "preacher_name": "Rev. John Smith",
            "sermon_title": "Faith and Hope",
            "service_time": "10:00 AM",
        },
        {
            "preacher_name": "Pastor Emily Johnson",
            "sermon_title": "Love and Compassion",
            "service_time": "11:30 AM",
        },
        {
            "preacher_name": "Father Michael Brown",
            "sermon_title": "Grace and Forgiveness",
            "service_time": "9:00 AM",
        },
    ]

    return sample_data[index]


import hashlib
from typing import Dict, Union


def get_next_grooming_appointment(
    pet_name: str, owner_name: str
) -> Dict[str, Union[str, None]]:
    """Find the next scheduled grooming appointment for a pet.

    Args:
        pet_name: The pet's name
        owner_name: The pet owner's name

    Returns:
        Dict containing:
            - pet_name: The name of the pet
            - owner_name: The name of the pet owner
            - appointment_date: The date of the next grooming appointment in 'YYYY-MM-DD' format
            - appointment_time: The time of the next grooming appointment in 'HH:MM AM/PM' format
    """

    if not pet_name or not owner_name:
        raise ValueError("Both pet_name and owner_name are required")

    # Generate a consistent but varied appointment date and time based on the hash of the inputs
    hash_input = f"{pet_name}{owner_name}".encode("utf-8")
    hash_digest = hashlib.sha256(hash_input).hexdigest()

    # Use the hash to generate a pseudo-random date and time
    year = 2023
    month = int(hash_digest[:2], 16) % 12 + 1
    day = int(hash_digest[2:4], 16) % 28 + 1
    hour = int(hash_digest[4:6], 16) % 12 + 1
    minute = int(hash_digest[6:8], 16) % 60
    am_pm = "AM" if int(hash_digest[8:10], 16) % 2 == 0 else "PM"

    appointment_date = f"{year}-{month:02d}-{day:02d}"
    appointment_time = f"{hour:02d}:{minute:02d} {am_pm}"

    return {
        "pet_name": pet_name,
        "owner_name": owner_name,
        "appointment_date": appointment_date,
        "appointment_time": appointment_time,
    }


from typing import Dict, Union


def get_preacher_info(preacher_id: str) -> Dict[str, Union[str, int, list]]:
    """Get information about a preacher.

    Args:
        preacher_id: The ID of the preacher

    Returns:
        Dict containing:
            - name: Name of the preacher
            - age: Age of the preacher
            - sermons: List of sermon titles given by the preacher
    """

    sample_data = {
        "preacher_001": {
            "name": "John Doe",
            "age": 45,
            "sermons": ["Faith and Hope", "The Power of Prayer"],
        },
        "preacher_30": {
            "name": "Jane Smith",
            "age": 50,
            "sermons": ["Love and Compassion", "Living with Purpose"],
        },
        "preacher_29": {
            "name": "Samuel Green",
            "age": 60,
            "sermons": ["Grace and Mercy", "Walking in Faith"],
        },
        "preacher_17": {
            "name": "Samuel Clemens",
            "age": 82,
            "sermons": ["Grace and Mercy", "The Power of Prayer"],
        },
    }

    if preacher_id not in sample_data:
        raise ValueError(f"Preacher ID not found: {preacher_id}")

    return sample_data[preacher_id]


from typing import Dict, Literal


def rank_stats_by_uuid(
    uuid: str, region: Literal["North America", "Europe", "Asia"]
) -> Dict[str, int]:
    """Get the ranked stats for the account with the given uuid.

    Args:
        uuid: The uuid of the account to grab.
        region: The region the account is in. Options are North America, Europe, or Asia.

    Returns:
        Dict containing:
            - uuid: The account uuid
            - region: The region of the account
            - rank: The rank of the account between 1 and 20
    """

    if not uuid or not isinstance(uuid, str):
        raise ValueError("Invalid uuid provided.")

    if region not in ["North America", "Europe", "Asia"]:
        raise ValueError("Invalid region provided.")

    # Simulate rank generation using a hash-based approach for consistency
    hash_value = hash(uuid + region)
    rank = abs(hash_value) % 20 + 1  # Ensure rank is between 1 and 20

    return {
        "uuid": uuid,
        "region": region,
        "rank": rank,
    }


from typing import Dict


def register(username: str, password: str) -> Dict[str, str]:
    """Register a new user with a username and a password.

    Args:
        username: The username for the new user, e.g., an email or phone number.
        password: The base64-encoded password SHA-256 hash.

    Returns:
        Dict containing:
            - message: Confirmation message of registration
            - user_id: Unique identifier for the registered user
    """

    if not username or not password:
        raise ValueError("Both username and password are required.")

    # Simulate user ID generation using a hash-based approach
    import hashlib

    user_id = hashlib.sha256(username.encode()).hexdigest()[:8]

    # Simulate a registration confirmation message
    return {"message": f"User {username} registered successfully.", "user_id": user_id}


from typing import Dict, List, Literal


def search_indeed(
    start: str,
    end: str,
    country: Literal["Canada", "USA", "UK", "Netherlands", "Germany"],
    city: str = "London",
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Search Indeed.com for jobs within a specified time range and location.

    Args:
        start: Timestamp of jobs posted from (e.g., '2023-01-01T00:00:00Z')
        end: Timestamp of jobs posted until (e.g., '2023-01-31T23:59:59Z')
        country: Country where the job is located. Allowed values: ['Canada', 'USA', 'UK', 'Netherlands', 'Germany']
        city: City name, case sensitive. Optional. Default 'London'.

    Returns:
        Dict containing:
            - country: Country where the job search was performed
            - city: City where the job search was performed
            - jobs: List of job postings with title and company
    """

    def fuzzy_match_location(
        search_country: str, search_city: str, job_data: Dict
    ) -> tuple:
        """Find the best matching country/city combination using fuzzy matching"""
        search_country_lower = search_country.lower().strip()
        search_city_lower = search_city.lower().strip()

        # Direct exact match
        for country, city in job_data.keys():
            if (
                country.lower() == search_country_lower
                and city.lower() == search_city_lower
            ):
                return (country, city)

        # Country variations
        country_mappings = {
            "usa": "USA",
            "us": "USA",
            "united states": "USA",
            "america": "USA",
            "uk": "UK",
            "united kingdom": "UK",
            "britain": "UK",
            "england": "UK",
            "canada": "Canada",
            "netherlands": "Netherlands",
            "holland": "Netherlands",
            "germany": "Germany",
            "deutschland": "Germany",
        }

        # City variations
        city_mappings = {
            "london": "London",
            "toronto": "Toronto",
            "new york": "New York",
            "nyc": "New York",
            "manhattan": "New York",
            "amsterdam": "Amsterdam",
            "berlin": "Berlin",
        }

        # Normalize country
        normalized_country = country_mappings.get(search_country_lower, search_country)
        normalized_city = city_mappings.get(search_city_lower, search_city)

        # Try with normalized values
        for country, city in job_data.keys():
            if country == normalized_country and city == normalized_city:
                return (country, city)

        # Try partial matching for city within same country
        for country, city in job_data.keys():
            if country == normalized_country:
                city_lower = city.lower()
                if search_city_lower in city_lower or city_lower in search_city_lower:
                    return (country, city)

        # Find any match for the country and use default city
        for country, city in job_data.keys():
            if country == normalized_country:
                return (country, city)

        return None

    if country not in ["Canada", "USA", "UK", "Netherlands", "Germany"]:
        raise ValueError(f"Country not supported: {country}")

    # Expanded mock job data with more locations and job types
    job_data = {
        ("Canada", "Toronto"): [
            {"title": "Software Engineer", "company": "TechCorp"},
            {"title": "Data Analyst", "company": "DataWorks"},
            {"title": "Marketing Manager", "company": "BrandForce"},
        ],
        ("Canada", "Vancouver"): [
            {"title": "UX Designer", "company": "DesignStudio"},
            {"title": "Product Manager", "company": "StartupInc"},
        ],
        ("USA", "New York"): [
            {"title": "Project Manager", "company": "Business Inc."},
            {"title": "Graphic Designer", "company": "Creative Studio"},
            {"title": "Sales Representative", "company": "SalesPro"},
        ],
        ("USA", "Detroit"): [
            {"title": "Automotive Engineer", "company": "AutoTech"},
            {"title": "Manufacturing Supervisor", "company": "Industrial Corp"},
            {"title": "Quality Assurance Specialist", "company": "QualityFirst"},
        ],
        ("USA", "Los Angeles"): [
            {"title": "Entertainment Coordinator", "company": "Hollywood Studios"},
            {"title": "Social Media Manager", "company": "InfluencerHub"},
        ],
        ("UK", "London"): [
            {"title": "Marketing Specialist", "company": "MarketGenius"},
            {"title": "Financial Analyst", "company": "FinancePro"},
            {"title": "Weekend Driver", "company": "LogisticsSolutions"},
            {"title": "Delivery Coordinator", "company": "TransportPlus"},
        ],
        ("UK", "Manchester"): [
            {"title": "Software Developer", "company": "CodeWorks"},
            {"title": "Business Analyst", "company": "ConsultingFirm"},
        ],
        ("Netherlands", "Amsterdam"): [
            {"title": "UX Designer", "company": "DesignHub"},
            {"title": "Backend Developer", "company": "CodeBase"},
        ],
        ("Germany", "Berlin"): [
            {"title": "Product Manager", "company": "InnovateTech"},
            {"title": "Sales Executive", "company": "SalesForce"},
        ],
    }

    # Try fuzzy matching first
    matched_location = fuzzy_match_location(country, city, job_data)

    if matched_location:
        matched_country, matched_city = matched_location
        jobs = job_data[matched_location]
    else:
        # Generate jobs based on the search criteria if no match found
        hash_seed = hash(f"{country}{city}{start}{end}") % 100

        job_titles = [
            "Software Engineer",
            "Data Analyst",
            "Project Manager",
            "Marketing Specialist",
            "Sales Representative",
            "UX Designer",
            "Business Analyst",
            "Financial Analyst",
            "Product Manager",
            "Operations Coordinator",
        ]

        companies = [
            "TechCorp",
            "DataWorks",
            "Business Inc.",
            "Creative Studio",
            "MarketGenius",
            "FinancePro",
            "StartupInc",
            "ConsultingFirm",
            "InnovateTech",
            "GlobalSolutions",
        ]

        # Generate 2-3 jobs based on hash
        num_jobs = (hash_seed % 3) + 2
        jobs = []

        for i in range(num_jobs):
            job_hash = (hash_seed + i * 10) % 100
            title = job_titles[job_hash % len(job_titles)]
            company = companies[(job_hash + 5) % len(companies)]
            jobs.append({"title": title, "company": company})

        matched_country = country
        matched_city = city

    return {
        "country": matched_country,
        "city": matched_city,
        "jobs": jobs,
    }


from typing import Dict, List, Literal, Union


def add_player(
    name: str,
    date_of_birth: str,
    age_groups: List[Literal["U8", "U10", "U12", "U14", "U16", "U18", "Adult"]],
    gender: Literal["Male", "Female"],
    positions: List[Dict[str, Union[str, float]]],
    skill_level: float = 5,
    availability: bool = True,
) -> Dict[str, Union[str, List[str], List[Dict[str, Union[str, float]]], float, bool]]:
    """Add a new player to the team roster with their basic information.

    Args:
        name: Full name of the player
        date_of_birth: Player's date of birth in YYYY-MM-DD format
        age_groups: List of age groups the player is eligible for
        gender: Player's gender
        positions: List of positions the player can play with their skill level
        skill_level: Player skill level on a scale of 1-10
        availability: Whether the player is currently available for selection

    Returns:
        Dict containing:
            - name: Full name of the player
            - date_of_birth: Player's date of birth
            - age_groups: Eligible age groups
            - gender: Player's gender
            - positions: Positions and skill scores
            - skill_level: Overall skill level
            - availability: Current availability status
    """
    if not name or not date_of_birth:
        raise ValueError("Name and date of birth are required fields.")

    if not age_groups:
        raise ValueError("At least one age group must be specified.")

    if not positions:
        raise ValueError("At least one position must be specified.")

    for position in positions:
        if position["skill_score"] < 0 or position["skill_score"] > 10:
            raise ValueError("Skill score must be between 0 and 10.")

    return {
        "name": name,
        "date_of_birth": date_of_birth,
        "age_groups": age_groups,
        "gender": gender,
        "positions": positions,
        "skill_level": skill_level,
        "availability": availability,
    }


from typing import Dict, Union


def check_email_leak(email: str) -> Dict[str, Union[str, bool]]:
    """Check if a password has been leaked for an email address.

    Args:
        email: Email to check for leaks for

    Returns:
        Dict containing:
            - email: The email address checked
            - leaked: Boolean indicating if the email's password was leaked
    """
    # Simulated hash-based leak detection
    sample_leaked_emails = {
        "test@example.com": True,
        "user@domain.com": False,
        "admin@website.org": True,
    }

    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Invalid email address provided")

    leaked = sample_leaked_emails.get(email, False)

    return {
        "email": email,
        "leaked": leaked,
    }


from typing import Dict, Union


def check_email_leak_via_domain(email: str, domain: str) -> Dict[str, Union[str, bool]]:
    """Check if a password has been leaked for an email address by a particular domain.

    Args:
        email: Email to check for leaks for
        domain: Domain to limit check for leaks to

    Returns:
        Dict containing:
            - email: The email address checked
            - domain: The domain used for checking
            - leaked: Boolean indicating if the email's password is leaked
    """
    # Simulated hash-based leak check
    email_hash = hash(email) % 100
    domain_hash = hash(domain) % 100

    # Simulate leak detection logic
    leaked = (email_hash + domain_hash) % 2 == 0

    return {
        "email": email,
        "domain": domain,
        "leaked": leaked,
    }


from typing import Dict, Union


def check_phone_number(phone_number: str) -> Dict[str, Union[str, bool, list]]:
    """Check if a password has been leaked that is linked to a particular phone number.

    Args:
        phone_number: Phone number to check for associated leaks

    Returns:
        Dict containing:
            - phone_number: The phone number checked
            - is_leaked: Boolean indicating if a leak is associated
            - leaked_passwords: List of leaked passwords associated with the phone number
    """

    # Simulated hash-based data generation for consistent results
    sample_leaks = {
        "1234567890": ["password123", "qwerty", "letmein"],
        "0987654321": ["123456", "password1"],
        "01234 5678": [],
    }

    is_leaked = phone_number in sample_leaks and bool(sample_leaks[phone_number])
    leaked_passwords = sample_leaks.get(phone_number, [])

    return {
        "phone_number": phone_number,
        "is_leaked": is_leaked,
        "leaked_passwords": leaked_passwords,
    }


from datetime import datetime, timedelta
from typing import Dict, Literal, Optional, Union


def check_photographer_availability(
    photographer_id: str,
    service_type: Literal["boudoir", "portrait", "wedding", "commercial", "fashion"],
    start_time: str,
    duration_minutes: int,
    location_id: Optional[str] = None,
) -> Dict[str, Union[str, bool]]:
    """Check a photographer's schedule for a time slot.

    Args:
        photographer_id: Unique identifier for the photographer
        service_type: Type of photography service
        start_time: ISO 8601 datetime
        duration_minutes: Length of the shoot in minutes
        location_id: Optional venue ID from search_venues

    Returns:
        Dict containing:
            - photographer_id: The ID of the photographer
            - service_type: The type of service requested
            - start_time: The requested start time
            - duration_minutes: The requested duration in minutes
            - location_id: The location ID if provided
            - available: Boolean indicating if the photographer is available
    """
    # Sample data for demonstration purposes
    sample_schedule = {
        "photographer_1": [
            ("2023-10-01T09:00:00", 120),
            ("2023-10-01T13:00:00", 60),
        ],
        "photographer_2": [
            ("2023-10-01T10:00:00", 90),
            ("2023-10-01T15:00:00", 120),
        ],
    }

    # Parse the start time
    try:
        requested_start = datetime.fromisoformat(start_time)
    except ValueError:
        raise ValueError("Invalid start_time format. Must be ISO 8601 datetime.")

    requested_end = requested_start + timedelta(minutes=duration_minutes)

    # Check availability
    schedule = sample_schedule.get(photographer_id, [])
    available = True
    for booked_start_str, booked_duration in schedule:
        booked_start = datetime.fromisoformat(booked_start_str)
        booked_end = booked_start + timedelta(minutes=booked_duration)
        if (requested_start < booked_end) and (requested_end > booked_start):
            available = False
            break

    return {
        "photographer_id": photographer_id,
        "service_type": service_type,
        "start_time": start_time,
        "duration_minutes": duration_minutes,
        "location_id": location_id,
        "available": available,
    }


from typing import Dict, Literal


def get_career_horoscope(
    zodiac_sign: str,
    focus_area: Literal[
        "job_search", "promotion", "business", "finances", "general"
    ] = "general",
    time_period: Literal["today", "this_week", "this_month"] = "today",
) -> Dict[str, str]:
    """Get the career and money horoscope for a given zodiac sign.

    Args:
        zodiac_sign: The zodiac sign to get the horoscope for (e.g. 'aries', 'taurus')
        focus_area: The area of career to focus on ('job_search', 'promotion', 'business', 'finances', 'general')
        time_period: The time period for the horoscope ('today', 'this_week', 'this_month')

    Returns:
        Dict containing:
            - zodiac_sign: The zodiac sign
            - focus_area: The focus area of the horoscope
            - time_period: The time period of the horoscope
            - horoscope: The career and money horoscope message
    """

    if zodiac_sign not in {
        "aries",
        "taurus",
        "gemini",
        "cancer",
        "leo",
        "virgo",
        "libra",
        "scorpio",
        "sagittarius",
        "capricorn",
        "aquarius",
        "pisces",
    }:
        raise ValueError(f"Unsupported zodiac sign: {zodiac_sign}")

    sample_horoscopes = {
        "aries": "Today is a great day to take initiative in your career.",
        "taurus": "Focus on building strong financial foundations this week.",
        "gemini": "Networking will open new doors for your business this month.",
        "cancer": "A promotion is on the horizon if you maintain your current efforts.",
        "leo": "Consider new job opportunities that align with your passions.",
        "virgo": "Financial planning will be crucial for your success today.",
        "libra": "Collaborations will enhance your business prospects this week.",
        "scorpio": "Expect positive changes in your financial situation this month.",
        "sagittarius": "Your career will benefit from taking calculated risks.",
        "capricorn": "Hard work will lead to a well-deserved promotion.",
        "aquarius": "Innovative ideas will boost your business growth.",
        "pisces": "Focus on balancing your finances to achieve stability.",
    }

    horoscope_key = f"{zodiac_sign}_{focus_area}_{time_period}"
    horoscope_message = sample_horoscopes.get(
        zodiac_sign, "Your career path is full of potential."
    )

    return {
        "zodiac_sign": zodiac_sign,
        "focus_area": focus_area,
        "time_period": time_period,
        "horoscope": horoscope_message,
    }


from typing import Dict


def get_daily_horoscope(zodiac_sign: str, date: str) -> Dict[str, str]:
    """Get the daily horoscope for a given zodiac sign and date.

    Args:
        zodiac_sign: The zodiac sign to get the horoscope for (e.g. 'aries', 'taurus')
        date: The date for which to get the horoscope in YYYY-MM-DD format

    Returns:
        Dict containing:
            - zodiac_sign: The zodiac sign
            - date: The date for the horoscope
            - horoscope: The daily horoscope message
    """

    sample_horoscopes = {
        "aries": "Today is a day to focus on your personal growth.",
        "taurus": "You might find unexpected opportunities at work.",
        "gemini": "Communication is key today, reach out to an old friend.",
        "cancer": "Take time to relax and recharge your energy.",
        "leo": "Your leadership skills will shine through today.",
        "virgo": "Pay attention to the details, they will make a difference.",
        "libra": "Balance is crucial, make sure to weigh your options.",
        "scorpio": "Trust your instincts, they will guide you well.",
        "sagittarius": "Adventure awaits, be open to new experiences.",
        "capricorn": "Hard work will pay off, stay focused on your goals.",
        "aquarius": "Innovation is your strength, think outside the box.",
        "pisces": "Embrace your creativity, it will lead to fulfillment.",
    }

    if zodiac_sign not in sample_horoscopes:
        raise ValueError(f"Zodiac sign not supported: {zodiac_sign}")

    return {
        "zodiac_sign": zodiac_sign,
        "date": date,
        "horoscope": sample_horoscopes[zodiac_sign],
    }


from typing import Dict


def get_instructions(type: str) -> Dict[str, str]:
    """Get setup instructions for a specific type of phone.

    Args:
        type: The type of phone to get instructions for (e.g. 'iPhone', 'Android')

    Returns:
        Dict containing:
            - type: The type of phone
            - instructions: Setup instructions for the phone
    """
    instructions_map = {
        "iPhone": "1. Turn on your iPhone.\n2. Follow the on-screen setup instructions.\n3. Sign in with your Apple ID.",
        "Android": "1. Turn on your Android phone.\n2. Connect to Wi-Fi.\n3. Sign in with your Google account.",
        "Windows Phone": "1. Turn on your Windows Phone.\n2. Connect to Wi-Fi.\n3. Sign in with your Microsoft account.",
    }

    if type not in instructions_map:
        raise ValueError(f"Phone type not supported: {type}")

    return {
        "type": type,
        "instructions": instructions_map[type],
    }


from typing import Dict


def get_league(team: str) -> Dict[str, str]:
    """Get the league for a given team.

    Args:
        team: Team name to get the league for (e.g. 'Lakers', 'Yankees')

    Returns:
        Dict containing:
            - team: Team name
            - league: League name the team belongs to
    """

    sample_leagues = {
        "Lakers": "NBA",
        "Yankees": "MLB",
        "Patriots": "NFL",
        "Red Sox": "MLB",
        "Warriors": "NBA",
        "Dodgers": "MLB",
    }

    if team not in sample_leagues:
        raise ValueError(f"Team not supported: {team}")

    return {
        "team": team,
        "league": sample_leagues[team],
    }


from typing import Dict


def get_weekly_horoscope(zodiac_sign: str, week_start: str) -> Dict[str, str]:
    """Get the weekly horoscope for a specific zodiac sign.

    Args:
        zodiac_sign: The zodiac sign to get the horoscope for (e.g., 'aries', 'taurus')
        week_start: The starting date of the week in YYYY_MM_DD format

    Returns:
        Dict containing:
            - zodiac_sign: The zodiac sign
            - week_start: The starting date of the week
            - horoscope: The horoscope prediction for the week
    """

    sample_horoscopes = {
        "aries": "This week, focus on your personal growth and embrace new challenges.",
        "taurus": "A financial opportunity may present itself. Be ready to seize it.",
        "gemini": "Communication is key this week. Reach out to old friends.",
        "cancer": "Take time to relax and recharge. Self-care is important.",
        "leo": "Your leadership skills will shine. Take the initiative at work.",
        "virgo": "Pay attention to the details. They will make a big difference.",
        "libra": "Balance is crucial. Make sure to spend time with loved ones.",
        "scorpio": "Passion and intensity will drive you. Channel it positively.",
        "sagittarius": "Adventure awaits. Be open to new experiences.",
        "capricorn": "Hard work will pay off. Stay focused on your goals.",
        "aquarius": "Innovation is your strength. Think outside the box.",
        "pisces": "Trust your intuition. It will guide you to the right path.",
    }

    if zodiac_sign not in sample_horoscopes:
        raise ValueError(f"Unsupported zodiac sign: {zodiac_sign}")

    return {
        "zodiac_sign": zodiac_sign,
        "week_start": week_start,
        "horoscope": sample_horoscopes[zodiac_sign],
    }


from typing import Dict


def motives_description(motives: str) -> Dict[str, str]:
    """Return a description of the inputted 7-letter MOTIVES combination.

    Args:
        motives: The 7-letter MOTIVES combination that the user wants a description of.
                 Each letter should be the first letter of the side that applies to the user more.

    Returns:
        Dict containing:
            - motives: The original 7-letter MOTIVES combination
            - description: A description of the combination based on the preferences
    """
    if len(motives) != 7:
        raise ValueError("MOTIVES combination must be exactly 7 letters long.")

    preference_map = {
        "M": "Materialistic",
        "O": "Offbeat",
        "T": "Thinking",
        "I": "Interpersonal",
        "V": "Vital",
        "E": "Easygoing",
        "S": "Sectarian",
        "A": "Ascetic",
        "C": "Conventional",
        "H": "Haphazard",
        "W": "Withholding",
        "D": "Depressed",
        "R": "Rigid",
        "G": "Globalistic",
    }

    description_parts = []
    for letter in motives:
        if letter not in preference_map:
            raise ValueError(f"Invalid letter in MOTIVES combination: {letter}")
        description_parts.append(preference_map[letter])

    description = ", ".join(description_parts)

    return {"motives": motives, "description": description}


from typing import Dict, Union


def quit_job(time_from_now: float) -> Dict[str, Union[str, float]]:
    """Schedule quitting a manager job after a specified number of days.

    Args:
        time_from_now: Time in days to quit from now. Can be decimal.

    Returns:
        Dict containing:
            - status: Confirmation message of the scheduled quit
            - days_until_quit: Number of days until the job is quit
    """
    if time_from_now < 0:
        raise ValueError("time_from_now must be a non-negative number")

    return {
        "status": "Job quitting scheduled",
        "days_until_quit": time_from_now,
    }


from typing import Dict, Union


def rate(id: int, score: float, comment: str = "") -> Dict[str, Union[int, float, str]]:
    """Leave a review of a given bathroom.

    Args:
        id: ID of the bathroom
        score: Review score, must be between 1 and 5
        comment: Optional review comment

    Returns:
        Dict containing:
            - id: ID of the bathroom
            - score: The review score
            - comment: The review comment
            - status: Status of the review submission
    """
    if not (1 <= score <= 5):
        raise ValueError("Score must be between 1 and 5")

    # Simulate a hash-based generation for consistent sample data
    status = "success" if hash((id, score, comment)) % 2 == 0 else "pending"

    return {
        "id": id,
        "score": score,
        "comment": comment,
        "status": status,
    }


from typing import Dict, Union


def reserve_court(
    reserve_time: str, duration: float = 1, location: str = None
) -> Dict[str, Union[str, float, bool]]:
    """Find and reserve an available pickleball court.

    Args:
        reserve_time: Start time for court reservation (e.g. '14:00')
        duration: Duration of court reservation time slot in hours
        location: Search location for closest pickleball court

    Returns:
        Dict containing:
            - location: Location of the reserved court
            - court_id: Identifier for the reserved court
            - start_time: Reservation start time
            - duration: Duration of the reservation
            - success: Boolean indicating if the reservation was successful
    """
    if not location:
        raise ValueError("Location must be specified for reservation.")

    def normalize_location(search_location: str) -> str:
        """Normalize location names for flexible matching."""
        location_mappings = {
            # NYC area variations
            "midtown": "New York",
            "midtown manhattan": "New York",
            "midtown manhattan, ny": "New York",
            "manhattan": "New York",
            "nyc": "New York",
            "new york city": "New York",
            "new york": "New York",
            "downtown manhattan": "New York",
            "upper east side": "New York",
            "upper west side": "New York",
            "times square": "New York",
            "financial district": "New York",
            "chelsea": "New York",
            "hell's kitchen": "New York",
            "central park": "New York",
            "east river park": "New York",
            "brooklyn": "New York",
            "queens": "New York",
            "bronx": "New York",
            "staten island": "New York",
            # LA area variations
            "los angeles": "Los Angeles",
            "la": "Los Angeles",
            "downtown la": "Los Angeles",
            "hollywood": "Los Angeles",
            "beverly hills": "Los Angeles",
            "santa monica": "Los Angeles",
            "west hollywood": "Los Angeles",
            "venice": "Los Angeles",
            # Chicago area variations
            "chicago": "Chicago",
            "downtown chicago": "Chicago",
            "loop": "Chicago",
            "lincoln park": "Chicago",
            "wicker park": "Chicago",
            "river north": "Chicago",
        }

        search_lower = search_location.lower().strip()
        return location_mappings.get(search_lower, search_location)

    def find_matching_location(search_location: str) -> str:
        """Find matching location with fuzzy logic."""
        normalized = normalize_location(search_location)

        # If we got a mapped location, check if it exists in our data
        if normalized in sample_courts:
            return normalized

        # Try partial matching on original search
        search_lower = search_location.lower().strip()
        for location_key in sample_courts.keys():
            location_lower = location_key.lower()
            if search_lower in location_lower or location_lower in search_lower:
                return location_key

        return None

    sample_courts = {
        "New York": ["Court A", "Court B"],
        "Los Angeles": ["Court C", "Court D"],
        "Chicago": ["Court E", "Court F"],
    }

    # Find matching location using normalization
    matching_location = find_matching_location(location)

    if not matching_location:
        raise ValueError(f"No courts available in the specified location: {location}")

    court_id = sample_courts[matching_location][
        hash(reserve_time) % len(sample_courts[matching_location])
    ]

    return {
        "location": matching_location,
        "court_id": court_id,
        "start_time": reserve_time,
        "duration": duration,
        "success": True,
    }


import hashlib
from typing import Dict, Optional, Union


def search_seek(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    city: Union[str, Dict[str, str]] = None,
    job_category: Optional[str] = None,
) -> Dict[str, Union[str, list]]:
    """Search for jobs on seek.co.nz based on specified criteria.

    Args:
        start_date: Timestamp of jobs posted from (optional)
        end_date: Timestamp of jobs posted until (optional)
        city: City information. Can be either:
            - A string containing the city name
            - A dictionary containing city information with at least a 'name' key
        job_category: Category of the job (optional)

    Returns:
        Dict containing:
            - city: City name
            - jobs: List of job titles found
            - total_jobs: Total number of jobs found
    """
    # Handle city parameter
    if not city:
        raise ValueError("City information is required.")

    # Convert string to dictionary format if needed
    if isinstance(city, str):
        city_dict = {"name": city}
    elif isinstance(city, dict):
        if "name" not in city:
            raise ValueError("City dictionary must include a 'name' key.")
        city_dict = city
    else:
        raise ValueError("City must be a string or dictionary.")

    # Generate a consistent but varied list of jobs based on input parameters
    seed = f"{start_date}-{end_date}-{city_dict['name']}-{job_category}"
    hash_object = hashlib.md5(seed.encode())
    hash_digest = hash_object.hexdigest()

    # Simulate job titles based on hash
    job_titles = [
        f"Software Engineer {hash_digest[:5]}",
        f"Data Analyst {hash_digest[5:10]}",
        f"Project Manager {hash_digest[10:15]}",
    ]

    return {
        "city": city_dict["name"],
        "jobs": job_titles,
        "total_jobs": len(job_titles),
    }


from typing import Dict, List


def team_schedule(
    name: str, year: int, incl_playoffs: bool = True
) -> Dict[str, Union[str, int, List[str]]]:
    """Retrieve the list of opponents a team played in a given year.

    Args:
        name: The name of the team (e.g. 'Lakers', 'Warriors')
        year: The season year to retrieve the schedule for
        incl_playoffs: Whether to include playoff games in the schedule

    Returns:
        Dict containing:
            - team: The name of the team
            - year: The season year
            - opponents: List of opponent team names played in the given year
    """

    # Sample data generation based on hash for consistency
    sample_teams = ["Lakers", "Warriors", "Celtics", "Bulls", "Heat"]
    sample_opponents = [
        ["Warriors", "Celtics", "Heat"],
        ["Lakers", "Bulls", "Celtics"],
        ["Heat", "Warriors", "Bulls"],
        ["Celtics", "Lakers", "Heat"],
        ["Bulls", "Warriors", "Lakers"],
    ]

    if name not in sample_teams:
        raise ValueError(f"Team not supported: {name}")

    index = sample_teams.index(name)
    opponents = sample_opponents[index]

    if incl_playoffs:
        playoff_opponents = ["Spurs", "Nets"]
        opponents.extend(playoff_opponents)

    return {
        "team": name,
        "year": year,
        "opponents": opponents,
    }


def convert_units(
    value: float,
    from_unit: Literal["celsius", "fahrenheit", "kelvin", "pounds", "kilograms"],
    to_unit: Literal["celsius", "fahrenheit", "kelvin", "pounds", "kilograms"],
) -> Dict[str, Union[float, str]]:
    """Convert values between different units (temperature and weight).

    Args:
        value: The value to convert
        from_unit: The unit to convert from ('celsius', 'fahrenheit', 'kelvin', 'pounds', 'kilograms')
        to_unit: The unit to convert to ('celsius', 'fahrenheit', 'kelvin', 'pounds', 'kilograms')

    Returns:
        Dict containing:
            - value: Converted value
            - unit: Unit of the converted value
    """
    if from_unit == to_unit:
        return {"value": value, "unit": to_unit}

    # Temperature conversions
    if (from_unit, to_unit) == ("fahrenheit", "celsius"):
        return {"value": (value - 32) * 5 / 9, "unit": "celsius"}
    if (from_unit, to_unit) == ("celsius", "fahrenheit"):
        return {"value": value * 9 / 5 + 32, "unit": "fahrenheit"}
    if (from_unit, to_unit) == ("kelvin", "celsius"):
        return {"value": value - 273.15, "unit": "celsius"}
    if (from_unit, to_unit) == ("celsius", "kelvin"):
        return {"value": value + 273.15, "unit": "kelvin"}
    if (from_unit, to_unit) == ("kelvin", "fahrenheit"):
        # First convert kelvin to celsius, then celsius to fahrenheit
        celsius = value - 273.15
        return {"value": celsius * 9 / 5 + 32, "unit": "fahrenheit"}
    if (from_unit, to_unit) == ("fahrenheit", "kelvin"):
        # First convert fahrenheit to celsius, then celsius to kelvin
        celsius = (value - 32) * 5 / 9
        return {"value": celsius + 273.15, "unit": "kelvin"}

    # Weight conversions
    if (from_unit, to_unit) == ("pounds", "kilograms"):
        return {"value": value * 0.453592, "unit": "kilograms"}
    if (from_unit, to_unit) == ("kilograms", "pounds"):
        return {"value": value / 0.453592, "unit": "pounds"}

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
        "THB": 36.25,
        "RON": 4.7,
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
        "Las Vegas": 651319,
        "Chicago": 2746388,
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
            - root1: First root (float or string representation if complex)
            - root2: Second root (float or string representation if complex)
    """
    import cmath

    discriminant = b**2 - 4 * a * c
    sqrt_disc = cmath.sqrt(discriminant)
    root1 = (-b + sqrt_disc) / (2 * a)
    root2 = (-b - sqrt_disc) / (2 * a)

    # Convert complex numbers to their real values if imaginary part is negligible,
    # otherwise convert to string representation for JSON serialization
    def serialize_root(root):
        if isinstance(root, complex):
            if abs(root.imag) < 1e-10:  # Effectively real
                return float(root.real)
            else:
                return (
                    f"{root.real:.6f}+{root.imag:.6f}j"
                    if root.imag >= 0
                    else f"{root.real:.6f}{root.imag:.6f}j"
                )
        return float(root)

    return {
        "root1": serialize_root(root1),
        "root2": serialize_root(root2),
    }


def check_sharecode(code: str) -> Dict[str, Union[str, bool]]:
    """Check the validity and details of a share code.

    Args:
        code: The share code to validate

    Returns:
        Dict containing:
            - code: The share code checked
            - valid: Whether the code is valid
            - status: Status description of the share code
    """

    # Basic validation - codes should be alphanumeric and at least 6 characters
    if not code or len(code) < 6 or not code.isalnum():
        return {
            "code": code,
            "valid": False,
            "status": "Invalid format - share codes must be at least 6 alphanumeric characters",
        }

    # Use hash to generate consistent but varied results
    code_hash = hash(code.upper()) % 100

    # 80% of codes are valid
    is_valid = code_hash < 80

    if is_valid:
        # Generate different statuses for valid codes
        status_hash = (code_hash * 3) % 5
        statuses = [
            "Active - Ready for employment verification",
            "Active - Valid for right to work checks",
            "Active - Verified and current",
            "Active - Recently updated",
            "Active - Standard verification available",
        ]
        status = statuses[status_hash]
    else:
        # Generate different error statuses
        error_hash = (code_hash * 7) % 4
        error_statuses = [
            "Expired - Please request a new share code",
            "Invalid - Code not found in system",
            "Suspended - Contact HMRC for assistance",
            "Revoked - This share code is no longer valid",
        ]
        status = error_statuses[error_hash]

    return {
        "code": code,
        "valid": is_valid,
        "status": status,
    }


def check_right_to_work(
    first_name: str, last_name: str, date_of_birth: str, share_code: str = None
) -> Dict[str, Union[str, bool]]:
    """Check an individual's right to work in the UK.

    Args:
        first_name: First name of the person
        last_name: Last name of the person
        date_of_birth: Date of birth in YYYY-MM-DD format
        share_code: Optional share code for verification

    Returns:
        Dict containing:
            - first_name: Person's first name
            - last_name: Person's last name
            - date_of_birth: Person's date of birth
            - share_code: Share code used (if provided)
            - right_to_work: Whether the person has right to work
            - work_restrictions: Any restrictions on employment
            - expiry_date: When the right to work expires (if applicable)
    """

    def validate_date_format(date_string: str) -> bool:
        """Validate YYYY-MM-DD date format"""
        try:
            from datetime import datetime

            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    if not first_name or not last_name:
        return {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "share_code": share_code,
            "right_to_work": False,
            "work_restrictions": "Invalid - Name fields are required",
            "expiry_date": None,
        }

    if not validate_date_format(date_of_birth):
        return {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "share_code": share_code,
            "right_to_work": False,
            "work_restrictions": "Invalid - Date of birth must be in YYYY-MM-DD format",
            "expiry_date": None,
        }

    # If share code is provided, validate it first
    if share_code:
        share_result = check_sharecode(share_code)
        if not share_result["valid"]:
            return {
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "share_code": share_code,
                "right_to_work": False,
                "work_restrictions": f"Share code invalid: {share_result['status']}",
                "expiry_date": None,
            }

    # Generate consistent results based on person's details
    person_hash = hash(f"{first_name.lower()}{last_name.lower()}{date_of_birth}") % 100

    # 85% of people have right to work (realistic for UK checks)
    has_right_to_work = person_hash < 85

    if has_right_to_work:
        # Determine work restrictions and expiry
        restriction_hash = (person_hash * 5) % 10

        if restriction_hash < 6:  # 60% have no restrictions
            restrictions = "No restrictions"
            expiry = None
        elif restriction_hash < 8:  # 20% have time-limited right to work
            restrictions = "Time-limited - Student visa holder"
            from datetime import datetime, timedelta

            expiry_date = datetime.now() + timedelta(days=365)
            expiry = expiry_date.strftime("%Y-%m-%d")
        else:  # 20% have some restrictions
            restrictions = "Restricted - Maximum 20 hours per week during term time"
            from datetime import datetime, timedelta

            expiry_date = datetime.now() + timedelta(days=730)
            expiry = expiry_date.strftime("%Y-%m-%d")
    else:
        restrictions = "No right to work - Visa required"
        expiry = None

    return {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "share_code": share_code,
        "right_to_work": has_right_to_work,
        "work_restrictions": restrictions,
        "expiry_date": expiry,
    }
