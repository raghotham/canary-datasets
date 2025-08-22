# Education Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def get_element_from_index(index: int) -> Dict[str, Union[int, str]]:
    """Get the element from the periodic table based on its index.

    Args:
        index: The index of the element in the periodic table (1-based index)

    Returns:
        Dict containing:
            - index: The index of the element
            - element: The name of the element corresponding to the index
    """
    periodic_table = [
        "Hydrogen",
        "Helium",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon",
        "Sodium",
        "Magnesium",
        "Aluminum",
        "Silicon",
        "Phosphorus",
        "Sulfur",
        "Chlorine",
        "Argon",
        "Potassium",
        "Calcium",
        # ... (list continues for all elements)
    ]

    if index < 1 or index > len(periodic_table):
        raise ValueError(f"Index out of range: {index}")

    return {
        "index": index,
        "element": periodic_table[index - 1],
    }


from typing import Dict


def get_element_number(element: str) -> Dict[str, int]:
    """Get the atomic number of a provided element from the periodic table.

    Args:
        element: The name of the element to get the atomic number for (e.g. 'Hydrogen', 'Oxygen')

    Returns:
        Dict containing:
            - element: Name of the element
            - atomic_number: Atomic number of the element
    """

    periodic_table = {
        "Hydrogen": 1,
        "Helium": 2,
        "Lithium": 3,
        "Beryllium": 4,
        "Boron": 5,
        "Carbon": 6,
        "Nitrogen": 7,
        "Oxygen": 8,
        "Fluorine": 9,
        "Neon": 10,
    }

    if element not in periodic_table:
        raise ValueError(f"Element not found: {element}")

    return {
        "element": element,
        "atomic_number": periodic_table[element],
    }


from typing import Dict, List, Optional


def recommend_book(
    author: Optional[List[str]] = None,
    genre: Optional[List[str]] = None,
    avaliable: bool = True,
    previously_enjoyed_book: Optional[List[str]] = None,
    previously_disliked_book: Optional[List[str]] = None,
) -> Dict[str, str]:
    """Recommend a book based on user preferences.

    Args:
        author: Authors that the user is interested in
        genre: Genres that the user is interested in
        avaliable: Whether the book is not on loan
        previously_enjoyed_book: List of books the user has previously enjoyed
        previously_disliked_book: List of books the user has previously disliked

    Returns:
        Dict containing:
            - title: Recommended book title
            - author: Author of the recommended book
            - genre: Genre of the recommended book
    """
    sample_books = [
        {"title": "The Great Adventure", "author": "John Doe", "genre": "Adventure"},
        {
            "title": "Mystery of the Old House",
            "author": "Jane Smith",
            "genre": "Mystery",
        },
        {
            "title": "Love in the Time of Algorithms",
            "author": "Emily White",
            "genre": "Romance",
        },
        {
            "title": "The Science of Everything",
            "author": "Albert Newton",
            "genre": "Science",
        },
    ]

    # Filter books based on availability
    if not avaliable:
        sample_books = sample_books[:2]  # Simulate some books being on loan

    # Filter books based on user preferences
    if author:
        sample_books = [book for book in sample_books if book["author"] in author]
    if genre:
        sample_books = [book for book in sample_books if book["genre"] in genre]
    if previously_enjoyed_book:
        sample_books = [
            book
            for book in sample_books
            if book["title"] not in previously_enjoyed_book
        ]
    if previously_disliked_book:
        sample_books = [
            book
            for book in sample_books
            if book["title"] not in previously_disliked_book
        ]

    if not sample_books:
        raise ValueError("No books available that match the given preferences.")

    # Return the first matching book as a recommendation
    recommended_book = sample_books[0]
    return {
        "title": recommended_book["title"],
        "author": recommended_book["author"],
        "genre": recommended_book["genre"],
    }


def accept_applicant(name: str, school: str) -> Dict[str, Union[str, int]]:
    """Officially accept an applicant to a school.

    Args:
        name: The name of the applicant
        school: School the applicant is applying to

    Returns:
        Dict containing:
            - applicant_name: Name of the accepted applicant
            - school_name: Name of the school
            - acceptance_id: Unique acceptance identifier
    """
    if not name or not school:
        raise ValueError("Both 'name' and 'school' must be provided")

    # Generate a unique acceptance ID using a hash-based approach
    acceptance_id = abs(hash(f"{name}-{school}")) % (10**8)

    return {
        "applicant_name": name,
        "school_name": school,
        "acceptance_id": acceptance_id,
    }


from typing import Dict, Union


def admit_student(app_id: int, type_number: int) -> Dict[str, Union[int, str]]:
    """Admit a student of type II or III to the university.

    Args:
        app_id: Student application number
        type_number: Student type (should be either 2 or 3)

    Returns:
        Dict containing:
            - app_id: The application ID of the student
            - status: Admission status message

    Raises:
        ValueError: If the type_number is not 2 or 3
    """
    if type_number not in (2, 3):
        raise ValueError(
            f"Invalid student type: {type_number}. Only type 2 or 3 are allowed."
        )

    # Simulating a hash-based admission decision for consistency
    decision_hash = hash((app_id, type_number)) % 2
    status = "admitted" if decision_hash == 0 else "waitlisted"

    return {
        "app_id": app_id,
        "status": status,
    }


from typing import Dict, Union


def admit_student_admission(
    app_id: int, type_number: Union[bool, None] = None
) -> Dict[str, Union[int, str, bool]]:
    """Admit a student to the university admit pool before admission.

    Args:
        app_id: Student application number
        type_number: Boolean indicating student type (e.g., international or domestic)

    Returns:
        Dict containing:
            - app_id: Student application number
            - status: Admission status message
            - type_number: Provided student type or default if not provided
    """

    if app_id <= 0:
        raise ValueError("Invalid application ID. Must be a positive integer.")

    # Simulate admission process
    admission_status = "Admitted" if app_id % 2 == 0 else "Pending Review"
    type_number = type_number if type_number is not None else False

    return {
        "app_id": app_id,
        "status": admission_status,
        "type_number": type_number,
    }


