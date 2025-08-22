from typing import Dict, List, Union, Any
# News Media Tools
# Auto-generated implementations from cached categorization

from typing import Dict, List, Union


def get_campaign_overview(
    candidate_name: str,
    include_sections: List[str] = ["donors", "travel", "speeches", "expenditures"]
) -> Dict[str, Union[str, Dict[str, Union[List[str], float]]]]:
    """Retrieve a high-level overview of a candidate's campaign.

    Args:
        candidate_name: Name of the candidate whose campaign overview is being requested.
        include_sections: List of sections to include in the overview (donors, travel, speeches, expenditures).

    Returns:
        Dict containing:
            - candidate_name: Name of the candidate
            - overview: A dictionary with keys as section names and values as section data
    """
    if not candidate_name:
        raise ValueError("Candidate name must be provided.")

    sample_data = {
        "donors": ["Alice Johnson", "Bob Smith", "Charlie Brown"],
        "travel": ["New York", "Los Angeles", "Chicago"],
        "speeches": ["Healthcare Reform", "Economic Growth", "Education Policy"],
        "expenditures": 125000.50,
    }

    overview = {}
    for section in include_sections:
        if section not in sample_data:
            raise ValueError(f"Section not supported: {section}")
        overview[section] = sample_data[section]

    return {
        "candidate_name": candidate_name,
        "overview": overview,
    }

from typing import Dict


def get_local_business_headline(location: str) -> Dict[str, str]:
    """Gets the local business headline in a specified location.

    Args:
        location: The city and country (e.g. 'New York, USA', 'Tokyo, Japan')

    Returns:
        Dict containing:
            - location: The specified location
            - headline: A headline about local business news
    """
    
    sample_headlines = {
        "New York, USA": "Wall Street sees record highs amid tech boom",
        "Tokyo, Japan": "Toyota announces new electric vehicle lineup",
        "London, UK": "Brexit impacts on local businesses continue to unfold",
        "Berlin, Germany": "Berlin startups attract record venture capital",
        "Sydney, Australia": "Australian dollar strengthens as exports rise",
    }
    
    if location not in sample_headlines:
        raise ValueError(f"Location not supported: {location}")

    return {
        "location": location,
        "headline": sample_headlines[location],
    }

from typing import Dict, List


def get_tv_news(channel: str, language: str = "en") -> Dict[str, Union[str, List[str]]]:
    """Fetch the latest TV news headlines for a specific channel or network.

    Args:
        channel: The channel whose news you want (e.g. 'CNN', 'BBC')
        language: ISO-639 language code for the headlines (default is 'en')

    Returns:
        Dict containing:
            - channel: Name of the channel
            - language: Language code of the headlines
            - headlines: List of latest news headlines
    """
    
    sample_news = {
        "CNN": {
            "en": [
                "Breaking: Major breakthrough in climate talks",
                "Stock markets rally as tech stocks soar",
                "New study reveals health benefits of coffee"
            ],
            "es": [
                "Última hora: Avance importante en las conversaciones sobre el clima",
                "Los mercados bursátiles se recuperan mientras las acciones tecnológicas suben",
                "Nuevo estudio revela beneficios para la salud del café"
            ]
        },
        "BBC": {
            "en": [
                "Prime Minister announces new economic plan",
                "Historic peace agreement signed in Middle East",
                "Scientists discover new species in the Amazon"
            ],
            "fr": [
                "Le Premier ministre annonce un nouveau plan économique",
                "Accord de paix historique signé au Moyen-Orient",
                "Les scientifiques découvrent une nouvelle espèce en Amazonie"
            ]
        }
    }
    
    if channel not in sample_news:
        raise ValueError(f"Channel not supported: {channel}")
    if language not in sample_news[channel]:
        raise ValueError(f"Language not supported for channel {channel}: {language}")

    return {
        "channel": channel,
        "language": language,
        "headlines": sample_news[channel][language]
    }

from typing import Dict, List, Union, Optional
from datetime import datetime


def search_speech_transcripts(
    candidate_name: str,
    keywords: List[str],
    date_range: Optional[Dict[str, Optional[str]]] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, List[str]]]]]]:
    """Search public campaign speech transcripts by keywords or topics.

    Args:
        candidate_name: Name of the candidate whose speeches are being searched.
        keywords: List of keywords or topics to search for in speech transcripts.
        date_range: Optional date range to filter speeches with 'start_date' and 'end_date' in YYYY-MM-DD format.

    Returns:
        Dict containing:
            - candidate: Name of the candidate
            - speeches: List of speeches with:
                - date: Date of the speech
                - location: Location where the speech was given
                - transcript: List of sentences containing the keywords
    """
    # Sample data for demonstration purposes
    sample_speeches = {
        "John Doe": [
            {
                "date": "2023-01-15",
                "location": "New York",
                "transcript": [
                    "Today we discuss the importance of healthcare reform.",
                    "Our economy needs a boost, and we have the plan to achieve it."
                ]
            },
            {
                "date": "2023-02-20",
                "location": "Los Angeles",
                "transcript": [
                    "Education is the cornerstone of our future.",
                    "We must invest in renewable energy sources."
                ]
            }
        ],
        "Jane Smith": [
            {
                "date": "2023-03-10",
                "location": "Chicago",
                "transcript": [
                    "Healthcare is a fundamental right for all.",
                    "We need to address climate change urgently."
                ]
            }
        ]
    }

    if candidate_name not in sample_speeches:
        raise ValueError(f"No speeches found for candidate: {candidate_name}")

    filtered_speeches = []
    for speech in sample_speeches[candidate_name]:
        if date_range:
            start_date = date_range.get("start_date")
            end_date = date_range.get("end_date")
            speech_date = datetime.strptime(speech["date"], "%Y-%m-%d")
            if start_date and speech_date < datetime.strptime(start_date, "%Y-%m-%d"):
                continue
            if end_date and speech_date > datetime.strptime(end_date, "%Y-%m-%d"):
                continue

        matching_sentences = [
            sentence for sentence in speech["transcript"]
            if any(keyword.lower() in sentence.lower() for keyword in keywords)
        ]
        if matching_sentences:
            filtered_speeches.append({
                "date": speech["date"],
                "location": speech["location"],
                "transcript": matching_sentences
            })

    return {
        "candidate": candidate_name,
        "speeches": filtered_speeches
    }

from typing import Dict, List, Union


def uk_election_statistics(location: str) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Get comprehensive data on general election voting statistics for any UK location for the past 5 years.

    Args:
        location: UK location (e.g. address, constituency, city)

    Returns:
        Dict containing:
            - location: The specified location
            - elections: List of dictionaries with election year and voting statistics
    """
    
    sample_data = {
        "London": [
            {"year": 2019, "votes": 5000000, "turnout_percentage": 68},
            {"year": 2017, "votes": 4800000, "turnout_percentage": 70},
            {"year": 2015, "votes": 4500000, "turnout_percentage": 65},
        ],
        "Manchester": [
            {"year": 2019, "votes": 1200000, "turnout_percentage": 66},
            {"year": 2017, "votes": 1150000, "turnout_percentage": 67},
            {"year": 2015, "votes": 1100000, "turnout_percentage": 64},
        ],
        "Edinburgh": [
            {"year": 2019, "votes": 800000, "turnout_percentage": 72},
            {"year": 2017, "votes": 750000, "turnout_percentage": 70},
            {"year": 2015, "votes": 700000, "turnout_percentage": 68},
        ],
    }
    
    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    return {
        "location": location,
        "elections": sample_data[location],
    }

