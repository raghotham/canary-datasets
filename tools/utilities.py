from typing import Any, Dict, List, Union

# Utilities Tools
# Auto-generated implementations from cached categorization


def calculate_area(coverage: float, volume: float) -> Dict[str, Union[float, str]]:
    """Calculate the surface area that can be covered by a given volume of paint.

    Args:
        coverage: Paint coverage in m^2/L
        volume: Volume of paint in L

    Returns:
        Dict containing:
            - area: Surface area in m^2 that the paint can cover
            - message: Informational message about the calculation
    """
    if coverage <= 0:
        raise ValueError("Coverage must be a positive number")
    if volume <= 0:
        raise ValueError("Volume must be a positive number")

    area = coverage * volume
    return {
        "area": area,
        "message": f"The paint can cover an area of {area:.2f} square meters.",
    }


def calculate_volume(area: float, coverage: float) -> Dict[str, Union[float, str]]:
    """Calculate the volume of paint required for a given room surface area.

    Args:
        area: Area of wall in m^2
        coverage: Paint coverage in m^2/L

    Returns:
        Dict containing:
            - volume: Volume of paint required in liters
            - unit: Unit of the volume
    """
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    if coverage <= 0:
        raise ValueError("Coverage must be greater than zero.")

    volume = area / coverage

    return {"volume": volume, "unit": "liters"}


from typing import Dict, Literal, Optional


def call_authorities(
    emergency_type: Literal["police", "fire", "medical", "security"],
    location: Optional[str] = None,
) -> Dict[str, str]:
    """Initiate a call to emergency services or a designated security contact.

    Args:
        emergency_type: The type of emergency ('police', 'fire', 'medical', or 'security').
        location: Specific location details for the emergency responders.

    Returns:
        Dict containing:
            - status: Status of the call initiation
            - message: Detailed message about the call
    """
    if emergency_type not in {"police", "fire", "medical", "security"}:
        raise ValueError(f"Unsupported emergency type: {emergency_type}")

    sample_responses = {
        "police": "Police have been notified and are en route.",
        "fire": "Fire department has been alerted and is on the way.",
        "medical": "Medical emergency services have been dispatched.",
        "security": "Security team has been contacted and is responding.",
    }

    if location:
        message = f"{sample_responses[emergency_type]} Location: {location}."
    else:
        message = f"{sample_responses[emergency_type]} Location details not provided."

    return {"status": "success", "message": message}


from typing import Dict


def call_police(
    is_fire: bool = False, is_burglary: bool = False, is_medical_emergency: bool = False
) -> Dict[str, str]:
    """Simulate calling the police for help based on the type of emergency.

    Args:
        is_fire: Indicates if there is a fire emergency
        is_burglary: Indicates if there is a burglary
        is_medical_emergency: Indicates if there is a medical emergency

    Returns:
        Dict containing:
            - response: The simulated response from the police
            - action: The action taken by the police
    """
    if not (is_fire or is_burglary or is_medical_emergency):
        raise ValueError("At least one emergency type must be specified")

    if is_fire:
        return {
            "response": "Fire department dispatched",
            "action": "Firefighters are on their way to handle the fire.",
        }
    if is_burglary:
        return {
            "response": "Police dispatched",
            "action": "Officers are on their way to investigate the burglary.",
        }
    if is_medical_emergency:
        return {
            "response": "Ambulance dispatched",
            "action": "Paramedics are on their way to provide medical assistance.",
        }

    # Fallback in case of unexpected logic flow
    raise RuntimeError("Unexpected error in emergency handling")


from typing import Dict, Optional, Union


def check_right_to_work(
    visa_type: Optional[str] = None, passport_country: Optional[str] = None
) -> Dict[str, Union[bool, str]]:
    """Check if an employee has the right to work in the US based on visa status or passport.

    Args:
        visa_type: Visa category code (e.g., 'H1B', 'L1', 'F1')
        passport_country: Country code of passport of origin (e.g., 'USA', 'CAN')

    Returns:
        Dict containing:
            - right_to_work: Boolean indicating if the person has the right to work in the US
            - reason: Explanation for the decision
    """

    # Sample data for visa types that allow work in the US
    work_visa_types = {"H1B", "L1", "E2", "O1", "TN"}
    # Sample data for countries whose citizens can work in the US without a visa
    visa_free_countries = {"USA", "CAN"}

    if visa_type is None and passport_country is None:
        raise ValueError(
            "At least one of visa_type or passport_country must be provided."
        )

    if visa_type and visa_type in work_visa_types:
        return {
            "right_to_work": True,
            "reason": f"Visa type '{visa_type}' allows work in the US.",
        }

    if passport_country and passport_country in visa_free_countries:
        return {
            "right_to_work": True,
            "reason": f"Citizens of '{passport_country}' can work in the US without a visa.",
        }

    return {"right_to_work": False, "reason": "No valid work authorization found."}


from typing import Dict, Union


def check_sharecode(sharecode: str) -> Dict[str, Union[str, bool]]:
    """Check the right to work in the UK using a sharecode.

    Args:
        sharecode: Prospective employee's sharecode.

    Returns:
        Dict containing:
            - sharecode: The provided sharecode
            - valid: Boolean indicating if the sharecode is valid
            - status: Description of the work status
    """

    # Simulated database of sharecodes and their statuses
    sharecode_database = {
        "ABC123": {"valid": True, "status": "Eligible to work"},
        "XYZ789": {"valid": False, "status": "Sharecode expired"},
        "DEF456": {"valid": True, "status": "Eligible to work"},
    }

    if sharecode not in sharecode_database:
        raise ValueError(f"Sharecode not recognized: {sharecode}")

    sharecode_info = sharecode_database[sharecode]

    return {
        "sharecode": sharecode,
        "valid": sharecode_info["valid"],
        "status": sharecode_info["status"],
    }


from datetime import datetime
from typing import Dict


def convert_time_zone(datetime_str: str, from_tz: str, to_tz: str) -> Dict[str, str]:
    """Convert an ISO datetime from one timezone to another.

    Args:
        datetime_str: The ISO formatted datetime string to convert
        from_tz: The timezone to convert from (e.g., 'UTC', 'America/New_York')
        to_tz: The timezone to convert to (e.g., 'UTC', 'Europe/London')

    Returns:
        Dict containing:
            - original_datetime: The original datetime string
            - converted_datetime: The converted datetime string in the target timezone
    """
    # Mock timezone conversion - simple hour offset simulation
    timezone_offsets = {
        "UTC": 0,
        "America/New_York": -5,
        "Europe/London": 0,
        "Asia/Tokyo": 9,
        "America/Los_Angeles": -8,
        "America/Vancouver": -8,
    }

    if from_tz not in timezone_offsets or to_tz not in timezone_offsets:
        raise ValueError(f"Unsupported timezone")

    try:
        base_datetime = datetime.fromisoformat(datetime_str.replace("Z", ""))
    except ValueError:
        raise ValueError("Invalid ISO datetime format")

    # Mock conversion by adding offset difference
    offset_diff = timezone_offsets[to_tz] - timezone_offsets[from_tz]
    from datetime import timedelta

    converted_datetime = base_datetime + timedelta(hours=offset_diff)

    return {
        "original_datetime": datetime_str,
        "converted_datetime": converted_datetime.isoformat(),
    }


