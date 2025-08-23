import hashlib

# Entertainment Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Literal, Optional, Union


def crawl_lightnovel(
    source: str,
    scope: str,
    output: str,
    media_handling: str = "basic",
) -> Dict[str, Union[str, List[str]]]:
    """Recursively fetch each raw chapter HTML from an online web source for a lightnovel.

    Args:
        source: URL of the lightnovel source
        scope: Chapter range to download (e.g., "31-41,43-60")
        output: Output format ("raw", "processed", "text")
        media_handling: How to handle media content ("basic", "download_all", "skip")

    Returns:
        Dict containing:
            - chapters: List of chapter HTML content
            - status: Status of the crawl operation
    """
    import hashlib

    # Parse scope string into chapter numbers
    chapters = []
    ranges = scope.split(",")
    for range_str in ranges:
        range_str = range_str.strip()
        if "-" in range_str:
            start, end = map(int, range_str.split("-"))
            chapters.extend(list(range(start, end + 1)))
        else:
            chapters.append(int(range_str))

    # Simulate fetching chapters
    chapter_htmls = []
    for chapter in chapters:
        chapter_hash = hashlib.md5(f"{source}/chapter-{chapter}".encode()).hexdigest()
        if output == "raw":
            chapter_html = f"<html><body><h1>Chapter {chapter}</h1><p>Raw HTML content - Hash: {chapter_hash}</p></body></html>"
        elif output == "text":
            chapter_html = f"Chapter {chapter}\n\nText content - Hash: {chapter_hash}"
        else:  # processed
            chapter_html = f"<div class='chapter'><h2>Chapter {chapter}</h2><p>Processed content - Hash: {chapter_hash}</p></div>"

        chapter_htmls.append(chapter_html)

    # Handle media based on media_handling parameter
    if media_handling == "download_all":
        status = f"Downloaded {len(chapters)} chapters with all media content"
    elif media_handling == "skip":
        status = f"Downloaded {len(chapters)} chapters without media content"
    else:  # basic
        status = f"Downloaded {len(chapters)} chapters with basic media handling"

    return {
        "chapters": chapter_htmls,
        "status": status,
    }


def get_preacher_sermons(preacher_id: str) -> Dict[str, Union[str, List[str]]]:
    """Get a list of sermons by a preacher.

    Args:
        preacher_id: The ID of the preacher

    Returns:
        Dict containing:
            - preacher_id: The ID of the preacher
            - sermons: List of sermon titles by the preacher
    """

    sample_sermons = {
        "preacher_17": [
            "The Path to Enlightenment",
            "Faith and Hope",
            "Love Thy Neighbor",
        ],
        "preacher_29": [
            "The Power of Prayer",
            "Finding Peace",
            "Overcoming Adversity",
        ],
        "preacher_30": [
            "The Journey of Faith",
            "Grace and Mercy",
            "Living with Purpose",
        ],
        "preacher_101": [
            "The Power of Positive Thinking",
            "The Law of Attraction",
            "The Secret",
        ],
    }

    if preacher_id not in sample_sermons:
        raise ValueError(f"Preacher ID not found: {preacher_id}")

    return {
        "preacher_id": preacher_id,
        "sermons": sample_sermons.get(preacher_id, []),
    }


from typing import Dict, List, Union