from typing import Dict


def admit_student_c(
    app_id: int, type_number: int, admitted: bool
) -> Dict[str, Union[int, bool, str]]:
    """Admit a student of type II to the university and chemistry program.

    Args:
        app_id: The student application number
        type_number: The student type number
        admitted: Whether the student is admitted

    Returns:
        Dict containing:
            - app_id: The student application number
            - type_number: The student type number
            - admitted: Admission status
            - program: The program the student is admitted to
    """
    if type_number != 2:
        raise ValueError("Only students of type II can be admitted to this program.")

    if not admitted:
        raise ValueError("Student must be marked as admitted to proceed.")

    return {
        "app_id": app_id,
        "type_number": type_number,
        "admitted": admitted,
        "program": "Chemistry",
    }


from typing import Dict, List, Union


def admit_students_e(
    app_id: Union[List[int], str], type_number: int, admitted: bool
) -> Dict[str, Union[List[int], str]]:
    """Admit students of type III to the university engineering program.

    Args:
        app_id: List of student application numbers
        type_number: The type number of the students
        admitted: Boolean indicating if the students are admitted

    Returns:
        Dict containing:
            - admitted_ids: List of admitted student application numbers
            - status: Admission status message
    """
    
    # Convert app_id parameter if provided as string
    if isinstance(app_id, str):
        if app_id.startswith('[') and app_id.endswith(']'):
            # Handle string representation of list like "[88290, 44992]"
            try:
                import ast
                parsed_app_id = ast.literal_eval(app_id)
                if isinstance(parsed_app_id, list):
                    app_id = [int(x) for x in parsed_app_id]
                else:
                    raise ValueError("Invalid app_id format. Expected a list.")
            except (ValueError, SyntaxError):
                raise ValueError("Invalid app_id format. Expected a valid list representation.")
        elif ',' in app_id:
            # Handle comma-separated string like "88290,44992"
            try:
                app_id = [int(x.strip()) for x in app_id.split(',')]
            except ValueError:
                raise ValueError("Invalid app_id format. All values must be integers.")
        else:
            # Handle single integer string like "88290"
            try:
                app_id = [int(app_id)]
            except ValueError:
                raise ValueError("Invalid app_id format. Must be an integer or list of integers.")
    
    if type_number != 3:
        raise ValueError("Only students of type III can be admitted.")

    if not admitted:
        return {
            "admitted_ids": [],
            "status": "No students were admitted.",
        }

    # Simulate admission process
    admitted_ids = [
        app for app in app_id if app % 2 == 0
    ]  # Example logic: admit even-numbered IDs

    return {
        "admitted_ids": admitted_ids,
        "status": f"{len(admitted_ids)} students admitted successfully.",
    }


from typing import Dict, Union


def attitudinal_psyche_description(attitudinal_psyche_combo: str) -> Dict[str, str]:
    """Return a description of the inputted 4-letter attitudinal psyche combination.

    Args:
        attitudinal_psyche_combo: The attitudinal psyche combination that the user wants a description of.

    Returns:
        Dict containing:
            - combination: The inputted attitudinal psyche combination
            - description: A brief description of the combination
    """

    descriptions = {
        "ABCD": "ABCD represents a balanced and harmonious psyche, often seen as adaptable and diplomatic.",
        "EFGH": "EFGH indicates a strong-willed and determined personality, with a focus on achieving goals.",
        "IJKL": "IJKL is characterized by creativity and intuition, often thriving in artistic environments.",
        "MNOP": "MNOP signifies a logical and analytical mindset, excelling in problem-solving and strategy.",
    }

    if attitudinal_psyche_combo not in descriptions:
        raise ValueError(
            f"Unsupported attitudinal psyche combination: {attitudinal_psyche_combo}"
        )

    return {
        "combination": attitudinal_psyche_combo,
        "description": descriptions[attitudinal_psyche_combo],
    }


from typing import Dict, Literal, Union


def calculate_final_grade(
    student_id: str,
    method: Literal["average", "weighted", "highest", "drop_lowest"],
    method_parameters: Dict[str, Union[List[float], int]] = None,
) -> Dict[str, Union[str, float]]:
    """Compute a student's overall grade based on a selected calculation method.

    Args:
        student_id: Unique identifier for the student.
        method: Calculation method to use ('average', 'weighted', 'highest', 'drop_lowest').
        method_parameters: Optional extra parameters for the chosen method (e.g. weights for 'weighted', number_to_drop for 'drop_lowest').

    Returns:
        Dict containing:
            - student_id: Unique identifier for the student
            - final_grade: Computed final grade for the student
    """
    # Sample grades for demonstration purposes
    sample_grades = {
        "student_001": [88, 92, 79, 85, 90],
        "student_002": [75, 80, 85, 70, 95],
        "student_003": [90, 93, 88, 84, 91],
    }

    if student_id not in sample_grades:
        raise ValueError(f"Student ID not found: {student_id}")

    grades = sample_grades[student_id]

    if method == "average":
        final_grade = sum(grades) / len(grades)
    elif method == "weighted":
        if not method_parameters or "weights" not in method_parameters:
            raise ValueError("Weights are required for the 'weighted' method")
        weights = method_parameters["weights"]
        if len(weights) != len(grades):
            raise ValueError("Weights and grades must have the same length")
        final_grade = sum(g * w for g, w in zip(grades, weights)) / sum(weights)
    elif method == "highest":
        final_grade = max(grades)
    elif method == "drop_lowest":
        number_to_drop = method_parameters.get("number_to_drop", 1)
        if number_to_drop >= len(grades):
            raise ValueError("Number to drop must be less than the number of grades")
        final_grade = sum(sorted(grades)[number_to_drop:]) / (
            len(grades) - number_to_drop
        )
    else:
        raise ValueError(f"Unsupported method: {method}")

    return {
        "student_id": student_id,
        "final_grade": final_grade,
    }