import hashlib
from typing import Dict, Literal, Union


def electricity_price(
    date: str,
    country: Literal[
        "FI", "EE", "SE1", "SE2", "SE3", "SE4", "NO", "DE", "BE", "AU", "LU"
    ],
    currency: Literal["EUR", "SEK", "NOK"],
    priceFormat: Literal["single", "cent"] = "single",
) -> Dict[str, Union[str, float]]:
    """Offers real-time spot prices for European electricity with analytical tools for market analysis.

    Args:
        date: The date to look up prices for in YYYY-MM-DD format.
        country: The country code of the country to fetch prices for.
        currency: Currency to display the prices in.
        priceFormat: The format to display prices in ('single' or 'cent').

    Returns:
        Dict containing:
            - date: The date for which the prices are fetched.
            - country: The country code.
            - currency: The currency in which prices are displayed.
            - price: The electricity price in the specified format and currency.
    """
    if not date or not country or not currency:
        raise ValueError("Date, country, and currency are required parameters.")

    # Generate a mock price based on hash of the date and country
    hash_input = f"{date}-{country}".encode()
    hash_value = int(hashlib.sha256(hash_input).hexdigest(), 16)
    base_price = (hash_value % 100) + 20  # Base price between 20 and 119

    # Adjust price based on currency
    currency_multiplier = {"EUR": 1.0, "SEK": 10.0, "NOK": 10.5}
    price_in_currency = base_price * currency_multiplier[currency]

    # Convert price to the requested format
    if priceFormat == "cent":
        price_in_currency *= 100

    return {
        "date": date,
        "country": country,
        "currency": currency,
        "price": round(price_in_currency, 2),
    }


from datetime import datetime
from typing import Dict


def get_date() -> Dict[str, str]:
    """Gets the current date in (YYYY-MM-DD) format.

    Returns:
        Dict containing:
            - date: Current date as a string in the format 'YYYY-MM-DD'
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    return {"date": current_date}


def is_even(num: float) -> Dict[str, Union[bool, str]]:
    """Check if a number is even.

    Args:
        num: Number to check

    Returns:
        Dict containing:
            - number: The original number
            - is_even: Boolean indicating if the number is even
    """
    if not isinstance(num, (int, float)):
        raise ValueError("The input must be a number.")

    return {
        "number": num,
        "is_even": num % 2 == 0,
    }


def is_odd(num: float) -> Dict[str, Union[bool, str]]:
    """Check if a number is odd.

    Args:
        num: Number to check

    Returns:
        Dict containing:
            - number: The original number
            - is_odd: Boolean indicating if the number is odd
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")

    return {
        "number": num,
        "is_odd": bool(num % 2 != 0),
    }


import hashlib
from typing import Dict, Union


def login(username: str, password: str) -> Dict[str, Union[str, int]]:
    """Authenticate a user and return a JWT if credentials are valid.

    Args:
        username: The username, which could be an email or phone number.
        password: The base64-encoded password SHA-256 hash.

    Returns:
        Dict containing:
            - token: The JWT token if login is successful
            - expires_in: Expiration time in seconds for the token

    Raises:
        ValueError: If the username or password is incorrect.
    """
    # Simulated user database with hashed passwords
    user_db = {
        "user@example.com": hashlib.sha256(b"password123").hexdigest(),
        "1234567890": hashlib.sha256(b"securepassword").hexdigest(),
    }

    # Mock password decoding - assume it's a hex string
    try:
        decoded_password = (
            password  # Simplified - assume password is already in hex format
        )
    except Exception:
        raise ValueError("Invalid password encoding")

    # Check if the username exists and the password matches
    if username not in user_db or user_db[username] != decoded_password:
        raise ValueError("Invalid username or password")

    # Generate a mock JWT token using simple hash
    mock_token = (
        f"jwt_{hashlib.sha256((username + 'secret').encode()).hexdigest()[:32]}"
    )

    return {
        "token": mock_token,
        "expires_in": 3600,
    }


from typing import Dict


def logout(JWT: str) -> Dict[str, str]:
    """Remove JWT from system, logging out the user.

    Args:
        JWT: Valid JWT to be removed

    Returns:
        Dict containing:
            - status: Status of the logout operation
            - message: Informational message about the operation
    """
    if not JWT or not isinstance(JWT, str):
        raise ValueError("Invalid JWT provided")

    # Simulate JWT removal process
    # In a real-world scenario, this would involve removing the JWT from a database or cache
    # Here we mock the process with a simple hash-based check for demonstration purposes
    if hash(JWT) % 2 == 0:
        return {"status": "success", "message": "User successfully logged out."}
    else:
        return {
            "status": "failure",
            "message": "Failed to log out user. JWT not found.",
        }


import hashlib
from typing import Dict


def renew(JWT: str) -> Dict[str, str]:
    """Renew a JWT and return a new token.

    Args:
        JWT: Valid JWT to be renewed

    Returns:
        Dict containing:
            - new_jwt: The newly generated JWT
    """
    if not JWT:
        raise ValueError("JWT cannot be empty")

    # Simulate JWT renewal by hashing the existing JWT
    new_jwt = hashlib.sha256(JWT.encode()).hexdigest()

    return {"new_jwt": new_jwt}


import subprocess
from typing import Dict, List, Union


def run_command(
    name: str, command: str, arguments: List[str] = [], user: str = None
) -> Dict[str, Union[str, int]]:
    """Run a shell command on a VPS.

    Args:
        name: The name of the server to run the command on.
        command: The command to run, not including arguments.
        arguments: List of command line arguments to send to the command.
        user: The name of the user account to run the command as.

    Returns:
        Dict containing:
            - server: Name of the server
            - command: Full command executed
            - exit_code: Exit code of the command
            - output: Output from the command execution
    """
    if not name or not command or not user:
        raise ValueError("Server name, command, and user are required.")

    full_command = ["ssh", f"{user}@{name}", command] + arguments
    try:
        result = subprocess.run(
            full_command, capture_output=True, text=True, check=True
        )
        output = result.stdout.strip()
        exit_code = result.returncode
    except subprocess.CalledProcessError as e:
        output = e.stderr.strip()
        exit_code = e.returncode

    return {
        "server": name,
        "command": " ".join(full_command),
        "exit_code": exit_code,
        "output": output,
    }


import hashlib
from typing import Dict, List, Union