def get_tickets(
    home_team: str, opponent: str, dates: List[str] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Get tickets for your home team against an opponent on specified dates.

    Args:
        home_team: Name of home team.
        opponent: Name of opponent team.
        dates: List of dates to check for games (optional).

    Returns:
        Dict containing:
            - home_team: Name of the home team
            - opponent: Name of the opponent team
            - available_games: List of dictionaries with game details
                - date: Date of the game
                - tickets_available: Number of tickets available
                - price: Price per ticket
    """

    if not home_team or not opponent:
        raise ValueError("Both home_team and opponent must be provided")

    # Sample data generation based on hash of team names and dates
    def generate_ticket_data(date: str) -> Dict[str, Union[str, int]]:
        hash_value = hash((home_team, opponent, date))
        return {
            "date": date,
            "tickets_available": (hash_value % 100) + 1,  # 1 to 100 tickets
            "price": (hash_value % 50) + 20,  # $20 to $70 per ticket
        }

    if dates is None:
        dates = ["2023-11-01", "2023-11-15", "2023-12-01"]  # Default dates

    available_games = [generate_ticket_data(date) for date in dates]

    return {
        "home_team": home_team,
        "opponent": opponent,
        "available_games": available_games,
    }


from typing import Dict, List, Union


def pool_halls(
    city: str, no_locations: int = 3
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Get a list of pool halls based on a given input city.

    Args:
        city: Name of the city to look for pool halls in
        no_locations: Number of pool halls to get data for

    Returns:
        Dict containing:
            - city: Name of the city
            - pool_halls: List of dictionaries with pool hall details
                - name: Name of the pool hall
                - tables: Number of pool tables available
                - rating: Average customer rating
    """

    sample_data = {
        "New York": [
            {"name": "The Corner Pocket", "tables": 12, "rating": 4.5},
            {"name": "Rack & Roll", "tables": 8, "rating": 4.2},
            {"name": "Cue Masters", "tables": 15, "rating": 4.7},
        ],
        "Los Angeles": [
            {"name": "LA Billiards", "tables": 10, "rating": 4.3},
            {"name": "Hollywood Pool House", "tables": 9, "rating": 4.6},
            {"name": "The Break Room", "tables": 11, "rating": 4.4},
        ],
        "Chicago": [
            {"name": "Windy City Billiards", "tables": 14, "rating": 4.5},
            {"name": "Chi-Town Pool Lounge", "tables": 7, "rating": 4.1},
            {"name": "Pocket Aces", "tables": 10, "rating": 4.3},
        ],
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    pool_halls_list = sample_data[city][:no_locations]

    return {
        "city": city,
        "pool_halls": pool_halls_list,
    }


from typing import Dict, List, Optional


def search_movies(title: str, genre: Optional[str] = None) -> Dict[str, List[int]]:
    """Retrieve available movie IDs from the catalogue based on title or genre.

    Args:
        title: Title of the movie to search for.
        genre: Filter results to the given category (optional).

    Returns:
        Dict containing:
            - movie_ids: List of movie IDs matching the search criteria.
    """

    # Sample movie catalogue
    catalogue = {
        "The Matrix": {"id": 1, "genre": "Sci-Fi"},
        "Inception": {"id": 2, "genre": "Sci-Fi"},
        "The Godfather": {"id": 3, "genre": "Crime"},
        "Pulp Fiction": {"id": 4, "genre": "Crime"},
        "Frozen": {"id": 5, "genre": "Animation"},
    }

    # Filter movies by title
    matching_movies = [
        details["id"]
        for movie_title, details in catalogue.items()
        if title.lower() in movie_title.lower()
    ]

    # Further filter by genre if provided
    if genre:
        matching_movies = [
            movie_id
            for movie_id in matching_movies
            if catalogue[
                next(
                    title
                    for title, details in catalogue.items()
                    if details["id"] == movie_id
                )
            ]["genre"].lower()
            == genre.lower()
        ]

    if not matching_movies:
        raise ValueError(f"No movies found for title '{title}' with genre '{genre}'")

    return {"movie_ids": matching_movies}


import hashlib
from typing import Dict, Union


def table_available(
    pool_hall: str, city: str, date: str, time: str
) -> Dict[str, Union[str, bool]]:
    """Check if a table is available at a specific pool hall.

    Args:
        pool_hall: Name of the pool hall
        city: Name of the city
        date: Date on which to look for tables (format: 'YYYY-MM-DD')
        time: Time at which to look for tables (format: 'HH:MM')

    Returns:
        Dict containing:
            - pool_hall: Name of the pool hall
            - city: Name of the city
            - date: Date checked
            - time: Time checked
            - available: Boolean indicating if a table is available
    """
    if not all([pool_hall, city, date, time]):
        raise ValueError("All parameters must be provided and non-empty")

    # Generate a hash to simulate table availability
    hash_input = f"{pool_hall}-{city}-{date}-{time}"
    hash_value = hashlib.md5(hash_input.encode()).hexdigest()

    # Simulate availability based on hash value
    available = int(hash_value, 16) % 2 == 0

    return {
        "pool_hall": pool_hall,
        "city": city,
        "date": date,
        "time": time,
        "available": available,
    }


from datetime import datetime
from typing import Dict, List, Literal, Union


def browse_events(
    city: str,
    date_range: Dict[str, str],
    genres: List[str] = None,
    budget_max: float = None,
    all_ages: bool = None,
    sort_by: Literal["date_asc", "price_asc", "popularity_desc"] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, bool]]]]]:
    """Search for live events in a city within a date range.

    Args:
        city: City to search in.
        date_range: Dictionary with 'start_date' and 'end_date' as keys (YYYY-MM-DD).
        genres: List of preferred event genres (e.g., ['rock', 'comedy']).
        budget_max: Maximum ticket price in local currency.
        all_ages: Only show all-ages events if True.
        sort_by: Sort order, e.g., 'date_asc', 'price_asc', 'popularity_desc'.

    Returns:
        Dict containing:
            - city: City where events are searched.
            - events: List of events with details such as name, date, price, genre, and all_ages.
    """
    # Sample event data
    sample_events = [
        {
            "name": "Rock Concert",
            "date": "2023-11-15",
            "price": 50.0,
            "genre": "rock",
            "all_ages": True,
        },
        {
            "name": "Comedy Night",
            "date": "2023-11-18",
            "price": 30.0,
            "genre": "comedy",
            "all_ages": False,
        },
        {
            "name": "Theater Play",
            "date": "2023-11-20",
            "price": 40.0,
            "genre": "theater",
            "all_ages": True,
        },
        {
            "name": "Jazz Festival",
            "date": "2023-11-22",
            "price": 60.0,
            "genre": "jazz",
            "all_ages": True,
        },
    ]

    # Validate date range
    try:
        start_date = datetime.strptime(date_range["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(date_range["end_date"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    if start_date > end_date:
        raise ValueError("Start date must be before end date.")

    # Filter events based on criteria
    filtered_events = [
        event
        for event in sample_events
        if start_date <= datetime.strptime(event["date"], "%Y-%m-%d") <= end_date
        and (genres is None or event["genre"] in genres)
        and (budget_max is None or event["price"] <= budget_max)
        and (all_ages is None or event["all_ages"] == all_ages)
    ]

    # Sort events if sort_by is specified
    if sort_by:
        if sort_by == "date_asc":
            filtered_events.sort(key=lambda x: x["date"])
        elif sort_by == "price_asc":
            filtered_events.sort(key=lambda x: x["price"])
        elif sort_by == "popularity_desc":
            # Assuming popularity is inversely related to price for mock purposes
            filtered_events.sort(key=lambda x: x["price"], reverse=True)

    return {"city": city, "events": filtered_events}


from typing import Dict, Union


def buy_event_tickets(
    event_name: str, location: str, date: str, tickets: int
) -> Dict[str, Union[str, int, float]]:
    """Purchase tickets for an event.

    Args:
        event_name: Name of the event, e.g. 'Coldplay'
        location: City or venue where the event is held
        date: Date of the event in YYYY-MM-DD format
        tickets: Number of tickets to purchase

    Returns:
        Dict containing:
            - event_name: Name of the event
            - location: Location of the event
            - date: Date of the event
            - tickets: Number of tickets purchased
            - total_cost: Total cost of the tickets
            - confirmation_code: Unique confirmation code for the purchase
    """
    if tickets <= 0:
        raise ValueError("Number of tickets must be greater than zero")

    # Simulate ticket pricing and confirmation code generation
    base_price_per_ticket = 50.0
    total_cost = base_price_per_ticket * tickets
    confirmation_code = f"{hash((event_name, location, date, tickets)) % 1000000:06}"

    return {
        "event_name": event_name,
        "location": location,
        "date": date,
        "tickets": tickets,
        "total_cost": total_cost,
        "confirmation_code": confirmation_code,
    }


from typing import Dict, List


def cast(title: str, include_uncredited: bool = False) -> Dict[str, List[str]]:
    """Retrieve actor names from a movie.

    Args:
        title: Title of the movie to retrieve actors from.
        include_uncredited: Whether to include uncredited actors.

    Returns:
        Dict containing:
            - title: Title of the movie
            - actors: List of actor names
    """
    sample_casts = {
        "Inception": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "The Matrix": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "Titanic": ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"],
    }

    uncredited_actors = {
        "Inception": ["Michael Caine"],
        "The Matrix": ["Hugo Weaving"],
        "Titanic": ["Kathy Bates"],
    }

    if title not in sample_casts:
        raise ValueError(f"Movie not supported: {title}")

    actors = sample_casts[title]
    if include_uncredited:
        actors.extend(uncredited_actors.get(title, []))

    return {
        "title": title,
        "actors": actors,
    }


from typing import Dict, Literal, Union


def check_average_movie_rating(
    movie_name: str, type: Literal["audience", "critic", "both"]
) -> Dict[str, Union[str, float]]:
    """Looks up the average rating out of 5 of a movie based on its name.

    Args:
        movie_name: The name of the movie for the lookup. Does not have to be exact.
        type: The type of reviews to get the average of ('audience', 'critic', 'both').

    Returns:
        Dict containing:
            - movie_name: The name of the movie
            - average_rating: The average rating out of 5
            - review_type: The type of reviews considered
    """

    # Sample data for demonstration purposes
    sample_data = {
        "Inception": {"audience": 4.7, "critic": 4.5},
        "The Matrix": {"audience": 4.6, "critic": 4.4},
        "Titanic": {"audience": 4.3, "critic": 4.2},
        # Comedy movies
        "Superbad": {"audience": 4.5, "critic": 4.0},
        "Step Brothers": {"audience": 4.4, "critic": 3.8},
        "The Hangover": {"audience": 4.6, "critic": 4.2},
    }

    # Normalize movie name for lookup
    normalized_name = movie_name.lower().strip()

    # Find the closest match in the sample data
    for key in sample_data.keys():
        if normalized_name in key.lower():
            movie_data = sample_data[key]
            break
    else:
        raise ValueError(f"Movie not found: {movie_name}")

    # Calculate the average rating based on the requested type
    if type == "audience":
        average_rating = movie_data["audience"]
    elif type == "critic":
        average_rating = movie_data["critic"]
    elif type == "both":
        average_rating = (movie_data["audience"] + movie_data["critic"]) / 2
    else:
        raise ValueError(f"Unsupported review type: {type}")

    return {
        "movie_name": key,
        "average_rating": average_rating,
        "review_type": type,
    }


from typing import Dict, List


def check_movie_tags(movie_name: str) -> Dict[str, List[str]]:
    """Checks the tags of a movie based on its name.

    Args:
        movie_name: The name of the movie for the lookup. Does not have to be exact.

    Returns:
        Dict containing:
            - movie_name: The name of the movie
            - tags: List of tags associated with the movie
    """

    # Sample movie database with tags
    movie_database = {
        "Inception": ["ACTION", "THRILLER", "SCI-FI"],
        "Titanic": ["DRAMA", "ROMANCE"],
        "The Conjuring": ["HORROR", "THRILLER"],
        "The Hangover": ["COMEDY", "CASUAL"],
        "Avengers": ["ACTION", "SCI-FI", "ADVENTURE"],
    }

    # Normalize the movie name for lookup
    normalized_name = movie_name.strip().lower()

    # Find matching movie tags
    for movie, tags in movie_database.items():
        if normalized_name in movie.lower():
            return {
                "movie_name": movie,
                "tags": tags,
            }

    raise ValueError(f"Movie not found: {movie_name}")


from typing import Dict, List


def crunchyroll_upcoming_shows() -> Dict[str, List[str]]:
    """Get a list of upcoming shows on Crunchyroll.

    Returns:
        Dict containing:
            - shows: List of upcoming show titles
    """

    sample_shows = [
        "Attack on Titan: The Final Season",
        "My Hero Academia: Season 6",
        "Demon Slayer: Kimetsu no Yaiba - Swordsmith Village Arc",
        "Jujutsu Kaisen: Season 2",
        "One Piece: Wano Arc",
    ]

    return {"shows": sample_shows}


from typing import Dict, Literal


def dances(
    name: Optional[str] = None,
    style: Optional[Literal[1, 2, 3, 4]] = None,
    participants: Optional[Literal[1, 2]] = None,
) -> Union[Dict[str, str], List[Dict[str, str]]]:
    """Set or get a list of ballroom and latin dance styles.

    Args:
        name: The name of the dance style (e.g., 'Waltz', 'Samba')
        style: The style category (1=ballroom, 2=latin, 3=arg tango, 4=flamenco)
        participants: The number of participants (1 or 2)

    Returns:
        Dict containing:
            - name: Name of the dance
            - style: Style category as a string
            - participants: Number of participants as a string
    """
    style_map = {1: "ballroom", 2: "latin", 3: "argentine tango", 4: "flamenco"}

    # If no parameters provided, return a list of all dance styles
    if name is None and style is None and participants is None:
        # Return a predefined list of common dance styles
        return [
            {"name": "Waltz", "style": "ballroom", "participants": "2 participants"},
            {"name": "Tango", "style": "ballroom", "participants": "2 participants"},
            {"name": "Foxtrot", "style": "ballroom", "participants": "2 participants"},
            {
                "name": "Quickstep",
                "style": "ballroom",
                "participants": "2 participants",
            },
            {
                "name": "Viennese Waltz",
                "style": "ballroom",
                "participants": "2 participants",
            },
            {"name": "Samba", "style": "latin", "participants": "2 participants"},
            {"name": "Cha-Cha", "style": "latin", "participants": "2 participants"},
            {"name": "Rumba", "style": "latin", "participants": "2 participants"},
            {"name": "Paso Doble", "style": "latin", "participants": "2 participants"},
            {"name": "Jive", "style": "latin", "participants": "2 participants"},
            {
                "name": "Argentine Tango",
                "style": "argentine tango",
                "participants": "2 participants",
            },
            {
                "name": "Sevillanas",
                "style": "flamenco",
                "participants": "1 participant",
            },
        ]

    # Validate parameters when they are provided
    if style is not None and style not in style_map:
        raise ValueError(f"Unsupported style: {style}")

    if participants is not None and participants not in [1, 2]:
        raise ValueError(f"Invalid number of participants: {participants}")

    # When parameters are provided, return a single dance
    return {
        "name": name or "Unnamed dance",
        "style": style_map[style] if style is not None else "unspecified",
        "participants": (
            f"{participants} participant{'s' if participants and participants > 1 else ''}"
            if participants is not None
            else "unspecified"
        ),
    }


from typing import Dict, Optional


def find_festival(
    artist_name: str, city: str, start_date: Optional[str] = None
) -> Dict[str, Optional[str]]:
    """Find a festival that includes an artist near you.

    Args:
        artist_name: The artist in the festival
        city: The city to search around
        start_date: Start date of the festival (optional)

    Returns:
        Dict containing:
            - festival_name: Name of the festival
            - city: City where the festival is held
            - artist_name: Name of the artist performing
            - start_date: Start date of the festival
    """

    def normalize_city_name(search_city: str) -> str:
        """Normalize city names for flexible matching."""
        city_mappings = {
            # German cities
            "berlin": "Berlin",
            "hamburg": "Hamburg",
            "munich": "Munich",
            "cologne": "Cologne",
            "frankfurt": "Frankfurt",
            # US cities
            "new york": "New York",
            "nyc": "New York",
            "new york city": "New York",
            "los angeles": "Los Angeles",
            "la": "Los Angeles",
            "chicago": "Chicago",
            "san francisco": "San Francisco",
            "sf": "San Francisco",
            # UK cities
            "london": "London",
            "manchester": "Manchester",
            "birmingham": "Birmingham",
            # Other European cities
            "paris": "Paris",
            "amsterdam": "Amsterdam",
            "madrid": "Madrid",
            "rome": "Rome",
            "barcelona": "Barcelona",
        }

        search_lower = search_city.lower().strip()
        return city_mappings.get(search_lower, search_city)

    def fuzzy_artist_match(search_artist: str, festival_artist: str) -> bool:
        """Check if artist names match with fuzzy logic."""
        search_lower = search_artist.lower().strip()
        festival_lower = festival_artist.lower().strip()

        # Exact match
        if search_lower == festival_lower:
            return True

        # Check if one contains the other
        if search_lower in festival_lower or festival_lower in search_lower:
            return True

        # Check individual words for partial matches
        search_words = set(search_lower.split())
        festival_words = set(festival_lower.split())

        # If any significant word matches (length > 2)
        common_words = search_words.intersection(festival_words)
        significant_matches = [word for word in common_words if len(word) > 2]
        if significant_matches:
            return True

        return False

    # Expanded sample data with more cities and popular artists
    sample_festivals = {
        "New York": [
            {
                "festival_name": "Summer Jam",
                "artist_name": "The Weeknd",
                "start_date": "2023-06-15",
            },
            {
                "festival_name": "Rock Fest",
                "artist_name": "Imagine Dragons",
                "start_date": "2023-07-20",
            },
            {
                "festival_name": "Pop Paradise",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-08-12",
            },
        ],
        "Los Angeles": [
            {
                "festival_name": "Coachella",
                "artist_name": "Beyoncé",
                "start_date": "2023-04-10",
            },
            {
                "festival_name": "Jazz Fest",
                "artist_name": "Norah Jones",
                "start_date": "2023-05-05",
            },
            {
                "festival_name": "Teen Choice Festival",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-07-22",
            },
        ],
        "Chicago": [
            {
                "festival_name": "Lollapalooza",
                "artist_name": "Kendrick Lamar",
                "start_date": "2023-08-01",
            },
            {
                "festival_name": "Blues Fest",
                "artist_name": "John Mayer",
                "start_date": "2023-06-10",
            },
        ],
        "Berlin": [
            {
                "festival_name": "Berlin Music Week",
                "artist_name": "The Killers",
                "start_date": "2023-07-15",
            },
            {
                "festival_name": "Tempelhof Sounds",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-06-25",
            },
            {
                "festival_name": "Lollapalooza Berlin",
                "artist_name": "Arctic Monkeys",
                "start_date": "2023-09-09",
            },
        ],
        "Hamburg": [
            {
                "festival_name": "Reeperbahn Festival",
                "artist_name": "Billie Eilish",
                "start_date": "2023-09-20",
            },
            {
                "festival_name": "Hamburg Music Festival",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-08-05",
            },
        ],
        "London": [
            {
                "festival_name": "Wireless Festival",
                "artist_name": "Drake",
                "start_date": "2023-07-07",
            },
            {
                "festival_name": "British Summer Time",
                "artist_name": "Taylor Swift",
                "start_date": "2023-06-30",
            },
            {
                "festival_name": "Reading Festival",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-08-25",
            },
        ],
        "Paris": [
            {
                "festival_name": "Lollapalooza Paris",
                "artist_name": "Dua Lipa",
                "start_date": "2023-07-22",
            },
            {
                "festival_name": "We Love Green",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-06-02",
            },
        ],
        "Amsterdam": [
            {
                "festival_name": "Amsterdam Open Air",
                "artist_name": "Martin Garrix",
                "start_date": "2023-06-10",
            },
            {
                "festival_name": "Milkshake Festival",
                "artist_name": "Sabrina Carpenter",
                "start_date": "2023-07-29",
            },
        ],
    }

    # Normalize the search city
    normalized_city = normalize_city_name(city)

    # Try to find the city in our data
    matching_city = None
    for festival_city in sample_festivals.keys():
        if normalized_city.lower() == festival_city.lower():
            matching_city = festival_city
            break

    # If exact city not found, try fuzzy matching on city names
    if not matching_city:
        for festival_city in sample_festivals.keys():
            if (
                city.lower() in festival_city.lower()
                or festival_city.lower() in city.lower()
            ):
                matching_city = festival_city
                break

    if not matching_city:
        raise ValueError(f"City not supported: {city}")

    def is_date_compatible(search_date: str, festival_date: str) -> bool:
        """Check if dates are compatible (same month/day, or within reasonable range)"""
        try:
            from datetime import datetime, timedelta

            search_dt = datetime.strptime(search_date, "%Y-%m-%d")
            festival_dt = datetime.strptime(festival_date, "%Y-%m-%d")

            # Same month and day (ignoring year)
            if (
                search_dt.month == festival_dt.month
                and search_dt.day == festival_dt.day
            ):
                return True

            # Within 30 days of each other (ignoring year)
            search_day_of_year = search_dt.timetuple().tm_yday
            festival_day_of_year = festival_dt.timetuple().tm_yday

            if abs(search_day_of_year - festival_day_of_year) <= 30:
                return True

            return False
        except ValueError:
            # If date parsing fails, just return True to be permissive
            return True

    # Look for matching festivals
    matching_festivals = []
    for festival in sample_festivals[matching_city]:
        if fuzzy_artist_match(artist_name, festival["artist_name"]):
            # If start_date provided, check compatibility (not exact match)
            if start_date and not is_date_compatible(
                start_date, festival["start_date"]
            ):
                continue
            matching_festivals.append(festival)

    # If no date-compatible festivals found but we have artist matches,
    # generate a festival with the requested date
    if not matching_festivals and start_date:
        # Find any festival for this artist (ignoring date)
        artist_festivals = [
            f
            for f in sample_festivals[matching_city]
            if fuzzy_artist_match(artist_name, f["artist_name"])
        ]
        if artist_festivals:
            # Use the first match but update the date
            base_festival = artist_festivals[0]
            matching_festivals = [
                {
                    "festival_name": base_festival["festival_name"],
                    "artist_name": base_festival["artist_name"],
                    "start_date": start_date,  # Use the requested date
                }
            ]

    if not matching_festivals:
        raise ValueError(
            f"No festival found for artist '{artist_name}' in {city} on {start_date or 'any date'}"
        )

    # Return the first matching festival
    festival = matching_festivals[0]
    # If we have a search date, use it instead of the festival's original date
    actual_start_date = start_date if start_date else festival["start_date"]

    return {
        "festival_name": festival["festival_name"],
        "city": matching_city,
        "artist_name": festival["artist_name"],
        "start_date": actual_start_date,
    }


from typing import Dict, List, Union


def find_tickets(
    festival_name: str, amount: int, maximum_price: Union[float, None] = None
) -> Dict[str, Union[str, int, float, List[Dict[str, Union[str, float]]]]]:
    """Find tickets for a festival.

    Args:
        festival_name: The name of the festival to search tickets for
        amount: The number of tickets to search for
        maximum_price: The maximum price to pay for tickets (optional)

    Returns:
        Dict containing:
            - festival_name: Name of the festival
            - requested_amount: Number of tickets requested
            - available_tickets: List of available tickets with price and section
    """
    sample_tickets = {
        "Music Fest": [
            {"section": "A", "price": 150.0},
            {"section": "B", "price": 120.0},
            {"section": "C", "price": 100.0},
        ],
        "Art Gala": [
            {"section": "VIP", "price": 300.0},
            {"section": "General", "price": 200.0},
        ],
        "Food Carnival": [
            {"section": "Front", "price": 80.0},
            {"section": "Back", "price": 50.0},
        ],
        "Tempelhof Sounds": [
            {"section": "VIP", "price": 250.0},
            {"section": "General", "price": 150.0},
        ],
    }

    if festival_name not in sample_tickets:
        raise ValueError(f"Festival not supported: {festival_name}")

    available_tickets = [
        ticket
        for ticket in sample_tickets[festival_name]
        if maximum_price is None or ticket["price"] <= maximum_price
    ]

    if len(available_tickets) < amount:
        raise ValueError(f"Not enough tickets available for {festival_name}")

    return {
        "festival_name": festival_name,
        "requested_amount": amount,
        "available_tickets": available_tickets[:amount],
    }


from typing import Dict, List, Union


def gasic_guzzler_meets(
    postcode: str, radius: float = 10
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find outdoor track meets for RC model racing enthusiasts.

    Args:
        postcode: The postcode or outcode to center the search on.
        radius: The search radius in miles around the central postcode.

    Returns:
        Dict containing:
            - centre_postcode: The central postcode used for the search
            - radius: The search radius in miles
            - meets: List of meets with details including:
                - name: Name of the meet
                - location: Location of the meet
                - distance: Distance from the central postcode in miles
    """

    # Mock data generation based on postcode hash
    def generate_meet_data(postcode_hash: int) -> List[Dict[str, Union[str, float]]]:
        sample_meets = [
            {"name": "Turbo Thrills", "location": "Greenfield Park", "distance": 5.2},
            {
                "name": "Nitro Nationals",
                "location": "Speedway Circuit",
                "distance": 8.7,
            },
            {"name": "Combustion Clash", "location": "Racers Arena", "distance": 12.3},
        ]
        # Use hash to simulate variability in returned data
        return [
            meet for i, meet in enumerate(sample_meets) if i % 3 == postcode_hash % 3
        ]

    if not postcode:
        raise ValueError("Postcode is required")

    # Generate a hash from the postcode to simulate different results
    postcode_hash = hash(postcode) % 100

    meets = generate_meet_data(postcode_hash)

    return {
        "centre_postcode": postcode,
        "radius": radius,
        "meets": meets,
    }


from typing import Dict, Union


def get_anime_details(anime_id: int) -> Dict[str, Union[str, int, float, list]]:
    """Retrieve detailed information about an anime given its unique ID.

    Args:
        anime_id: The numeric identifier of the anime

    Returns:
        Dict containing:
            - title: The title of the anime
            - episodes: Total number of episodes
            - rating: Average user rating
            - genres: List of genres the anime belongs to
            - synopsis: Brief description of the anime
    """
    sample_data = {
        1: {
            "title": "Naruto",
            "episodes": 220,
            "rating": 8.3,
            "genres": ["Action", "Adventure", "Fantasy"],
            "synopsis": "A young ninja strives to be the best and gain recognition.",
        },
        2: {
            "title": "Attack on Titan",
            "episodes": 75,
            "rating": 9.0,
            "genres": ["Action", "Drama", "Fantasy"],
            "synopsis": "Humanity fights for survival against giant humanoid creatures.",
        },
        3: {
            "title": "My Hero Academia",
            "episodes": 113,
            "rating": 8.5,
            "genres": ["Action", "Comedy", "Superhero"],
            "synopsis": "A boy without powers enrolls in a hero academy.",
        },
    }

    if anime_id not in sample_data:
        raise ValueError(f"Anime ID not found: {anime_id}")

    return sample_data[anime_id]


from typing import Dict, List, Union


def get_blu_ray_information(title_name: str) -> Dict[str, Union[str, int, List[str]]]:
    """Get information about a specific blu-ray title.

    Args:
        title_name: The name of the title to get information about

    Returns:
        Dict containing:
            - title: The name of the blu-ray title
            - runtime: The runtime of the movie in minutes
            - certification: The certification rating of the movie
            - cast: List of main cast members
            - crew: List of main crew members
    """

    sample_data = {
        "Inception": {
            "runtime": 148,
            "certification": "PG-13",
            "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
            "crew": ["Christopher Nolan", "Emma Thomas"],
        },
        "The Matrix": {
            "runtime": 136,
            "certification": "R",
            "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
            "crew": ["Lana Wachowski", "Lilly Wachowski"],
        },
        "Interstellar": {
            "runtime": 169,
            "certification": "PG-13",
            "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
            "crew": ["Christopher Nolan", "Emma Thomas"],
        },
    }

    if title_name not in sample_data:
        raise ValueError(f"Title not supported: {title_name}")

    return {"title": title_name, **sample_data[title_name]}


from typing import Dict, List, Union


def get_channel_video_urls(search_query: str) -> Dict[str, Union[str, List[str]]]:
    """Get a list of video URLs from the channel that most closely matches your search.

    Args:
        search_query: Search query that is as close as possible to the channel you want to find

    Returns:
        Dict containing:
            - channel_name: Name of the channel
            - video_urls: List of video URLs from the channel
    """
    # Simulated channel data
    channels = {
        "Tech Reviews": [
            "https://video.example.com/tech-reviews-1",
            "https://video.example.com/tech-reviews-2",
            "https://video.example.com/tech-reviews-3",
        ],
        "Cooking with Jamie": [
            "https://video.example.com/cooking-jamie-1",
            "https://video.example.com/cooking-jamie-2",
            "https://video.example.com/cooking-jamie-3",
        ],
        "Travel Vlogs": [
            "https://video.example.com/travel-vlogs-1",
            "https://video.example.com/travel-vlogs-2",
            "https://video.example.com/travel-vlogs-3",
        ],
        "Rotary Generators": [
            "https://video.example.com/rotary-generators-1",
            "https://video.example.com/rotary-generators-2",
            "https://video.example.com/rotary-generators-3",
        ],
        "Mechanical Marvels": [
            "https://video.example.com/mechanical-marvels-1",
            "https://video.example.com/mechanical-marvels-2",
            "https://video.example.com/mechanical-marvels-3",
        ],
        "Gears and Motors": [
            "https://video.example.com/gears-motors-1",
            "https://video.example.com/gears-motors-2",
            "https://video.example.com/gears-motors-3",
        ],
        "Kids Engineering": [
            "https://video.example.com/kids-engineering-1",
            "https://video.example.com/kids-engineering-2",
            "https://video.example.com/kids-engineering-3",
        ],
        "How Machines Work": [
            "https://video.example.com/how-machines-work-1",
            "https://video.example.com/how-machines-work-2",
            "https://video.example.com/how-machines-work-3",
        ],
        "Car Mechanics for Kids": [
            "https://video.example.com/car-mechanics-kids-1",
            "https://video.example.com/car-mechanics-kids-2",
            "https://video.example.com/car-mechanics-kids-3",
        ],
    }

    # Simple matching logic based on search query
    matched_channel = None
    for channel in channels:
        if search_query.lower() in channel.lower():
            matched_channel = channel
            break

    if not matched_channel:
        raise ValueError(f"No channel found matching the search query: {search_query}")

    return {
        "channel_name": matched_channel,
        "video_urls": channels[matched_channel],
    }


from typing import Dict, Literal


def get_love_horoscope(
    zodiac_sign: str,
    time_period: Literal["today", "this_week", "this_month"] = "today",
) -> Dict[str, str]:
    """Get the love and relationship horoscope for a zodiac sign.

    Args:
        zodiac_sign: The zodiac sign to get the horoscope for (e.g. 'aries', 'taurus')
        time_period: The time period for the love horoscope ('today', 'this_week', 'this_month')

    Returns:
        Dict containing:
            - zodiac_sign: The zodiac sign
            - time_period: The time period for the horoscope
            - horoscope: A love and relationship horoscope message
    """

    horoscopes = {
        "aries": {
            "today": "Today is a great day to express your feelings to someone special.",
            "this_week": "This week, focus on building trust in your relationships.",
            "this_month": "This month, you may find love in unexpected places.",
        },
        "taurus": {
            "today": "Patience is key today in your love life.",
            "this_week": "This week, you might reconnect with an old flame.",
            "this_month": "This month, take time to nurture your relationships.",
        },
        # Add entries for other zodiac signs...
    }

    if zodiac_sign not in horoscopes:
        raise ValueError(f"Zodiac sign not supported: {zodiac_sign}")

    return {
        "zodiac_sign": zodiac_sign,
        "time_period": time_period,
        "horoscope": horoscopes[zodiac_sign].get(
            time_period, "No horoscope available for this time period."
        ),
    }


from typing import Dict, List


def get_movie_cast(movie_id: str) -> Dict[str, Union[str, List[str]]]:
    """Retrieve the cast members of a movie given its ID.

    Args:
        movie_id: Movie's unique identifier

    Returns:
        Dict containing:
            - movie_id: The unique identifier of the movie
            - cast: List of cast members' names
    """

    sample_casts = {
        "movie_001": ["John Doe", "Jane Smith", "Alice Johnson"],
        "movie_002": ["Tom Hanks", "Emma Watson", "Chris Evans"],
        "movie_003": ["Scarlett Johansson", "Robert Downey Jr.", "Chris Hemsworth"],
    }

    if movie_id not in sample_casts:
        raise ValueError(f"Movie ID not found: {movie_id}")

    return {
        "movie_id": movie_id,
        "cast": sample_casts[movie_id],
    }


from typing import Dict


def get_movie_genre(movie_name: str) -> Dict[str, str]:
    """Retrieve the genre of a movie.

    Args:
        movie_name: The name of the movie to get the genre of.

    Returns:
        Dict containing:
            - movie_name: The name of the movie
            - genre: The genre of the movie
    """

    sample_genres = {
        "Inception": "Science Fiction",
        "The Godfather": "Crime",
        "Pulp Fiction": "Crime",
        "The Shawshank Redemption": "Drama",
        "The Dark Knight": "Action",
    }

    if movie_name not in sample_genres:
        raise ValueError(f"Movie not supported: {movie_name}")

    return {
        "movie_name": movie_name,
        "genre": sample_genres[movie_name],
    }


from typing import Dict, Union


def get_movie_ratings(
    title: str, year: Union[int, None] = None
) -> Dict[str, Union[str, float, list]]:
    """Returns ratings and content advisories for a movie.

    Args:
        title: Movie title.
        year: Release year (optional).

    Returns:
        Dict containing:
            - title: Movie title
            - year: Release year
            - rating: Average rating out of 10
            - advisories: List of content advisories
    """

    # Simulated data based on title hash for consistency
    sample_ratings = {
        "Inception": 8.8,
        "The Matrix": 8.7,
        "Titanic": 7.8,
    }
    sample_advisories = {
        "Inception": ["Violence", "Language"],
        "The Matrix": ["Sci-Fi Violence", "Language"],
        "Titanic": ["Nudity", "Disaster"],
    }

    if title not in sample_ratings:
        raise ValueError(f"Movie not supported: {title}")

    return {
        "title": title,
        "year": year if year is not None else "Unknown",
        "rating": sample_ratings[title],
        "advisories": sample_advisories[title],
    }


from typing import Dict, Union


def get_movie_recommendation(
    genre: str, rating: float = 5, actor: Union[str, None] = None
) -> Dict[str, Union[str, float]]:
    """Recommends a movie based on genre, minimum rating, and optional actor.

    Args:
        genre: The genre of the movie to be recommended (e.g. 'Action', 'Comedy')
        rating: The minimum rating of the movie to be recommended (default is 5)
        actor: The actor that should be starred in the movie (optional)

    Returns:
        Dict containing:
            - title: Title of the recommended movie
            - genre: Genre of the recommended movie
            - rating: Rating of the recommended movie
            - actor: Lead actor of the recommended movie
    """

    sample_movies = {
        "Action": [
            {"title": "Fast & Furious", "rating": 7.2, "actor": "Vin Diesel"},
            {"title": "Mad Max: Fury Road", "rating": 8.1, "actor": "Tom Hardy"},
        ],
        "Comedy": [
            {"title": "Superbad", "rating": 7.6, "actor": "Jonah Hill"},
            {"title": "The Hangover", "rating": 7.7, "actor": "Bradley Cooper"},
        ],
        "Drama": [
            {
                "title": "The Shawshank Redemption",
                "rating": 9.3,
                "actor": "Tim Robbins",
            },
            {"title": "Forrest Gump", "rating": 8.8, "actor": "Tom Hanks"},
        ],
    }

    if genre not in sample_movies:
        raise ValueError(f"Genre not supported: {genre}")

    for movie in sample_movies[genre]:
        if movie["rating"] >= rating and (actor is None or movie["actor"] == actor):
            return {
                "title": movie["title"],
                "genre": genre,
                "rating": movie["rating"],
                "actor": movie["actor"],
            }

    raise ValueError("No movie found matching the criteria")


from typing import Dict, List, Optional, Union


def get_movies(
    movie_name: Optional[str] = None,
    genre: Optional[str] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    num_movies: Optional[int] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Retrieve movies that meet the specified criteria.

    Args:
        movie_name: The name of the movie to search for.
        genre: A specific movie genre to filter by.
        min_length: The minimum length of the movie in minutes.
        max_length: The maximum length of the movie in minutes.
        num_movies: The number of movies to retrieve.

    Returns:
        Dict containing:
            - criteria: Description of the search criteria used
            - movies: List of movies matching the criteria, each with:
                - title: The title of the movie
                - genre: The genre of the movie
                - length: The length of the movie in minutes
    """

    sample_movies = [
        {"title": "The Great Adventure", "genre": "Action", "length": 120},
        {"title": "Romantic Getaway", "genre": "Romance", "length": 95},
        {"title": "Mystery of the Old House", "genre": "Mystery", "length": 110},
        {"title": "Comedy Night", "genre": "Comedy", "length": 85},
        {"title": "Sci-Fi Odyssey", "genre": "Science Fiction", "length": 130},
    ]

    def matches_criteria(movie):
        if movie_name and movie_name.lower() not in movie["title"].lower():
            return False
        if genre and genre.lower() != movie["genre"].lower():
            return False
        if min_length and movie["length"] < min_length:
            return False
        if max_length and movie["length"] > max_length:
            return False
        return True

    filtered_movies = list(filter(matches_criteria, sample_movies))

    if num_movies is not None:
        filtered_movies = filtered_movies[:num_movies]

    return {
        "criteria": f"movie_name={movie_name}, genre={genre}, min_length={min_length}, max_length={max_length}, num_movies={num_movies}",
        "movies": filtered_movies,
    }


from typing import Dict, Optional, Union


def get_movies_playing(
    name: Optional[str] = None,
    genre: Optional[str] = None,
    date: Optional[str] = None,
    start_time: Optional[str] = None,
    rating: Optional[float] = None,
) -> Dict[str, Union[str, float, list]]:
    """Retrieve local movies that are playing based on optional filters.

    Args:
        name: Name of the movie to filter by (e.g. 'Inception')
        genre: Genre of the movie to filter by (e.g. 'Action')
        date: Date of the movie showing to filter by (e.g. '2023-10-15')
        start_time: Start time of the movie to filter by (e.g. '19:00')
        rating: Minimum rating of the movie to filter by (e.g. 8.0)

    Returns:
        Dict containing:
            - movies: List of movies matching the criteria, each with:
                - name: Name of the movie
                - genre: Genre of the movie
                - date: Date of the showing
                - start_time: Start time of the movie
                - rating: Rating of the movie
    """
    sample_movies = [
        {
            "name": "Inception",
            "genre": "Action",
            "date": "2023-10-15",
            "start_time": "19:00",
            "rating": 8.8,
        },
        {
            "name": "The Godfather",
            "genre": "Crime",
            "date": "2023-10-15",
            "start_time": "20:00",
            "rating": 9.2,
        },
        {
            "name": "Toy Story",
            "genre": "Animation",
            "date": "2023-10-15",
            "start_time": "17:00",
            "rating": 8.3,
        },
        {
            "name": "Titanic",
            "genre": "Romance",
            "date": "2023-10-16",
            "start_time": "18:00",
            "rating": 7.8,
        },
    ]

    def matches_criteria(movie):
        if name and movie["name"] != name:
            return False
        if genre and movie["genre"] != genre:
            return False
        if date and movie["date"] != date:
            return False
        if start_time and movie["start_time"] != start_time:
            return False
        if rating and movie["rating"] < rating:
            return False
        return True

    filtered_movies = [movie for movie in sample_movies if matches_criteria(movie)]

    return {"movies": filtered_movies}


from typing import Dict, List


def get_netflix_streaming_availability(
    movie_name: str,
) -> Dict[str, Union[str, List[str]]]:
    """Retrieve the countries where a movie is available on Netflix.

    Args:
        movie_name: The name of the movie to check availability for.

    Returns:
        Dict containing:
            - movie_name: The name of the movie
            - available_countries: List of countries where the movie is available
    """

    # Sample data simulating availability based on movie name hash
    sample_data = {
        "Inception": ["United States", "Canada", "United Kingdom", "Germany"],
        "Parasite": ["South Korea", "Japan", "France", "Australia"],
        "The Godfather": ["Italy", "United States", "Brazil"],
    }

    # Use a hash-based approach to simulate consistent but varied availability
    hash_value = hash(movie_name) % 3
    movie_keys = list(sample_data.keys())

    if movie_name not in movie_keys:
        raise ValueError(f"Movie not supported: {movie_name}")

    available_countries = sample_data[movie_keys[hash_value]]

    return {
        "movie_name": movie_name,
        "available_countries": available_countries,
    }


from typing import Dict, List


def get_player_details(
    player_name: str, date_of_birth: str
) -> Dict[str, Union[str, List[str]]]:
    """Get detailed information about a specific player including their positions, availability, and team eligibility.

    Args:
        player_name: Name of the player to get details for
        date_of_birth: Player's date of birth in YYYY-MM-DD format (used for unique identification)

    Returns:
        Dict containing:
            - player_name: Name of the player
            - positions: List of positions the player can play
            - availability: Availability status of the player
            - team_eligibility: List of teams the player is eligible to play for
    """
    # Sample data generation based on hash of player_name and date_of_birth
    sample_positions = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
    sample_availability = ["Available", "Injured", "Suspended"]
    sample_teams = ["Team A", "Team B", "Team C", "Team D"]

    if not player_name or not date_of_birth:
        raise ValueError("Both player_name and date_of_birth are required")

    # Generate a hash-based index for sample data selection
    index = hash(player_name + date_of_birth) % 4

    return {
        "player_name": player_name,
        "positions": [sample_positions[index], sample_positions[(index + 1) % 4]],
        "availability": sample_availability[index % 3],
        "team_eligibility": [sample_teams[index], sample_teams[(index + 2) % 4]],
    }


from typing import Dict, List, Union


def get_top_rated(
    page: int = 1,
) -> Dict[str, Union[int, List[Dict[str, Union[str, float]]]]]:
    """Get a paginated list of top-rated animes.

    Args:
        page: Page number to retrieve (default is 1)

    Returns:
        Dict containing:
            - page: Current page number
            - animes: List of dictionaries with anime details, each containing:
                - title: Title of the anime
                - rating: Average rating of the anime
    """
    if page < 1:
        raise ValueError("Page number must be a positive integer")

    # Sample data for demonstration purposes
    sample_animes = [
        {"title": "Fullmetal Alchemist: Brotherhood", "rating": 9.25},
        {"title": "Attack on Titan", "rating": 9.15},
        {"title": "Steins;Gate", "rating": 9.10},
        {"title": "Your Lie in April", "rating": 8.90},
        {"title": "My Hero Academia", "rating": 8.75},
        {"title": "Demon Slayer", "rating": 8.70},
        {"title": "One Punch Man", "rating": 8.55},
        {"title": "Naruto", "rating": 8.50},
        {"title": "Death Note", "rating": 9.00},
        {"title": "Dragon Ball Z", "rating": 8.40},
    ]

    # Simulate pagination by dividing the sample data into pages
    items_per_page = 3
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paginated_animes = sample_animes[start_index:end_index]

    if not paginated_animes:
        raise ValueError(f"No animes found for page {page}")

    return {
        "page": page,
        "animes": paginated_animes,
    }


from typing import Dict, List, Union


def get_upcoming_tv_shows(
    channel: str, limit: int = 5
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Retrieve a list of upcoming television shows for a given channel or platform.

    Args:
        channel: The TV channel, streaming service, or network to query.
        limit: Maximum number of shows to return (default is 5).

    Returns:
        Dict containing:
            - channel: The queried channel or platform
            - shows: List of upcoming shows with title and premiere date
    """

    sample_data = {
        "Netflix": [
            {"title": "Stranger Things", "premiere_date": "2023-11-15"},
            {"title": "The Crown", "premiere_date": "2023-12-01"},
            {"title": "Black Mirror", "premiere_date": "2023-12-10"},
        ],
        "HBO": [
            {"title": "Game of Thrones", "premiere_date": "2023-11-20"},
            {"title": "Westworld", "premiere_date": "2023-12-05"},
            {"title": "Succession", "premiere_date": "2023-12-15"},
        ],
        "Disney+": [
            {"title": "The Mandalorian", "premiere_date": "2023-11-25"},
            {"title": "Loki", "premiere_date": "2023-12-03"},
            {"title": "WandaVision", "premiere_date": "2023-12-12"},
        ],
    }

    if channel not in sample_data:
        raise ValueError(f"Channel not supported: {channel}")

    shows = sample_data[channel][:limit]

    return {
        "channel": channel,
        "shows": shows,
    }


from datetime import datetime, timedelta
from typing import Dict, List, Union


def get_venue_schedule(
    venue_id: str, date: Union[str, None] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Retrieve a venue’s event schedule for a specific date or the next 7 days if no date is given.

    Args:
        venue_id: Unique ID of the venue
        date: Target date (YYYY-MM-DD). If omitted, returns the upcoming 7-day schedule.

    Returns:
        Dict containing:
            - venue_id: Unique ID of the venue
            - schedule: List of events with each event containing:
                - event_name: Name of the event
                - start_time: Event start time in HH:MM format
                - duration: Duration of the event in minutes
    """

    # Sample data generation based on venue_id hash
    def generate_event_data(seed: int) -> Dict[str, Union[str, int]]:
        event_names = ["Concert", "Play", "Exhibition", "Conference", "Workshop"]
        return {
            "event_name": event_names[seed % len(event_names)],
            "start_time": f"{10 + seed % 12:02d}:{seed % 60:02d}",
            "duration": 60 + (seed % 120),
        }

    # Validate date format if provided
    if date:
        try:
            target_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Invalid date format: {date}. Expected format is YYYY-MM-DD."
            )
    else:
        target_date = datetime.now()

    # Generate schedule for the specified date or the next 7 days
    schedule = []
    for i in range(7 if date is None else 1):
        current_date = target_date + timedelta(days=i)
        seed = hash((venue_id, current_date.date())) % 1000
        schedule.append(
            {"date": current_date.strftime("%Y-%m-%d"), **generate_event_data(seed)}
        )

    return {"venue_id": venue_id, "schedule": schedule}


from typing import Dict, List


def get_video_urls(search_query: str) -> Dict[str, List[str]]:
    """Get a list of video URLs that satisfy the search query.

    Args:
        search_query: The search query for the video you want to find

    Returns:
        Dict containing:
            - search_query: The original search query
            - video_urls: List of video URLs that match the search query
    """
    if not search_query:
        raise ValueError("Search query must not be empty")

    # Simulate video URL generation based on the search query
    base_url = "https://video.example.com/watch?v="
    hash_base = abs(hash(search_query)) % 1000
    video_urls = [f"{base_url}{hash_base + i}" for i in range(5)]

    return {
        "search_query": search_query,
        "video_urls": video_urls,
    }


from typing import Dict, List, Union


def hold_tickets(
    event_id: str,
    quantity: int,
    section_preference: List[str] = None,
    hold_minutes: int = 15,
    buyer_name: str = None,
) -> Dict[str, Union[str, int, List[str]]]:
    """Place a temporary hold on tickets for a specific event and quantity.

    Args:
        event_id: Unique ID of the event
        quantity: Number of tickets to hold (integer)
        section_preference: Preferred sections, e.g., ['floor', 'balcony']
        hold_minutes: How long to hold tickets (max 20 minutes). Defaults to 15.
        buyer_name: Name to associate with the hold

    Returns:
        Dict containing:
            - event_id: Unique ID of the event
            - quantity: Number of tickets held
            - sections: List of sections where tickets are held
            - hold_time: Duration of the hold in minutes
            - buyer_name: Name associated with the hold
    """
    if hold_minutes > 20:
        raise ValueError("Hold time cannot exceed 20 minutes")

    sample_sections = {
        "concert123": ["floor", "balcony", "vip"],
        "theater456": ["orchestra", "mezzanine", "balcony"],
    }

    if event_id not in sample_sections:
        raise ValueError(f"Event ID not supported: {event_id}")

    available_sections = sample_sections[event_id]
    selected_sections = (
        [section for section in section_preference if section in available_sections]
        if section_preference
        else available_sections[:1]
    )

    return {
        "event_id": event_id,
        "quantity": quantity,
        "sections": selected_sections,
        "hold_time": hold_minutes,
        "buyer_name": buyer_name or "Anonymous",
    }


from typing import Dict, List


def list_movies() -> Dict[str, List[Dict[str, str]]]:
    """Gets all upcoming movies and their showing date/time and location.

    Returns:
        Dict containing:
            - movies: List of dictionaries with each movie's details:
                - title: Title of the movie
                - showtime: Date and time of the showing
                - location: Location of the theater
    """

    sample_movies = [
        {
            "title": "The Great Adventure",
            "showtime": "2023-11-15 19:00",
            "location": "Cinema City",
        },
        {
            "title": "Space Odyssey",
            "showtime": "2023-11-16 20:30",
            "location": "Grand Theater",
        },
        {
            "title": "Mystery of the Night",
            "showtime": "2023-11-17 18:45",
            "location": "Downtown Cinema",
        },
    ]

    return {"movies": sample_movies}


from typing import Dict, List, Literal


def lookup_movies(
    tag: Literal["CASUAL", "ACTION", "THRILLER", "HORROR", "COMEDY", "DRAMA", "ROMANCE"]
) -> Dict[str, List[str]]:
    """Search for movies based on a tag.

    Args:
        tag: The tag to search for (e.g. 'ACTION', 'COMEDY')

    Returns:
        Dict containing:
            - tag: The tag used for searching
            - movies: List of movie titles that match the tag
    """

    movie_database = {
        "CASUAL": ["The Easy Life", "Just Chillin'", "Everyday Adventures"],
        "ACTION": ["Fast & Furious", "Die Hard", "Mad Max: Fury Road"],
        "THRILLER": ["Inception", "Se7en", "Gone Girl"],
        "HORROR": ["The Conjuring", "A Nightmare on Elm Street", "It"],
        "COMEDY": ["Superbad", "Step Brothers", "The Hangover"],
        "DRAMA": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
        "ROMANCE": ["The Notebook", "Pride & Prejudice", "La La Land"],
    }

    if tag not in movie_database:
        raise ValueError(f"Tag not supported: {tag}")

    return {
        "tag": tag,
        "movies": movie_database[tag],
    }


from typing import Dict, Union


def movie_details(title: str) -> Dict[str, Union[str, list]]:
    """Retrieve the description and genre of a movie.

    Args:
        title: Title of the movie to retrieve details for

    Returns:
        Dict containing:
            - title: Title of the movie
            - description: Brief description of the movie
            - genre: List of genres the movie belongs to
    """

    sample_data = {
        "Inception": {
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
            "genre": ["Action", "Adventure", "Sci-Fi"],
        },
        "The Godfather": {
            "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
            "genre": ["Crime", "Drama"],
        },
        "The Shawshank Redemption": {
            "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "genre": ["Drama"],
        },
    }

    if title not in sample_data:
        raise ValueError(f"Movie not found: {title}")

    return {
        "title": title,
        "description": sample_data[title]["description"],
        "genre": sample_data[title]["genre"],
    }


from typing import Dict, List


def movie_genre(movie_id: str) -> Dict[str, List[str]]:
    """Get genres of a given movie by database ID.

    Args:
        movie_id: ID of the movie.

    Returns:
        Dict containing:
            - movie_id: The ID of the movie
            - genres: List of genres associated with the movie
    """

    # Simulated database of movie genres
    movie_genres_db = {
        "tt0111161": ["Drama"],
        "tt0068646": ["Crime", "Drama"],
        "tt0071562": ["Crime", "Drama"],
        "tt0468569": ["Action", "Crime", "Drama"],
        "tt0050083": ["Crime", "Drama", "Mystery"],
        "932281": ["Romance", "Comedy"],
    }

    if movie_id not in movie_genres_db:
        raise ValueError(f"Movie ID not found: {movie_id}")

    return {
        "movie_id": movie_id,
        "genres": movie_genres_db[movie_id],
    }


from typing import Dict, List, Union


def movie_reviews(
    title: str, review_score: Union[int, None] = None
) -> Dict[str, Union[str, List[str]]]:
    """Returns a list of review comments about a movie.

    Args:
        title: Title of the movie.
        review_score: If set, only reviews with the given review scores will be returned. Must be between 1 and 5.

    Returns:
        Dict containing:
            - title: Title of the movie
            - reviews: List of review comments
    """

    sample_reviews = {
        "Inception": [
            (5, "A mind-bending masterpiece!"),
            (4, "Great visuals and story."),
            (3, "Good, but a bit confusing."),
            (2, "Too complex for my taste."),
            (1, "Didn't enjoy it at all."),
        ],
        "The Matrix": [
            (5, "A revolutionary sci-fi classic."),
            (4, "Amazing action and story."),
            (3, "Interesting, but overhyped."),
            (2, "Not my cup of tea."),
            (1, "Found it boring."),
        ],
    }

    if title not in sample_reviews:
        raise ValueError(f"Movie not supported: {title}")

    if review_score is not None:
        if not (1 <= review_score <= 5):
            raise ValueError("Review score must be between 1 and 5.")
        reviews = [
            comment for score, comment in sample_reviews[title] if score == review_score
        ]
    else:
        reviews = [comment for _, comment in sample_reviews[title]]

    return {
        "title": title,
        "reviews": reviews,
    }


from typing import Dict, List


def movies_by_genre(genre: str) -> Dict[str, List[str]]:
    """Retrieve a list of movies for a given genre.

    Args:
        genre: A movie genre (e.g. 'Action', 'Comedy', 'Drama')

    Returns:
        Dict containing:
            - genre: The genre requested
            - movies: List of movie titles within the specified genre
    """

    sample_data = {
        "Action": ["Mad Max: Fury Road", "Die Hard", "John Wick"],
        "Comedy": ["Superbad", "Step Brothers", "The Hangover"],
        "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
        "Horror": ["The Exorcist", "Get Out", "A Nightmare on Elm Street"],
        "Sci-Fi": ["Inception", "The Matrix", "Interstellar"],
    }

    if genre not in sample_data:
        raise ValueError(f"Genre not supported: {genre}")

    return {
        "genre": genre,
        "movies": sample_data[genre],
    }


from typing import Dict, List


def movies_by_year(year: int) -> Dict[str, Union[int, List[str]]]:
    """Retrieve movies released in a given year.

    Args:
        year: Year of movie release

    Returns:
        Dict containing:
            - year: The year of movie release
            - movies: List of movie titles released in that year
    """
    sample_data = {
        1994: ["The Shawshank Redemption", "Pulp Fiction", "Forrest Gump"],
        2001: [
            "The Lord of the Rings: The Fellowship of the Ring",
            "Harry Potter and the Sorcerer's Stone",
            "Shrek",
        ],
        2010: ["Inception", "The Social Network", "Toy Story 3"],
    }

    if year not in sample_data:
        raise ValueError(f"No data available for the year: {year}")

    return {
        "year": year,
        "movies": sample_data[year],
    }


from typing import Dict, Literal, Union


def myanimelist_data(
    series_title: str, series_format: str, data_type: str
) -> Dict[str, Union[str, int, float]]:
    """Retrieve data from MyAnimeList for a specified series.

    Args:
        series_title: The title of the series to retrieve data for.
        series_format: The format of the series (e.g., 'anime', 'manga').
        data_type: The type of data to retrieve (e.g., 'score', 'popularity rank').

    Returns:
        Dict containing:
            - series_title: Title of the series
            - series_format: Format of the series
            - data_type: Type of data requested
            - value: The value of the requested data type
    """

    # Sample data generation based on series_title hash
    hash_value = hash(series_title) % 1000

    if series_format not in ["anime", "manga", "manhwa"]:
        raise ValueError(f"Unsupported series format: {series_format}")

    if data_type not in ["score", "popularity rank", "score rank"]:
        raise ValueError(f"Unsupported data type: {data_type}")

    # Mock data based on data_type
    if data_type == "score":
        value = 5.0 + (hash_value % 50) / 10  # Score between 5.0 and 9.9
    elif data_type == "popularity rank":
        value = hash_value % 10000 + 1  # Rank between 1 and 10000
    elif data_type == "score rank":
        value = hash_value % 5000 + 1  # Rank between 1 and 5000

    return {
        "series_title": series_title,
        "series_format": series_format,
        "data_type": data_type,
        "value": value,
    }


from typing import Dict


def play_movie_chromecast(movie_id: str, device_id: str) -> Dict[str, str]:
    """Play a movie with the given ID on the specified Chromecast device.

    Args:
        movie_id: Movie's unique identifier
        device_id: Device's unique identifier

    Returns:
        Dict containing:
            - status: Status of the playback initiation
            - message: Detailed message about the playback status
    """
    # Sample data for devices and movies
    devices = {
        "device_001": "Living Room Chromecast",
        "device_002": "Bedroom Chromecast",
    }
    movies = {
        "movie_001": "Inception",
        "movie_002": "The Matrix",
    }

    if device_id not in devices:
        raise ValueError(f"Device not found: {device_id}")
    if movie_id not in movies:
        raise ValueError(f"Movie not found: {movie_id}")

    # Simulate playing the movie
    return {
        "status": "success",
        "message": f"Playing '{movies[movie_id]}' on {devices[device_id]}",
    }


from typing import Dict, Union


def post_movie_rating(name: str, rating: float) -> Dict[str, Union[str, float]]:
    """Post a rating for a movie.

    Args:
        name: The name of the movie to be rated
        rating: The rating of the movie

    Returns:
        Dict containing:
            - name: The name of the movie
            - rating: The rating given to the movie
            - status: Status of the rating post operation
    """
    if not (0 <= rating <= 10):
        raise ValueError("Rating must be between 0 and 10")

    # Simulate a hash-based generation for consistent but varied sample data
    hash_value = hash(name) % 100
    status = "success" if hash_value % 2 == 0 else "pending"

    return {
        "name": name,
        "rating": rating,
        "status": status,
    }


from typing import Dict, Union


def purchase_movie_tickets(
    title: str, cinema: str, date: str, time: str, seats: int = 1
) -> Dict[str, Union[str, int, float]]:
    """Purchases movie tickets for a given show.

    Args:
        title: Movie title.
        cinema: Cinema name or location.
        date: Show date (YYYY-MM-DD).
        time: Show time (HH:MM).
        seats: Number of seats to purchase (default is 1).

    Returns:
        Dict containing:
            - title: Movie title
            - cinema: Cinema name
            - date: Show date
            - time: Show time
            - seats: Number of seats purchased
            - total_cost: Total cost of the tickets
    """
    if seats < 1:
        raise ValueError("Number of seats must be at least 1")

    # Mocked ticket pricing logic
    base_price = 12.5
    total_cost = base_price * seats

    return {
        "title": title,
        "cinema": cinema,
        "date": date,
        "time": time,
        "seats": seats,
        "total_cost": total_cost,
    }


from typing import Dict, List, Literal, Union


def purchase_tickets(
    event_id: str,
    seat_ids: List[str] = None,
    quantity: int = None,
    payment_token: str = None,
    delivery_method: Literal["mobile", "will_call", "print_at_home"] = None,
    email: str = None,
    agree_to_terms: bool = None,
) -> Dict[str, Union[str, int, List[str], bool]]:
    """Complete a ticket purchase for specific seats using a payment token.

    Args:
        event_id: Unique ID of the event
        seat_ids: Exact seat identifiers to purchase
        quantity: Number of tickets (must match seat_ids length if provided)
        payment_token: Tokenized payment method
        delivery_method: Ticket delivery: 'mobile', 'will_call', or 'print_at_home'
        email: Receipt and ticket email address
        agree_to_terms: Must be true to complete purchase

    Returns:
        Dict containing:
            - purchase_id: Unique identifier for the purchase
            - event_id: The event ID for which tickets were purchased
            - seats: List of seat IDs purchased
            - quantity: Number of tickets purchased
            - delivery_method: Method of ticket delivery
            - email: Email address for receipt and tickets
            - success: Boolean indicating if the purchase was successful
    """
    if not agree_to_terms:
        raise ValueError("You must agree to the terms to complete the purchase.")
    if seat_ids and quantity and len(seat_ids) != quantity:
        raise ValueError("Quantity must match the number of seat IDs provided.")
    if not seat_ids and not quantity:
        raise ValueError("Either seat_ids or quantity must be provided.")

    # Mock purchase ID generation
    purchase_id = f"PUR-{hash((event_id, payment_token)) % 10000:04d}"

    # Mock successful purchase
    return {
        "purchase_id": purchase_id,
        "event_id": event_id,
        "seats": seat_ids if seat_ids else [f"Seat-{i+1}" for i in range(quantity)],
        "quantity": len(seat_ids) if seat_ids else quantity,
        "delivery_method": delivery_method,
        "email": email or "not_provided@example.com",
        "success": True,
    }


from typing import Dict, List, Optional


def recommend_books(genre: str, author: Optional[str] = None) -> Dict[str, List[str]]:
    """Get book recommendations based on a genre or author.

    Args:
        genre: Genre to base recommendations on (e.g. 'Science Fiction', 'Fantasy')
        author: (Optional) Author to base recommendations on (e.g. 'Isaac Asimov')

    Returns:
        Dict containing:
            - recommendations: List of recommended book titles
    """

    # Sample data for book recommendations
    genre_based_recommendations = {
        "Science Fiction": ["Dune", "Neuromancer", "Foundation"],
        "Fantasy": [
            "The Hobbit",
            "Harry Potter and the Sorcerer's Stone",
            "The Name of the Wind",
        ],
        "Mystery": [
            "The Girl with the Dragon Tattoo",
            "Gone Girl",
            "The Da Vinci Code",
        ],
    }

    author_based_recommendations = {
        "Isaac Asimov": ["Foundation", "I, Robot", "The Gods Themselves"],
        "J.K. Rowling": [
            "Harry Potter and the Sorcerer's Stone",
            "Harry Potter and the Chamber of Secrets",
        ],
        "Agatha Christie": ["Murder on the Orient Express", "And Then There Were None"],
    }

    if genre not in genre_based_recommendations:
        raise ValueError(f"Genre not supported: {genre}")


def recommend_movie(
    director: Optional[str] = None,
    actor: Optional[str] = None,
    similar_movies: Optional[List[str]] = None,
    genre: Optional[str] = None,
    length_less_than: Optional[Union[int, str]] = None,
    length_more_than: Optional[Union[int, str]] = None,
) -> Dict[str, Union[str, int]]:
    """Recommend a movie based on various criteria.

    Args:
        director: Recommend a movie by this director.
        actor: Recommend a movie with this actor.
        similar_movies: Recommend a movie similar to these movies.
        genre: Recommend a movie of this genre.
        length_less_than: Recommend a movie not longer than this in minutes.
        length_more_than: Recommend a movie not shorter than this in minutes.

    Returns:
        Dict containing:
            - title: Title of the recommended movie
            - director: Director of the recommended movie
            - actor: Lead actor of the recommended movie
            - genre: Genre of the recommended movie
            - length: Length of the recommended movie in minutes
    """

    def fuzzy_match_genre(search_genre: str, movie_genre: str) -> bool:
        """Fuzzy match genres to handle variations like 'Science Fiction' -> 'Sci-Fi'"""
        if not search_genre or not movie_genre:
            return True

        search_lower = search_genre.lower().strip()
        movie_lower = movie_genre.lower().strip()

        # Exact match
        if search_lower == movie_lower:
            return True

        # Common abbreviations and variations
        sci_fi_variants = [
            "sci-fi",
            "scifi",
            "science fiction",
            "science-fiction",
            "sf",
        ]
        if search_lower in sci_fi_variants and movie_lower in sci_fi_variants:
            return True

        # Check if one contains the other (for partial matches)
        if search_lower in movie_lower or movie_lower in search_lower:
            return True

        # Check word overlap for compound genres
        search_words = set(search_lower.replace("-", " ").split())
        movie_words = set(movie_lower.replace("-", " ").split())

        # If there's significant word overlap
        if search_words and movie_words:
            overlap = search_words.intersection(movie_words)
            if len(overlap) / max(len(search_words), len(movie_words)) > 0.5:
                return True

        return False

    def fuzzy_match_name(search_name: str, movie_name: str) -> bool:
        """Fuzzy match for names (director, actor) to handle minor variations"""
        if not search_name or not movie_name:
            return True

        search_lower = search_name.lower().strip()
        movie_lower = movie_name.lower().strip()

        # Exact match
        if search_lower == movie_lower:
            return True

        # Check if one contains the other
        if search_lower in movie_lower or movie_lower in search_lower:
            return True

        # Check word overlap for names
        search_words = set(search_lower.split())
        movie_words = set(movie_lower.split())

        if search_words and movie_words:
            overlap = search_words.intersection(movie_words)
            # For names, require at least one matching word
            if len(overlap) > 0:
                return True

        return False

    # Convert string inputs to integers for length parameters
    if length_less_than is not None and isinstance(length_less_than, str):
        length_less_than = int(length_less_than)
    if length_more_than is not None and isinstance(length_more_than, str):
        length_more_than = int(length_more_than)

    # Sample data for demonstration
    sample_movies = [
        {
            "title": "Inception",
            "director": "Christopher Nolan",
            "actor": "Leonardo DiCaprio",
            "genre": "Sci-Fi",
            "length": 148,
        },
        {
            "title": "The Dark Knight",
            "director": "Christopher Nolan",
            "actor": "Christian Bale",
            "genre": "Action",
            "length": 152,
        },
        {
            "title": "Pulp Fiction",
            "director": "Quentin Tarantino",
            "actor": "John Travolta",
            "genre": "Crime",
            "length": 154,
        },
        {
            "title": "The Shawshank Redemption",
            "director": "Frank Darabont",
            "actor": "Tim Robbins",
            "genre": "Drama",
            "length": 142,
        },
        {
            "title": "Forrest Gump",
            "director": "Robert Zemeckis",
            "actor": "Tom Hanks",
            "genre": "Drama",
            "length": 142,
        },
        {
            "title": "RoboCop",
            "director": "Paul Verhoeven",
            "actor": "Peter Weller",
            "genre": "Sci-Fi",
            "length": 102,
        },
        {
            "title": "Total Recall",
            "director": "Paul Verhoeven",
            "actor": "Arnold Schwarzenegger",
            "genre": "Sci-Fi",
            "length": 113,
        },
        {
            "title": "American Graffiti",
            "director": "George Lucas",
            "actor": "Richard Dreyfuss",
            "genre": "Drama",
            "length": 110,
        },
        {
            "title": "THX 1138",
            "director": "George Lucas",
            "actor": "Robert Duvall",
            "genre": "Sci-Fi",
            "length": 95,
        },
    ]

    # Filter movies based on criteria using fuzzy matching
    filtered_movies = sample_movies
    if director:
        filtered_movies = [
            movie
            for movie in filtered_movies
            if fuzzy_match_name(director, movie["director"])
        ]
    if actor:
        filtered_movies = [
            movie
            for movie in filtered_movies
            if fuzzy_match_name(actor, movie["actor"])
        ]
    if genre:
        filtered_movies = [
            movie
            for movie in filtered_movies
            if fuzzy_match_genre(genre, movie["genre"])
        ]
    if length_less_than is not None:
        filtered_movies = [
            movie for movie in filtered_movies if movie["length"] < length_less_than
        ]
    if length_more_than is not None:
        filtered_movies = [
            movie for movie in filtered_movies if movie["length"] > length_more_than
        ]

    # If similar_movies is provided, prioritize those
    if similar_movies:
        similar_set = set(similar_movies)
        filtered_movies = [
            movie for movie in filtered_movies if movie["title"] in similar_set
        ] or filtered_movies

    # Return the first match or raise an exception if no match is found
    if not filtered_movies:
        raise ValueError("No movies found matching the given criteria")

    return filtered_movies[0]


from typing import Dict, List, Union


def recommend_movies(
    search_query: str,
    genre: List[str] = None,
    language: str = "en",
    min_rating: float = 0.0,
    subtitles: str = "en",
    max_duration: int = 90,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, int]]]]]:
    """Returns a list of movies based on provided preferences.

    Args:
        search_query: Movie search query
        genre: A list of genres (e.g., 'comedy', 'drama', 'action')
        language: Language of the movie
        min_rating: The minimum rating of the movie
        subtitles: Language of subtitle
        max_duration: The maximum length of the movie in minutes

    Returns:
        Dict containing:
            - search_query: The original search query
            - results: List of movies matching the criteria, each with:
                - title: Title of the movie
                - genre: Genre of the movie
                - language: Language of the movie
                - rating: Rating of the movie
                - duration: Duration of the movie in minutes
    """

    # Sample data based on hash of search_query for consistent results
    sample_movies = [
        {
            "title": "The Great Adventure",
            "genre": "action",
            "language": "en",
            "rating": 8.2,
            "duration": 120,
        },
        {
            "title": "Love in Paris",
            "genre": "romance",
            "language": "fr",
            "rating": 7.5,
            "duration": 95,
        },
        {
            "title": "Horror Night",
            "genre": "horror",
            "language": "en",
            "rating": 6.8,
            "duration": 85,
        },
        {
            "title": "Animated Dreams",
            "genre": "animation",
            "language": "en",
            "rating": 8.0,
            "duration": 80,
        },
        {
            "title": "Documentary on Life",
            "genre": "documentary",
            "language": "en",
            "rating": 9.0,
            "duration": 60,
        },
    ]

    # Filter movies based on provided preferences
    filtered_movies = [
        movie
        for movie in sample_movies
        if (not genre or movie["genre"] in genre)
        and movie["language"] == language
        and movie["rating"] >= min_rating
        and movie["duration"] <= max_duration
    ]

    if not filtered_movies:
        raise ValueError("No movies found matching the criteria")

    return {
        "search_query": search_query,
        "results": filtered_movies,
    }