from typing import Dict


def checkout_ebook(name: str) -> Dict[str, str]:
    """Checkout a given ebook.

    Args:
        name: Name of the ebook to check out.

    Returns:
        Dict containing:
            - name: Name of the ebook
            - status: Checkout status message
    """
    available_ebooks = {
        "The Great Gatsby": "Available",
        "1984": "Checked Out",
        "To Kill a Mockingbird": "Available",
    }

    if name not in available_ebooks:
        raise ValueError(f"Ebook not found: {name}")

    status = available_ebooks[name]
    if status == "Checked Out":
        return {"name": name, "status": "Ebook is currently checked out."}

    # Simulate checking out the ebook
    return {"name": name, "status": "Ebook checked out successfully."}


from typing import Dict, Literal, Union


def create_goal_xp(
    rsn: str, skill: str, target_xp: float, game: Literal["osrs", "rs3"] = "rs3"
) -> Dict[str, Union[str, float, int]]:
    """Create a goal for a skill to track progress towards the skill.

    Args:
        rsn: Runescape player's name
        skill: Skill name
        target_xp: Target XP to reach in a skill
        game: 'osrs' or 'rs3'; defaults to 'rs3'

    Returns:
        Dict containing:
            - rsn: Player's name
            - skill: Skill name
            - current_xp: Current XP in the skill
            - target_xp: Target XP to reach
            - progress_percentage: Percentage of progress towards the goal
            - game: Game type ('osrs' or 'rs3')
    """
    if not rsn or not skill or target_xp <= 0:
        raise ValueError(
            "Invalid input: rsn, skill, and target_xp must be valid and target_xp must be positive."
        )

    # Simulate current XP based on hash of rsn and skill for consistency
    hash_value = hash((rsn, skill)) % 1000000
    current_xp = hash_value % target_xp

    progress_percentage = (current_xp / target_xp) * 100

    return {
        "rsn": rsn,
        "skill": skill,
        "current_xp": current_xp,
        "target_xp": target_xp,
        "progress_percentage": round(progress_percentage, 2),
        "game": game,
    }


from typing import Dict, List


def define_research_question(
    research_question: str,
    inclusion_criteria: List[str],
    exclusion_criteria: List[str],
) -> Dict[str, List[str]]:
    """Define the research question and inclusion/exclusion criteria according to PRISMA guidelines.

    Args:
        research_question: The main research question being addressed.
        inclusion_criteria: List of criteria for including studies in the review.
        exclusion_criteria: List of criteria for excluding studies from the review.

    Returns:
        Dict containing:
            - research_question: The main research question
            - inclusion_criteria: List of inclusion criteria
            - exclusion_criteria: List of exclusion criteria
    """
    if not research_question:
        raise ValueError("Research question must be provided.")
    if not inclusion_criteria:
        raise ValueError("Inclusion criteria must be provided.")
    if not exclusion_criteria:
        raise ValueError("Exclusion criteria must be provided.")

    return {
        "research_question": research_question,
        "inclusion_criteria": inclusion_criteria,
        "exclusion_criteria": exclusion_criteria,
    }


def deny_applicant(name: str, school: str) -> Dict[str, str]:
    """Officially deny an applicant to a school.

    Args:
        name: The name of the applicant
        school: School the applicant is applying to

    Returns:
        Dict containing:
            - message: A formal denial message for the applicant
            - applicant: Name of the applicant
            - school: Name of the school
    """
    if not name or not school:
        raise ValueError("Both 'name' and 'school' must be provided")

    denial_messages = [
        "We regret to inform you that your application has not been successful.",
        "Unfortunately, we are unable to offer you a place at this time.",
        "After careful consideration, we have decided not to proceed with your application.",
    ]

    # Use a simple hash-based selection for consistent message choice
    message_index = (hash(name) + hash(school)) % len(denial_messages)
    message = denial_messages[message_index]

    return {
        "message": message,
        "applicant": name,
        "school": school,
    }


from typing import Dict


def enneagram_description(enneagram: str) -> Dict[str, str]:
    """Return a description of the inputted enneagram type.

    Args:
        enneagram: The enneagram type that the user wants a description of. Just input the core enneagram number, without the wing.

    Returns:
        Dict containing:
            - enneagram: The enneagram type
            - description: A brief description of the enneagram type
    """
    descriptions = {
        "1": "The Reformer: Principled, purposeful, self-controlled, and perfectionistic.",
        "2": "The Helper: Generous, demonstrative, people-pleasing, and possessive.",
        "3": "The Achiever: Adaptable, excelling, driven, and image-conscious.",
        "4": "The Individualist: Expressive, dramatic, self-absorbed, and temperamental.",
        "5": "The Investigator: Perceptive, innovative, secretive, and isolated.",
        "6": "The Loyalist: Engaging, responsible, anxious, and suspicious.",
        "7": "The Enthusiast: Spontaneous, versatile, acquisitive, and scattered.",
        "8": "The Challenger: Self-confident, decisive, willful, and confrontational.",
        "9": "The Peacemaker: Receptive, reassuring, complacent, and resigned.",
    }

    if enneagram not in descriptions:
        raise ValueError(f"Unsupported enneagram type: {enneagram}")

    return {
        "enneagram": enneagram,
        "description": descriptions[enneagram],
    }


from typing import Dict


def enneagram_tritype_description(tritype: str) -> Dict[str, str]:
    """Return a description of the inputted 3-digit enneagram tritype.

    Args:
        tritype: The 3-digit enneagram tritype that the user wants a description of.

    Returns:
        Dict containing:
            - tritype: The inputted tritype
            - description: A brief description of the tritype
    """
    descriptions = {
        "123": "The Achiever: Driven, success-oriented, and pragmatic.",
        "456": "The Loyal Skeptic: Responsible, committed, and security-oriented.",
        "789": "The Peacemaker: Easygoing, self-effacing, and accommodating.",
        "258": "The Helper: Caring, interpersonal, and generous.",
        "369": "The Mediator: Harmonious, balanced, and diplomatic.",
    }

    if tritype not in descriptions:
        raise ValueError(f"Tritype not supported: {tritype}")

    return {
        "tritype": tritype,
        "description": descriptions[tritype],
    }


