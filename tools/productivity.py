# Productivity Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def cancel_appointment(date: str, time: str, location: str) -> Dict[str, str]:
    """Cancel an appointment for a given date, time, and location.

    Args:
        date: Appointment date in the format 'dd/mm/yyyy'
        time: Appointment time in the format 'hh:mm'
        location: Room in which the appointment would have been held

    Returns:
        Dict containing:
            - status: Status of the cancellation ('success' or 'failure')
            - message: Details about the cancellation result
    """

    # Simulated database of appointments
    appointments = {
        ("15/10/2023", "10:00", "Room 101"): True,
        ("16/10/2023", "14:00", "Room 202"): True,
        ("17/10/2023", "09:00", "Room 303"): True,
    }

    appointment_key = (date, time, location)

    if appointment_key not in appointments:
        return {
            "status": "failure",
            "message": f"No appointment found for {date} at {time} in {location}.",
        }

    if not appointments[appointment_key]:
        return {
            "status": "failure",
            "message": f"Appointment for {date} at {time} in {location} is already canceled.",
        }

    # Cancel the appointment
    appointments[appointment_key] = False

    return {
        "status": "success",
        "message": f"Appointment for {date} at {time} in {location} has been successfully canceled.",
    }


from datetime import datetime, timedelta
from typing import Dict, Union


def check_room_availability(
    room_id: str, date: str, window_start: str, window_end: str
) -> Dict[str, Union[str, bool]]:
    """Check an office room's availability for a given time window.

    Args:
        room_id: The identifier of the room to check availability for
        date: The date to check availability on (format 'YYYY-MM-DD')
        window_start: The start time of the window (format 'HH:MM')
        window_end: The end time of the window (format 'HH:MM')

    Returns:
        Dict containing:
            - room_id: The identifier of the room
            - date: The date checked
            - window_start: The start time of the window
            - window_end: The end time of the window
            - available: Boolean indicating if the room is available
    """
    # Sample data simulating room bookings
    bookings = {
        "room_101": [
            ("2023-10-01", "09:00", "11:00"),
            ("2023-10-01", "13:00", "15:00"),
        ],
        "room_102": [
            ("2023-10-01", "10:00", "12:00"),
            ("2023-10-01", "14:00", "16:00"),
        ],
    }

    # Convert strings to datetime objects for comparison
    try:
        window_start_dt = datetime.strptime(f"{date} {window_start}", "%Y-%m-%d %H:%M")
        window_end_dt = datetime.strptime(f"{date} {window_end}", "%Y-%m-%d %H:%M")
    except ValueError as e:
        raise ValueError("Invalid date or time format") from e

    if window_start_dt >= window_end_dt:
        raise ValueError("window_start must be before window_end")

    # Check for room availability
    room_bookings = bookings.get(room_id, [])
    available = True
    for booking_date, start, end in room_bookings:
        if booking_date == date:
            booked_start_dt = datetime.strptime(f"{date} {start}", "%Y-%m-%d %H:%M")
            booked_end_dt = datetime.strptime(f"{date} {end}", "%Y-%m-%d %H:%M")
            if not (
                window_end_dt <= booked_start_dt or window_start_dt >= booked_end_dt
            ):
                available = False
                break

    return {
        "room_id": room_id,
        "date": date,
        "window_start": window_start,
        "window_end": window_end,
        "available": available,
    }


from typing import Dict, List, Union


def create_calendar_hold(
    title: str, start_time: str, end_time: str, attendees: Union[List[str], str], notes: str = ""
) -> Dict[str, Union[str, List[str]]]:
    """Create a tentative calendar hold.

    Args:
        title: The title of the calendar hold
        start_time: The start time of the hold in ISO 8601 format
        end_time: The end time of the hold in ISO 8601 format
        attendees: List of email addresses of attendees or comma-separated string
        notes: Additional notes for the hold (optional)

    Returns:
        Dict containing:
            - id: Unique identifier for the calendar hold
            - title: Title of the calendar hold
            - start_time: Start time of the hold
            - end_time: End time of the hold
            - attendees: List of attendees
            - notes: Additional notes for the hold
    """
    if not title or not start_time or not end_time or not attendees:
        raise ValueError(
            "Missing required fields: title, start_time, end_time, or attendees"
        )
        
    # Convert attendees from string to list if needed
    if isinstance(attendees, str):
        # Handle both comma-separated strings and string representations of lists
        if attendees.startswith('[') and attendees.endswith(']'):
            # Handle string representation of list like "['email1', 'email2']"
            import ast
            try:
                attendees = ast.literal_eval(attendees)
            except:
                # If parsing fails, fall back to comma-separated handling
                attendees = [email.strip() for email in attendees.split(',')]
        else:
            # Handle comma-separated strings like "email1,email2" or "email1, email2"
            attendees = [email.strip() for email in attendees.split(',')]

    # Simulate unique ID generation using hash
    unique_id = hash((title, start_time, end_time, tuple(attendees)))

    return {
        "id": f"hold-{unique_id}",
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "attendees": attendees,
        "notes": notes,
    }


import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Literal, Union


def find_overlapping_slots(
    attendees: Union[List[str], str],
    duration_min: int,
    window_start: str,
    window_end: str,
    priority: Literal["earliest", "latest"] = "earliest",
) -> Dict[str, Union[str, List[str]]]:
    """Compute common free time slots for attendees within a specified window.

    Args:
        attendees: List of email addresses of the attendees
        duration_min: Required duration of the free slot in minutes
        window_start: Start of the time window in ISO 8601 format with timezone
        window_end: End of the time window in ISO 8601 format with timezone
        priority: Whether to prioritize the earliest or latest slot

    Returns:
        Dict containing:
            - slot_start: Start time of the common free slot in ISO 8601 format
            - slot_end: End time of the common free slot in ISO 8601 format
            - attendees: List of attendees who are available
    """
    # Convert window_start and window_end to datetime objects
    start_dt = datetime.fromisoformat(window_start)
    end_dt = datetime.fromisoformat(window_end)

    # Calculate the total available minutes in the window
    total_minutes = int((end_dt - start_dt).total_seconds() / 60)

    # Convert string of attendees to list if necessary
    if isinstance(attendees, str):
        attendees = [email.strip() for email in attendees.split(",")]
        
    # Simulate availability for each attendee using a hash-based approach
    availability = {}
    for attendee in attendees:
        hash_value = int(hashlib.md5(attendee.encode()).hexdigest(), 16)
        available_start_minute = hash_value % total_minutes
        available_end_minute = available_start_minute + duration_min
        if available_end_minute <= total_minutes:
            availability[attendee] = (
                start_dt + timedelta(minutes=available_start_minute),
                start_dt + timedelta(minutes=available_end_minute),
            )

    # Find the common overlapping slot
    if not availability:
        raise ValueError("No available slots for the given duration.")

    if priority == "earliest":
        common_start = max(slot[0] for slot in availability.values())
        common_end = common_start + timedelta(minutes=duration_min)
    else:  # priority == "latest"
        common_end = min(slot[1] for slot in availability.values())
        common_start = common_end - timedelta(minutes=duration_min)

    if common_start >= common_end:
        raise ValueError("No common overlapping slots available.")

    return {
        "slot_start": common_start.isoformat(),
        "slot_end": common_end.isoformat(),
        "attendees": list(availability.keys()),
    }