from typing import Dict, List


def recommend_similar_by_title(title: str) -> Dict[str, List[str]]:
    """Return a list of animes similar to the one specified by title.

    Args:
        title: The exact title of the anime for which recommendations are sought

    Returns:
        Dict containing:
            - title: The original anime title
            - recommendations: List of similar anime titles
    """
    sample_recommendations = {
        "Naruto": ["Bleach", "One Piece", "Dragon Ball Z"],
        "Attack on Titan": ["Tokyo Ghoul", "Death Note", "Fullmetal Alchemist"],
        "My Hero Academia": ["One Punch Man", "Hunter x Hunter", "Mob Psycho 100"],
    }

    if title not in sample_recommendations:
        raise ValueError(f"Anime title not supported: {title}")

    return {
        "title": title,
        "recommendations": sample_recommendations.get(title, []),
    }


from typing import Dict, List, Optional, Union


def recommend_tv_show(
    creator: Optional[str] = None,
    similar_shows: Optional[List[str]] = None,
    genre: Optional[str] = None,
    length_less_than: Optional[int] = None,
    length_more_than: Optional[int] = None,
) -> Dict[str, Union[str, int]]:
    """Recommend a TV show based on various criteria.

    Args:
        creator: Recommend a TV show by this creator.
        similar_shows: Recommend a TV show similar to these TV shows.
        genre: Recommend a TV show of this genre.
        length_less_than: Recommend a TV show not longer than this in episodes.
        length_more_than: Recommend a TV show not shorter than this in episodes.

    Returns:
        Dict containing:
            - title: Title of the recommended TV show
            - creator: Creator of the recommended TV show
            - genre: Genre of the recommended TV show
            - episodes: Number of episodes of the recommended TV show
    """

    # Sample data for demonstration purposes
    sample_shows = [
        {
            "title": "Mystery Manor",
            "creator": "John Doe",
            "genre": "Mystery",
            "episodes": 10,
        },
        {
            "title": "Sci-Fi Saga",
            "creator": "Jane Smith",
            "genre": "Sci-Fi",
            "episodes": 20,
        },
        {
            "title": "Comedy Central",
            "creator": "Alice Johnson",
            "genre": "Comedy",
            "episodes": 15,
        },
        {
            "title": "Drama Dreams",
            "creator": "Bob Brown",
            "genre": "Drama",
            "episodes": 25,
        },
    ]

    # Filter shows based on provided criteria
    filtered_shows = sample_shows
    if creator:
        filtered_shows = [show for show in filtered_shows if show["creator"] == creator]
    if similar_shows:
        filtered_shows = [
            show for show in filtered_shows if show["title"] in similar_shows
        ]
    if genre:
        filtered_shows = [show for show in filtered_shows if show["genre"] == genre]
    if length_less_than is not None:
        filtered_shows = [
            show for show in filtered_shows if show["episodes"] < length_less_than
        ]
    if length_more_than is not None:
        filtered_shows = [
            show for show in filtered_shows if show["episodes"] > length_more_than
        ]

    if not filtered_shows:
        raise ValueError("No TV shows found matching the given criteria.")

    # Return the first matching show as a recommendation
    recommended_show = filtered_shows[0]
    return {
        "title": recommended_show["title"],
        "creator": recommended_show["creator"],
        "genre": recommended_show["genre"],
        "episodes": recommended_show["episodes"],
    }