def broken_links_finder(url: str) -> Dict[str, Union[str, List[str]]]:
    """Find broken links from a given URL.

    Args:
        url: URL from which to find broken links.

    Returns:
        Dict containing:
            - url: The original URL checked
            - broken_links: List of broken links found on the page
    """

    # Simulate broken link detection using hash-based generation
    def simulate_broken_links(url: str) -> List[str]:
        # Create a hash of the URL to generate consistent but varied results
        hash_value = hashlib.md5(url.encode()).hexdigest()
        # Use the hash to determine a fixed number of broken links
        num_broken_links = int(hash_value, 16) % 5  # Up to 4 broken links
        return [f"http://example.com/broken_link_{i}" for i in range(num_broken_links)]

    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError(f"Invalid URL format: {url}")

    broken_links = simulate_broken_links(url)

    return {
        "url": url,
        "broken_links": broken_links,
    }


from typing import Dict, List, Union


def calculate_sum_of_list(
    numbers_list: Union[List[Union[int, float]], str]
) -> Dict[str, Union[float, str]]:
    """Calculate the total sum of a list of numbers.

    Args:
        numbers_list: A list of numbers to add together or a string representation of a list (e.g., '[8, 2, 3]').

    Returns:
        Dict containing:
            - total_sum: The total sum of the numbers in the list
            - description: A brief description of the operation
    """
    # Convert string representation of list to actual list
    if isinstance(numbers_list, str):
        try:
            import ast
            parsed_list = ast.literal_eval(numbers_list)
            if isinstance(parsed_list, list):
                numbers_list = parsed_list
            else:
                raise ValueError("Invalid numbers_list format. Expected a list.")
        except (ValueError, SyntaxError):
            raise ValueError("Invalid numbers_list format. Expected a valid list representation.")

    if not numbers_list:
        raise ValueError("The numbers_list cannot be empty.")

    total_sum = sum(numbers_list)

    return {
        "total_sum": total_sum,
        "description": "Sum of the provided list of numbers.",
    }


from typing import Dict


def cancel_membership(
    current_member_name: str,
    email: str,
    phone_number: str,
    cancellation_reason: str,
    cancellation_date: str,
) -> Dict[str, str]:
    """Cancel a currently existing membership.

    Args:
        current_member_name: First name and surname of the member wanting to cancel their membership.
        email: Email address of the member wanting to cancel their membership.
        phone_number: Contact/phone number of the member wanting to cancel their membership.
        cancellation_reason: Reason the member gives for wanting to cancel their membership.
        cancellation_date: The member's desired date for their membership cancellation (YYYY-MM-DD).

    Returns:
        Dict containing:
            - status: Status of the cancellation process
            - message: Additional information about the cancellation
    """

    # Simulate a database of current members
    members_db = {
        "john.doe@example.com": {
            "name": "John Doe",
            "phone": "123-456-7890",
            "membership_status": "active",
        },
        "jane.smith@example.com": {
            "name": "Jane Smith",
            "phone": "987-654-3210",
            "membership_status": "active",
        },
    }

    # Check if the member exists in the database
    member = members_db.get(email)
    if not member:
        raise ValueError("Member not found with the provided email address.")

    # Verify the member's details
    if member["name"] != current_member_name or member["phone"] != phone_number:
        raise ValueError("Member details do not match our records.")

    # Simulate cancellation process
    if member["membership_status"] == "active":
        member["membership_status"] = "cancelled"
        return {
            "status": "success",
            "message": f"Membership for {current_member_name} has been successfully cancelled as of {cancellation_date}.",
        }
    else:
        return {"status": "failure", "message": "Membership is already cancelled."}


from typing import Dict, Literal


def change_case(
    id: int,
    line_number: int,
    start_character: int,
    end_character: int,
    case_style: Literal[
        "title", "sentence", "lower", "upper", "camel", "pascal", "snake"
    ],
) -> Dict[str, str]:
    """Change the case of a specific portion of text based on the given parameters.

    Args:
        id: The id of the scene narration for which to change case
        line_number: The line number for which to change case
        start_character: The start position for which to change case
        end_character: The end position for which to change case
        case_style: One of title, sentence, lower, upper, camel, pascal, or snake

    Returns:
        Dict containing:
            - original_text: The original text before case change
            - modified_text: The text after applying the case change
    """

    # Mock data representing a scene narration
    scene_narrations = {
        1: [
            "Once upon a time, in a land far, far away, there lived a king.",
            "He was a kind and just ruler, beloved by all his subjects.",
        ],
        2: [
            "In the heart of the forest, a mysterious creature lurked.",
            "Its eyes glowed in the dark, watching every move.",
        ],
    }

    if id not in scene_narrations:
        raise ValueError(f"Scene ID not found: {id}")
    if line_number >= len(scene_narrations[id]):
        raise ValueError(f"Line number out of range: {line_number}")

    original_text = scene_narrations[id][line_number]
    if not (0 <= start_character < end_character <= len(original_text)):
        raise ValueError("Character positions are out of range")

    text_to_change = original_text[start_character:end_character]

    if case_style == "title":
        modified_text = text_to_change.title()
    elif case_style == "sentence":
        modified_text = text_to_change.capitalize()
    elif case_style == "lower":
        modified_text = text_to_change.lower()
    elif case_style == "upper":
        modified_text = text_to_change.upper()
    elif case_style == "camel":
        modified_text = "".join(
            word.capitalize() if i != 0 else word.lower()
            for i, word in enumerate(text_to_change.split())
        )
    elif case_style == "pascal":
        modified_text = "".join(word.capitalize() for word in text_to_change.split())
    elif case_style == "snake":
        modified_text = text_to_change.replace(" ", "_").lower()
    else:
        raise ValueError(f"Unsupported case style: {case_style}")

    modified_text = (
        original_text[:start_character] + modified_text + original_text[end_character:]
    )

    return {
        "original_text": original_text,
        "modified_text": modified_text,
    }


from typing import Dict, Union


def check_rust_zone(city: str) -> Dict[str, Union[str, bool]]:
    """Checks whether the given location is prone to rust formation.

    Args:
        city: The city to check for rust-prone conditions (e.g. 'San Francisco', 'Miami')

    Returns:
        Dict containing:
            - city: City name
            - rust_prone: Boolean indicating if the city is prone to rust
    """

    rust_prone_cities = {
        "San Francisco": True,
        "Miami": True,
        "Phoenix": False,
        "Denver": False,
        "Seattle": True,
    }

    if city not in rust_prone_cities:
        raise ValueError(f"City not supported: {city}")

    return {
        "city": city,
        "rust_prone": rust_prone_cities[city],
    }


from datetime import datetime, timedelta
from typing import Dict, Optional, Union


