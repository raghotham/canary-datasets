from typing import Dict, List, Union, Any
# Music Tools
# Auto-generated implementations from cached categorization

from typing import Dict, Optional


def play_song(
    song_title: str, 
    artist_name: Optional[str] = None, 
    volume_level: Optional[int] = 50
) -> Dict[str, Union[str, int]]:
    """Play a specific song from the user's library or a streaming service.

    Args:
        song_title: The title of the song to be played.
        artist_name: The name of the artist who performs the song.
        volume_level: The playback volume level from 0 (muted) to 100 (maximum).

    Returns:
        Dict containing:
            - song_title: Title of the song being played
            - artist_name: Name of the artist
            - volume_level: Volume level at which the song is played
            - status: Playback status message
    """
    
    if not (0 <= volume_level <= 100):
        raise ValueError("Volume level must be between 0 and 100")

    # Sample data simulating a music library
    library = {
        ("Shape of You", "Ed Sheeran"): "Playing 'Shape of You' by Ed Sheeran",
        ("Blinding Lights", "The Weeknd"): "Playing 'Blinding Lights' by The Weeknd",
        ("Rolling in the Deep", "Adele"): "Playing 'Rolling in the Deep' by Adele",
    }

    # Determine the playback status
    key = (song_title, artist_name) if artist_name else (song_title, None)
    status = library.get(key, f"Playing '{song_title}'")

    return {
        "song_title": song_title,
        "artist_name": artist_name or "Unknown Artist",
        "volume_level": volume_level,
        "status": status,
    }

from typing import Dict, List, Union


def create_playlist(
    playlist_name: str,
    songs: List[Dict[str, str]] = [],
    is_public: bool = False
) -> Dict[str, Union[str, bool, List[Dict[str, str]]]]:
    """Creates a new music playlist with optional initial songs.

    Args:
        playlist_name: The name of the playlist to be created.
        songs: A list of songs to add to the playlist. Each song is an object containing a title and artist.
        is_public: Whether the playlist should be visible to others.

    Returns:
        Dict containing:
            - playlist_name: The name of the created playlist
            - is_public: Visibility status of the playlist
            - songs: List of songs in the playlist
    """
    if not playlist_name:
        raise ValueError("Playlist name is required.")

    # Simulate a hash-based unique identifier for the playlist
    playlist_id = hash(playlist_name) % 10000

    # Mock data for demonstration purposes
    sample_songs = [
        {"title": "Song A", "artist": "Artist 1"},
        {"title": "Song B", "artist": "Artist 2"},
        {"title": "Song C", "artist": "Artist 3"},
    ]

    # If no songs are provided, use a sample list
    if not songs:
        songs = sample_songs[:2]  # Add the first two sample songs

    return {
        "playlist_name": f"{playlist_name} (ID: {playlist_id})",
        "is_public": is_public,
        "songs": songs,
    }

from typing import Dict, List, Optional