from typing import Dict, Union


def revenue(title: str, domestic: bool = True) -> Dict[str, Union[str, int]]:
    """Retrieve revenue data for a movie.

    Args:
        title: Title of the movie
        domestic: If true, return only domestic revenue; if false, return only international revenue

    Returns:
        Dict containing:
            - title: Title of the movie
            - revenue: Revenue amount in millions
            - type: 'domestic' or 'international' based on the input parameter
    """

    # Sample revenue data based on movie title
    sample_revenue_data = {
        "Inception": {"domestic": 292, "international": 535},
        "Titanic": {"domestic": 659, "international": 1543},
        "Avatar": {"domestic": 760, "international": 2020},
        "I Know What You Did Last Winter": {"domestic": 250, "international": 522},
        "I Know What You Did Last Winter II": {"domestic": 123, "international": 231},
        "I Know What You Did Last Winter III": {"domestic": 430, "international": 876},
    }

    if title not in sample_revenue_data:
        raise ValueError(f"Movie title not supported: {title}")

    revenue_type = "domestic" if domestic else "international"
    revenue_amount = sample_revenue_data[title][revenue_type]

    return {
        "title": title,
        "revenue": revenue_amount,
        "type": revenue_type,
    }


from typing import Dict, Union


def ride_look_up(
    location: Dict[str, Union[str, Dict[str, Union[str, float]]]] = None,
    ride_name: str = "",
    amusement_park_name: str = "",
) -> Dict[str, Union[str, Dict[str, Union[str, float]]]]:
    """Find an amusement park ride based on parameters.

    Args:
        location: A dictionary containing the location details of the ride, including country, state, city, and coordinates.
        ride_name: The name of the ride.
        amusement_park_name: The name of the amusement park where the ride is located.

    Returns:
        Dict containing:
            - ride_name: Name of the ride
            - amusement_park_name: Name of the amusement park
            - location: A dictionary with location details
    """

    sample_rides = {
        "Roller Coaster": {
            "amusement_park_name": "Thrill Land",
            "location": {
                "country": "USA",
                "state": "California",
                "city": "Los Angeles",
                "coordinates": {"latitude": 34.0522, "longitude": -118.2437},
            },
        },
        "Ferris Wheel": {
            "amusement_park_name": "Fun Park",
            "location": {
                "country": "Japan",
                "state": "Tokyo",
                "city": "Tokyo",
                "coordinates": {"latitude": 35.6895, "longitude": 139.6917},
            },
        },
    }

    if ride_name and ride_name in sample_rides:
        return {
            "ride_name": ride_name,
            "amusement_park_name": sample_rides[ride_name]["amusement_park_name"],
            "location": sample_rides[ride_name]["location"],
        }

    if amusement_park_name:
        for ride, details in sample_rides.items():
            if details["amusement_park_name"] == amusement_park_name:
                return {
                    "ride_name": ride,
                    "amusement_park_name": amusement_park_name,
                    "location": details["location"],
                }

    if location:
        for ride, details in sample_rides.items():
            if details["location"] == location:
                return {
                    "ride_name": ride,
                    "amusement_park_name": details["amusement_park_name"],
                    "location": location,
                }

    raise ValueError("Ride not found with the provided parameters")