import hashlib
from typing import Dict, Literal, Union


def export_grades(
    format: Literal["csv", "xlsx", "pdf"],
    scope: Literal["student", "class"],
    student_id: str = None,
) -> Dict[str, Union[str, list]]:
    """Export student grades in a chosen file format.

    Args:
        format: File format for export ('csv', 'xlsx', 'pdf')
        scope: Specify 'student' or 'class'
        student_id: Unique identifier for the student (required if scope is 'student')

    Returns:
        Dict containing:
            - file_name: Name of the exported file
            - content: List of grades or a message indicating the export status
    """
    if scope == "student" and not student_id:
        raise ValueError("student_id is required when scope is 'student'")

    # Mock data generation based on scope
    if scope == "student":
        # Generate a consistent hash-based grade list for the student
        hash_object = hashlib.md5(student_id.encode())
        grades = [int(hash_object.hexdigest(), 16) % 100 for _ in range(5)]
        file_name = f"student_{student_id}_grades.{format}"
    else:
        # Generate a consistent hash-based grade list for a class
        hash_object = hashlib.md5("class".encode())
        grades = [int(hash_object.hexdigest(), 16) % 100 for _ in range(30)]
        file_name = f"class_grades.{format}"

    # Simulate file content based on the format
    if format == "csv":
        content = [f"Grade {i+1}: {grade}" for i, grade in enumerate(grades)]
    elif format == "xlsx":
        content = [f"Excel Grade {i+1}: {grade}" for i, grade in enumerate(grades)]
    elif format == "pdf":
        content = [f"PDF Grade {i+1}: {grade}" for i, grade in enumerate(grades)]
    else:
        raise ValueError(f"Unsupported format: {format}")

    return {"file_name": file_name, "content": content}


from typing import Dict, Union


def find_boiling_point(element: str) -> Dict[str, Union[str, float]]:
    """Find the boiling point of a given element.

    Args:
        element: The chemical element to find the boiling point for (e.g. 'Hydrogen', 'Oxygen')

    Returns:
        Dict containing:
            - element: Name of the element
            - boiling_point: Boiling point in Kelvin

    Raises:
        ValueError: If the element is not supported
    """

    sample_boiling_points = {
        "Hydrogen": 20.28,
        "Helium": 4.22,
        "Oxygen": 90.2,
        "Nitrogen": 77.36,
        "Carbon": 4300.0,
    }

    if element not in sample_boiling_points:
        raise ValueError(f"Element not supported: {element}")

    return {
        "element": element,
        "boiling_point": sample_boiling_points[element],
    }


from typing import Dict, List


def find_homologs(
    gene_symbol: str, target_organism: str
) -> Dict[str, Union[str, List[str]]]:
    """Find homologous sequences for a gene in a target organism.

    Args:
        gene_symbol: Gene to search by symbol.
        target_organism: Scientific name of the target organism, e.g., 'Mus musculus'.

    Returns:
        Dict containing:
            - gene_symbol: The gene symbol used for the search
            - target_organism: The scientific name of the target organism
            - homologs: List of homologous gene sequences
    """

    # Sample data for demonstration purposes
    sample_data = {
        ("BRCA1", "Mus musculus"): ["ENSMUSG00000017146", "ENSMUSG00000017147"],
        ("TP53", "Mus musculus"): ["ENSMUSG00000059552"],
        ("BRCA1", "Homo sapiens"): ["ENSG00000012048"],
        ("HBA1", "Homo sapiens"): ["ENSG00000206172"],
        ("HBA1", "Mus musculus"): ["ENSMUSG00000069919"],
    }

    key = (gene_symbol, target_organism)
    if key not in sample_data:
        raise ValueError(
            f"No homologous sequences found for gene '{gene_symbol}' in '{target_organism}'"
        )

    return {
        "gene_symbol": gene_symbol,
        "target_organism": target_organism,
        "homologs": sample_data[key],
    }


from typing import Dict, List


def flag_at_risk_students(threshold: float) -> Dict[str, List[str]]:
    """Identify students whose grades fall below a defined threshold.

    Args:
        threshold: Minimum passing grade threshold.

    Returns:
        Dict containing:
            - at_risk_students: List of student names who are at risk
    """

    # Sample student data with grades
    student_grades = {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 68,
        "David": 90,
        "Eva": 59,
        "Frank": 77,
        "Grace": 65,
    }

    if threshold < 0 or threshold > 100:
        raise ValueError("Threshold must be between 0 and 100")

    at_risk_students = [
        student for student, grade in student_grades.items() if grade < threshold
    ]

    return {"at_risk_students": at_risk_students}


from typing import Dict, List, Literal, Union