def check_warranty(
    brand: str,
    model_number: str,
    serial_number: str,
    purchase_date: Optional[str] = None,
    coverage_type: Optional[str] = None,
) -> Dict[str, Union[str, bool, None]]:
    """Verify warranty coverage status for a product using serial and purchase details.

    Args:
        brand: Manufacturer brand
        model_number: Model number
        serial_number: Unique serial number
        purchase_date: Original purchase date (YYYY-MM-DD)
        coverage_type: Coverage class to verify, e.g., 'parts', 'labor', 'full'

    Returns:
        Dict containing:
            - brand: Manufacturer brand
            - model_number: Model number
            - serial_number: Unique serial number
            - coverage_status: Boolean indicating if the warranty is valid
            - coverage_type: Type of coverage checked
            - warranty_expiry: Expiry date of the warranty
    """
    # Simulated warranty periods for different brands
    warranty_periods = {
        "BrandA": 365,  # 1 year
        "BrandB": 730,  # 2 years
        "BrandC": 1095,  # 3 years
    }

    if brand not in warranty_periods:
        raise ValueError(f"Brand not supported: {brand}")

    # Default purchase date to today if not provided
    if purchase_date is None:
        purchase_date = datetime.now().strftime("%Y-%m-%d")

    try:
        purchase_date_obj = datetime.strptime(purchase_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid purchase date format. Use YYYY-MM-DD.")

    warranty_days = warranty_periods[brand]
    warranty_expiry_date = purchase_date_obj + timedelta(days=warranty_days)
    coverage_status = datetime.now() <= warranty_expiry_date

    return {
        "brand": brand,
        "model_number": model_number,
        "serial_number": serial_number,
        "coverage_status": coverage_status,
        "coverage_type": coverage_type,
        "warranty_expiry": warranty_expiry_date.strftime("%Y-%m-%d"),
    }


from typing import Dict, List, Union


def create_list_from_numbers(numbers_text: str) -> Dict[str, Union[str, List[int]]]:
    """Create a list of integers from a string of numbers separated by commas.

    Args:
        numbers_text: A string of numbers separated by commas (e.g., '8, 2, 5')

    Returns:
        Dict containing:
            - original_text: The original input string
            - numbers_list: List of integers extracted from the string
    """
    if not numbers_text:
        raise ValueError("Input string cannot be empty")

    try:
        numbers_list = [int(num.strip()) for num in numbers_text.split(",")]
    except ValueError as e:
        raise ValueError(
            "Input string must contain only numbers separated by commas"
        ) from e

    return {
        "original_text": numbers_text,
        "numbers_list": numbers_list,
    }


from typing import Dict, List, Literal


def dns_record_checker(
    domain: str,
    record_type: Literal[
        "A",
        "AAAA",
        "CNAME",
        "NS",
        "SOA",
        "MX",
        "SRV",
        "TXT",
        "CAA",
        "NAPTR",
        "PTR",
        "HINFO",
        "A6",
    ],
) -> Dict[str, List[str]]:
    """Get specified DNS records for a domain.

    Args:
        domain: Domain for which to get DNS records
        record_type: Type of record to return

    Returns:
        Dict containing:
            - domain: The domain name
            - records: List of DNS records of the specified type
    """

    sample_data = {
        "example.com": {
            "A": ["93.184.216.34"],
            "AAAA": ["2606:2800:220:1:248:1893:25c8:1946"],
            "CNAME": ["cname.example.com"],
            "NS": ["ns1.example.com", "ns2.example.com"],
            "SOA": [
                "ns1.example.com hostmaster.example.com 2020102201 7200 3600 1209600 3600"
            ],
            "MX": ["10 mail.example.com"],
            "SRV": ["0 5 5060 sip.example.com"],
            "TXT": ["v=spf1 include:_spf.example.com ~all"],
            "CAA": ['0 issue "letsencrypt.org"'],
            "NAPTR": [
                '100 10 "U" "E2U+sip" "!^.*$!sip:customer-service@example.com!" .'
            ],
            "PTR": ["ptr.example.com"],
            "HINFO": ['"CPU" "OS"'],
            "A6": ["2001:0db8:85a3::8a2e:0370:7334"],
        }
    }

    if domain not in sample_data:
        raise ValueError(f"Domain not supported: {domain}")
    if record_type not in sample_data[domain]:
        raise ValueError(
            f"Record type not supported for domain {domain}: {record_type}"
        )

    return {
        "domain": domain,
        "records": sample_data[domain][record_type],
    }


import random
import string
from typing import Dict


def generate_id() -> Dict[str, str]:
    """Generate a unique 8-digit hexadecimal identifier code.

    Returns:
        Dict containing:
            - id: A unique 8-digit hexadecimal identifier
    """
    existing_ids = {"293CCCB4", "A1B2C3D4", "DEADBEEF"}

    def create_hex_id() -> str:
        return "".join(random.choices(string.hexdigits.upper(), k=8))

    new_id = create_hex_id()
    while new_id in existing_ids:
        new_id = create_hex_id()

    return {"id": new_id}


from typing import Dict, Union


def getAutoclaveConfig() -> Dict[str, Union[str, int, float]]:
    """Fetch the current configuration settings of the autoclave.

    Returns:
        Dict containing:
            - mode: Current operational mode of the autoclave
            - temperature: Set temperature in Celsius
            - pressure: Set pressure in PSI
            - cycle_time: Duration of the current cycle in minutes
    """

    # Simulated configuration settings
    config = {
        "mode": "sterilization",
        "temperature": 121,  # in Celsius
        "pressure": 15,  # in PSI
        "cycle_time": 30,  # in minutes
    }

    return config


from typing import Dict, Union


def getError() -> Dict[str, Union[str, int]]:
    """Retrieve details about the current error state.

    Returns:
        Dict containing:
            - error_code: Numeric code representing the error
            - error_message: Description of the error
            - severity: Severity level of the error ('low', 'medium', 'high')
    """

    # Simulated error states
    error_states = [
        {"error_code": 404, "error_message": "Not Found", "severity": "low"},
        {
            "error_code": 500,
            "error_message": "Internal Server Error",
            "severity": "high",
        },
        {"error_code": 403, "error_message": "Forbidden", "severity": "medium"},
    ]

    # For demonstration, we select an error state based on a hash of a constant string
    import hashlib

    index = int(hashlib.sha256("current_error_state".encode()).hexdigest(), 16) % len(
        error_states
    )

    return error_states[index]


from datetime import datetime, timedelta
from typing import Dict


def get_additive_date(initial_date: str, days_to_add: int) -> Dict[str, str]:
    """Add a specified number of days to a given date.

    Args:
        initial_date: The initial date to start from in 'YYYY-MM-DD' format.
        days_to_add: The number of days to add to the initial date.

    Returns:
        Dict containing:
            - initial_date: The original date provided
            - new_date: The new date after adding the specified days
    """
    try:
        date_obj = datetime.strptime(initial_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {initial_date}. Expected 'YYYY-MM-DD'.")

    new_date_obj = date_obj + timedelta(days=days_to_add)
    new_date_str = new_date_obj.strftime("%Y-%m-%d")

    return {
        "initial_date": initial_date,
        "new_date": new_date_str,
    }


from typing import Dict, Union


def get_appliance_manual(
    brand: str, model_number: str, year: Union[int, None] = None, language: str = "en"
) -> Dict[str, Union[str, int]]:
    """Fetch a user manual or installation guide PDF for a specific brand/model.

    Args:
        brand: Manufacturer brand
        model_number: Exact model number
        year: Approximate production year (YYYY)
        language: Manual language code, e.g., 'en', 'es'

    Returns:
        Dict containing:
            - brand: Manufacturer brand
            - model_number: Exact model number
            - year: Production year if provided
            - language: Language code of the manual
            - manual_url: URL to the PDF manual
    """

    # Simulated hash-based URL generation for consistency
    manual_base_url = "https://manuals.example.com"
    hash_suffix = hash((brand, model_number, year, language)) % 10000
    manual_url = (
        f"{manual_base_url}/{brand}/{model_number}/{language}/manual_{hash_suffix}.pdf"
    )

    # Simulating a check for supported brands and models
    supported_brands = {"Samsung", "LG", "Whirlpool"}
    if brand not in supported_brands:
        raise ValueError(f"Brand not supported: {brand}")

    # Simulating a check for model number format
    if not model_number.isalnum():
        raise ValueError(f"Invalid model number format: {model_number}")

    return {
        "brand": brand,
        "model_number": model_number,
        "year": year,
        "language": language,
        "manual_url": manual_url,
    }


from typing import Dict, List, Literal, Union


def get_country(
    country_code: str, output_language: Literal["en", "es", "tr", "fr"] = "en"
) -> Dict[str, Union[str, List[Dict[str, Union[str, List[str]]]]]]:
    """Get a country and the list of the supported services and their details.

    Args:
        country_code: ISO 3166-1 alpha-2 code of the country
        output_language: ISO 639-1 code of the output language. Determines in which language the output will be in

    Returns:
        Dict containing:
            - country: Name of the country in the specified language
            - services: List of services with their details
    """

    country_data = {
        "US": {
            "en": "United States",
            "es": "Estados Unidos",
            "tr": "Amerika Birleşik Devletleri",
            "fr": "États-Unis",
        },
        "FR": {"en": "France", "es": "Francia", "tr": "Fransa", "fr": "France"},
        "TR": {"en": "Turkey", "es": "Turquía", "tr": "Türkiye", "fr": "Turquie"},
    }

    services_data = {
        "US": [
            {"name": "Streaming", "details": ["Netflix", "Hulu", "Disney+"]},
            {"name": "E-commerce", "details": ["Amazon", "eBay"]},
        ],
        "FR": [
            {"name": "Streaming", "details": ["Canal+", "Netflix"]},
            {"name": "E-commerce", "details": ["Cdiscount", "Amazon"]},
        ],
        "TR": [
            {"name": "Streaming", "details": ["BluTV", "Netflix"]},
            {"name": "E-commerce", "details": ["Trendyol", "Hepsiburada"]},
        ],
    }

    if country_code not in country_data:
        raise ValueError(f"Country code not supported: {country_code}")

    country_name = country_data[country_code].get(
        output_language, country_data[country_code]["en"]
    )
    services = services_data.get(country_code, [])

    return {"country": country_name, "services": services}


from typing import Dict, Union


def get_cpu_temp(
    device_id: str, convert_to_celsius: bool = False
) -> Dict[str, Union[float, str]]:
    """Return the temperature of the CPU for a given device.

    Args:
        device_id: ID number linked to the device
        convert_to_celsius: Convert temperature to Celsius if True

    Returns:
        Dict containing:
            - device_id: The ID of the device
            - temperature: Current CPU temperature
            - unit: Unit of the temperature ('celsius' or 'fahrenheit')
    """

    # Simulate CPU temperature based on device_id hash
    base_temp_fahrenheit = 70 + (hash(device_id) % 30)

    if convert_to_celsius:
        temperature = (base_temp_fahrenheit - 32) * 5 / 9
        unit = "celsius"
    else:
        temperature = base_temp_fahrenheit
        unit = "fahrenheit"

    return {"device_id": device_id, "temperature": temperature, "unit": unit}


import hashlib
from datetime import datetime, timedelta
from typing import Dict, Literal


def get_current_datetime(
    location: Literal[
        "FI", "EE", "SE1", "SE2", "SE3", "SE4", "NO", "DE", "BE", "AU", "LU"
    ]
) -> Dict[str, str]:
    """Get the current date and time based on user location.

    Args:
        location: The country code of the user country (e.g. 'FI', 'DE')

    Returns:
        Dict containing:
            - location: Country code
            - datetime: Current date and time in ISO 8601 format
    """

    # Sample timezone offsets in hours for each location
    timezone_offsets = {
        "FI": 2,
        "EE": 2,
        "SE1": 1,
        "SE2": 1,
        "SE3": 1,
        "SE4": 1,
        "NO": 1,
        "DE": 1,
        "BE": 1,
        "AU": 10,
        "LU": 1,
    }

    if location not in timezone_offsets:
        raise ValueError(f"Location not supported: {location}")

    # Get the current UTC time
    current_utc_time = datetime.utcnow()

    # Calculate the local time based on the timezone offset
    local_time = current_utc_time + timedelta(hours=timezone_offsets[location])

    # Format the local time in ISO 8601 format
    formatted_time = local_time.isoformat()

    return {
        "location": location,
        "datetime": formatted_time,
    }


from datetime import datetime, timedelta, timezone
from typing import Dict, Optional


def get_current_iso_time(location: Optional[str] = None) -> Dict[str, str]:
    """Get the current time in ISO 8601 format with offset for a given location.

    Args:
        location: The location in which to get the current time. If not provided, UTC time is used.

    Returns:
        Dict containing:
            - location: The location for which the time is provided
            - iso_time: Current time in ISO 8601 format with offset
    """

    # Sample time offsets for different locations
    location_offsets = {
        "New York": -4,  # UTC-4
        "London": 0,  # UTC+0
        "Tokyo": 9,  # UTC+9
    }

    if location and location not in location_offsets:
        raise ValueError(f"Location not supported: {location}")

    offset_hours = location_offsets.get(location, 0)
    current_time = datetime.now(timezone.utc) + timedelta(hours=offset_hours)
    iso_time = current_time.isoformat()

    return {
        "location": location if location else "UTC",
        "iso_time": iso_time,
    }


from typing import Dict, List, Union


def get_dataset_columns(dataset_id: str) -> Dict[str, List[Dict[str, str]]]:
    """Retrieve the list of column names and types for a given dataset from the Austin Open Data Portal.

    Args:
        dataset_id: The Socrata dataset identifier (e.g., 'abcd-1234').

    Returns:
        Dict containing:
            - columns: List of dictionaries with 'name' and 'type' keys for each column
    """

    # Sample data based on hash of dataset_id for consistent but varied results
    sample_data = {
        "abcd-1234": [
            {"name": "id", "type": "number"},
            {"name": "name", "type": "text"},
            {"name": "created_at", "type": "date"},
        ],
        "efgh-5678": [
            {"name": "record_id", "type": "number"},
            {"name": "description", "type": "text"},
            {"name": "value", "type": "number"},
        ],
    }

    if dataset_id not in sample_data:
        raise ValueError(f"Dataset ID not supported: {dataset_id}")

    return {"columns": sample_data[dataset_id]}


from typing import Dict, List, Union


def get_dataset_rows(
    dataset_id: str,
    limit: int = 100,
    offset: int = 0,
    filters: Dict[str, Union[str, int, float]] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]:
    """Retrieve rows of data from a given dataset on the Austin Open Data Portal.

    Args:
        dataset_id: The Socrata dataset identifier (e.g., 'abcd-1234').
        limit: Number of rows to return.
        offset: Number of rows to skip before returning results.
        filters: Optional key-value filters to apply when retrieving rows.

    Returns:
        Dict containing:
            - dataset_id: The dataset identifier
            - rows: List of dictionaries representing dataset rows
    """
    if not dataset_id:
        raise ValueError("dataset_id is required")

    # Simulate dataset rows using hash-based generation for consistency
    def generate_row(index: int) -> Dict[str, Union[str, int, float]]:
        return {
            "id": index,
            "name": f"Sample Name {index}",
            "value": index * 1.5,
            "category": "Category A" if index % 2 == 0 else "Category B",
        }

    # Generate sample data
    total_rows = 1000  # Assume there are 1000 rows in the dataset
    if offset >= total_rows:
        return {"dataset_id": dataset_id, "rows": []}

    # Apply filters if provided
    def matches_filters(row: Dict[str, Union[str, int, float]]) -> bool:
        if not filters:
            return True
        for key, value in filters.items():
            if row.get(key) != value:
                return False
        return True

    rows = [
        generate_row(i)
        for i in range(offset, min(offset + limit, total_rows))
        if matches_filters(generate_row(i))
    ]

    return {"dataset_id": dataset_id, "rows": rows}


from datetime import datetime
from typing import Dict


def get_day_from_date(date: str) -> Dict[str, str]:
    """Gets the day of the week for the given date (YYYY-MM-DD).

    Args:
        date: The initial date to check in 'YYYY-MM-DD' format.

    Returns:
        Dict containing:
            - date: The input date
            - day_of_week: The day of the week corresponding to the date
    """
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            f"Invalid date format: {date}. Expected format is 'YYYY-MM-DD'."
        )

    day_of_week = parsed_date.strftime("%A")

    return {
        "date": date,
        "day_of_week": day_of_week,
    }


from datetime import datetime
from typing import Dict, Union


def get_dst_transition(tz: str, date: str) -> Dict[str, Union[str, bool]]:
    """Return DST status for a timezone on a specific date.

    Args:
        tz: IANA timezone string (e.g., 'America/New_York')
        date: Date in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - timezone: The IANA timezone string
            - date: The date checked
            - is_dst: Boolean indicating if DST is in effect on the given date
    """
    # Mock DST status based on common DST patterns
    dst_timezones = {
        "America/New_York",
        "America/Los_Angeles",
        "Europe/London",
        "Europe/Berlin",
        "Australia/Sydney",
    }

    if tz not in dst_timezones:
        raise ValueError(f"Unknown timezone: {tz}")

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date}")

    # Mock DST logic: assume DST is active roughly from March to November
    month = date_obj.month
    is_dst = 3 <= month <= 10  # Simplified DST period

    return {
        "timezone": tz,
        "date": date,
        "is_dst": is_dst,
    }