from datetime import datetime, timedelta
from typing import Dict, List


def get_calendar_events(
    start_date: str, end_date: str
) -> Dict[str, List[Dict[str, str]]]:
    """Gets all the events in a calendar in the specified date range.

    Args:
        start_date: Date range start in ISO format (e.g. '2023-01-01').
        end_date: Date range end in ISO format (e.g. '2023-01-31').

    Returns:
        Dict containing:
            - events: List of events with each event containing:
                - title: Title of the event
                - date: Date of the event in ISO format
                - description: Brief description of the event
    """
    try:
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)
    except ValueError:
        raise ValueError("Invalid date format. Please use ISO format (YYYY-MM-DD).")

    if start > end:
        raise ValueError("Start date must be before end date.")

    # Generate sample events
    sample_events = [
        {"title": "Meeting with Team", "description": "Discuss project updates."},
        {"title": "Doctor Appointment", "description": "Routine check-up."},
        {"title": "Lunch with Sarah", "description": "Catch up over lunch."},
        {"title": "Conference Call", "description": "Quarterly business review."},
        {"title": "Gym Session", "description": "Evening workout."},
    ]

    # Generate events within the date range
    events = []
    current_date = start
    while current_date <= end:
        # Use hash-based generation for consistent but varied sample data
        index = hash(current_date) % len(sample_events)
        event = sample_events[index].copy()
        event["date"] = current_date.isoformat()
        events.append(event)
        current_date += timedelta(days=1)

    return {"events": events}


import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Union