def add_song_to_playlist(
    playlist_name: str, song_title: str, artist_name: Optional[str] = None
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Add a song to an existing playlist.

    Args:
        playlist_name: The name of the playlist to update.
        song_title: The title of the song to add.
        artist_name: The name of the artist performing the song (optional).

    Returns:
        Dict containing:
            - playlist_name: The name of the updated playlist.
            - songs: List of songs in the playlist, each with title and artist.
    """
    
    # Mock existing playlists with songs
    playlists = {
        "Chill Vibes": [
            {"title": "Sunset Lover", "artist": "Petit Biscuit"},
            {"title": "Weightless", "artist": "Marconi Union"},
        ],
        "Workout Hits": [
            {"title": "Eye of the Tiger", "artist": "Survivor"},
            {"title": "Stronger", "artist": "Kanye West"},
        ],
    }
    
    if playlist_name not in playlists:
        raise ValueError(f"Playlist not found: {playlist_name}")

    # Add the new song to the playlist
    new_song = {"title": song_title, "artist": artist_name or "Unknown Artist"}
    playlists[playlist_name].append(new_song)

    return {
        "playlist_name": playlist_name,
        "songs": playlists[playlist_name],
    }

from typing import Dict, List, Literal


def search_music(
    query: str, filter_type: Literal["song", "album", "artist"] = "song"
) -> Dict[str, List[Dict[str, str]]]:
    """Search for songs, albums, or artists matching the given query.

    Args:
        query: The search term for the music content.
        filter_type: Type of content to search for ('song', 'album', 'artist').

    Returns:
        Dict containing:
            - results: List of dictionaries with matching music content
                - name: Name of the song, album, or artist
                - type: Type of the content ('song', 'album', 'artist')
    """
    sample_data = {
        "song": [
            {"name": "Shape of You", "type": "song"},
            {"name": "Blinding Lights", "type": "song"},
            {"name": "Rolling in the Deep", "type": "song"},
        ],
        "album": [
            {"name": "Divide", "type": "album"},
            {"name": "After Hours", "type": "album"},
            {"name": "21", "type": "album"},
        ],
        "artist": [
            {"name": "Ed Sheeran", "type": "artist"},
            {"name": "The Weeknd", "type": "artist"},
            {"name": "Adele", "type": "artist"},
        ],
    }

    if filter_type not in sample_data:
        raise ValueError(f"Unsupported filter type: {filter_type}")

    results = [
        item for item in sample_data[filter_type] if query.lower() in item["name"].lower()
    ]

    return {"results": results}

from typing import Dict, List, Union


def get_recommendations(
    genre: Union[str, None] = None, limit: int = 10
) -> Dict[str, Union[str, List[str]]]:
    """Generates music recommendations based on listening history or selected genres.

    Args:
        genre: A music genre to base recommendations on (e.g. 'rock', 'jazz').
        limit: The number of recommendations to return.

    Returns:
        Dict containing:
            - genre: The genre used for recommendations
            - recommendations: List of recommended music tracks
    """
    
    sample_data = {
        "rock": [
            "Bohemian Rhapsody - Queen",
            "Stairway to Heaven - Led Zeppelin",
            "Hotel California - Eagles",
            "Sweet Child o' Mine - Guns N' Roses",
            "Back in Black - AC/DC",
        ],
        "jazz": [
            "So What - Miles Davis",
            "Take Five - Dave Brubeck",
            "Feeling Good - Nina Simone",
            "My Favorite Things - John Coltrane",
            "What a Wonderful World - Louis Armstrong",
        ],
        "pop": [
            "Thriller - Michael Jackson",
            "Like a Prayer - Madonna",
            "Rolling in the Deep - Adele",
            "Uptown Funk - Mark Ronson ft. Bruno Mars",
            "Shake It Off - Taylor Swift",
        ],
    }

    if genre and genre not in sample_data:
        raise ValueError(f"Genre not supported: {genre}")

    selected_genre = genre if genre else "rock"
    recommendations = sample_data[selected_genre][:limit]

    return {
        "genre": selected_genre,
        "recommendations": recommendations,
    }

from typing import Dict, Optional


def like_song(song_title: str, artist_name: Optional[str] = None) -> Dict[str, str]:
    """Marks a song as liked or adds it to the user's favorites.

    Args:
        song_title: The title of the song to like.
        artist_name: The name of the artist performing the song (optional).

    Returns:
        Dict containing:
            - song_title: The title of the liked song
            - artist_name: The name of the artist (if provided)
            - status: Confirmation message of the action
    """
    
    if not song_title:
        raise ValueError("Song title is required to like a song.")
    
    # Simulate a hash-based generation for consistent but varied sample data
    liked_songs = {
        "Bohemian Rhapsody": "Queen",
        "Imagine": "John Lennon",
        "Billie Jean": "Michael Jackson",
    }
    
    if artist_name and liked_songs.get(song_title) != artist_name:
        raise ValueError(f"Artist name does not match the known artist for '{song_title}'.")
    
    return {
        "song_title": song_title,
        "artist_name": artist_name or liked_songs.get(song_title, "Unknown Artist"),
        "status": f"'{song_title}' has been added to your favorites."
    }

from typing import Dict, List


def remove_song_from_playlist(playlist_name: str, song_title: str) -> Dict[str, Union[str, List[str]]]:
    """Remove a specific song from a playlist.

    Args:
        playlist_name: The name of the playlist to update.
        song_title: The title of the song to remove.

    Returns:
        Dict containing:
            - playlist_name: The name of the updated playlist
            - songs: List of songs remaining in the playlist
    """
    
    # Sample playlists with songs
    playlists = {
        "Chill Vibes": ["Sunset Lover", "Weightless", "Night Owl"],
        "Workout Hits": ["Eye of the Tiger", "Stronger", "Can't Hold Us"],
        "Classic Rock": ["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"],
    }
    
    if playlist_name not in playlists:
        raise ValueError(f"Playlist not found: {playlist_name}")
    
    if song_title not in playlists[playlist_name]:
        raise ValueError(f"Song not found in playlist: {song_title}")
    
    # Remove the song from the playlist
    playlists[playlist_name].remove(song_title)
    
    return {
        "playlist_name": playlist_name,
        "songs": playlists[playlist_name],
    }

from typing import Dict, List, Union


def search_publisher(
    name: Union[str, None] = None,
    genre: Union[str, None] = None,
    song_titles: Union[List[str], None] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, List[str]]]]]]:
    """Search for a publisher by name, genre, or song titles.

    Args:
        name: Name of the publisher to search for.
        genre: Genre to filter publishers by.
        song_titles: List of song titles to search publishers by.

    Returns:
        Dict containing:
            - name: Publisher's name
            - founding_date: Date when the publisher was founded
            - published_songs: List of published songs with details
            - published_albums: List of published albums with details
    """
    
    sample_publishers = {
        "Universal Music": {
            "founding_date": "1934-09-01",
            "published_songs": [
                {"title": "Song A", "genre": "Pop"},
                {"title": "Song B", "genre": "Rock"},
            ],
            "published_albums": [
                {"title": "Album 1", "release_year": 2001},
                {"title": "Album 2", "release_year": 2005},
            ],
        },
        "Sony Music": {
            "founding_date": "1929-03-15",
            "published_songs": [
                {"title": "Song C", "genre": "Jazz"},
                {"title": "Song D", "genre": "Classical"},
            ],
            "published_albums": [
                {"title": "Album 3", "release_year": 1999},
                {"title": "Album 4", "release_year": 2010},
            ],
        },
    }

    def matches_criteria(publisher_data):
        if name and name != publisher:
            return False
        if genre and not any(song["genre"] == genre for song in publisher_data["published_songs"]):
            return False
        if song_titles and not any(song["title"] in song_titles for song in publisher_data["published_songs"]):
            return False
        return True

    for publisher, data in sample_publishers.items():
        if matches_criteria(data):
            return {
                "name": publisher,
                "founding_date": data["founding_date"],
                "published_songs": data["published_songs"],
                "published_albums": data["published_albums"],
            }

    raise ValueError("No publisher found matching the given criteria")

from typing import Dict, List
import random


def shuffle_play_playlist(playlist_name: str) -> Dict[str, Union[str, List[str]]]:
    """Plays a playlist in random order.

    Args:
        playlist_name: The name of the playlist to shuffle play.

    Returns:
        Dict containing:
            - playlist_name: The name of the playlist
            - shuffled_tracks: List of tracks in shuffled order
    """
    sample_playlists = {
        "Chill Vibes": ["Track A", "Track B", "Track C", "Track D"],
        "Workout Mix": ["Track E", "Track F", "Track G", "Track H"],
        "Party Hits": ["Track I", "Track J", "Track K", "Track L"],
    }

    if playlist_name not in sample_playlists:
        raise ValueError(f"Playlist not found: {playlist_name}")

    tracks = sample_playlists[playlist_name]
    random.seed(hash(playlist_name))  # Ensure consistent shuffling for the same playlist
    shuffled_tracks = tracks[:]
    random.shuffle(shuffled_tracks)

    return {
        "playlist_name": playlist_name,
        "shuffled_tracks": shuffled_tracks,
    }

from typing import Dict, Union


def play_music(song_name: str, volume: Union[int, None] = None) -> Dict[str, Union[str, int]]:
    """Play music on a connected smart speaker.

    Args:
        song_name: Name of the song or playlist to play.
        volume: Playback volume level (0-100). Defaults to a standard level if not provided.

    Returns:
        Dict containing:
            - song_name: The name of the song being played
            - volume: The volume level at which the song is played
            - status: The status of the playback
    """
    if not song_name:
        raise ValueError("Song name must be provided")

    if volume is not None and (volume < 0 or volume > 100):
        raise ValueError("Volume must be between 0 and 100")

    # Simulate playing music with a default volume if not specified
    default_volume = 50
    actual_volume = volume if volume is not None else default_volume

    return {
        "song_name": song_name,
        "volume": actual_volume,
        "status": "playing"
    }

from typing import Dict, Union
from datetime import datetime

def check_instrument_availability(instrument_name: str, date: str) -> Dict[str, Union[str, bool]]:
    """Check the availability of an instrument on a given date.

    Args:
        instrument_name: Instrument name (must match list_instruments).
        date: Date in the format YYYY-MM-DD.

    Returns:
        Dict containing:
            - instrument_name: Name of the instrument
            - date: Date checked
            - available: Boolean indicating if the instrument is available
    """
    # Sample data for available instruments and their booked dates
    sample_instruments = {
        "Guitar": ["2023-10-01", "2023-10-05"],
        "Piano": ["2023-10-03"],
        "Violin": ["2023-10-02", "2023-10-04"],
    }

    # Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

    # Check if the instrument is in the sample list
    if instrument_name not in sample_instruments:
        raise ValueError(f"Instrument not supported: {instrument_name}")

    # Determine availability
    booked_dates = sample_instruments[instrument_name]
    available = date not in booked_dates

    return {
        "instrument_name": instrument_name,
        "date": date,
        "available": available,
    }

from typing import Dict


def get_artist_name(song_name: str) -> Dict[str, str]:
    """Find the name of an artist by song.

    Args:
        song_name: Name of the song to search for

    Returns:
        Dict containing:
            - song_name: The name of the song
            - artist_name: The name of the artist who performed the song
    """
    
    # Simulated song-to-artist mapping
    song_artist_map = {
        "Shape of You": "Ed Sheeran",
        "Blinding Lights": "The Weeknd",
        "Rolling in the Deep": "Adele",
        "Bohemian Rhapsody": "Queen",
        "Billie Jean": "Michael Jackson",
    }
    
    if song_name not in song_artist_map:
        raise ValueError(f"Song not found: {song_name}")

    return {
        "song_name": song_name,
        "artist_name": song_artist_map[song_name],
    }

from typing import Dict


def play_album(album_id: str, randomise: bool = False) -> Dict[str, Union[str, List[str]]]:
    """Start playing an album.

    Args:
        album_id: ID of album to play
        randomise: Play the songs in a random order

    Returns:
        Dict containing:
            - album_id: ID of the album being played
            - order: 'random' if randomise is True, otherwise 'sequential'
            - tracks: List of track names in the order they will be played
    """
    sample_albums = {
        "album_001": ["Track A", "Track B", "Track C"],
        "album_002": ["Track D", "Track E", "Track F"],
        "album_003": ["Track G", "Track H", "Track I"],
    }

    if album_id not in sample_albums:
        raise ValueError(f"Album ID not found: {album_id}")

    tracks = sample_albums[album_id]
    if randomise:
        import random
        random.seed(hash(album_id))
        random.shuffle(tracks)

    return {
        "album_id": album_id,
        "order": "random" if randomise else "sequential",
        "tracks": tracks,
    }

from typing import Dict, Literal


def reserve_instrument(
    instrument_name: str, date: str, time_slot: Literal["morning", "afternoon", "evening"]
) -> Dict[str, str]:
    """Books an instrument for a specific date and time slot.

    Args:
        instrument_name: Instrument name (must match list_instruments).
        date: Date in the format YYYY-MM-DD.
        time_slot: Named slot for the day ('morning', 'afternoon', 'evening').

    Returns:
        Dict containing:
            - instrument_name: Name of the instrument booked
            - date: Date for which the instrument is booked
            - time_slot: Time slot for which the instrument is booked
            - confirmation_code: Unique confirmation code for the booking
    """
    
    # Simulate a list of available instruments
    available_instruments = ["guitar", "piano", "violin", "drums"]
    
    if instrument_name not in available_instruments:
        raise ValueError(f"Instrument not available: {instrument_name}")
    
    # Simulate a hash-based confirmation code generation
    confirmation_code = f"{hash((instrument_name, date, time_slot)) & 0xFFFFFFFF:08X}"
    
    return {
        "instrument_name": instrument_name,
        "date": date,
        "time_slot": time_slot,
        "confirmation_code": confirmation_code,
    }

from typing import Dict, List, Optional, Union
import hashlib


def search_album(
    query: str,
    genre: Optional[str] = None,
    artist: Optional[str] = None,
    language: Optional[str] = None,
    release_date: Optional[str] = None,
    released_after: Optional[str] = None,
    released_before: Optional[str] = None,
    publisher: Optional[str] = None,
) -> Dict[str, Union[str, List[str], Dict[str, Union[str, List[str]]]]]:
    """Search for an album using various filters and return album data in JSON format.

    Args:
        query: Search term for album title
        genre: Search for album in specific genre
        artist: Search for album by artist
        language: Language of album
        release_date: Exact release date (format: YYYYMMDD)
        released_after: Search for album released after date (format: YYYYMMDD)
        released_before: Search for album released before date (format: YYYYMMDD)
        publisher: Name of publisher of album

    Returns:
        Dict containing:
            - title: Album title
            - artist: List of artist(s)
            - songwriters: List of songwriter(s)
            - genre: Genre of the album
            - language: Language of the album
            - release_date: Release date of the album
            - publisher: Publisher of the album
    """
    # Simulate a database of albums using hash-based generation
    def generate_album_data(query: str) -> Dict[str, Union[str, List[str]]]:
        hash_value = int(hashlib.sha256(query.encode()).hexdigest(), 16)
        artists = ["Artist A", "Artist B", "Artist C"]
        songwriters = ["Songwriter X", "Songwriter Y", "Songwriter Z"]
        genres = ["Pop", "Rock", "Jazz"]
        languages = ["English", "Spanish", "French"]
        publishers = ["Publisher 1", "Publisher 2", "Publisher 3"]

        return {
            "title": f"Album {hash_value % 100}",
            "artist": [artists[hash_value % len(artists)]],
            "songwriters": [songwriters[hash_value % len(songwriters)]],
            "genre": genres[hash_value % len(genres)],
            "language": languages[hash_value % len(languages)],
            "release_date": f"2023{hash_value % 12 + 1:02d}{hash_value % 28 + 1:02d}",
            "publisher": publishers[hash_value % len(publishers)],
        }

    album_data = generate_album_data(query)

    # Filter based on optional parameters
    if genre and album_data["genre"] != genre:
        raise ValueError(f"No album found with genre: {genre}")
    if artist and artist not in album_data["artist"]:
        raise ValueError(f"No album found by artist: {artist}")
    if language and album_data["language"] != language:
        raise ValueError(f"No album found with language: {language}")
    if release_date and album_data["release_date"] != release_date:
        raise ValueError(f"No album found with release date: {release_date}")
    if released_after and album_data["release_date"] <= released_after:
        raise ValueError(f"No album found released after: {released_after}")
    if released_before and album_data["release_date"] >= released_before:
        raise ValueError(f"No album found released before: {released_before}")
    if publisher and album_data["publisher"] != publisher:
        raise ValueError(f"No album found with publisher: {publisher}")

    return album_data

from typing import Dict, List, Union, Optional


def search_artist(
    name: Optional[str] = None,
    genre: Optional[str] = None,
    song_titles: Optional[List[str]] = None,
    album_titles: Optional[List[str]] = None,
    nationality: Optional[str] = None,
    birth_date: Optional[str] = None,
) -> Dict[str, Union[str, List[str], None]]:
    """Search for an artist by various attributes and return their data.

    Args:
        name: Name of the artist.
        genre: Genre associated with the artist.
        song_titles: List of song titles by the artist.
        album_titles: List of album titles by the artist.
        nationality: Nationality of the artist.
        birth_date: Birth date of the artist in YYYYMMDD format.

    Returns:
        Dict containing:
            - name: Name of the artist
            - birth_date: Birth date of the artist
            - nationality: Nationality of the artist
            - genre: Genre associated with the artist
            - songs: List of published songs
            - albums: List of published albums
    """
    
    # Sample data for mock implementation
    sample_artists = {
        "John Doe": {
            "birth_date": "19800101",
            "nationality": "American",
            "genre": "Rock",
            "songs": ["Rock Anthem", "Guitar Hero"],
            "albums": ["Rock On", "Live Loud"]
        },
        "Jane Smith": {
            "birth_date": "19900202",
            "nationality": "British",
            "genre": "Pop",
            "songs": ["Pop Hit", "Dance Floor"],
            "albums": ["Pop Life", "Dance Party"]
        }
    }
    
    # Search logic
    for artist, data in sample_artists.items():
        if name and name != artist:
            continue
        if genre and genre != data["genre"]:
            continue
        if nationality and nationality != data["nationality"]:
            continue
        if birth_date and birth_date != data["birth_date"]:
            continue
        if song_titles and not any(song in data["songs"] for song in song_titles):
            continue
        if album_titles and not any(album in data["albums"] for album in album_titles):
            continue
        return {
            "name": artist,
            "birth_date": data["birth_date"],
            "nationality": data["nationality"],
            "genre": data["genre"],
            "songs": data["songs"],
            "albums": data["albums"]
        }
    
    raise ValueError("Artist not found with the given criteria")

from typing import Dict, List, Optional, Union
import hashlib


def search_song(
    query: str,
    genre: Optional[str] = None,
    artist: Optional[str] = None,
    songwriter: Optional[str] = None,
    language: Optional[str] = None,
    release_date: Optional[str] = None,
    released_after: Optional[str] = None,
    released_before: Optional[str] = None,
    publisher: Optional[str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, List[str]]]]]]:
    """Search for a song using various filters and return song data in JSON format.

    Args:
        query: Search term for song title.
        genre: Search for song in specific genre.
        artist: Search for song by artist.
        songwriter: Search for song by songwriter.
        language: Language of song.
        release_date: Exact release date (format: YYYYMMDD).
        released_after: Search for song released after date (format: YYYYMMDD).
        released_before: Search for song released before date (format: YYYYMMDD).
        publisher: Name of publisher of song.

    Returns:
        Dict containing:
            - query: The search term used.
            - results: List of dictionaries with song details including:
                - title: Title of the song.
                - artist: List of artists.
                - songwriter: List of songwriters.
                - genre: Genre of the song.
                - language: Language of the song.
                - release_date: Release date of the song.
                - publisher: Publisher of the song.
    """
    # Simulate a database of songs
    sample_songs = [
        {
            "title": "Song A",
            "artist": ["Artist 1"],
            "songwriter": ["Songwriter 1"],
            "genre": "Pop",
            "language": "English",
            "release_date": "20230101",
            "publisher": "Publisher 1",
        },
        {
            "title": "Song B",
            "artist": ["Artist 2"],
            "songwriter": ["Songwriter 2"],
            "genre": "Rock",
            "language": "Spanish",
            "release_date": "20220215",
            "publisher": "Publisher 2",
        },
        {
            "title": "Song C",
            "artist": ["Artist 3"],
            "songwriter": ["Songwriter 3"],
            "genre": "Jazz",
            "language": "French",
            "release_date": "20210120",
            "publisher": "Publisher 3",
        },
    ]

    def matches_criteria(song: Dict[str, Union[str, List[str]]]) -> bool:
        if genre and song["genre"] != genre:
            return False
        if artist and artist not in song["artist"]:
            return False
        if songwriter and songwriter not in song["songwriter"]:
            return False
        if language and song["language"] != language:
            return False
        if release_date and song["release_date"] != release_date:
            return False
        if released_after and song["release_date"] <= released_after:
            return False
        if released_before and song["release_date"] >= released_before:
            return False
        if publisher and song["publisher"] != publisher:
            return False
        return True

    # Filter songs based on the criteria
    results = [
        song for song in sample_songs
        if query.lower() in song["title"].lower() and matches_criteria(song)
    ]

    return {
        "query": query,
        "results": results,
    }