from typing import Dict, List, Literal


def get_emergency_numbers(
    country: str, number_type: str = "General emergency"
) -> Dict[str, Union[str, List[str]]]:
    """Returns a list of emergency hotlines for a specified country.

    Args:
        country: The country which to retrieve emergency hotline numbers for.
        number_type: The type of emergency hotline required, e.g. mental health, mountain rescue, animal control, etc.

    Returns:
        Dict containing:
            - country: The country name
            - number_type: The type of emergency hotline
            - numbers: List of emergency hotline numbers
    """

    sample_data = {
        "USA": {
            "General emergency": ["911"],
            "Mental health": ["988"],
            "Animal control": ["311"],
        },
        "UK": {
            "General emergency": ["999"],
            "Mental health": ["116 123"],
            "Mountain rescue": ["999"],
        },
        "Germany": {
            "General emergency": ["112"],
            "Mental health": ["0800 111 0 111"],
            "Animal control": ["112"],
        },
    }

    if country not in sample_data:
        raise ValueError(f"Country not supported: {country}")

    country_data = sample_data[country]
    if number_type not in country_data:
        raise ValueError(f"Number type not supported for {country}: {number_type}")

    return {
        "country": country,
        "number_type": number_type,
        "numbers": country_data[number_type],
    }


from typing import Dict, Optional, Union