from datetime import datetime
from typing import Dict, Optional, Union


def schedule(
    location: Optional[str] = None,
    floor: Optional[str] = None,
    time: Optional[Union[str, datetime]] = None,
    dance: Optional[str] = None,
    dancer: Optional[int] = None,
    lead: Optional[bool] = None,
    follow: Optional[bool] = None,
) -> Dict[str, Union[str, int, bool]]:
    """Get or set a dancer's event schedule.

    Args:
        location: Name of the venue (e.g., 'Grand Hall')
        floor: Specific floor or room (e.g., 'main ballroom')
        time: Scheduled start time of the event
        dance: Type of dance (e.g., 'waltz', 'tango')
        dancer: Dancer number
        lead: Whether the dancer is leading
        follow: Whether the dancer is following

    Returns:
        Dict containing:
            - location: Venue name
            - floor: Floor or room name
            - time: Scheduled start time
            - dance: Type of dance
            - dancer: Dancer number
            - lead: Lead status
            - follow: Follow status
    """
    if dancer is not None and (lead is None and follow is None):
        raise ValueError(
            "Either 'lead' or 'follow' must be specified if 'dancer' is provided."
        )

    # If no specific parameters provided, return a list of schedule entries
    if (
        location is None
        and floor is None
        and time is None
        and dance is None
        and dancer is None
        and lead is None
        and follow is None
    ):
        return {
            "schedules": [
                {
                    "location": "Grand Hall",
                    "floor": "main ballroom",
                    "time": "2023-10-15T18:00:00",
                    "dance": "waltz",
                    "dancer": 101,
                    "lead": True,
                    "follow": False,
                },
                {
                    "location": "Grand Hall",
                    "floor": "practice room",
                    "time": "2023-10-15T19:30:00",
                    "dance": "tango",
                    "dancer": 102,
                    "lead": False,
                    "follow": True,
                },
                {
                    "location": "Community Center",
                    "floor": "main hall",
                    "time": "2023-10-16T17:00:00",
                    "dance": "foxtrot",
                    "dancer": 103,
                    "lead": True,
                    "follow": False,
                },
            ]
        }

    # Process the time parameter to ensure it's serializable
    schedule_time = None
    if time is not None:
        if isinstance(time, datetime):
            schedule_time = time.isoformat()
        else:
            schedule_time = time
    else:
        schedule_time = "2023-10-15T18:00:00"

    # Mock data generation for a single schedule entry
    sample_data = {
        "location": location or "Grand Hall",
        "floor": floor or "main ballroom",
        "time": schedule_time,
        "dance": dance or "waltz",
        "dancer": dancer or 101,
        "lead": lead if lead is not None else True,
        "follow": follow if follow is not None else False,
    }

    return sample_data