def generate_grade_report(
    scope: Literal["student", "class"], student_id: str = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Generate a detailed grade report for a student or the entire class.

    Args:
        scope: Specify 'student' or 'class'.
        student_id: Unique identifier for the student (required if scope is 'student').

    Returns:
        Dict containing:
            - scope: The scope of the report ('student' or 'class')
            - report: List of dictionaries with student grade details
                - student_id: Unique identifier for the student
                - name: Name of the student
                - grades: List of grades for different subjects
                - average: Average grade of the student
    """
    if scope == "student" and not student_id:
        raise ValueError("student_id is required when scope is 'student'.")

    # Sample data for demonstration
    students_data = {
        "S001": {"name": "Alice", "grades": {"Math": 85, "Science": 90, "English": 78}},
        "S002": {"name": "Bob", "grades": {"Math": 88, "Science": 76, "English": 92}},
        "S003": {
            "name": "Charlie",
            "grades": {"Math": 95, "Science": 89, "English": 85},
        },
    }

    def calculate_average(grades: Dict[str, float]) -> float:
        return sum(grades.values()) / len(grades)

    if scope == "student":
        if student_id not in students_data:
            raise ValueError(f"Student ID not found: {student_id}")
        student_info = students_data[student_id]
        average = calculate_average(student_info["grades"])
        report = [
            {
                "student_id": student_id,
                "name": student_info["name"],
                "grades": student_info["grades"],
                "average": average,
            }
        ]
    elif scope == "class":
        report = []
        for sid, info in students_data.items():
            average = calculate_average(info["grades"])
            report.append(
                {
                    "student_id": sid,
                    "name": info["name"],
                    "grades": info["grades"],
                    "average": average,
                }
            )
    else:
        raise ValueError("Invalid scope. Must be 'student' or 'class'.")

    return {
        "scope": scope,
        "report": report,
    }


from typing import Dict


def generate_prisma_flow_diagram(
    identification_count: int,
    screened_count: int,
    excluded_count: int,
    included_count: int,
) -> Dict[str, int]:
    """Generate a PRISMA flow diagram summarizing study selection process.

    Args:
        identification_count: Number of records identified through database searching.
        screened_count: Number of records screened after deduplication.
        excluded_count: Number of records excluded after screening.
        included_count: Number of studies included in qualitative and/or quantitative synthesis.

    Returns:
        Dict containing:
            - identification: Number of records identified
            - screened: Number of records screened
            - excluded: Number of records excluded
            - included: Number of studies included
    """
    if (
        identification_count < 0
        or screened_count < 0
        or excluded_count < 0
        or included_count < 0
    ):
        raise ValueError("Counts cannot be negative")

    if screened_count > identification_count:
        raise ValueError("Screened count cannot exceed identification count")

    if excluded_count > screened_count:
        raise ValueError("Excluded count cannot exceed screened count")

    if included_count > (screened_count - excluded_count):
        raise ValueError(
            "Included count cannot exceed available records after exclusion"
        )

    return {
        "identification": identification_count,
        "screened": screened_count,
        "excluded": excluded_count,
        "included": included_count,
    }


from typing import Dict, Union


def get_author_bio(author: str) -> Dict[str, Union[str, int]]:
    """Retrieve a biography for a given author.

    Args:
        author: The author's full name

    Returns:
        Dict containing:
            - name: Author's full name
            - birth_year: Year the author was born
            - biography: A short biography of the author
    """

    sample_bios = {
        "Jane Austen": {
            "birth_year": 1775,
            "biography": "Jane Austen was an English novelist known primarily for her six major novels, "
            "which interpret, critique and comment upon the British landed gentry at the end of the 18th century.",
        },
        "Mark Twain": {
            "birth_year": 1835,
            "biography": "Mark Twain, born Samuel Langhorne Clemens, was an American writer, humorist, entrepreneur, "
            "publisher, and lecturer. He was lauded as the 'greatest humorist the United States has produced'.",
        },
        "George Orwell": {
            "birth_year": 1903,
            "biography": "George Orwell was an English novelist, essayist, journalist and critic. His work is "
            "characterized by lucid prose, biting social criticism, opposition to totalitarianism, and outspoken support of democratic socialism.",
        },
    }

    if author not in sample_bios:
        raise ValueError(f"Author not found: {author}")

    return {
        "name": author,
        "birth_year": sample_bios[author]["birth_year"],
        "biography": sample_bios[author]["biography"],
    }


from typing import Dict


def get_book_summary(title: str) -> Dict[str, str]:
    """Retrieve a detailed summary of a specific book.

    Args:
        title: The exact title of the book

    Returns:
        Dict containing:
            - title: The title of the book
            - author: The author of the book
            - summary: A brief summary of the book's plot
    """

    sample_summaries = {
        "1984": {
            "author": "George Orwell",
            "summary": "A dystopian novel set in a totalitarian society under constant surveillance.",
        },
        "To Kill a Mockingbird": {
            "author": "Harper Lee",
            "summary": "A novel about racial injustice in the Deep South, seen through the eyes of a young girl.",
        },
        "The Great Gatsby": {
            "author": "F. Scott Fitzgerald",
            "summary": "A critique of the American Dream, centered around the mysterious Jay Gatsby.",
        },
    }

    if title not in sample_summaries:
        raise ValueError(f"Book not found: {title}")

    return {
        "title": title,
        "author": sample_summaries[title]["author"],
        "summary": sample_summaries[title]["summary"],
    }


from typing import Dict, List, Literal, Union


def get_dataset_metadata(
    search_query: Union[str, None] = None,
    limit: int = 100,
    offset: int = 0,
    sort_by: Literal["date_created", "date_modified", "alphabetical"] = "alphabetical",
) -> Dict[str, Union[List[Dict[str, Union[str, List[str]]]], int]]:
    """Retrieve metadata about datasets from the Austin Open Data Portal.

    Args:
        search_query: Text to search for in dataset titles or descriptions.
        limit: Number of datasets to return.
        offset: Number of datasets to skip before returning results.
        sort_by: How to sort the results. Options: 'date_created', 'date_modified', or 'alphabetical'.

    Returns:
        Dict containing:
            - datasets: List of datasets with metadata including title, description, categories, and dataset ID.
            - total_count: Total number of datasets matching the search criteria.
    """

    # Sample data simulating datasets
    sample_datasets = [
        {
            "id": "1",
            "title": "Austin Traffic Data",
            "description": "Traffic data for Austin city",
            "categories": ["Transportation", "Public Safety"],
        },
        {
            "id": "2",
            "title": "Austin Crime Reports",
            "description": "Crime reports in Austin",
            "categories": ["Public Safety"],
        },
        {
            "id": "3",
            "title": "Austin Parks Information",
            "description": "Information about parks in Austin",
            "categories": ["Recreation", "Environment"],
        },
        {
            "id": "4",
            "title": "Austin Water Usage",
            "description": "Water usage statistics in Austin",
            "categories": ["Utilities", "Environment"],
        },
        {
            "id": "5",
            "title": "Austin Housing Data",
            "description": "Housing data and statistics for Austin",
            "categories": ["Housing", "Economy"],
        },
    ]

    # Filter datasets based on search_query
    if search_query:
        sample_datasets = [
            dataset
            for dataset in sample_datasets
            if search_query.lower() in dataset["title"].lower()
            or search_query.lower() in dataset["description"].lower()
        ]

    # Sort datasets
    if sort_by == "alphabetical":
        sample_datasets.sort(key=lambda x: x["title"])
    elif sort_by == "date_created":
        # Simulate sorting by date_created
        sample_datasets.sort(key=lambda x: x["id"])
    elif sort_by == "date_modified":
        # Simulate sorting by date_modified
        sample_datasets.sort(key=lambda x: x["id"], reverse=True)

    # Apply offset and limit
    datasets = sample_datasets[offset : offset + limit]

    return {"datasets": datasets, "total_count": len(sample_datasets)}


from typing import Dict


def get_gene_summary(gene_symbol: str) -> Dict[str, str]:
    """Returns a short official summary for a gene symbol.

    Args:
        gene_symbol: Official gene symbol, e.g., 'HBA1', 'TP53'.

    Returns:
        Dict containing:
            - gene_symbol: The input gene symbol
            - summary: A short official summary of the gene
    """

    sample_summaries = {
        "HBA1": "HBA1 is a gene that encodes the alpha 1 subunit of hemoglobin, which is involved in oxygen transport in the blood.",
        "TP53": "TP53 is a tumor suppressor gene that regulates the cell cycle and prevents cancer formation.",
        "BRCA1": "BRCA1 is a gene that produces a protein responsible for repairing DNA, playing a role in maintaining genomic stability.",
        "HBA1": "The HBA1 gene provides instructions for making a protein called alpha-globin.",
    }

    if gene_symbol not in sample_summaries:
        raise ValueError(f"Gene symbol not supported: {gene_symbol}")

    return {
        "gene_symbol": gene_symbol,
        "summary": sample_summaries[gene_symbol],
    }


def hold_ebook(name: str) -> Dict[str, Union[str, bool]]:
    """Place a hold for a given ebook.

    Args:
        name: Name of the ebook to place a hold for.

    Returns:
        Dict containing:
            - name: Name of the ebook
            - hold_placed: Boolean indicating if the hold was successfully placed
    """
    available_ebooks = {
        "The Great Gatsby": True,
        "1984": False,
        "To Kill a Mockingbird": True,
        "Moby Dick": False,
    }

    if name not in available_ebooks:
        raise ValueError(f"Ebook not found: {name}")

    hold_placed = available_ebooks[name]
    return {
        "name": name,
        "hold_placed": hold_placed,
    }


from typing import Dict, List


def list_instruments() -> Dict[str, List[Dict[str, str]]]:
    """List supported lab instruments and their time-slot granularity.

    Returns:
        Dict containing:
            - instruments: List of dictionaries with:
                - name: Name of the instrument
                - granularity: Time-slot granularity for booking
    """

    instruments = [
        {"name": "Microscope", "granularity": "15 minutes"},
        {"name": "Spectrometer", "granularity": "30 minutes"},
        {"name": "Centrifuge", "granularity": "1 hour"},
        {"name": "PCR Machine", "granularity": "45 minutes"},
    ]

    return {"instruments": instruments}


from typing import Dict, Optional, Union


def math_calculator(
    expression: str, show_steps: Optional[bool] = False, precision: Optional[int] = None
) -> Dict[str, Union[float, str, list]]:
    """Evaluate a mathematical expression exactly as provided.

    Args:
        expression: A single mathematical expression to evaluate (e.g., "(12.4 + 7) / 3").
        show_steps: If true, return a step-by-step breakdown along with the result.
        precision: Optional number of decimal places to round the final result to.

    Returns:
        Dict containing:
            - result: The evaluated result of the expression
            - steps: (Optional) List of steps showing the evaluation process
    """
    try:
        # Evaluate the expression
        result = eval(expression, {"__builtins__": {}})

        # Apply precision if specified
        if precision is not None:
            result = round(result, precision)

        # Prepare the response
        response = {"result": result}

        # Add steps if requested
        if show_steps:
            steps = [f"Evaluating: {expression}", f"Result: {result}"]
            response["steps"] = steps

        return response
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}. Error: {str(e)}")


from typing import Dict


def mbti_description(mbti: str) -> Dict[str, str]:
    """Return a description of the inputted 4-letter MBTI type.

    Args:
        mbti: The 4-letter MBTI type that the user wants a description of.

    Returns:
        Dict containing:
            - mbti: The MBTI type
            - description: A brief description of the MBTI type
    """
    descriptions = {
        "INTJ": "Imaginative and strategic thinkers, with a plan for everything.",
        "ENTP": "Smart and curious thinkers who cannot resist an intellectual challenge.",
        "INFJ": "Quiet and mystical, yet very inspiring and tireless idealists.",
        "ENFP": "Enthusiastic, creative, and sociable free spirits, who can always find a reason to smile.",
        "ISTJ": "Practical and fact-minded individuals, whose reliability cannot be doubted.",
        "ESFJ": "Extraordinarily caring, social, and popular people, always eager to help.",
        "ISFP": "Flexible and charming artists, always ready to explore and experience something new.",
        "ESTP": "Smart, energetic, and very perceptive people, who truly enjoy living on the edge.",
    }

    if mbti not in descriptions:
        raise ValueError(f"MBTI type not supported: {mbti}")

    return {
        "mbti": mbti,
        "description": descriptions[mbti],
    }


from typing import Dict


def save_grade(
    student_id: str, assignment_id: str, grade: float
) -> Dict[str, Union[str, float]]:
    """Add or update a student's grade for a specific assignment or exam.

    Args:
        student_id: Unique identifier for the student.
        assignment_id: Unique identifier for the assignment or exam.
        grade: Grade achieved by the student.

    Returns:
        Dict containing:
            - student_id: The student's unique identifier
            - assignment_id: The assignment's unique identifier
            - grade: The grade that was saved
            - status: Status message indicating success
    """
    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100")

    # Simulate a database with a dictionary
    database = {
        "student_1": {"assignment_1": 85.0, "assignment_2": 90.0},
        "student_2": {"assignment_1": 78.0},
    }

    if student_id not in database:
        database[student_id] = {}

    database[student_id][assignment_id] = grade

    return {
        "student_id": student_id,
        "assignment_id": assignment_id,
        "grade": grade,
        "status": "Grade saved successfully",
    }


from typing import Dict, List, Literal


def screen_studies(
    study_ids: List[str],
    screening_stage: Literal["title_abstract", "full_text"],
    criteria_reference: str,
) -> Dict[str, List[str]]:
    """Screen identified studies for eligibility by title, abstract, and full-text review.

    Args:
        study_ids: List of unique identifiers for studies to be screened.
        screening_stage: The screening stage ('title_abstract' or 'full_text').
        criteria_reference: Reference to inclusion/exclusion criteria definition used in screening.

    Returns:
        Dict containing:
            - included: List of study IDs that meet the criteria
            - excluded: List of study IDs that do not meet the criteria
    """
    if not study_ids:
        raise ValueError("study_ids cannot be empty")
    if screening_stage not in ["title_abstract", "full_text"]:
        raise ValueError(f"Unsupported screening stage: {screening_stage}")

    # Simulate screening process with hash-based decision
    included = []
    excluded = []
    for study_id in study_ids:
        # Use a simple hash to simulate screening decision
        decision = hash(study_id + screening_stage + criteria_reference) % 2
        if decision == 0:
            included.append(study_id)
        else:
            excluded.append(study_id)

    return {
        "included": included,
        "excluded": excluded,
    }


from typing import Dict, List, Optional, Union


def search_author(
    name: Optional[str] = None,
    genre: Optional[str] = None,
    book_titles: Optional[List[str]] = None,
    nationality: Optional[str] = None,
    birth_date: Optional[str] = None,
) -> Dict[str, Union[str, List[str], Dict[str, str]]]:
    """Search for an author by various attributes and return their data.

    Args:
        name: Name of the author to search for.
        genre: Genre associated with the author.
        book_titles: List of book titles written by the author.
        nationality: Nationality of the author.
        birth_date: Birth date of the author in YYYYMMDD format.

    Returns:
        Dict containing:
            - name: Author's name
            - birth_date: Author's birth date
            - nationality: Author's nationality
            - books: List of published books by the author
            - genre: Genre associated with the author
    """
    sample_authors = [
        {
            "name": "Jane Austen",
            "birth_date": "17751216",
            "nationality": "British",
            "books": ["Pride and Prejudice", "Sense and Sensibility"],
            "genre": "Romance",
        },
        {
            "name": "George Orwell",
            "birth_date": "19030625",
            "nationality": "British",
            "books": ["1984", "Animal Farm"],
            "genre": "Dystopian",
        },
        {
            "name": "Gabriel Garcia Marquez",
            "birth_date": "19270306",
            "nationality": "Colombian",
            "books": ["One Hundred Years of Solitude", "Love in the Time of Cholera"],
            "genre": "Magical Realism",
        },
    ]

    for author in sample_authors:
        if (
            (name and author["name"] != name)
            or (genre and author["genre"] != genre)
            or (
                book_titles
                and not any(title in author["books"] for title in book_titles)
            )
            or (nationality and author["nationality"] != nationality)
            or (birth_date and author["birth_date"] != birth_date)
        ):
            continue
        return author

    raise ValueError("No author found matching the given criteria")


from typing import Dict, Optional, Union


def search_book(
    query: str,
    genre: Optional[str] = None,
    author: Optional[str] = None,
    language: Optional[str] = None,
    release_date: Optional[str] = None,
    released_after: Optional[str] = None,
    released_before: Optional[str] = None,
    publisher: Optional[str] = None,
    isbn: Optional[int] = None,
    asin: Optional[int] = None,
) -> Dict[str, Union[str, int, float, list]]:
    """Search for a book using various criteria and return book data in JSON format.

    Args:
        query: Search term for book title
        genre: Search for book in specific genre
        author: Search for book by author
        language: Language of book
        release_date: Exact release date (format: YYYYMMDD)
        released_after: Search for book released after date (format: YYYYMMDD)
        released_before: Search for book released before date (format: YYYYMMDD)
        publisher: Name of publisher of book
        isbn: ISBN number of book
        asin: ASIN number of book

    Returns:
        Dict containing:
            - title: Title of the book
            - author: Author of the book
            - isbn: ISBN number
            - asin: ASIN number
            - genre: Genre of the book
            - language: Language of the book
            - release_date: Release date of the book
            - publisher: Publisher of the book
            - ratings: Average ratings of the book
    """

    # Sample data for demonstration purposes
    sample_books = [
        {
            "title": "The Great Adventure",
            "author": "John Doe",
            "isbn": 1234567890123,
            "asin": 9876543210123,
            "genre": "Adventure",
            "language": "English",
            "release_date": "20220101",
            "publisher": "Adventure Books Inc.",
            "ratings": 4.5,
        },
        {
            "title": "Mystery of the Old House",
            "author": "Jane Smith",
            "isbn": 2345678901234,
            "asin": 8765432101234,
            "genre": "Mystery",
            "language": "English",
            "release_date": "20210515",
            "publisher": "Mystery House",
            "ratings": 4.2,
        },
    ]

    # Filter books based on the provided criteria
    results = []
    for book in sample_books:
        if query.lower() not in book["title"].lower():
            continue
        if genre and genre.lower() != book["genre"].lower():
            continue
        if author and author.lower() != book["author"].lower():
            continue
        if language and language.lower() != book["language"].lower():
            continue
        if release_date and release_date != book["release_date"]:
            continue
        if released_after and book["release_date"] <= released_after:
            continue
        if released_before and book["release_date"] >= released_before:
            continue
        if publisher and publisher.lower() != book["publisher"].lower():
            continue
        if isbn and isbn != book["isbn"]:
            continue
        if asin and asin != book["asin"]:
            continue
        results.append(book)

    if not results:
        raise ValueError("No books found matching the search criteria.")

    return results[0]  # Return the first matching book for simplicity


from typing import Dict, List, Optional


def search_books(
    title: str, author: Optional[str] = None, genre: Optional[str] = None
) -> Dict[str, List[Dict[str, str]]]:
    """Search for books by title, author, or genre.

    Args:
        title: Book title to search for
        author: Book author to search for (optional)
        genre: Genre of the book (e.g., mystery, fantasy, history) (optional)

    Returns:
        Dict containing:
            - books: List of dictionaries with book details, each containing:
                - title: Title of the book
                - author: Author of the book
                - genre: Genre of the book
    """

    sample_books = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "fiction",
        },
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "fiction"},
        {"title": "1984", "author": "George Orwell", "genre": "dystopian"},
        {"title": "Moby Dick", "author": "Herman Melville", "genre": "adventure"},
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "genre": "fiction",
        },
    ]

    def matches(book: Dict[str, str]) -> bool:
        return (
            title.lower() in book["title"].lower()
            and (author is None or author.lower() in book["author"].lower())
            and (genre is None or genre.lower() == book["genre"].lower())
        )

    matched_books = [book for book in sample_books if matches(book)]

    if not matched_books:
        raise ValueError("No books found matching the criteria")

    return {"books": matched_books}


from datetime import datetime
from typing import Dict, List, Union


def search_databases(
    databases: List[str], search_terms: List[str], date_range: Dict[str, str] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, datetime]]]]]:
    """Perform literature searches across specified databases with defined search terms and filters.

    Args:
        databases: List of databases to search (e.g., 'PubMed', 'Cochrane', 'Scopus').
        search_terms: Keywords, phrases, and Boolean operators to use in the search.
        date_range: Start and end dates for the search period in 'YYYY-MM-DD' format.

    Returns:
        Dict containing:
            - databases: List of databases searched
            - results: List of dictionaries with search results, each containing:
                - title: Title of the article
                - authors: Authors of the article
                - publication_date: Date of publication
                - database: Database where the article was found
    """
    if not databases:
        raise ValueError("At least one database must be specified.")
    if not search_terms:
        raise ValueError("At least one search term must be specified.")

    sample_results = [
        {
            "title": "Sample Article on Health",
            "authors": "Doe, J.; Smith, A.",
            "publication_date": datetime(2021, 5, 17),
            "database": "PubMed",
        },
        {
            "title": "Research on Climate Change",
            "authors": "Brown, B.; Green, C.",
            "publication_date": datetime(2020, 11, 23),
            "database": "Scopus",
        },
        {
            "title": "Innovations in Technology",
            "authors": "White, D.; Black, E.",
            "publication_date": datetime(2022, 3, 14),
            "database": "Cochrane",
        },
    ]

    # Filter results based on the specified databases
    filtered_results = [
        result for result in sample_results if result["database"] in databases
    ]

    # Further filter by date range if specified
    if date_range:
        start_date = datetime.strptime(
            date_range.get("start_date", "1900-01-01"), "%Y-%m-%d"
        )
        end_date = datetime.strptime(
            date_range.get("end_date", "2100-01-01"), "%Y-%m-%d"
        )
        filtered_results = [
            result
            for result in filtered_results
            if start_date <= result["publication_date"] <= end_date
        ]

    return {"databases": databases, "results": filtered_results}


from typing import Dict, Union


def student_admission(
    app_id: int, type_number: Union[bool, None] = None
) -> Dict[str, Union[int, str, bool]]:
    """Admit a student to the university based on application details.

    Args:
        app_id: The unique application ID of the student.
        type_number: Boolean indicating the type of student (e.g., True for international, False for domestic).

    Returns:
        Dict containing:
            - app_id: The application ID of the student.
            - admission_status: The status of the admission process.
            - student_type: The type of student (international or domestic).
    """

    if not isinstance(app_id, int) or app_id <= 0:
        raise ValueError("Invalid application ID. It must be a positive integer.")

    # Simulate admission status based on a hash of the app_id
    admission_status = "admitted" if hash(app_id) % 2 == 0 else "waitlisted"

    # Determine student type
    if type_number is None:
        student_type = "unknown"
    else:
        student_type = "international" if type_number else "domestic"

    return {
        "app_id": app_id,
        "admission_status": admission_status,
        "student_type": student_type,
    }


from typing import Dict


def student_admit_type(app_id: int, type_number: int) -> Dict[str, Union[int, str]]:
    """Assign a student type to a student based on application ID and type number.

    Args:
        app_id: The student application number.
        type_number: The student type number.

    Returns:
        Dict containing:
            - app_id: The student application number.
            - type: The assigned student type as a string.
    """
    type_mapping = {
        1: "Undergraduate",
        2: "Graduate",
        3: "PhD",
        4: "Exchange",
    }

    if type_number not in type_mapping:
        raise ValueError(f"Unsupported type number: {type_number}")

    return {
        "app_id": app_id,
        "type": type_mapping[type_number],
    }


from typing import Dict


def waitlist_applicant(name: str, school: str) -> Dict[str, str]:
    """Officially waitlist an applicant to a school.

    Args:
        name: The name of the applicant
        school: School the applicant is applying to

    Returns:
        Dict containing:
            - applicant_id: Unique identifier for the applicant
            - name: Name of the applicant
            - school: School the applicant is waitlisted for
            - status: Current status of the application
    """
    if not name or not school:
        raise ValueError("Both 'name' and 'school' are required parameters.")

    # Simulating unique applicant ID generation using a hash
    applicant_id = f"{hash(name + school) % 10000:04}"

    return {
        "applicant_id": applicant_id,
        "name": name,
        "school": school,
        "status": "waitlisted",
    }