def get_energy_cost_estimate(
    station_id: str, kWh: float, membership_tier: Optional[str] = None
) -> Dict[str, Union[str, float]]:
    """Estimate the charging cost at a specific station for a planned energy amount.

    Args:
        station_id: Provider's station identifier.
        kWh: Planned energy in kWh.
        membership_tier: Pricing tier or membership plan code, if any.

    Returns:
        Dict containing:
            - station_id: The station identifier
            - kWh: The planned energy in kWh
            - cost: Estimated cost for the charging session
            - currency: Currency of the estimated cost
    """
    # Sample pricing data based on station_id
    base_rate = {
        "Electrify America E": 0.30,
        "Tesla Supercharger C": 0.35,
        "ChargePoint Station A": 0.25,
    }

    # Sample membership discounts
    membership_discounts = {
        "premium": 0.10,  # 10% discount
        "standard": 0.05,  # 5% discount
    }

    if station_id not in base_rate:
        raise ValueError(f"Station ID not supported: {station_id}")

    # Calculate base cost
    cost_per_kWh = base_rate[station_id]
    total_cost = kWh * cost_per_kWh

    # Apply membership discount if applicable
    if membership_tier and membership_tier in membership_discounts:
        discount = membership_discounts[membership_tier]
        total_cost *= 1 - discount

    return {
        "station_id": station_id,
        "kWh": kWh,
        "cost": round(total_cost, 2),
        "currency": "USD",
    }


from typing import Dict


def get_fuel_price_by_country(city: str, date: str = "2025-01-01") -> Dict[str, float]:
    """Get the fuel price by country in the EU.

    Args:
        city: Country code, e.g., 'DE'
        date: Date to search the fuel price for, default is '2025-01-01'

    Returns:
        Dict containing:
            - city: Country code
            - date: Date of the fuel price
            - fuel_price: Price of fuel in euros per liter
    """

    # Sample data based on city codes
    sample_prices = {
        "DE": 1.45,
        "FR": 1.55,
        "IT": 1.60,
        "ES": 1.50,
        "NL": 1.65,
    }

    if city not in sample_prices:
        raise ValueError(f"City code not supported: {city}")

    # Simulate a price fluctuation based on the date
    date_hash = hash(date) % 10
    fluctuation = (date_hash - 5) * 0.01  # Fluctuation between -0.05 and +0.04

    fuel_price = sample_prices[city] + fluctuation

    return {
        "city": city,
        "date": date,
        "fuel_price": round(fuel_price, 2),
    }