from typing import Dict, Literal


def schedule_vr_event(
    event_name: str,
    space_name: str,
    date_time: str,
    event_type: Literal[
        "party",
        "meeting",
        "concert",
        "game_night",
        "art_gallery",
        "meditation",
        "workshop",
    ] = "party",
) -> Dict[str, str]:
    """Create a scheduled event in a virtual space.

    Args:
        event_name: Name of the event
        space_name: Virtual space where event will take place
        date_time: Event date and time (YYYY-MM-DD HH:MM)
        event_type: Type of event being held (default is 'party')

    Returns:
        Dict containing:
            - event_id: Unique identifier for the event
            - confirmation: Confirmation message for the scheduled event
            - details: Summary of the event details
    """
    if not event_name or not space_name or not date_time:
        raise ValueError("Event name, space name, and date time are required.")

    # Simulate event ID generation using a hash
    event_id = hash((event_name, space_name, date_time, event_type)) % 10000

    confirmation = (
        f"Event '{event_name}' scheduled successfully in '{space_name}' on {date_time}."
    )
    details = (
        f"Event Type: {event_type.capitalize()}, "
        f"Location: {space_name}, "
        f"Date & Time: {date_time}"
    )

    return {
        "event_id": f"EVT-{event_id}",
        "confirmation": confirmation,
        "details": details,
    }


from typing import Dict, List


def search_anime(query: str) -> Dict[str, Union[str, List[str]]]:
    """Search for an anime by its title.

    Args:
        query: The title to search for

    Returns:
        Dict containing:
            - title: The title of the anime
            - genres: List of genres the anime belongs to
            - description: A brief description of the anime
    """
    sample_data = {
        "Naruto": {
            "genres": ["Action", "Adventure", "Fantasy"],
            "description": "A young ninja seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village.",
        },
        "Attack on Titan": {
            "genres": ["Action", "Drama", "Fantasy"],
            "description": "Humans are nearly exterminated by giant creatures called Titans. The survivors hide behind enormous walls.",
        },
        "My Hero Academia": {
            "genres": ["Action", "Comedy", "Superhero"],
            "description": "In a world where people with superpowers are the norm, a boy without them dreams of becoming a hero.",
        },
        "Bleach": {
            "genres": ["Action", "Adventure", "Supernatural"],
            "description": "A high school student gains the powers of a Soul Reaper and fights against evil spirits.",
        },
        "One Piece": {
            "genres": ["Action", "Adventure", "Comedy"],
            "description": "A young pirate dreams of becoming the Pirate King by finding the legendary treasure known as 'One Piece'.",
        },
        "Dragon Ball Z": {
            "genres": ["Action", "Adventure", "Martial Arts"],
            "description": "Earth's mightiest warriors defend the planet against powerful foes and otherworldly threats.",
        },
    }

    if query not in sample_data:
        raise ValueError(f"Anime not found: {query}")

    anime_info = sample_data[query]
    return {
        "title": query,
        "genres": anime_info["genres"],
        "description": anime_info["description"],
    }


from datetime import datetime
from typing import Dict, List, Literal, Union


def search_events(
    country: str,
    city: str,
    type: Union[
        List[
            Literal[
                "music", "food", "sports", "arts", "technology", "theatre", "family"
            ]
        ],
        Literal["music", "food", "sports", "arts", "technology", "theatre", "family"],
        str,
    ],
    date_range: Union[Dict[str, str], str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, str]]]]]:
    """Search for events by city.

    Args:
        country: The country where the event is.
        city: The city where the event is.
        type: Event category or list of event categories.
        date_range: Date window for event with 'start_date' and 'end_date'.

    Returns:
        Dict containing:
            - city: City name
            - events: List of events with details such as name, category, and date
    """

    def fuzzy_match_location(
        search_country: str, search_city: str, event_country: str, event_city: str
    ) -> bool:
        """Fuzzy match locations to handle variations and abbreviations"""
        # Normalize inputs
        search_country_lower = search_country.lower().strip()
        search_city_lower = search_city.lower().strip()
        event_country_lower = event_country.lower().strip()
        event_city_lower = event_city.lower().strip()

        # Country mappings
        country_mappings = {
            "usa": "united states",
            "us": "united states",
            "america": "united states",
            "uk": "united kingdom",
            "britain": "united kingdom",
            "australia": "australia",
            "aus": "australia",
            "france": "france",
            "fr": "france",
        }

        # City mappings
        city_mappings = {
            "ny": "new york",
            "nyc": "new york",
            "new york city": "new york",
            "la": "los angeles",
            "sydney": "sydney",
            "melbourne": "melbourne",
            "paris": "paris",
            "london": "london",
        }

        # Normalize using mappings
        normalized_search_country = country_mappings.get(
            search_country_lower, search_country_lower
        )
        normalized_search_city = city_mappings.get(search_city_lower, search_city_lower)
        normalized_event_country = country_mappings.get(
            event_country_lower, event_country_lower
        )
        normalized_event_city = city_mappings.get(event_city_lower, event_city_lower)

        # Check matches
        country_match = (
            normalized_search_country == normalized_event_country
            or normalized_search_country in normalized_event_country
            or normalized_event_country in normalized_search_country
        )

        city_match = (
            normalized_search_city == normalized_event_city
            or normalized_search_city in normalized_event_city
            or normalized_event_city in normalized_search_city
        )

        return country_match and city_match

    def fuzzy_match_event_type(search_types: List[str], event_category: str) -> bool:
        """Fuzzy match event types to handle sports variations and alternatives"""
        event_category_lower = event_category.lower().strip()

        for search_type in search_types:
            search_type_lower = search_type.lower().strip()

            # Direct match
            if search_type_lower == event_category_lower:
                return True

            # Sports-specific matching
            if event_category_lower == "sports":
                sports_variants = [
                    "sport",
                    "sports",
                    "nrl",
                    "afl",
                    "football",
                    "soccer",
                    "basketball",
                    "rugby",
                    "tennis",
                    "cricket",
                    "baseball",
                    "hockey",
                    "athletics",
                    "swimming",
                    "cycling",
                    "golf",
                    "volleyball",
                    "netball",
                ]
                if search_type_lower in sports_variants:
                    return True

            # Music variants
            if event_category_lower == "music":
                music_variants = [
                    "music",
                    "concert",
                    "festival",
                    "gig",
                    "show",
                    "performance",
                ]
                if search_type_lower in music_variants:
                    return True

            # Arts variants
            if event_category_lower == "arts":
                arts_variants = [
                    "art",
                    "arts",
                    "gallery",
                    "exhibition",
                    "theater",
                    "theatre",
                ]
                if search_type_lower in arts_variants:
                    return True

            # Technology variants
            if event_category_lower == "technology":
                tech_variants = ["tech", "technology", "conference", "expo", "summit"]
                if search_type_lower in tech_variants:
                    return True

            # Food variants
            if event_category_lower == "food":
                food_variants = ["food", "culinary", "restaurant", "dining", "cooking"]
                if search_type_lower in food_variants:
                    return True

            # Family variants
            if event_category_lower == "family":
                family_variants = ["family", "kids", "children", "playground"]
                if search_type_lower in family_variants:
                    return True

        return False

    # Convert date_range parameter if provided as string
    if isinstance(date_range, str):
        if " to " in date_range:
            start_date_str, end_date_str = date_range.split(" to ", 1)
            date_range = {
                "start_date": start_date_str.strip(),
                "end_date": end_date_str.strip(),
            }
        else:
            raise ValueError(
                "Invalid date_range format. Expected format: 'YYYY-MM-DD to YYYY-MM-DD'"
            )

    # Expanded sample events with more cities and countries
    sample_events = {
        ("United States", "New York"): [
            {
                "name": "Jazz Festival",
                "category": "music",
                "date": datetime(2023, 11, 5),
            },
            {
                "name": "Tech Expo",
                "category": "technology",
                "date": datetime(2023, 11, 12),
            },
            {
                "name": "NBA Basketball Game",
                "category": "sports",
                "date": datetime(2023, 11, 15),
            },
        ],
        ("United States", "Los Angeles"): [
            {
                "name": "Hollywood Art Exhibition",
                "category": "arts",
                "date": datetime(2023, 11, 8),
            },
            {
                "name": "Lakers vs Warriors",
                "category": "sports",
                "date": datetime(2023, 11, 20),
            },
        ],
        ("Australia", "Sydney"): [
            {
                "name": "Sydney Opera House Concert",
                "category": "music",
                "date": datetime(2023, 11, 10),
            },
            {
                "name": "NRL Grand Final",
                "category": "sports",
                "date": datetime(2023, 10, 1),
            },
            {
                "name": "AFL Sydney Swans vs Brisbane",
                "category": "sports",
                "date": datetime(2023, 11, 18),
            },
            {
                "name": "Harbour Bridge Marathon",
                "category": "sports",
                "date": datetime(2023, 11, 25),
            },
            {
                "name": "Sydney Food & Wine Festival",
                "category": "food",
                "date": datetime(2023, 11, 30),
            },
        ],
        ("Australia", "Melbourne"): [
            {
                "name": "Melbourne Cup Horse Racing",
                "category": "sports",
                "date": datetime(2023, 11, 7),
            },
            {
                "name": "Australian Open Tennis",
                "category": "sports",
                "date": datetime(2024, 1, 15),
            },
            {
                "name": "Melbourne Comedy Festival",
                "category": "arts",
                "date": datetime(2023, 12, 5),
            },
        ],
        ("France", "Paris"): [
            {
                "name": "Art Gallery Opening",
                "category": "arts",
                "date": datetime(2023, 11, 8),
            },
            {
                "name": "Gourmet Food Fair",
                "category": "food",
                "date": datetime(2023, 11, 15),
            },
            {
                "name": "Paris Saint-Germain Football Match",
                "category": "sports",
                "date": datetime(2023, 11, 22),
            },
        ],
        ("United Kingdom", "London"): [
            {
                "name": "West End Theatre Show",
                "category": "theatre",
                "date": datetime(2023, 11, 12),
            },
            {
                "name": "Premier League Football",
                "category": "sports",
                "date": datetime(2023, 11, 19),
            },
            {
                "name": "London Tech Conference",
                "category": "technology",
                "date": datetime(2023, 12, 1),
            },
        ],
    }

    # Find matching events using fuzzy location matching
    matching_events = []
    for (event_country, event_city), events in sample_events.items():
        if fuzzy_match_location(country, city, event_country, event_city):
            matching_events.extend(events)

    if not matching_events:
        raise ValueError(f"No events found for {city}, {country}")

    # Convert type parameter to list if needed
    search_types = [type] if isinstance(type, str) else type

    # Filter events by type using fuzzy matching
    filtered_events = [
        event
        for event in matching_events
        if fuzzy_match_event_type(search_types, event["category"])
    ]

    # Filter by date range if provided
    if date_range:
        start_date = datetime.strptime(date_range["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(date_range["end_date"], "%Y-%m-%d")
        filtered_events = [
            event
            for event in filtered_events
            if start_date <= event["date"] <= end_date
        ]

    # If no filtered events found, return a default event to avoid errors
    if not filtered_events:
        # Generate a default event based on the search parameters
        default_event = {
            "name": f"Local {search_types[0].capitalize()} Event",
            "category": (
                "sports"
                if any(
                    "sport" in t.lower()
                    or t.lower() in ["nrl", "afl", "football", "soccer", "basketball"]
                    for t in search_types
                )
                else search_types[0]
            ),
            "date": datetime(2023, 11, 30),
        }
        filtered_events = [default_event]

    # Convert datetime objects to strings for JSON serialization
    serializable_events = []
    for event in filtered_events:
        serializable_event = event.copy()
        if isinstance(event["date"], datetime):
            serializable_event["date"] = event["date"].strftime("%Y-%m-%d")
        serializable_events.append(serializable_event)

    return {
        "city": city,
        "events": serializable_events,
    }


import hashlib
from typing import Dict, Literal, Union


def search_for_db_id(
    keyword_string: str, keywords_type: Literal["movie", "cast"] = "movie"
) -> Dict[str, Union[str, int]]:
    """Search for database IDs of movies or cast based on a keyword string.

    Args:
        keyword_string: String of keywords to search for movies or cast.
        keywords_type: Enum for searching either cast or movies ('movie' or 'cast').

    Returns:
        Dict containing:
            - keyword: The original keyword string
            - type: The type of search ('movie' or 'cast')
            - db_id: Simulated database ID based on the keyword string
    """
    if not keyword_string.strip():
        raise ValueError("Keyword string cannot be empty")

    # Generate a consistent but varied sample database ID using a hash
    hash_object = hashlib.md5(keyword_string.encode())
    db_id = int(hash_object.hexdigest(), 16) % 1000000  # Simulate a 6-digit ID

    return {
        "keyword": keyword_string,
        "type": keywords_type,
        "db_id": db_id,
    }


import re
from typing import Dict, List, Union


def search_metadata_regex(query_regex: str) -> Dict[str, Union[str, List[str]]]:
    """Search the scene narrations based on a regex query.

    Args:
        query_regex: The regular expression for which to search video narrations

    Returns:
        Dict containing:
            - query: The regex query used for searching
            - matches: List of scene narrations that match the regex
    """
    sample_narrations = [
        "The sun sets over the horizon, painting the sky in hues of orange and pink.",
        "A gentle breeze rustles the leaves of the ancient oak tree.",
        "The bustling city streets are alive with the sounds of honking cars and chattering pedestrians.",
        "A cat lounges lazily on the windowsill, basking in the warm afternoon sun.",
        "Raindrops patter softly against the windowpane, creating a soothing rhythm.",
    ]

    try:
        pattern = re.compile(query_regex)
    except re.error as e:
        raise ValueError(f"Invalid regex pattern: {e}")

    matches = [
        narration for narration in sample_narrations if pattern.search(narration)
    ]

    return {"query": query_regex, "matches": matches}


from typing import Dict, List, Literal, Optional, Union


def search_shows_by_filters(
    country: str,
    cursor: Optional[str] = None,
    year_max: Optional[int] = None,
    year_min: Optional[int] = None,
    series_granularity: Literal["show", "season", "episode"] = "show",
    show_type: Optional[Literal["movie", "series"]] = None,
    genres: Optional[str] = None,
    genres_relation: Optional[Literal["and", "or"]] = None,
    order_by: Optional[
        Literal[
            "original_title",
            "release_date",
            "rating",
            "popularity_alltime",
            "popularity_1year",
            "popularity_1month",
            "popularity_1week",
        ]
    ] = None,
    order_direction: Optional[Literal["asc", "desc"]] = None,
    show_original_language: Optional[str] = None,
    keyword: Optional[str] = None,
    output_language: Literal["en", "es", "tr", "fr"] = "en",
    catalogs: Optional[str] = None,
    rating_max: Optional[int] = None,
    rating_min: Optional[int] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, List[str]]]]]]:
    """Search through the catalog of streaming services in a given country with various filters.

    Args:
        country: ISO 3166-1 alpha-2 code of the target country.
        cursor: Cursor for pagination.
        year_max: Maximum release/air year of the shows.
        year_min: Minimum release/air year of the shows.
        series_granularity: Level of detail for series.
        show_type: Type of shows to search in.
        genres: Comma separated list of genre ids.
        genres_relation: Relation between multiple genres.
        order_by: Ordering of the shows.
        order_direction: Order direction of the results.
        show_original_language: Original language of the shows.
        keyword: Keyword to search within the shows.
        output_language: Language of the output.
        catalogs: Comma separated list of catalogs to search in.
        rating_max: Maximum rating of the shows.
        rating_min: Minimum rating of the shows.

    Returns:
        Dict containing:
            - country: The country code for the search.
            - shows: List of shows with detailed information.
    """
    if not country:
        raise ValueError("Country is required")

    # Mock data generation
    shows_sample = [
        {
            "title": "Sample Show 1",
            "imdb_id": "tt1234567",
            "tmdb_id": 12345,
            "release_year": 2020,
            "deep_links": ["https://example.com/show1"],
            "subtitles": ["en", "es"],
            "audios": ["en"],
            "video_quality": ["HD", "SD"],
        },
        {
            "title": "Sample Show 2",
            "imdb_id": "tt7654321",
            "tmdb_id": 54321,
            "release_year": 2018,
            "deep_links": ["https://example.com/show2"],
            "subtitles": ["en", "fr"],
            "audios": ["fr"],
            "video_quality": ["4K", "HD"],
        },
    ]

    return {
        "country": country,
        "shows": shows_sample,
    }