def get_free_busy(
    attendees: List[str], start_date: str, end_date: str
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Return free/busy blocks for attendees over a date range.

    Args:
        attendees: List of email addresses of attendees or comma-separated string
        start_date: Start date of the range in 'YYYY-MM-DD' format
        end_date: End date of the range in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - attendees: List of attendees
            - free_busy: List of dictionaries with 'attendee', 'start', and 'end' keys
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    if start > end:
        raise ValueError("Start date must be before end date.")

    free_busy_data = []
    for attendee in attendees:
        # Generate a consistent but varied free/busy schedule based on attendee's hash
        hash_seed = int(hashlib.sha256(attendee.encode()).hexdigest(), 16)
        busy_start = start + timedelta(days=hash_seed % 5)
        busy_end = busy_start + timedelta(hours=hash_seed % 8 + 1)

        if busy_start < end:
            free_busy_data.append(
                {
                    "attendee": attendee,
                    "start": busy_start.strftime("%Y-%m-%d %H:%M"),
                    "end": busy_end.strftime("%Y-%m-%d %H:%M"),
                }
            )

    return {
        "attendees": attendees,
        "free_busy": free_busy_data,
    }


from typing import Dict, List, Literal


def get_schedule(
    calendar_type: Literal["work", "personal"], date: str, time: str
) -> Dict[str, Union[str, List[str]]]:
    """Gets the schedule for a day based on the given calendar type.

    Args:
        calendar_type: Type of calendar to check ('work' or 'personal')
        date: Day to check schedule (YYYY-MM-DD)
        time: Time to check schedule (HH:MM:SS)

    Returns:
        Dict containing:
            - calendar_type: The type of calendar
            - date: The date for the schedule
            - time: The time for the schedule
            - events: List of scheduled events at the given time
    """
    sample_data = {
        "work": {
            "2023-10-01": {
                "09:00:00": ["Team Meeting", "Project Discussion"],
                "14:00:00": ["Client Call"],
            },
            "2023-10-02": {
                "10:00:00": ["Code Review"],
                "15:00:00": ["Sprint Planning"],
            },
        },
        "personal": {
            "2023-10-01": {
                "18:00:00": ["Dinner with Family"],
                "20:00:00": ["Gym"],
            },
            "2023-10-02": {
                "19:00:00": ["Movie Night"],
            },
        },
    }

    if calendar_type not in sample_data:
        raise ValueError(f"Unsupported calendar type: {calendar_type}")

    day_schedule = sample_data.get(calendar_type, {}).get(date, {})
    events = day_schedule.get(time, [])

    return {
        "calendar_type": calendar_type,
        "date": date,
        "time": time,
        "events": events,
    }


from typing import Dict


def schedule_appointment(date: str, time: str, location: str) -> Dict[str, str]:
    """Book an appointment for a given date, time, and location.

    Args:
        date: Appointment date in the format 'dd/mm/yyyy'
        time: Appointment time in the format 'hh:mm'
        location: Room in which the appointment will be held

    Returns:
        Dict containing:
            - date: The date of the appointment
            - time: The time of the appointment
            - location: The location of the appointment
            - confirmation_id: A unique confirmation ID for the appointment
    """
    if not date or not time or not location:
        raise ValueError("All parameters (date, time, location) must be provided")

    # Generate a mock confirmation ID based on input parameters
    confirmation_id = f"{hash((date, time, location)) % 1000000:06}"

    return {
        "date": date,
        "time": time,
        "location": location,
        "confirmation_id": confirmation_id,
    }


from typing import Dict, List


def send_calendar_email(to: List[str], subject: str, body: str) -> Dict[str, str]:
    """Send an email to participants about scheduling.

    Args:
        to: List of email addresses to send the email to
        subject: Subject of the email
        body: Body content of the email

    Returns:
        Dict containing:
            - status: Status of the email sending process
            - message: Detailed message about the sending process
    """
    if not to:
        raise ValueError("Recipient list cannot be empty.")
    if not subject:
        raise ValueError("Subject cannot be empty.")
    if not body:
        raise ValueError("Body cannot be empty.")

    # Simulate sending email
    email_hash = hash((tuple(to), subject, body)) % 1000
    if email_hash % 2 == 0:
        return {"status": "success", "message": f"Email sent to {len(to)} recipients."}
    else:
        return {
            "status": "failure",
            "message": "Failed to send email due to server error.",
        }


from datetime import datetime
from typing import Dict, List, Union


def add_calendar_event(
    title: str, notes: str, emails: List[str], start_datetime: str, end_datetime: str
) -> Dict[str, Union[str, List[str]]]:
    """Add an event to multiple people's calendars.

    Args:
        title: The title of the event
        notes: Additional notes/description for the event's guests
        emails: The email addresses to book the event for
        start_datetime: The start date & time of the event in ISO format
        end_datetime: The end date & time of the event in ISO format

    Returns:
        Dict containing:
            - title: Title of the event
            - attendees: List of email addresses the event was added for
            - start: Start date & time of the event
            - end: End date & time of the event
            - notes: Notes for the event
    """
    try:
        start = datetime.fromisoformat(start_datetime)
        end = datetime.fromisoformat(end_datetime)
    except ValueError as e:
        raise ValueError("Invalid date-time format") from e

    if start >= end:
        raise ValueError("Start time must be before end time")

    if not emails:
        raise ValueError("At least one email address must be provided")

    # Simulate adding the event to calendars
    sample_attendees = [email for email in emails if "@" in email]

    return {
        "title": title,
        "attendees": sample_attendees,
        "start": start_datetime,
        "end": end_datetime,
        "notes": notes,
    }


from typing import Dict, Literal


def add_schedule(
    calendar_type: Literal["work", "personal"], date: str, time: str
) -> Dict[str, str]:
    """Add an item to the schedule for a specific day based on the given calendar type.

    Args:
        calendar_type: The type of calendar to add the item to ('work' or 'personal')
        date: The day to add the item to the schedule (format: 'YYYY-MM-DD')
        time: The time to add the item to the schedule (format: 'HH:MM:SS')

    Returns:
        Dict containing:
            - calendar_type: The type of calendar the item was added to
            - date: The date the item was added
            - time: The time the item was added
            - item: Description of the scheduled item
    """
    if calendar_type not in ["work", "personal"]:
        raise ValueError(f"Unsupported calendar type: {calendar_type}")

    # Simulate adding an item to the schedule
    sample_items = {
        "work": "Team meeting",
        "personal": "Gym session",
    }

    item = sample_items.get(calendar_type, "General task")

    return {
        "calendar_type": calendar_type,
        "date": date,
        "time": time,
        "item": item,
    }


from typing import Dict, Union


def check_activity_cancelled(
    activity_name: str,
    activity_date: str,
    location_name: str,
    location_city: str = None,
    location_country: str = None,
) -> Dict[str, Union[str, bool]]:
    """Checks if the activity on the specified date has been cancelled.

    Args:
        activity_name: The name of the activity to be looked up.
        activity_date: The date the activity takes place on.
        location_name: The name of the location where the activity takes place.
        location_city: The name of the city the activity takes place in.
        location_country: The name of the country the activity takes place in.

    Returns:
        Dict containing:
            - activity_name: Name of the activity
            - activity_date: Date of the activity
            - location_name: Name of the location
            - is_cancelled: Boolean indicating if the activity is cancelled
    """
    # Simulated cancellation data based on a hash of the activity name and date
    cancellation_hash = hash((activity_name, activity_date)) % 3

    is_cancelled = cancellation_hash == 0

    return {
        "activity_name": activity_name,
        "activity_date": activity_date,
        "location_name": location_name,
        "is_cancelled": is_cancelled,
    }


from datetime import datetime
from typing import Dict, Union


def create_calendar_event(
    start: Dict[str, Union[int, str]],
    end: Dict[str, Union[int, str]],
    title: str,
    description: str = None,
    location: str = None,
) -> Dict[str, Union[str, Dict[str, Union[int, str]]]]:
    """Adds a new event to the calendar.

    Args:
        start: Start date and time of the event (e.g., {'year': 2023, 'month': 10, 'day': 15, 'hour': 9, 'minute': 30})
        end: End date and time of the event (e.g., {'year': 2023, 'month': 10, 'day': 15, 'hour': 10, 'minute': 30})
        title: Concise summary of the event
        description: Details to describe the contents of what the event is about or for
        location: Location of where the event will take place

    Returns:
        Dict containing:
            - id: Unique identifier for the event
            - start: Start date and time of the event
            - end: End date and time of the event
            - title: Title of the event
            - description: Description of the event
            - location: Location of the event
    """
    # Validate start and end times
    start_dt = datetime(**start)
    end_dt = datetime(**end)
    if end_dt <= start_dt:
        raise ValueError("End time must be after start time")

    # Generate a unique event ID based on hash
    event_id = hash((start_dt, end_dt, title, description, location))

    return {
        "id": f"event-{event_id}",
        "start": start,
        "end": end,
        "title": title,
        "description": description or "No description provided",
        "location": location or "No location specified",
    }


from typing import Dict, Union


def create_calendar_event(
    title: str,
    start_time: str,
    end_time: Union[str, None] = None,
    location: Union[str, None] = None,
    notes: Union[str, None] = None,
    reminder_text_minutes: Union[int, None] = None,
) -> Dict[str, Union[str, int, None]]:
    """Create a calendar event with the specified details.

    Args:
        title: The title of the event.
        start_time: The start time of the event in ISO 8601 format.
        end_time: The end time of the event in ISO 8601 format (optional).
        location: The location of the event (optional).
        notes: Additional notes for the event (optional).
        reminder_text_minutes: Minutes before the event to send a reminder (optional).

    Returns:
        Dict containing:
            - event_id: Unique identifier for the event
            - title: Title of the event
            - start_time: Start time of the event
            - end_time: End time of the event
            - location: Location of the event
            - notes: Notes for the event
            - reminder_text_minutes: Reminder time in minutes
    """
    if not title or not start_time:
        raise ValueError("Both 'title' and 'start_time' are required fields.")

    # Simulate event ID generation using a hash
    event_id = hash(
        (title, start_time, end_time, location, notes, reminder_text_minutes)
    )

    return {
        "event_id": event_id,
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "location": location,
        "notes": notes,
        "reminder_text_minutes": reminder_text_minutes,
    }


from typing import Dict, List, Union


def create_event(
    title: str, start_time: str, end_time: str = None, attendees: List[str] = None
) -> Dict[str, Union[str, List[str]]]:
    """Create a new calendar event with optional end time and attendees.

    Args:
        title: The title of the calendar event.
        start_time: The start date and time of the event in ISO 8601 format.
        end_time: The end date and time of the event in ISO 8601 format.
        attendees: A list of email addresses of the event attendees.

    Returns:
        Dict containing:
            - event_id: A unique identifier for the event
            - title: The title of the event
            - start_time: The start time of the event
            - end_time: The end time of the event, if provided
            - attendees: List of attendees' email addresses, if provided
    """
    if not title or not start_time:
        raise ValueError("Both 'title' and 'start_time' are required fields.")

    # Generate a mock event ID using a hash-based approach
    event_id = hash((title, start_time, end_time, tuple(attendees or [])))

    return {
        "event_id": f"evt_{abs(event_id)}",
        "title": title,
        "start_time": start_time,
        "end_time": end_time or "N/A",
        "attendees": attendees or [],
    }


def delete_event(event_id: str) -> Dict[str, Union[str, bool]]:
    """Delete a specific calendar event using its unique ID.

    Args:
        event_id: The unique identifier of the event to delete.

    Returns:
        Dict containing:
            - event_id: The ID of the deleted event
            - success: Boolean indicating if the deletion was successful
            - message: A message describing the result of the operation
    """
    # Simulated event storage
    events = {
        "evt_123": {"name": "Meeting with Bob", "date": "2023-10-01"},
        "evt_456": {"name": "Dentist Appointment", "date": "2023-10-02"},
        "evt_789": {"name": "Lunch with Alice", "date": "2023-10-03"},
    }

    if event_id not in events:
        return {
            "event_id": event_id,
            "success": False,
            "message": "Event not found",
        }

    # Simulate deletion
    del events[event_id]

    return {
        "event_id": event_id,
        "success": True,
        "message": "Event successfully deleted",
    }


from typing import Dict, Union


def draw_circle(
    x_0: int, y_0: int, radius: int, color: str = "#000000"
) -> Dict[str, Union[int, str]]:
    """Draw a circle on the canvas using the bottom left corner as the origin.

    Args:
        x_0: Position of the circle's center along the x-axis in pixels.
        y_0: Position of the circle's center along the y-axis in pixels.
        radius: Radius of the circle in pixels.
        color: Color in hexadecimal format.

    Returns:
        Dict containing:
            - x_0: X-coordinate of the circle's center
            - y_0: Y-coordinate of the circle's center
            - radius: Radius of the circle
            - color: Color of the circle in hexadecimal format
            - area: Calculated area of the circle
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive integer")

    # Calculate the area of the circle
    area = 3.14159 * radius * radius

    return {
        "x_0": x_0,
        "y_0": y_0,
        "radius": radius,
        "color": color,
        "area": round(area, 2),
    }


from typing import Dict, Union


def draw_line(
    x_0: int,
    y_0: int,
    x_1: int,
    y_1: int,
    line_thickness: int = 1,
    color: str = "#000000",
) -> Dict[str, Union[str, int]]:
    """Draw a line segment on a canvas using the bottom left corner as the origin.

    Args:
        x_0: First vertex of the line segment along the x-axis in pixels.
        y_0: First vertex of the line segment along the y-axis in pixels.
        x_1: Second vertex of the line segment along the x-axis in pixels.
        y_1: Second vertex of the line segment along the y-axis in pixels.
        line_thickness: Thickness of the line in pixels.
        color: Color in hexadecimal format.

    Returns:
        Dict containing:
            - start: Starting point of the line as a tuple (x_0, y_0)
            - end: Ending point of the line as a tuple (x_1, y_1)
            - line_thickness: Thickness of the line in pixels
            - color: Color of the line in hexadecimal format
    """
    if not (
        0 <= x_0 <= 1000 and 0 <= y_0 <= 1000 and 0 <= x_1 <= 1000 and 0 <= y_1 <= 1000
    ):
        raise ValueError(
            "Coordinates must be within the canvas bounds (0, 0) to (1000, 1000)."
        )

    if line_thickness <= 0:
        raise ValueError("Line thickness must be a positive integer.")

    if not isinstance(color, str) or not color.startswith("#") or len(color) != 7:
        raise ValueError("Color must be a valid hexadecimal string (e.g., '#RRGGBB').")

    return {
        "start": (x_0, y_0),
        "end": (x_1, y_1),
        "line_thickness": line_thickness,
        "color": color,
    }


from typing import Dict, Union


def draw_rectangle(
    x_0: int, y_0: int, x_1: int, y_1: int, color: str = "#000000"
) -> Dict[str, Union[str, int]]:
    """Draw a rectangle on the canvas using the bottom left corner as the origin.

    Args:
        x_0: Location of bottom left vertex along the x-axis in pixels.
        y_0: Location of bottom left vertex along the y-axis in pixels.
        x_1: Location of top right vertex along the x-axis in pixels.
        y_1: Location of top right vertex along the y-axis in pixels.
        color: Color in hexadecimal format.

    Returns:
        Dict containing:
            - bottom_left: Coordinates of the bottom left vertex
            - top_right: Coordinates of the top right vertex
            - color: Color of the rectangle
            - area: Calculated area of the rectangle
    """
    if x_0 >= x_1 or y_0 >= y_1:
        raise ValueError("Invalid rectangle dimensions: ensure x_0 < x_1 and y_0 < y_1")

    area = (x_1 - x_0) * (y_1 - y_0)

    return {
        "bottom_left": (x_0, y_0),
        "top_right": (x_1, y_1),
        "color": color,
        "area": area,
    }


from typing import Dict, Union


def draw_text(
    x_0: int,
    y_0: int,
    text: str,
    font: str = "Arial",
    font_size: int = 12,
    rotation: int = 0,
    color: str = "#000000",
) -> Dict[str, Union[str, int]]:
    """Draws a text on the canvas using the bottom left corner as the origin.

    Args:
        x_0: Location of bottom left vertex along the x-axis in pixels.
        y_0: Location of bottom left vertex along the y-axis in pixels.
        text: Text to be drawn on the canvas.
        font: Font family of the text.
        font_size: Size of the font in pixels.
        rotation: Rotation of the text around bottom left corner in degrees.
        color: Color in hexadecimal format.

    Returns:
        Dict containing:
            - x_0: X-coordinate of the text's bottom left corner
            - y_0: Y-coordinate of the text's bottom left corner
            - text: The text that was drawn
            - font: Font used for the text
            - font_size: Size of the font in pixels
            - rotation: Rotation of the text in degrees
            - color: Color of the text in hexadecimal format
    """
    if not (0 <= rotation < 360):
        raise ValueError("Rotation must be between 0 and 359 degrees")

    if not color.startswith("#") or len(color) != 7:
        raise ValueError("Color must be in hexadecimal format, e.g., '#RRGGBB'")

    # Simulate drawing the text by returning the parameters
    return {
        "x_0": x_0,
        "y_0": y_0,
        "text": text,
        "font": font,
        "font_size": font_size,
        "rotation": rotation,
        "color": color,
    }


from datetime import datetime, timedelta
from typing import Dict, Union


def find_opening(
    location: str, floor: str, time: datetime
) -> Dict[str, Union[str, datetime]]:
    """Find the next available time slot at a venue after the specified time.

    Args:
        location: Name of the venue (e.g., 'Conference Center')
        floor: Specific area within the venue (e.g., 'main ballroom', 'practice room')
        time: Scheduled start time to search for the next available slot

    Returns:
        Dict containing:
            - location: Name of the venue
            - floor: Specific area within the venue
            - next_available_time: Next available time slot as a datetime object
    """
    # Mocked schedule data for demonstration purposes
    schedule = {
        ("Conference Center", "main ballroom"): [
            datetime(2023, 10, 1, 9, 0),
            datetime(2023, 10, 1, 11, 0),
            datetime(2023, 10, 1, 14, 0),
        ],
        ("Conference Center", "practice room"): [
            datetime(2023, 10, 1, 10, 0),
            datetime(2023, 10, 1, 13, 0),
            datetime(2023, 10, 1, 15, 0),
        ],
    }

    key = (location, floor)
    if key not in schedule:
        raise ValueError(f"Location or floor not supported: {location}, {floor}")

    # Find the next available time slot after the given time
    for slot in schedule[key]:
        if slot > time:
            return {
                "location": location,
                "floor": floor,
                "next_available_time": slot,
            }

    # If no future slots are available, return the next day at 9 AM
    next_day = datetime(time.year, time.month, time.day) + timedelta(days=1)
    next_available_time = next_day.replace(hour=9, minute=0)
    return {
        "location": location,
        "floor": floor,
        "next_available_time": next_available_time,
    }


from typing import Dict


def fire_employee(employee_id: str) -> Dict[str, str]:
    """Fire an employee from the crew.

    Args:
        employee_id: ID of the employee to fire.

    Returns:
        Dict containing:
            - employee_id: ID of the fired employee
            - status: Status of the firing process
            - message: Message indicating the result of the operation
    """
    # Simulated employee database
    employees = {
        "E001": "John Doe",
        "E002": "Jane Smith",
        "E003": "Alice Johnson",
    }

    if employee_id not in employees:
        raise ValueError(f"Employee ID not found: {employee_id}")

    # Simulate firing process
    fired_employee = employees.pop(employee_id)

    return {
        "employee_id": employee_id,
        "status": "success",
        "message": f"Employee {fired_employee} has been successfully fired.",
    }


from typing import Dict


def get_calendar(email: str) -> Dict[str, str]:
    """Retrieve the calendar ID of a person's calendar.

    Args:
        email: The email address of the owner of the calendar

    Returns:
        Dict containing:
            - email: The email address provided
            - calendar_id: The unique calendar ID associated with the email
    """
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError(f"Invalid email address: {email}")

    # Simulate a hash-based generation for a consistent calendar ID
    calendar_id = f"cal-{hash(email) % 1000000:06d}"

    return {
        "email": email,
        "calendar_id": calendar_id,
    }


from datetime import datetime, timedelta
from typing import Dict, List


def get_work_calendar(
    start_date: str, end_date: str
) -> Dict[str, List[Dict[str, str]]]:
    """Returns work calendar events between a start and end date, including availability and time off.

    Args:
        start_date: Start date (YYYY-MM-DD).
        end_date: End date (YYYY-MM-DD).

    Returns:
        Dict containing:
            - events: List of events with details such as date, type, and description
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    if start > end:
        raise ValueError("Start date must be before end date.")

    # Sample data generation
    events = []
    current_date = start
    while current_date <= end:
        day_of_week = current_date.weekday()
        if day_of_week < 5:  # Weekdays
            events.append(
                {
                    "date": current_date.strftime("%Y-%m-%d"),
                    "type": "work",
                    "description": "Available for work",
                }
            )
        else:  # Weekends
            events.append(
                {
                    "date": current_date.strftime("%Y-%m-%d"),
                    "type": "time_off",
                    "description": "Weekend",
                }
            )
        current_date += timedelta(days=1)

    return {"events": events}


def hire_employee(applicant_name: str) -> Dict[str, Union[str, int]]:
    """Hire an applicant as an employee.

    Args:
        applicant_name: Name of the applicant to hire.

    Returns:
        Dict containing:
            - employee_id: Unique identifier for the new employee
            - name: Name of the hired employee
            - status: Hiring status message
    """
    if not applicant_name:
        raise ValueError("Applicant name must be provided")

    # Simulate generating a unique employee ID based on the applicant's name
    employee_id = abs(hash(applicant_name)) % 10000

    return {
        "employee_id": employee_id,
        "name": applicant_name,
        "status": "Hired successfully",
    }


from typing import Dict, List, Literal, Union


def job_search(
    query: str,
    page: int = 1,
    country: str = "us",
    date_posted: Literal["all", "today", "3days", "week", "month"] = "all",
    work_from_home: bool = False,
    radius: Union[int, None] = None,
) -> Dict[str, Union[str, int, List[Dict[str, Union[str, int]]]]]:
    """Search for jobs based on various criteria.

    Args:
        query: Free-form jobs search query.
        page: Page to return (each page includes up to ten records).
        country: Country code of the country from which to return job postings.
        date_posted: Find jobs posted within the time you specify.
        work_from_home: Only return work from home / remote jobs.
        radius: Return jobs within a certain distance from location as specified as part of the query (in km).

    Returns:
        Dict containing:
            - query: The search query used
            - page: The page number of results
            - jobs: List of job postings, each containing:
                - title: Job title
                - company: Company offering the job
                - location: Job location
                - posted_date: Date the job was posted
                - remote: Whether the job is remote
    """

    # Sample data generation based on hash of query for consistency
    sample_jobs = [
        {
            "title": "Software Engineer",
            "company": "Tech Corp",
            "location": "New York, NY",
            "posted_date": "2023-10-01",
            "remote": True,
        },
        {
            "title": "Data Analyst",
            "company": "Data Inc.",
            "location": "San Francisco, CA",
            "posted_date": "2023-09-28",
            "remote": False,
        },
        {
            "title": "Product Manager",
            "company": "Innovate LLC",
            "location": "Remote",
            "posted_date": "2023-09-30",
            "remote": True,
        },
    ]

    # Simulate filtering based on parameters
    filtered_jobs = [
        job
        for job in sample_jobs
        if (work_from_home and job["remote"]) or not work_from_home
    ]

    # Simulate pagination
    start_index = (page - 1) * 10
    end_index = start_index + 10
    paginated_jobs = filtered_jobs[start_index:end_index]

    return {"query": query, "page": page, "jobs": paginated_jobs}


from datetime import datetime
from typing import Dict, List


def list_events(start_time: str, end_time: str) -> Dict[str, List[Dict[str, str]]]:
    """Retrieves a list of calendar events within a specified time range.

    Args:
        start_time: The start date and time of the range to list events from, in ISO 8601 format (e.g., '2025-08-12T09:00:00Z').
        end_time: The end date and time of the range to list events until, in ISO 8601 format (e.g., '2025-08-12T17:00:00Z').

    Returns:
        Dict containing:
            - events: List of events, each with:
                - title: Title of the event
                - start: Start time of the event in ISO 8601 format
                - end: End time of the event in ISO 8601 format
    """
    try:
        start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end_dt = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError("Invalid date format. Please use ISO 8601 format.")

    if start_dt >= end_dt:
        raise ValueError("Start time must be before end time.")

    # Sample events data
    sample_events = [
        {
            "title": "Team Meeting",
            "start": "2025-08-12T10:00:00Z",
            "end": "2025-08-12T11:00:00Z",
        },
        {
            "title": "Project Deadline",
            "start": "2025-08-12T12:00:00Z",
            "end": "2025-08-12T13:00:00Z",
        },
        {
            "title": "Lunch with Client",
            "start": "2025-08-12T14:00:00Z",
            "end": "2025-08-12T15:00:00Z",
        },
    ]

    # Filter events within the specified time range
    events_in_range = [
        event
        for event in sample_events
        if start_dt
        <= datetime.fromisoformat(event["start"].replace("Z", "+00:00"))
        < end_dt
    ]

    return {"events": events_in_range}


from typing import Dict


def post_format_metadata(
    id: int, line_number: int, format_style: str
) -> Dict[str, str]:
    """Format a section of text in the scene narration.

    Args:
        id: The id of the scene narration
        line_number: The line number of the record to format the metadata
        format_style: The style data to apply to the description

    Returns:
        Dict containing:
            - id: Scene narration ID as a string
            - line_number: Line number as a string
            - formatted_text: Text formatted with the specified style
    """
    if id < 0 or line_number < 0:
        raise ValueError("ID and line number must be non-negative integers")

    # Simulate formatted text based on the format style
    sample_texts = {
        1: "The sun sets over the horizon, casting a golden glow.",
        2: "A gentle breeze rustles the leaves.",
        3: "The city lights flicker in the distance.",
    }
    base_text = sample_texts.get(line_number, "A quiet scene unfolds.")

    if format_style == "bold":
        formatted_text = f"**{base_text}**"
    elif format_style == "italic":
        formatted_text = f"*{base_text}*"
    elif format_style == "underline":
        formatted_text = f"__{base_text}__"
    else:
        raise ValueError(f"Unsupported format style: {format_style}")

    return {
        "id": str(id),
        "line_number": str(line_number),
        "formatted_text": formatted_text,
    }


from typing import Dict, Union


def post_seo_check(id: int) -> Dict[str, Union[int, str, bool]]:
    """Run an SEO check for a given record.

    Args:
        id: The ID of the record to run the SEO check on

    Returns:
        Dict containing:
            - id: The ID of the record
            - title: The title of the record
            - seo_score: The SEO score of the record
            - is_optimized: Boolean indicating if the record is SEO optimized
    """

    # Simulated data based on the record ID
    titles = {
        1: "How to Learn Python",
        2: "Top 10 Travel Destinations",
        3: "Best Practices for SEO",
    }
    seo_scores = {
        1: 85,
        2: 78,
        3: 92,
    }

    if id not in titles or id not in seo_scores:
        raise ValueError(f"Record ID not found: {id}")

    title = titles[id]
    seo_score = seo_scores[id]
    is_optimized = seo_score > 80

    return {
        "id": id,
        "title": title,
        "seo_score": seo_score,
        "is_optimized": is_optimized,
    }


from typing import Dict


def process_applicant(name: str, school: str) -> Dict[str, str]:
    """Send applicant to processing.

    Args:
        name: The name of the applicant
        school: School the applicant is applying to

    Returns:
        Dict containing:
            - applicant_id: Unique identifier for the applicant
            - status: Current processing status of the applicant
            - school: School the applicant is applying to
    """
    if not name or not school:
        raise ValueError("Both 'name' and 'school' must be provided.")

    # Generate a mock applicant ID using a hash-based approach
    applicant_id = f"{hash(name + school) % 10000:04d}"

    return {
        "applicant_id": applicant_id,
        "status": "processing",
        "school": school,
    }


from typing import Dict


def promote_employee(employee_id: str) -> Dict[str, str]:
    """Promote an employee to the next level.

    Args:
        employee_id: The ID of employee to promote.

    Returns:
        Dict containing:
            - employee_id: The ID of the promoted employee
            - new_title: The new title of the employee after promotion
            - promotion_date: The date of promotion
    """

    # Mock employee data
    employee_titles = {
        "E001": "Junior Developer",
        "E002": "Developer",
        "E003": "Senior Developer",
        "E004": "Lead Developer",
    }

    # Promotion logic
    promotion_path = {
        "Junior Developer": "Developer",
        "Developer": "Senior Developer",
        "Senior Developer": "Lead Developer",
        "Lead Developer": "Principal Developer",
    }

    if employee_id not in employee_titles:
        raise ValueError(f"Employee ID not found: {employee_id}")

    current_title = employee_titles[employee_id]
    new_title = promotion_path.get(current_title)

    if not new_title:
        raise ValueError(f"No promotion available for title: {current_title}")

    # Mock promotion date
    promotion_date = "2023-10-01"

    return {
        "employee_id": employee_id,
        "new_title": new_title,
        "promotion_date": promotion_date,
    }


from typing import Dict, Union


def schedule_service(
    contractor_id: str,
    work_order_id: Union[str, None] = None,
    arrival_window: Dict[str, str] = None,
    access_instructions: Union[str, None] = None,
    contact_phone: Union[str, None] = None,
    agree_to_terms: bool = None,
) -> Dict[str, Union[str, bool]]:
    """Confirm and schedule a service visit with a contractor.

    Args:
        contractor_id: Chosen contractor ID
        work_order_id: Quote or work order reference ID
        arrival_window: Requested arrival window with 'start' and 'end' in ISO 8601 format
        access_instructions: Gate codes, pet notes, parking, etc.
        contact_phone: Day-of contact phone
        agree_to_terms: Must be true to confirm appointment

    Returns:
        Dict containing:
            - confirmation_id: Unique confirmation ID for the scheduled service
            - contractor_id: The ID of the contractor assigned
            - scheduled: Boolean indicating if the service was successfully scheduled
            - message: Additional information about the scheduling status
    """
    if not agree_to_terms:
        raise ValueError("You must agree to the terms to schedule the service.")

    if (
        not arrival_window
        or "start" not in arrival_window
        or "end" not in arrival_window
    ):
        raise ValueError("Invalid arrival window provided.")

    # Simulate a hash-based confirmation ID generation
    confirmation_id = f"CONF-{hash(contractor_id + arrival_window['start']) % 10000:04}"

    # Mock response data
    return {
        "confirmation_id": confirmation_id,
        "contractor_id": contractor_id,
        "scheduled": True,
        "message": "Service visit successfully scheduled.",
    }


from datetime import datetime
from typing import Dict, List


def search_calendar_events(
    email: str, start_datetime: str, end_datetime: str
) -> List[Dict[str, str]]:
    """Returns a list of events on a person's calendar.

    Args:
        email: The email address of the owner of the calendar
        start_datetime: The start date & time to search for events after
        end_datetime: The end date & time to search for events before

    Returns:
        List of dictionaries, each containing:
            - title: The title of the event
            - start: The start date & time of the event
            - end: The end date & time of the event
            - location: The location of the event
    """
    # Sample data generation based on email hash
    sample_events = {
        "alice@example.com": [
            {
                "title": "Team Meeting",
                "start": "2023-10-01T10:00:00",
                "end": "2023-10-01T11:00:00",
                "location": "Conference Room A",
            },
            {
                "title": "Project Deadline",
                "start": "2023-10-02T09:00:00",
                "end": "2023-10-02T09:30:00",
                "location": "Office",
            },
        ],
        "bob@example.com": [
            {
                "title": "Doctor Appointment",
                "start": "2023-10-01T15:00:00",
                "end": "2023-10-01T15:30:00",
                "location": "Clinic",
            },
            {
                "title": "Lunch with Client",
                "start": "2023-10-03T12:00:00",
                "end": "2023-10-03T13:00:00",
                "location": "Downtown Cafe",
            },
        ],
        "sarah@example.com": [
            {
                "title": "Marketing Review",
                "start": "2025-08-21T14:00:00",
                "end": "2025-08-21T15:00:00",
                "location": "Office Building A",
            },
            {
                "title": "Client Presentation",
                "start": "2025-08-21T16:30:00",
                "end": "2025-08-21T17:30:00",
                "location": "Main Conference Room",
            },
            {
                "title": "Budget Planning",
                "start": "2025-08-22T13:00:00",
                "end": "2025-08-22T14:30:00",
                "location": "Finance Department",
            },
        ],
        "tom@example.com": [
            {
                "title": "Engineering Standup",
                "start": "2025-08-21T09:00:00",
                "end": "2025-08-21T09:30:00",
                "location": "Dev Team Room",
            },
            {
                "title": "Code Review Session",
                "start": "2025-08-21T15:00:00",
                "end": "2025-08-21T16:00:00",
                "location": "Tech Lab",
            },
            {
                "title": "Architecture Discussion",
                "start": "2025-08-22T10:00:00",
                "end": "2025-08-22T11:30:00",
                "location": "Building B Meeting Room",
            },
            {
                "title": "Sprint Planning",
                "start": "2025-08-22T14:00:00",
                "end": "2025-08-22T15:30:00",
                "location": "Agile Room",
            },
        ],
        "harry@example.com": [
            {
                "title": "Sales Call",
                "start": "2025-08-21T11:00:00",
                "end": "2025-08-21T12:00:00",
                "location": "Phone Conference",
            },
            {
                "title": "Customer Onboarding",
                "start": "2025-08-21T14:30:00",
                "end": "2025-08-21T15:30:00",
                "location": "Customer Success Office",
            },
            {
                "title": "Weekly Sales Review",
                "start": "2025-08-22T09:30:00",
                "end": "2025-08-22T10:30:00",
                "location": "Sales Conference Room",
            },
            {
                "title": "Training Session",
                "start": "2025-08-22T16:00:00",
                "end": "2025-08-22T17:00:00",
                "location": "Training Center",
            },
        ],
    }

    if email not in sample_events:
        return []  # Return empty list instead of raising error for unknown emails

    # Parse input datetimes
    start_dt = datetime.fromisoformat(start_datetime)
    end_dt = datetime.fromisoformat(end_datetime)

    # Filter events based on the provided datetime range
    filtered_events = [
        event
        for event in sample_events[email]
        if start_dt <= datetime.fromisoformat(event["start"]) <= end_dt
    ]

    return filtered_events


from typing import Dict, Optional


def send_contract(
    shoot_id: str,
    contract_template_id: str,
    recipient_email: str,
    require_signature_by: Optional[str] = None,
    terms_overrides: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """Send contract and model release for e-signature.

    Args:
        shoot_id: Unique identifier for the shoot
        contract_template_id: Template to use for the contract
        recipient_email: Email address to send contract to
        require_signature_by: Date by which signature is required (YYYY-MM-DD)
        terms_overrides: Custom terms to override in the contract

    Returns:
        Dict containing:
            - status: Status of the contract sending process
            - contract_id: Unique identifier for the sent contract
            - message: Additional information about the sending process
    """
    if "@" not in recipient_email:
        raise ValueError(f"Invalid email address: {recipient_email}")

    # Simulate contract sending process
    contract_id = f"contract_{hash(shoot_id + contract_template_id) % 10000}"
    status = "sent"
    message = f"Contract sent to {recipient_email}"

    if require_signature_by:
        message += f", requires signature by {require_signature_by}"

    if terms_overrides:
        message += f", with {len(terms_overrides)} terms overridden"

    return {
        "status": status,
        "contract_id": contract_id,
        "message": message,
    }


from typing import Dict


def set_reminder(task: str, time: str) -> Dict[str, str]:
    """Set a reminder for a specific task and time.

    Args:
        task: Description of the task
        time: Time for the reminder (DD-MM-YYYY HH:MM)

    Returns:
        Dict containing:
            - task: Description of the task
            - time: Scheduled time for the reminder
            - status: Confirmation message of the reminder being set
    """
    # Validate the time format
    try:
        day, month, year_hour, minute = (
            time.split("-")[0],
            time.split("-")[1],
            time.split("-")[2].split(" ")[0],
            time.split(" ")[1],
        )
        if not (
            1 <= int(day) <= 31
            and 1 <= int(month) <= 12
            and len(year_hour) == 4
            and 0 <= int(minute) < 60
        ):
            raise ValueError
    except (ValueError, IndexError):
        raise ValueError("Time format should be 'DD-MM-YYYY HH:MM'")

    # Simulate setting a reminder
    return {
        "task": task,
        "time": time,
        "status": f"Reminder set for '{task}' at {time}",
    }


from typing import Dict, Literal, Optional


def submit_time_off_request(
    start_date: str,
    end_date: str,
    reason: Literal["vacation", "sick", "personal", "bereavement", "other"],
    partial_day: Optional[Literal["AM", "PM", "Full"]] = "Full",
    notes: Optional[str] = None,
) -> Dict[str, str]:
    """Request time off from work.

    Args:
        start_date: The start date of the time off in YYYY-MM-DD format.
        end_date: The end date of the time off in YYYY-MM-DD format.
        reason: The reason category for the time off.
        partial_day: If only part of a day is requested (default is "Full").
        notes: Additional context or notes for the request.

    Returns:
        Dict containing:
            - request_id: A unique identifier for the time off request.
            - status: The status of the request submission.
            - message: A message providing additional information about the request.
    """
    import hashlib
    from datetime import datetime

    # Validate date format
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    # Validate date range
    if start > end:
        raise ValueError("End date must be after start date.")

    # Generate a unique request ID
    request_id = hashlib.md5(f"{start_date}{end_date}{reason}".encode()).hexdigest()[:8]

    # Simulate a successful submission
    return {
        "request_id": request_id,
        "status": "submitted",
        "message": "Your time off request has been successfully submitted.",
    }


import hashlib
from typing import Dict, Optional, Union


def summarize_url(
    url: str,
    focus: Optional[str] = None,
    max_words: Optional[int] = None,
    include_quotes: Optional[bool] = None,
) -> Dict[str, Union[str, int, bool]]:
    """Fetch and summarize the main content of a specific URL.

    Args:
        url: The URL to fetch and summarize.
        focus: Optional focus for the summary (e.g., key findings, pros/cons, methods).
        max_words: Approximate maximum length of the summary in words.
        include_quotes: If true, include brief verbatim quotes with minimal context.

    Returns:
        Dict containing:
            - url: The URL that was summarized
            - summary: The generated summary of the content
            - word_count: The word count of the summary
            - included_quotes: Whether quotes were included in the summary
    """
    # Simulate fetching and summarizing content using hash-based generation
    hash_object = hashlib.md5(url.encode())
    hash_digest = hash_object.hexdigest()

    # Generate a mock summary based on the hash
    summary_base = "This is a summary of the content from the provided URL. "
    if focus:
        summary_base += f"Focus: {focus}. "
    if include_quotes:
        summary_base += "Including quotes: 'Sample quote from the content.' "

    # Determine the word count
    word_count = len(summary_base.split())
    if max_words and word_count > max_words:
        summary_base = " ".join(summary_base.split()[:max_words])
        word_count = max_words

    return {
        "url": url,
        "summary": summary_base,
        "word_count": word_count,
        "included_quotes": include_quotes if include_quotes is not None else False,
    }


from datetime import datetime
from typing import Dict


def take_break() -> Dict[str, str]:
    """Log the time that break starts.

    Returns:
        Dict containing:
            - message: Confirmation message of break start
            - start_time: The timestamp when the break started
    """
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "message": "Break started successfully.",
        "start_time": start_time,
    }


from typing import Dict, List, Union


def update_event(
    event_id: str,
    title: Union[str, None] = None,
    start_time: Union[str, None] = None,
    end_time: Union[str, None] = None,
    attendees: Union[List[str], None] = None,
) -> Dict[str, Union[str, List[str]]]:
    """Update an existing calendar event using its unique ID.

    Args:
        event_id: The unique identifier of the event to update.
        title: The new title of the event.
        start_time: The new start date and time in ISO 8601 format.
        end_time: The new end date and time in ISO 8601 format.
        attendees: The new list of email addresses for attendees.

    Returns:
        Dict containing:
            - event_id: The unique identifier of the updated event.
            - title: The updated title of the event.
            - start_time: The updated start time of the event.
            - end_time: The updated end time of the event.
            - attendees: The updated list of attendees.
    """

    # Mock existing event data
    existing_event = {
        "event_id": event_id,
        "title": "Team Meeting",
        "start_time": "2025-08-13T09:00:00Z",
        "end_time": "2025-08-13T10:00:00Z",
        "attendees": ["alice@example.com", "bob@example.com"],
    }

    if event_id != existing_event["event_id"]:
        raise ValueError(f"Event ID not found: {event_id}")

    # Update fields if new values are provided
    updated_event = {
        "event_id": event_id,
        "title": title if title is not None else existing_event["title"],
        "start_time": (
            start_time if start_time is not None else existing_event["start_time"]
        ),
        "end_time": end_time if end_time is not None else existing_event["end_time"],
        "attendees": (
            attendees if attendees is not None else existing_event["attendees"]
        ),
    }

    return updated_event


from typing import Dict, Optional


def update_profile(
    id: str,
    phone: Optional[str] = "",
    name: Optional[str] = "",
    birthday: Optional[str] = "",
) -> Dict[str, str]:
    """Update a profile with a specific 8-digit ID with new information.

    Args:
        id: The profile's unique 8-digit hexadecimal ID (e.g. 293CCCB4)
        phone: The contact's new phone number (123-456-7890)
        name: The contact's new name
        birthday: The contact's new birthday (YYYY-MM-DD)

    Returns:
        Dict containing:
            - id: The profile ID
            - phone: Updated phone number
            - name: Updated name
            - birthday: Updated birthday
    """
    # Mock database of profiles
    profiles = {
        "293CCCB4": {
            "phone": "111-222-3333",
            "name": "Alice Smith",
            "birthday": "1990-01-01",
        },
        "A1B2C3D4": {
            "phone": "444-555-6666",
            "name": "Bob Johnson",
            "birthday": "1985-05-15",
        },
    }

    if id not in profiles:
        raise ValueError(f"Profile ID not found: {id}")

    # Update the profile with new information
    profile = profiles[id]
    if phone:
        profile["phone"] = phone
    if name:
        profile["name"] = name
    if birthday:
        profile["birthday"] = birthday

    return {
        "id": id,
        "phone": profile["phone"],
        "name": profile["name"],
        "birthday": profile["birthday"],
    }


def schedule_meeting(
    date: str, time: str, duration_minutes: int, attendee: str
) -> Dict[str, Union[str, int]]:
    """
    Schedule a meeting with specified details.
    Args:
        date: Date of the meeting (YYYY-MM-DD)
        time: Time of the meeting (HH:MM, 24-hour)
        duration_minutes: Duration in minutes
        attendee: Attendee name or username
    Returns:
        Dict containing:
            - date
            - time
            - duration_minutes
            - attendee
            - confirmation: Confirmation message
    """
    confirmation = f"Meeting scheduled on {date} at {time} for {duration_minutes} minutes with {attendee}."
    return {
        "date": date,
        "time": time,
        "duration_minutes": duration_minutes,
        "attendee": attendee,
        "confirmation": confirmation,
    }