from typing import Dict, Optional, Union


def get_ram_usage(
    device_id: str, specify_individual_stick: Optional[int] = None
) -> Dict[str, Union[str, int, Dict[int, int]]]:
    """Return how much RAM is currently in use on a given device.

    Args:
        device_id: ID number linked to the device
        specify_individual_stick: Index of RAM stick to return usage information on. Omit for all.

    Returns:
        Dict containing:
            - device_id: ID of the device
            - total_usage: Total RAM usage in MB
            - individual_stick_usage: Dictionary with stick index as key and usage in MB as value
    """

    # Simulated RAM usage data based on device_id hash
    hash_value = hash(device_id)
    total_ram = (hash_value % 16 + 1) * 1024  # Total RAM in MB (1GB to 16GB)
    used_ram = hash_value % total_ram  # Used RAM in MB

    # Simulated individual stick usage
    ram_sticks = 4
    stick_usage = {
        i: (used_ram // ram_sticks) + (i * 10) % 50 for i in range(ram_sticks)
    }

    if specify_individual_stick is not None:
        if specify_individual_stick < 0 or specify_individual_stick >= ram_sticks:
            raise ValueError(f"Invalid RAM stick index: {specify_individual_stick}")
        return {
            "device_id": device_id,
            "total_usage": used_ram,
            "individual_stick_usage": {
                specify_individual_stick: stick_usage[specify_individual_stick]
            },
        }

    return {
        "device_id": device_id,
        "total_usage": used_ram,
        "individual_stick_usage": stick_usage,
    }


from typing import Dict, List


def get_regional_holidays(
    regions: Union[str, List[str]], date: str
) -> Dict[str, List[str]]:
    """Return public holidays for given regions on a date.

    Args:
        regions: Region codes to get holidays for. Can be either:
            - A single region code string (e.g., 'US-NY', 'PT', 'NZ')
            - A list of region codes (e.g., ['US-NY', 'PT', 'NZ'])
        date: The date to check for holidays in YYYY-MM-DD format

    Returns:
        Dict containing:
            - region: List of holiday names for the specified date
    """

    # Convert single string to list if needed
    if isinstance(regions, str):
        regions_list = [regions]
    elif isinstance(regions, list):
        regions_list = regions
    else:
        raise ValueError("Regions must be a string or list of strings")

    # Sample holiday data
    holidays_data = {
        "US-NY": {
            "2023-12-25": ["Christmas Day"],
            "2023-07-04": ["Independence Day"],
        },
        "PT": {
            "2023-04-25": ["Freedom Day"],
            "2023-12-25": ["Natal"],
        },
        "NZ": {
            "2023-02-06": ["Waitangi Day"],
            "2023-12-25": ["Christmas Day"],
        },
        "JP-26": {
            "2023-12-25": ["Christmas Day"],
            "2023-05-03": ["Constitution Memorial Day"],
            "2023-11-03": ["Culture Day"],
        },
    }

    result = {}
    for region in regions_list:
        if region not in holidays_data:
            raise ValueError(f"Region not supported: {region}")

        holidays = holidays_data.get(region, {}).get(date, [])
        result[region] = holidays

    return result


import hashlib
from datetime import datetime, timedelta
from typing import Dict


def get_time(location: str) -> Dict[str, str]:
    """Get the current time for a given location.

    Args:
        location: The city name to get the current time for (e.g. 'London', 'New York')

    Returns:
        Dict containing:
            - location: City name
            - current_time: Current time in HH:MM format
    """

    # Sample time zones for demonstration purposes
    time_zones = {
        "New York": -4,
        "London": 0,
        "Tokyo": 9,
        "Sydney": 10,
    }

    if location not in time_zones:
        raise ValueError(f"Location not supported: {location}")

    # Get the current UTC time
    utc_now = datetime.utcnow()

    # Calculate the local time based on the location's time zone
    local_time = utc_now + timedelta(hours=time_zones[location])

    # Format the local time in HH:MM format
    formatted_time = local_time.strftime("%H:%M")

    return {
        "location": location,
        "current_time": formatted_time,
    }


def is_divisible(num_a: float, num_b: float) -> Dict[str, Union[bool, str]]:
    """Check if one number is divisible by another without a remainder.

    Args:
        num_a: Number to check if divisible by num_b
        num_b: Number to check if divides num_a without a remainder

    Returns:
        Dict containing:
            - divisible: Boolean indicating if num_a is divisible by num_b
            - message: Explanation of the result
    """
    if num_b == 0:
        raise ValueError("Division by zero is not allowed")

    divisible = num_a % num_b == 0
    message = (
        f"{num_a} is divisible by {num_b}."
        if divisible
        else f"{num_a} is not divisible by {num_b}."
    )

    return {
        "divisible": divisible,
        "message": message,
    }


def is_square_of(num_a: float, num_b: float) -> Dict[str, Union[bool, float]]:
    """Check if num_a is the square of num_b.

    Args:
        num_a: Number to check if a square of num_b
        num_b: Number to check if squared will equal to num_a

    Returns:
        Dict containing:
            - is_square: Boolean indicating if num_a is the square of num_b
            - num_a: The original number checked
            - num_b: The number whose square was checked
    """
    if num_b == 0:
        if num_a == 0:
            return {"is_square": True, "num_a": num_a, "num_b": num_b}
        else:
            return {"is_square": False, "num_a": num_a, "num_b": num_b}

    is_square = num_a == num_b**2
    return {
        "is_square": is_square,
        "num_a": num_a,
        "num_b": num_b,
    }


import math
from typing import Dict, Union


def is_squared(num: float) -> Dict[str, Union[bool, float]]:
    """Check if a number is a perfect square of an integer.

    Args:
        num: Number to check if it is a perfect square

    Returns:
        Dict containing:
            - is_square: Boolean indicating if the number is a perfect square
            - square_root: The integer square root if it is a perfect square, otherwise -1
    """
    if num < 0:
        return {"is_square": False, "square_root": -1}

    root = math.isqrt(int(num))
    is_square = root * root == num

    return {
        "is_square": is_square,
        "square_root": root if is_square else -1,
    }


import hashlib
from typing import Dict, List, Union
from urllib.parse import urlparse


def link_analyzer(url: str) -> Dict[str, Union[str, List[str]]]:
    """Provide analysis of hyperlinks from a given URL.

    Args:
        url: URL for which to analyze hyperlinks.

    Returns:
        Dict containing:
            - url: The original URL
            - domain: The domain extracted from the URL
            - links: List of hyperlinks found on the page
    """
    if not url.startswith(("http://", "https://")):
        raise ValueError(
            "Invalid URL format. URL must start with 'http://' or 'https://'"
        )

    # Simulate domain extraction
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Generate mock links based on the hash of the URL
    hash_object = hashlib.md5(url.encode())
    hash_digest = hash_object.hexdigest()

    # Create a list of mock links
    links = [f"https://{domain}/page/{i}" for i in range(1, 6)]

    # Shuffle links based on hash digest to simulate variability
    links = sorted(links, key=lambda x: hash_digest)

    return {
        "url": url,
        "domain": domain,
        "links": links,
    }


from typing import Dict, List, Union


def query_data(
    table_name: str,
    columns: Union[List[str], str] = None,
    where: Union[Dict[str, Union[str, int, float]], str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]:
    """Execute a query on a table and return results.

    Args:
        table_name: Name of the table to query.
        columns: List of column names to select.
        where: Conditions for filtering query results. Can be a dictionary of column-value pairs
               or a SQL-like WHERE clause string.

    Returns:
        Dict containing:
            - table_name: Name of the queried table
            - results: List of dictionaries representing rows with selected columns
    """
    # Mock database schema
    mock_db = {
        "employees": [
            {"id": 1, "name": "Alice", "age": 30, "department": "HR"},
            {"id": 2, "name": "Bob", "age": 25, "department": "Engineering"},
            {"id": 3, "name": "Charlie", "age": 35, "department": "Sales"},
        ],
        "departments": [
            {"id": 1, "name": "HR"},
            {"id": 2, "name": "Engineering"},
            {"id": 3, "name": "Sales"},
        ],
    }

    if table_name not in mock_db:
        raise ValueError(f"Table not found: {table_name}")

    # Convert columns parameter if provided as string
    if isinstance(columns, str):
        if columns == "*":
            # Handle wildcard selector
            columns = None
        elif columns.startswith("[") and columns.endswith("]"):
            # Handle string representation of list like "['id', 'name']"
            try:
                import ast

                parsed_columns = ast.literal_eval(columns)
                if isinstance(parsed_columns, list):
                    columns = parsed_columns
                else:
                    raise ValueError("Invalid columns format. Expected a list.")
            except (ValueError, SyntaxError):
                raise ValueError(
                    "Invalid columns format. Expected a valid list representation."
                )
        else:
            # Handle comma-separated string like "id, name, age"
            columns = [col.strip() for col in columns.split(",")]
    
    # Convert where parameter if provided as string
    if isinstance(where, str):
        # For SQL-like WHERE clauses, we'll simply accept them as valid
        # In a real implementation, this would parse the SQL WHERE clause
        # For now, we'll treat any string as a placeholder condition and return all rows
        # This prevents the conversion error while maintaining backward compatibility
        where = None  # Ignore the SQL string for this mock implementation

    # Select all columns if none are specified
    if columns is None:
        columns = list(mock_db[table_name][0].keys())

    # Filter rows based on 'where' conditions
    def row_matches_conditions(row):
        if where is None:
            return True
        return all(row.get(key) == value for key, value in where.items())

    # Generate results based on columns and conditions
    results = [
        {col: row[col] for col in columns if col in row}
        for row in mock_db[table_name]
        if row_matches_conditions(row)
    ]

    return {
        "table_name": table_name,
        "results": results,
    }


from typing import Dict


def reset(username: str) -> Dict[str, str]:
    """Reset user password by generating an MFA request.

    Args:
        username: The username for which to reset the password (e.g., email or phone number)

    Returns:
        Dict containing:
            - username: The username for which the password reset was requested
            - mfa_token: A mock MFA token generated for the user
            - status: Status of the password reset request
    """
    if not username:
        raise ValueError("Username must be provided")

    # Mock MFA token generation using a simple hash-based approach
    mfa_token = f"mfa_{hash(username) % 10000:04d}"

    return {
        "username": username,
        "mfa_token": mfa_token,
        "status": "MFA request generated",
    }


from typing import Dict, List, Union


def search_web(
    query: str,
    recency_days: Union[int, None] = None,
    domains: Union[List[str], None] = None,
    top_k: Union[int, None] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Search the live web for up-to-date or niche information.

    Args:
        query: Natural-language search query to run.
        recency_days: Restrict results to the last N days.
        domains: Optional list of domains to prefer or restrict to.
        top_k: Maximum number of results to retrieve.

    Returns:
        Dict containing:
            - query: The search query used
            - results: List of search results with title, snippet, and domain
    """
    if not query:
        raise ValueError("Query must be provided")

    # Simulate search results with hash-based generation for consistency
    import hashlib

    def generate_result(query: str, domain: str) -> Dict[str, Union[str, int]]:
        hash_value = int(hashlib.sha256((query + domain).encode()).hexdigest(), 16)
        return {
            "title": f"Result for {query} on {domain}",
            "snippet": f"Snippet of content related to {query} from {domain}.",
            "domain": domain,
            "rank": hash_value % 100,
        }

    # Sample domains if none provided
    sample_domains = ["example.com", "sample.org", "testsite.net"]
    if domains is None:
        domains = sample_domains

    # Generate results
    results = [generate_result(query, domain) for domain in domains]

    # Sort results by rank and apply top_k limit
    results.sort(key=lambda x: x["rank"])
    if top_k is not None:
        results = results[:top_k]

    return {
        "query": query,
        "results": results,
    }


def square(num: float) -> Dict[str, Union[float, str]]:
    """Square a given number.

    Args:
        num: The number to square

    Returns:
        Dict containing:
            - original: The original number
            - squared: The squared result
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")

    squared_value = num**2
    return {
        "original": num,
        "squared": squared_value,
    }


from typing import Dict, Literal, Optional, Union


def unit_converter(
    value: float,
    from_unit: str,
    to_unit: str,
    rate: Optional[float] = None,
    round_to: Optional[int] = None,
) -> Dict[str, Union[float, str]]:
    """Convert a numeric value from one unit to another.

    Args:
        value: The numeric value to convert.
        from_unit: The source unit symbol/name (e.g., "km", "lb", "C").
        to_unit: The target unit symbol/name (e.g., "mi", "kg", "F").
        rate: Optional direct conversion rate.
        round_to: Optional number of decimal places to round the result to.

    Returns:
        Dict containing:
            - value: Converted numeric value
            - unit: Unit of the converted value
    """
    # Predefined conversion rates for length and mass
    conversion_rates = {
        ("km", "mi"): 0.621371,
        ("mi", "km"): 1.60934,
        ("lb", "kg"): 0.453592,
        ("kg", "lb"): 2.20462,
    }

    # Temperature conversion
    if from_unit in ["C", "F"] and to_unit in ["C", "F"]:
        if from_unit == to_unit:
            converted_value = value
        elif from_unit == "C" and to_unit == "F":
            converted_value = value * 9 / 5 + 32
        elif from_unit == "F" and to_unit == "C":
            converted_value = (value - 32) * 5 / 9
    # Currency or other direct rate conversion
    elif rate is not None:
        converted_value = value * rate
    # Length and mass conversion using predefined rates
    elif (from_unit, to_unit) in conversion_rates:
        converted_value = value * conversion_rates[(from_unit, to_unit)]
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")

    if round_to is not None:
        converted_value = round(converted_value, round_to)

    return {"value": converted_value, "unit": to_unit}


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