from typing import Dict, List, Literal, Union


def search_shows_by_title(
    country: str,
    title: str,
    series_granularity: Literal["show", "season", "episode"] = "show",
    show_type: Union[Literal["movie", "series"], None] = None,
    output_language: Literal["en", "es", "tr", "fr"] = "en",
) -> Dict[
    str, Union[str, List[Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]]]
]:
    """Search for movies and series by a title with streaming availability info for the target country.

    Args:
        country: ISO 3166-1 alpha-2 code of the target country
        title: Title phrase to search for
        series_granularity: Level of detail for series ('show', 'season', 'episode')
        show_type: Type of shows to search in ('movie' or 'series')
        output_language: ISO 639-1 code of the output language

    Returns:
        Dict containing:
            - country: Target country code
            - title: Searched title
            - results: List of shows with streaming availability
    """

    def normalize_country_code(country_code: str) -> str:
        """Normalize country codes using fuzzy matching"""
        input_lower = country_code.lower().strip()

        # Standard country data with common variations
        countries = [
            {"code": "US", "names": ["us", "usa", "united states", "america"]},
            {
                "code": "GB",
                "names": ["gb", "uk", "united kingdom", "britain", "england"],
            },
            {"code": "ES", "names": ["es", "spain", "españa"]},
            {"code": "FR", "names": ["fr", "france"]},
            {"code": "DE", "names": ["de", "germany", "deutschland"]},
            {"code": "CA", "names": ["ca", "canada"]},
            {"code": "AU", "names": ["au", "australia"]},
            {"code": "JP", "names": ["jp", "japan"]},
        ]

        # Direct match
        for country in countries:
            if input_lower in country["names"]:
                return country["code"]

        # Fuzzy match - check if input contains any country name
        for country in countries:
            for name in country["names"]:
                if name in input_lower or input_lower in name:
                    return country["code"]

        # If no match, return uppercase of input (fallback)
        return country_code.upper()

    def fuzzy_match_title(search_title: str, show_title: str) -> bool:
        """Fuzzy match titles to handle variations"""
        search_lower = search_title.lower().strip()
        show_lower = show_title.lower().strip()

        # Exact match
        if search_lower == show_lower:
            return True

        # Partial match - search term in show title
        if search_lower in show_lower:
            return True

        # Word-based matching
        search_words = set(search_lower.split())
        show_words = set(show_lower.split())

        # If significant word overlap
        if search_words and show_words:
            overlap = search_words.intersection(show_words)
            if len(overlap) / len(search_words) > 0.5:
                return True

        return False

    # Normalize the country code
    normalized_country = normalize_country_code(country)

    # Extended sample data with more countries and shows
    sample_data = {
        "en": {
            "movie": [
                {"title": "The Great Adventure", "availability": ["Netflix", "Amazon"]},
                {"title": "Mystery of the Lost City", "availability": ["Hulu"]},
                {"title": "Paradise", "availability": ["BBC iPlayer", "Amazon Prime"]},
                {"title": "Paradise Lost", "availability": ["Netflix", "Hulu"]},
            ],
            "series": [
                {"title": "The Detective Chronicles", "availability": ["Netflix"]},
                {"title": "Space Odyssey", "availability": ["Amazon", "Hulu"]},
                {"title": "Paradise", "availability": ["BBC iPlayer", "ITV Hub"]},
                {
                    "title": "Paradise Hotel",
                    "availability": ["Netflix", "Amazon Prime"],
                },
                {"title": "Paradise Falls", "availability": ["Hulu", "Netflix"]},
            ],
        },
        "es": {
            "movie": [
                {"title": "La Gran Aventura", "availability": ["Netflix", "Amazon"]},
                {"title": "Misterio de la Ciudad Perdida", "availability": ["Hulu"]},
                {"title": "Paraíso", "availability": ["Movistar+", "Amazon Prime"]},
            ],
            "series": [
                {"title": "Las Crónicas del Detective", "availability": ["Netflix"]},
                {"title": "Odisea Espacial", "availability": ["Amazon", "Hulu"]},
                {"title": "Paraíso", "availability": ["Movistar+", "Netflix"]},
            ],
        },
        "fr": {
            "movie": [
                {"title": "La Grande Aventure", "availability": ["Canal+", "Amazon"]},
                {"title": "Paradis", "availability": ["France.tv", "Netflix"]},
            ],
            "series": [
                {"title": "Chroniques Détectives", "availability": ["Netflix"]},
                {"title": "Paradis", "availability": ["Canal+", "France.tv"]},
            ],
        },
        "tr": {
            "movie": [
                {"title": "Büyük Macera", "availability": ["Netflix", "Amazon"]},
                {"title": "Cennet", "availability": ["BluTV", "Netflix"]},
            ],
            "series": [
                {"title": "Dedektif Hikayeleri", "availability": ["Netflix"]},
                {"title": "Cennet", "availability": ["BluTV", "Exxen"]},
            ],
        },
    }

    # Support common country codes
    supported_countries = ["US", "GB", "ES", "FR", "DE", "CA", "AU", "JP"]
    if normalized_country not in supported_countries:
        # Default to US if unsupported
        normalized_country = "US"

    if output_language not in sample_data:
        raise ValueError(f"Output language not supported: {output_language}")

    results = []
    for show_category, shows in sample_data[output_language].items():
        if show_type and show_type != show_category:
            continue
        for show in shows:
            if fuzzy_match_title(title, show["title"]):
                if series_granularity == "show":
                    results.append(
                        {"title": show["title"], "availability": show["availability"]}
                    )
                elif series_granularity == "season":
                    results.append(
                        {
                            "title": show["title"],
                            "availability": show["availability"],
                            "seasons": [
                                {"season": 1, "episodes": 10},
                                {"season": 2, "episodes": 8},
                            ],
                        }
                    )
                elif series_granularity == "episode":
                    results.append(
                        {
                            "title": show["title"],
                            "availability": show["availability"],
                            "seasons": [
                                {
                                    "season": 1,
                                    "episodes": [
                                        {"episode": 1, "title": "Pilot"},
                                        {"episode": 2, "title": "The Beginning"},
                                    ],
                                },
                                {
                                    "season": 2,
                                    "episodes": [
                                        {"episode": 1, "title": "Return"},
                                        {"episode": 2, "title": "The Journey"},
                                    ],
                                },
                            ],
                        }
                    )

    return {"country": normalized_country, "title": title, "results": results}


def get_country(
    country_code: str, output_language: Literal["en", "es", "tr", "fr"] = "en"
) -> Dict[str, Union[str, List[str]]]:
    """Get country information based on country code.

    Args:
        country_code: ISO 3166-1 alpha-2 country code or country name
        output_language: ISO 639-1 code of the output language

    Returns:
        Dict containing:
            - country_code: Normalized country code
            - country_name: Country name in the specified language
            - supported_services: List of streaming services available in that country
    """

    def normalize_country_code(country_input: str) -> str:
        """Normalize country codes using fuzzy matching"""
        input_lower = country_input.lower().strip()

        # Country data with multilingual variations
        countries = [
            {
                "code": "US",
                "variants": [
                    "us",
                    "usa",
                    "united states",
                    "america",
                    "estados unidos",
                    "états-unis",
                    "amerika",
                ],
            },
            {
                "code": "GB",
                "variants": [
                    "gb",
                    "uk",
                    "united kingdom",
                    "britain",
                    "england",
                    "scotland",
                    "wales",
                    "reino unido",
                    "royaume-uni",
                    "birleşik krallık",
                ],
            },
            {"code": "ES", "variants": ["es", "spain", "españa", "espagne", "ispanya"]},
            {"code": "FR", "variants": ["fr", "france", "francia", "fransa"]},
            {
                "code": "DE",
                "variants": [
                    "de",
                    "germany",
                    "deutschland",
                    "alemania",
                    "allemagne",
                    "almanya",
                ],
            },
            {"code": "CA", "variants": ["ca", "canada", "canadá"]},
            {"code": "AU", "variants": ["au", "australia", "aus"]},
            {"code": "JP", "variants": ["jp", "japan"]},
            {"code": "IT", "variants": ["it", "italy", "italia", "italie"]},
            {"code": "BR", "variants": ["br", "brazil", "brasil", "brésil"]},
        ]

        # Direct match
        for country in countries:
            if input_lower in country["variants"]:
                return country["code"]

        # Fuzzy match - check partial matches
        for country in countries:
            for variant in country["variants"]:
                if variant in input_lower or input_lower in variant:
                    return country["code"]

        # Fallback
        return country_input.upper()

    # Normalize the input
    normalized_code = normalize_country_code(country_code)

    # Country data in multiple languages
    country_data = {
        "US": {
            "en": {
                "name": "United States",
                "services": ["Netflix", "Hulu", "Amazon Prime", "Disney+", "HBO Max"],
            },
            "es": {
                "name": "Estados Unidos",
                "services": ["Netflix", "Hulu", "Amazon Prime", "Disney+", "HBO Max"],
            },
            "fr": {
                "name": "États-Unis",
                "services": ["Netflix", "Hulu", "Amazon Prime", "Disney+", "HBO Max"],
            },
            "tr": {
                "name": "Amerika Birleşik Devletleri",
                "services": ["Netflix", "Hulu", "Amazon Prime", "Disney+", "HBO Max"],
            },
        },
        "GB": {
            "en": {
                "name": "United Kingdom",
                "services": [
                    "BBC iPlayer",
                    "ITV Hub",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Go",
                ],
            },
            "es": {
                "name": "Reino Unido",
                "services": [
                    "BBC iPlayer",
                    "ITV Hub",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Go",
                ],
            },
            "fr": {
                "name": "Royaume-Uni",
                "services": [
                    "BBC iPlayer",
                    "ITV Hub",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Go",
                ],
            },
            "tr": {
                "name": "Birleşik Krallık",
                "services": [
                    "BBC iPlayer",
                    "ITV Hub",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Go",
                ],
            },
        },
        "ES": {
            "en": {
                "name": "Spain",
                "services": [
                    "Movistar+",
                    "Netflix",
                    "Amazon Prime",
                    "Atresplayer",
                    "RTVE Play",
                ],
            },
            "es": {
                "name": "España",
                "services": [
                    "Movistar+",
                    "Netflix",
                    "Amazon Prime",
                    "Atresplayer",
                    "RTVE Play",
                ],
            },
            "fr": {
                "name": "Espagne",
                "services": [
                    "Movistar+",
                    "Netflix",
                    "Amazon Prime",
                    "Atresplayer",
                    "RTVE Play",
                ],
            },
            "tr": {
                "name": "İspanya",
                "services": [
                    "Movistar+",
                    "Netflix",
                    "Amazon Prime",
                    "Atresplayer",
                    "RTVE Play",
                ],
            },
        },
        "FR": {
            "en": {
                "name": "France",
                "services": ["Canal+", "France.tv", "Netflix", "Amazon Prime", "Salto"],
            },
            "es": {
                "name": "Francia",
                "services": ["Canal+", "France.tv", "Netflix", "Amazon Prime", "Salto"],
            },
            "fr": {
                "name": "France",
                "services": ["Canal+", "France.tv", "Netflix", "Amazon Prime", "Salto"],
            },
            "tr": {
                "name": "Fransa",
                "services": ["Canal+", "France.tv", "Netflix", "Amazon Prime", "Salto"],
            },
        },
        "DE": {
            "en": {
                "name": "Germany",
                "services": [
                    "ARD Mediathek",
                    "ZDF Mediathek",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Deutschland",
                ],
            },
            "es": {
                "name": "Alemania",
                "services": [
                    "ARD Mediathek",
                    "ZDF Mediathek",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Deutschland",
                ],
            },
            "fr": {
                "name": "Allemagne",
                "services": [
                    "ARD Mediathek",
                    "ZDF Mediathek",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Deutschland",
                ],
            },
            "tr": {
                "name": "Almanya",
                "services": [
                    "ARD Mediathek",
                    "ZDF Mediathek",
                    "Netflix",
                    "Amazon Prime",
                    "Sky Deutschland",
                ],
            },
        },
        "CA": {
            "en": {
                "name": "Canada",
                "services": ["CBC Gem", "Crave", "Netflix", "Amazon Prime", "Disney+"],
            },
            "es": {
                "name": "Canadá",
                "services": ["CBC Gem", "Crave", "Netflix", "Amazon Prime", "Disney+"],
            },
            "fr": {
                "name": "Canada",
                "services": ["CBC Gem", "Crave", "Netflix", "Amazon Prime", "Disney+"],
            },
            "tr": {
                "name": "Kanada",
                "services": ["CBC Gem", "Crave", "Netflix", "Amazon Prime", "Disney+"],
            },
        },
        "AU": {
            "en": {
                "name": "Australia",
                "services": [
                    "ABC iview",
                    "SBS On Demand",
                    "Netflix",
                    "Amazon Prime",
                    "Stan",
                ],
            },
            "es": {
                "name": "Australia",
                "services": [
                    "ABC iview",
                    "SBS On Demand",
                    "Netflix",
                    "Amazon Prime",
                    "Stan",
                ],
            },
            "fr": {
                "name": "Australie",
                "services": [
                    "ABC iview",
                    "SBS On Demand",
                    "Netflix",
                    "Amazon Prime",
                    "Stan",
                ],
            },
            "tr": {
                "name": "Avustralya",
                "services": [
                    "ABC iview",
                    "SBS On Demand",
                    "Netflix",
                    "Amazon Prime",
                    "Stan",
                ],
            },
        },
    }

    if normalized_code not in country_data:
        raise ValueError(f"Country code not supported: {country_code}")

    if output_language not in country_data[normalized_code]:
        raise ValueError(f"Output language not supported: {output_language}")

    country_info = country_data[normalized_code][output_language]

    return {
        "country_code": normalized_code,
        "country_name": country_info["name"],
        "supported_services": country_info["services"],
    }


from typing import Dict, Literal


def soldier_poet_king_description(
    spk_archetype: Literal["Soldier", "Poet", "King"]
) -> Dict[str, str]:
    """Return a description of the specified archetype: Soldier, Poet, or King.

    Args:
        spk_archetype: The archetype to describe ('Soldier', 'Poet', or 'King')

    Returns:
        Dict containing:
            - archetype: The name of the archetype
            - description: A brief description of the archetype
    """

    descriptions = {
        "Soldier": "The Soldier is brave and disciplined, always ready to defend and protect.",
        "Poet": "The Poet is creative and introspective, finding beauty and meaning in the world.",
        "King": "The King is wise and authoritative, leading with vision and fairness.",
    }

    if spk_archetype not in descriptions:
        raise ValueError(f"Archetype not supported: {spk_archetype}")

    return {"archetype": spk_archetype, "description": descriptions[spk_archetype]}


from typing import Dict, Literal, Optional, Union


def talents(
    dancer: Optional[int] = None,
    dance: Optional[str] = None,
    talent: Optional[Literal[0, 1, 2]] = None,
) -> Dict[str, Union[int, str, None]]:
    """Set or get dancer talents based on provided parameters.

    Args:
        dancer: The dancer number (e.g. 1, 2, 3)
        dance: The name of the dance (e.g. 'Salsa', 'Tango')
        talent: The talent type (0=lead, 1=follow, 2=both)

    Returns:
        Dict containing:
            - dancer: Dancer number
            - dance: Name of the dance
            - talent: Talent type (0=lead, 1=follow, 2=both)
    """

    # Sample data for demonstration purposes
    sample_data = {
        1: {"dance": "Salsa", "talent": 0},
        2: {"dance": "Tango", "talent": 1},
        3: {"dance": "Waltz", "talent": 2},
    }

    if dancer is not None:
        if dancer not in sample_data:
            raise ValueError(f"Dancer not found: {dancer}")
        if dance is not None:
            sample_data[dancer]["dance"] = dance
        if talent is not None:
            sample_data[dancer]["talent"] = talent
        return {
            "dancer": dancer,
            "dance": sample_data[dancer]["dance"],
            "talent": sample_data[dancer]["talent"],
        }

    return {
        "dancer": None,
        "dance": dance,
        "talent": talent,
    }


from typing import Dict, Union


def team_record(
    name: str, year: int, incl_playoffs: bool = True
) -> Dict[str, Union[str, int, bool]]:
    """Get the win/loss record of a team for a given season.

    Args:
        name: Team name (e.g. 'Lakers', 'Warriors')
        year: Season year (e.g. 2022)
        incl_playoffs: Include playoff stats in the record

    Returns:
        Dict containing:
            - team: Team name
            - year: Season year
            - wins: Number of wins
            - losses: Number of losses
            - incl_playoffs: Whether playoff stats are included
    """

    # Simulated data based on team name and year
    base_wins = hash(name + str(year)) % 50 + 20
    base_losses = 82 - base_wins

    if incl_playoffs:
        playoff_wins = hash(name + str(year) + "playoffs") % 16
        playoff_losses = hash(name + str(year) + "playoffs") % (16 - playoff_wins)
        total_wins = base_wins + playoff_wins
        total_losses = base_losses + playoff_losses
    else:
        total_wins = base_wins
        total_losses = base_losses

    return {
        "team": name,
        "year": year,
        "wins": total_wins,
        "losses": total_losses,
        "incl_playoffs": incl_playoffs,
    }


from typing import Dict, List, Union


def where_can_i_watch(
    title: str, country: str, free: bool = True
) -> Dict[str, Union[str, List[str]]]:
    """Returns a list of streaming services where a movie is available.

    Args:
        title: Name of the searched movie
        country: Country code to search in (e.g., 'us', 'uk', 'in', 'fr')
        free: True if the streaming service should be free, false otherwise

    Returns:
        Dict containing:
            - title: Name of the movie
            - available_on: List of streaming services where the movie is available
    """

    # Sample data based on hash of the title for consistent but varied results
    sample_services = {
        "us": {True: ["Tubi", "Crackle"], False: ["Netflix", "Hulu", "Amazon Prime"]},
        "uk": {
            True: ["BBC iPlayer", "All 4"],
            False: ["Netflix", "Sky Go", "Amazon Prime"],
        },
        "in": {True: ["Hotstar", "Voot"], False: ["Netflix", "Amazon Prime", "Zee5"]},
        "fr": {
            True: ["Arte", "France.tv"],
            False: ["Netflix", "Canal+", "Amazon Prime"],
        },
    }

    if country not in sample_services:
        raise ValueError(f"Country not supported: {country}")

    available_services = sample_services[country][free]

    # Simulate a hash-based selection for demonstration purposes
    hash_value = hash(title) % len(available_services)
    selected_services = available_services[: hash_value + 1]

    return {"title": title, "available_on": selected_services}


from typing import Dict, List


def where_to_watch(show_title: str) -> Dict[str, Union[str, List[str]]]:
    """List platforms where a certain show can be watched.

    Args:
        show_title: The title of the show that the user wants to find platforms to watch.

    Returns:
        Dict containing:
            - show_title: Title of the show
            - platforms: List of platforms where the show is available
    """

    sample_data = {
        "Breaking Bad": ["Netflix", "Amazon Prime", "Hulu"],
        "Game of Thrones": ["HBO Max", "Amazon Prime"],
        "Stranger Things": ["Netflix"],
        "The Office": ["Peacock", "Amazon Prime"],
        "Friends": ["HBO Max", "Netflix"],
    }

    if show_title not in sample_data:
        raise ValueError(f"Show not supported: {show_title}")

    return {
        "show_title": show_title,
        "platforms": sample_data[show_title],
    }


from typing import Dict, List, Optional, Union

# Movie Information Tools
# Auto-generated implementations for movie-related operations


def find_movie_showing(
    city: str,
    movie_name: Optional[str] = None,
    day: Optional[str] = None,
    starting_from: Optional[str] = None,
    ending_until: Optional[str] = None,
    seat_type: Optional[List[str]] = None,
    screen_type: Optional[List[str]] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Find movie showing times.

    Args:
        city: The name of the city to search for movie showtimes in
        movie_name: The name of the movie
        day: The day to search (YYYY-MM-DD)
        starting_from: Return movies starting after this time (24h time format, HH:mm)
        ending_until: Return movies ending before this time (24h time format, HH:mm)
        seat_type: The type of seat available for the movie showing
        screen_type: The screen type of the movie screening

    Returns:
        Dict containing:
            - city: The city searched
            - movie_name: The movie searched for (if specified)
            - search_date: The date searched for
            - showtimes: List of available showtimes with details
    """

    # Sample movie showtimes data
    sample_movies = {
        "Man of Steel": [
            {
                "time": "14:30",
                "theater": "AMC Downtown",
                "screen_type": "imax",
                "seat_type": "recliner",
            },
            {
                "time": "18:45",
                "theater": "Cineplex Central",
                "screen_type": "standard",
                "seat_type": "standard",
            },
            {
                "time": "21:15",
                "theater": "IMAX Theater",
                "screen_type": "imax",
                "seat_type": "recliner",
            },
        ],
        "Avengers": [
            {
                "time": "15:00",
                "theater": "AMC Downtown",
                "screen_type": "4dx",
                "seat_type": "recliner",
            },
            {
                "time": "19:30",
                "theater": "Cineplex Central",
                "screen_type": "standard",
                "seat_type": "standard",
            },
        ],
        "Top Gun": [
            {
                "time": "16:00",
                "theater": "IMAX Theater",
                "screen_type": "imax",
                "seat_type": "love_bed",
            },
            {
                "time": "20:00",
                "theater": "AMC Downtown",
                "screen_type": "jumbotron",
                "seat_type": "recliner",
            },
        ],
    }

    # Default search date
    search_date = day if day else "2024-01-15"

    # Get showtimes for the specific movie or all movies
    if movie_name and movie_name in sample_movies:
        available_showtimes = sample_movies[movie_name]
        actual_movie_name = movie_name
    else:
        # If no specific movie or movie not found, return all showtimes
        available_showtimes = []
        for movie, times in sample_movies.items():
            for showtime in times:
                showtime_copy = showtime.copy()
                showtime_copy["movie"] = movie
                available_showtimes.append(showtime_copy)
        actual_movie_name = "All Movies"

    # Filter by time constraints
    filtered_showtimes = available_showtimes.copy()
    if starting_from:
        filtered_showtimes = [
            s for s in filtered_showtimes if s["time"] >= starting_from
        ]
    if ending_until:
        # Estimate end time (assume 2.5 hour movies)
        filtered_showtimes = [
            s for s in filtered_showtimes if s["time"] <= ending_until
        ]

    # Filter by seat type
    if seat_type:
        filtered_showtimes = [
            s for s in filtered_showtimes if s["seat_type"] in seat_type
        ]

    # Filter by screen type
    if screen_type:
        filtered_showtimes = [
            s for s in filtered_showtimes if s["screen_type"] in screen_type
        ]

    return {
        "city": city,
        "movie_name": actual_movie_name,
        "search_date": search_date,
        "showtimes": filtered_showtimes,
    }


def get_movie_certification(movie_name: str) -> Dict[str, Union[str, int]]:
    """Get the certification for the movie specified.

    Args:
        movie_name: The name of the movie

    Returns:
        Dict containing:
            - movie_name: The movie title
            - certification: Movie rating/certification
            - reason: Reason for the certification
            - runtime_minutes: Runtime in minutes
    """

    # Sample movie certification data
    certification_data = {
        "Man of Steel": {
            "certification": "PG-13",
            "reason": "Intense sequences of sci-fi violence, action and destruction, and for some language",
            "runtime_minutes": 143,
        },
        "Avengers": {
            "certification": "PG-13",
            "reason": "Intense sequences of sci-fi action violence and destruction throughout",
            "runtime_minutes": 143,
        },
        "Top Gun": {
            "certification": "PG",
            "reason": "Action violence, some mild language and brief sensuality",
            "runtime_minutes": 110,
        },
        "The Dark Knight": {
            "certification": "PG-13",
            "reason": "Intense sequences of violence and some menace",
            "runtime_minutes": 152,
        },
    }

    if movie_name in certification_data:
        movie_info = certification_data[movie_name]
        return {
            "movie_name": movie_name,
            "certification": movie_info["certification"],
            "reason": movie_info["reason"],
            "runtime_minutes": movie_info["runtime_minutes"],
        }
    else:
        return {
            "movie_name": movie_name,
            "certification": "Not Found",
            "reason": "Movie not found in certification database",
            "runtime_minutes": 0,
        }


def get_movie_cinematographer(movie_name: str) -> Dict[str, Union[str, List[str]]]:
    """Get the cinematographer for movie specified.

    Args:
        movie_name: The name of the movie

    Returns:
        Dict containing:
            - movie_name: The movie title
            - cinematographer: Name of the cinematographer
            - nationality: Cinematographer's nationality
            - filming_techniques: List of notable filming techniques used
            - camera_equipment: Information about cameras used
            - imax_shot: Whether the movie was shot with IMAX cameras
    """

    # Sample cinematographer data
    cinematographer_data = {
        "Man of Steel": {
            "cinematographer": "Amir Mokri",
            "nationality": "Iranian-American",
            "filming_techniques": [
                "Handheld camera work",
                "Aerial cinematography",
                "Digital intermediate",
            ],
            "camera_equipment": "Panavision cameras, Arri Alexa cameras",
            "imax_shot": True,
        },
        "The Dark Knight": {
            "cinematographer": "Wally Pfister",
            "nationality": "American",
            "filming_techniques": [
                "IMAX photography",
                "Practical effects",
                "Minimal CGI",
            ],
            "camera_equipment": "65mm IMAX cameras, 35mm film cameras",
            "imax_shot": True,
        },
        "Avengers": {
            "cinematographer": "Seamus McGarvey",
            "nationality": "Northern Irish",
            "filming_techniques": [
                "Digital cinematography",
                "Motion capture",
                "Virtual sets",
            ],
            "camera_equipment": "Arri Alexa cameras, Red Epic cameras",
            "imax_shot": False,
        },
        "Top Gun": {
            "cinematographer": "Jeffrey Kimball",
            "nationality": "American",
            "filming_techniques": [
                "Aerial photography",
                "High-speed cameras",
                "Practical stunts",
            ],
            "camera_equipment": "Panavision cameras, 35mm film",
            "imax_shot": False,
        },
    }

    if movie_name in cinematographer_data:
        movie_info = cinematographer_data[movie_name]
        return {
            "movie_name": movie_name,
            "cinematographer": movie_info["cinematographer"],
            "nationality": movie_info["nationality"],
            "filming_techniques": movie_info["filming_techniques"],
            "camera_equipment": movie_info["camera_equipment"],
            "imax_shot": movie_info["imax_shot"],
        }
    else:
        return {
            "movie_name": movie_name,
            "cinematographer": "Unknown",
            "nationality": "Unknown",
            "filming_techniques": [],
            "camera_equipment": "Information not available",
            "imax_shot": False,
        }
