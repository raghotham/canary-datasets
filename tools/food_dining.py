from datetime import datetime, timedelta

# Food Dining Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def book_table(
    table_id: str,
    start_time: Dict[str, Union[int, str]],
    duration: int = 90,
    customer_id: str = None,
) -> Dict[str, Union[str, int, Dict[str, Union[int, str]]]]:
    """Mark a table as booked in the system.

    Args:
        table_id: The unique identifier for a table.
        start_time: The start time of the booking as a dictionary with 'year', 'month', 'day', 'hour', 'minute'.
        duration: The duration of the booking, in minutes (default is 90).
        customer_id: The unique identifier of the customer who has made the booking.

    Returns:
        Dict containing:
            - table_id: The unique identifier for the table.
            - customer_id: The unique identifier of the customer.
            - start_time: The start time of the booking.
            - end_time: The end time of the booking.
            - status: The status of the booking.
    """
    if not table_id or not customer_id or not start_time:
        raise ValueError("table_id, customer_id, and start_time are required fields")

    try:
        start_dt = datetime(
            year=start_time["year"],
            month=start_time["month"],
            day=start_time["day"],
            hour=start_time["hour"],
            minute=start_time["minute"],
        )
    except KeyError as e:
        raise ValueError(f"Missing time component: {e}")

    end_dt = start_dt + timedelta(minutes=duration)

    return {
        "table_id": table_id,
        "customer_id": customer_id,
        "start_time": start_time,
        "end_time": {
            "year": end_dt.year,
            "month": end_dt.month,
            "day": end_dt.day,
            "hour": end_dt.hour,
            "minute": end_dt.minute,
        },
        "status": "booked",
    }


from typing import Dict, Optional, Union


def check_inventory(
    ingredient: Optional[str] = None,
) -> Dict[str, Union[str, int, Dict[str, int]]]:
    """Checks the current inventory levels for bar ingredients.

    Args:
        ingredient: Optional specific ingredient to check.

    Returns:
        Dict containing:
            - ingredient: Name of the ingredient checked or 'all'
            - quantity: Quantity available for the specified ingredient
            - inventory: Dictionary of all ingredients and their quantities if no specific ingredient is provided
    """
    inventory_data = {
        "vodka": 50,
        "gin": 30,
        "rum": 20,
        "tequila": 15,
        "whiskey": 40,
        "triple sec": 25,
        "vermouth": 10,
        "bitters": 5,
    }

    if ingredient:
        if ingredient not in inventory_data:
            raise ValueError(f"Ingredient not found in inventory: {ingredient}")
        return {
            "ingredient": ingredient,
            "quantity": inventory_data[ingredient],
        }

    return {
        "ingredient": "all",
        "inventory": inventory_data,
    }


from typing import Dict, Union


def add_new_menu_item(
    name: str,
    price: float,
    quantity: int,
    description: str = None,
    is_daily_special: bool = False,
) -> Dict[str, Union[str, float, int, bool]]:
    """Add a new item to the menu.

    Args:
        name: The name of the menu item
        price: The price of the menu item
        quantity: The number of times the menu item can be served in a day
        description: A description of the menu item
        is_daily_special: True if the menu item is a daily special

    Returns:
        Dict containing:
            - name: Name of the menu item
            - price: Price of the menu item
            - quantity: Available quantity per day
            - description: Description of the menu item
            - is_daily_special: Whether the item is a daily special
    """
    if not name or price <= 0 or quantity <= 0:
        raise ValueError(
            "Invalid input: Ensure name is provided and price/quantity are positive."
        )

    # Simulate adding the item to a menu
    menu_item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "description": description or "No description available.",
        "is_daily_special": is_daily_special,
    }

    # Mocked response as if the item was successfully added to a database
    return menu_item


from typing import Dict, Optional


def cut_off_patron(
    patron_id: str, reason: Optional[str] = None
) -> Dict[str, Union[str, bool]]:
    """Flags a patron as cut off from further alcohol service.

    Args:
        patron_id: The unique identifier for the patron.
        reason: Optional reason for cutting off the patron.

    Returns:
        Dict containing:
            - patron_id: The unique identifier for the patron.
            - cut_off: Boolean indicating if the patron is cut off.
            - reason: Reason for cutting off the patron, if provided.
    """

    if not patron_id:
        raise ValueError("patron_id is required")

    # Simulate a database of patrons with a simple hash-based check
    cut_off_status = (
        hash(patron_id) % 2 == 0
    )  # Randomly decide cut-off status for demonstration

    return {
        "patron_id": patron_id,
        "cut_off": cut_off_status,
        "reason": reason if reason else "No reason provided",
    }


from typing import Dict, List, Union


def find_delivery_now(
    location: str,
    open_now: bool,
    takes_delivery: bool,
    cuisine_type: Union[str, None] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, bool]]]]]:
    """Find open restaurants near the user that can deliver to them.

    Args:
        location: The user's location, to search for nearby restaurants.
        open_now: Filter results to restaurants that are currently open.
        takes_delivery: Filter results to restaurants that take delivery orders.
        cuisine_type: Filter results to restaurants that serve the desired cuisine.

    Returns:
        Dict containing:
            - location: The user's location
            - restaurants: List of restaurants with details
                - name: Name of the restaurant
                - open_now: Whether the restaurant is currently open
                - takes_delivery: Whether the restaurant takes delivery orders
                - cuisine: Type of cuisine served
    """
    sample_restaurants = {
        "New York": [
            {
                "name": "Pizza Palace",
                "open_now": True,
                "takes_delivery": True,
                "cuisine": "Italian",
            },
            {
                "name": "Sushi Central",
                "open_now": False,
                "takes_delivery": True,
                "cuisine": "Japanese",
            },
            {
                "name": "Burger Barn",
                "open_now": True,
                "takes_delivery": False,
                "cuisine": "American",
            },
        ],
        "San Francisco": [
            {
                "name": "Taco Town",
                "open_now": True,
                "takes_delivery": True,
                "cuisine": "Mexican",
            },
            {
                "name": "Curry Corner",
                "open_now": True,
                "takes_delivery": True,
                "cuisine": "Indian",
            },
            {
                "name": "Noodle Nook",
                "open_now": False,
                "takes_delivery": True,
                "cuisine": "Chinese",
            },
        ],
    }

    if location not in sample_restaurants:
        raise ValueError(f"Location not supported: {location}")

    restaurants = sample_restaurants[location]
    filtered_restaurants = [
        restaurant
        for restaurant in restaurants
        if (not open_now or restaurant["open_now"])
        and (not takes_delivery or restaurant["takes_delivery"])
        and (cuisine_type is None or restaurant["cuisine"] == cuisine_type)
    ]

    return {
        "location": location,
        "restaurants": filtered_restaurants,
    }


from typing import Dict, List, Union


def find_energy_drinks_by_ingredient(
    ingredient: str,
) -> Dict[str, Union[str, List[str]]]:
    """Search for energy drinks that contain a specific ingredient.

    Args:
        ingredient: The ingredient to search for (e.g., 'taurine', 'guarana').

    Returns:
        Dict containing:
            - ingredient: The ingredient searched for
            - energy_drinks: List of energy drinks containing the ingredient
    """
    sample_data = {
        "taurine": ["Red Bull", "Monster", "Rockstar"],
        "guarana": ["5-hour Energy", "AMP Energy", "NOS"],
        "caffeine": ["Red Bull", "Monster", "5-hour Energy", "NOS"],
        "ginseng": ["Monster", "Rockstar"],
    }

    if ingredient not in sample_data:
        raise ValueError(f"Ingredient not supported: {ingredient}")

    return {
        "ingredient": ingredient,
        "energy_drinks": sample_data.get(ingredient, []),
    }


from typing import Dict, Union


def get_daily_feeding_plan(
    pet_name: str, species: str, weight_kg: float
) -> Dict[str, Union[str, float, list]]:
    """Retrieve the daily feeding plan for a pet based on its dietary needs.

    Args:
        pet_name: The pet's name
        species: Species of the pet (e.g., dog, cat, rabbit)
        weight_kg: The pet's weight in kilograms

    Returns:
        Dict containing:
            - pet_name: The pet's name
            - species: Species of the pet
            - weight_kg: The pet's weight in kilograms
            - meals: List of meals with their respective quantities in grams
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number")

    feeding_guidelines = {
        "dog": lambda w: [("breakfast", w * 10), ("dinner", w * 15)],
        "cat": lambda w: [("breakfast", w * 8), ("dinner", w * 12)],
        "rabbit": lambda w: [("morning", w * 5), ("evening", w * 5)],
    }

    if species not in feeding_guidelines:
        raise ValueError(f"Species not supported: {species}")

    meals = feeding_guidelines[species](weight_kg)

    return {
        "pet_name": pet_name,
        "species": species,
        "weight_kg": weight_kg,
        "meals": [{"name": meal[0], "quantity_g": meal[1]} for meal in meals],
    }


from datetime import datetime
from typing import Dict, Optional, Union


def get_drink_summary(
    patron_id: str, time_range: Optional[Dict[str, Optional[str]]] = None
) -> Dict[str, Union[str, int]]:
    """Retrieves a summary of how many drinks a patron has consumed.

    Args:
        patron_id: The unique identifier for the patron.
        time_range: Optional time range to filter drinks consumed, with
                    'start_time' and 'end_time' in ISO 8601 format.

    Returns:
        Dict containing:
            - patron_id: The unique identifier for the patron.
            - total_drinks: Total number of drinks consumed by the patron.
    """
    # Mock data for demonstration purposes
    drink_data = {
        "patron_001": 5,
        "patron_002": 3,
        "patron_003": 8,
    }

    if patron_id not in drink_data:
        raise ValueError(f"Patron ID not found: {patron_id}")

    total_drinks = drink_data[patron_id]

    if time_range:
        start_time = time_range.get("start_time")
        end_time = time_range.get("end_time")

        # Simulate filtering by time range
        if start_time:
            try:
                datetime.fromisoformat(start_time)
            except ValueError:
                raise ValueError(f"Invalid start_time format: {start_time}")

        if end_time:
            try:
                datetime.fromisoformat(end_time)
            except ValueError:
                raise ValueError(f"Invalid end_time format: {end_time}")

        # For simplicity, assume half the drinks were consumed in the given time range
        total_drinks = total_drinks // 2

    return {
        "patron_id": patron_id,
        "total_drinks": total_drinks,
    }


from typing import Dict, Optional


def get_energy_drink_info(
    brand_name: str, flavor: Optional[str] = None
) -> Dict[str, str]:
    """Retrieves detailed information about a specific energy drink.

    Args:
        brand_name: The brand name of the energy drink.
        flavor: The flavor variant of the drink (optional).

    Returns:
        Dict containing:
            - brand_name: The brand name of the energy drink
            - flavor: The flavor variant of the drink
            - caffeine_content: Caffeine content in mg
            - sugar_content: Sugar content in grams
            - description: A brief description of the drink
    """

    sample_data = {
        "Red Bull": {
            "Original": {
                "caffeine_content": "80mg",
                "sugar_content": "27g",
                "description": "The original energy drink with a unique taste.",
            },
            "Sugarfree": {
                "caffeine_content": "80mg",
                "sugar_content": "0g",
                "description": "The sugar-free version of the classic energy drink.",
            },
        },
        "Monster": {
            "Original": {
                "caffeine_content": "160mg",
                "sugar_content": "54g",
                "description": "A powerful energy drink with a bold flavor.",
            },
            "Ultra": {
                "caffeine_content": "140mg",
                "sugar_content": "0g",
                "description": "A zero-sugar energy drink with a refreshing taste.",
            },
        },
    }

    if brand_name not in sample_data:
        raise ValueError(f"Brand not supported: {brand_name}")

    brand_info = sample_data[brand_name]

    if flavor:
        if flavor not in brand_info:
            raise ValueError(f"Flavor not supported for {brand_name}: {flavor}")
        flavor_info = brand_info[flavor]
    else:
        # Default to the first available flavor if none specified
        flavor, flavor_info = next(iter(brand_info.items()))

    return {
        "brand_name": brand_name,
        "flavor": flavor,
        "caffeine_content": flavor_info["caffeine_content"],
        "sugar_content": flavor_info["sugar_content"],
        "description": flavor_info["description"],
    }


from typing import Dict, Union


def get_friends_rating(restaurant_name: str) -> Dict[str, Union[str, float]]:
    """Returns the average of all friends' ratings for the restaurant.

    Args:
        restaurant_name: Name of the restaurant to get ratings for

    Returns:
        Dict containing:
            - restaurant_name: Name of the restaurant
            - average_rating: Average rating from friends
    """

    # Simulated ratings data based on restaurant names
    ratings_data = {
        "Pasta Palace": [4.5, 4.0, 4.7, 5.0],
        "Burger Barn": [3.5, 3.8, 4.0, 4.2],
        "Sushi Spot": [4.8, 4.9, 5.0, 4.7],
    }

    if restaurant_name not in ratings_data:
        raise ValueError(f"Restaurant not found: {restaurant_name}")

    ratings = ratings_data[restaurant_name]
    average_rating = sum(ratings) / len(ratings)

    return {
        "restaurant_name": restaurant_name,
        "average_rating": round(average_rating, 2),
    }


from typing import Dict, List, Union


def get_ingredients(
    location: str = "Kitchen", on_order: bool = False
) -> Dict[str, Union[str, List[str]]]:
    """Retrieve all ingredients paid for in the restaurant.

    Args:
        location: Specific location to retrieve available ingredients from (default is 'Kitchen')
        on_order: Include ingredients on order from vendor within 3 days (default is False)

    Returns:
        Dict containing:
            - location: The location from which ingredients are retrieved
            - ingredients: List of ingredients available at the specified location
    """

    sample_data = {
        "Kitchen": ["Tomatoes", "Basil", "Olive Oil", "Garlic"],
        "Pantry": ["Flour", "Sugar", "Salt", "Baking Powder"],
        "Bar": ["Lemon", "Mint", "Rum", "Vodka"],
    }

    on_order_data = {
        "Kitchen": ["Parmesan Cheese", "Pasta"],
        "Pantry": ["Yeast", "Cocoa Powder"],
        "Bar": ["Gin", "Tonic Water"],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    ingredients = sample_data[location]

    if on_order:
        ingredients.extend(on_order_data.get(location, []))

    return {
        "location": location,
        "ingredients": ingredients,
    }


from typing import Dict, Union


def get_public_rating(restaurant_name: str) -> Dict[str, Union[str, float]]:
    """Returns the average of all ratings for the specified restaurant.

    Args:
        restaurant_name: Name of the restaurant to get the average rating for

    Returns:
        Dict containing:
            - restaurant_name: Name of the restaurant
            - average_rating: Average rating of the restaurant
    """

    sample_ratings = {
        "The Gourmet Kitchen": [4.5, 4.0, 5.0, 3.5],
        "Pasta Palace": [3.0, 3.5, 4.0, 4.5],
        "Burger Barn": [4.0, 4.5, 4.0, 5.0],
    }

    if restaurant_name not in sample_ratings:
        raise ValueError(f"Restaurant not found: {restaurant_name}")

    ratings = sample_ratings[restaurant_name]
    average_rating = sum(ratings) / len(ratings)

    return {
        "restaurant_name": restaurant_name,
        "average_rating": average_rating,
    }


from typing import Dict, List, Optional


def get_top_restaurants(
    cuisine: Optional[str] = None, price: Optional[str] = None
) -> Dict[str, List[Dict[str, Union[str, float]]]]:
    """Returns top 10 public rated restaurants filtered by cuisine and price.

    Args:
        cuisine: Filters the list based on the cuisine (e.g. 'Italian', 'Chinese')
        price: Filters the list based on the price range ($-$$$$)

    Returns:
        Dict containing:
            - restaurants: List of top 10 restaurants with:
                - name: Name of the restaurant
                - rating: Average public rating
                - cuisine: Type of cuisine
                - price: Price range
    """

    sample_restaurants = [
        {"name": "Pasta Palace", "rating": 4.8, "cuisine": "Italian", "price": "$$"},
        {"name": "Sushi Central", "rating": 4.7, "cuisine": "Japanese", "price": "$$$"},
        {"name": "Taco Town", "rating": 4.6, "cuisine": "Mexican", "price": "$"},
        {"name": "Burger Bonanza", "rating": 4.5, "cuisine": "American", "price": "$"},
        {"name": "Curry Corner", "rating": 4.9, "cuisine": "Indian", "price": "$$"},
        {"name": "Dragon Delight", "rating": 4.4, "cuisine": "Chinese", "price": "$$"},
        {"name": "Vegan Vibes", "rating": 4.3, "cuisine": "Vegan", "price": "$$$"},
        {"name": "Pizza Paradise", "rating": 4.2, "cuisine": "Pizza", "price": "$"},
        {"name": "Bistro Bliss", "rating": 4.1, "cuisine": "French", "price": "$$$"},
        {"name": "Seafood Shack", "rating": 4.0, "cuisine": "Seafood", "price": "$$$$"},
    ]

    if cuisine:
        sample_restaurants = [
            restaurant
            for restaurant in sample_restaurants
            if restaurant["cuisine"] == cuisine
        ]

    if price:
        sample_restaurants = [
            restaurant
            for restaurant in sample_restaurants
            if restaurant["price"] == price
        ]

    if not sample_restaurants:
        raise ValueError("No restaurants found with the specified filters")

    return {"restaurants": sample_restaurants[:10]}


from typing import Dict, Literal, Union


def make_drink(
    drink_name: str,
    customizations: Dict[str, Union[str, bool]] = None,
    patron_id: str = None,
) -> Dict[str, Union[str, Dict[str, Union[str, bool]]]]:
    """Prepares a drink based on the specified recipe.

    Args:
        drink_name: The name of the drink to prepare.
        customizations: Optional customizations (e.g., extra ice, no garnish).
        patron_id: Optional patron ID to associate with the drink order.

    Returns:
        Dict containing:
            - drink_name: The name of the drink prepared
            - customizations: Applied customizations for the drink
            - patron_id: ID of the patron associated with the order (if provided)
    """
    if not drink_name:
        raise ValueError("Drink name must be provided")

    # Default customizations
    default_customizations = {
        "ice_level": "normal",
        "alcohol_strength": "normal",
        "garnish": True,
    }

    # Merge provided customizations with defaults
    if customizations is None:
        customizations = default_customizations
    else:
        customizations = {**default_customizations, **customizations}

    # Simulated drink preparation logic
    available_drinks = ["Mojito", "Martini", "Old Fashioned"]
    if drink_name not in available_drinks:
        raise ValueError(f"Drink not supported: {drink_name}")

    # Simulated response
    return {
        "drink_name": drink_name,
        "customizations": customizations,
        "patron_id": patron_id,
    }


from typing import Dict, Union


def rate_energy_drink(
    brand_name: str,
    rating: float,
    flavor: Union[str, None] = None,
    review: Union[str, None] = None,
) -> Dict[str, Union[str, float, None]]:
    """Rate and review an energy drink.

    Args:
        brand_name: The brand name of the drink being rated.
        rating: A rating from 1 to 5.
        flavor: The flavor variant being rated (optional).
        review: An optional written review.

    Returns:
        Dict containing:
            - brand_name: The brand name of the drink
            - flavor: The flavor variant, if provided
            - rating: The rating given to the drink
            - review: The written review, if provided
            - summary: A summary of the review
    """
    if not (1 <= rating <= 5):
        raise ValueError("Rating must be between 1 and 5.")

    # Generate a summary based on the rating
    summary_map = {1: "Terrible", 2: "Poor", 3: "Average", 4: "Good", 5: "Excellent"}
    summary = summary_map.get(int(rating), "No summary available")

    return {
        "brand_name": brand_name,
        "flavor": flavor,
        "rating": rating,
        "review": review,
        "summary": summary,
    }


from typing import Dict, Optional


def rate_restaurant(
    restaurant_name: str, rating: str, review: Optional[str] = None
) -> Dict[str, Union[str, float]]:
    """Rates a given restaurant out of 5.

    Args:
        restaurant_name: Name of the restaurant.
        rating: Rating of the restaurant from 0.0-5.0, inclusive.
        review: Optional notes about the experience with the restaurant.

    Returns:
        Dict containing:
            - restaurant_name: Name of the restaurant
            - rating: Rating of the restaurant
            - review: Review notes if provided
    """
    try:
        numeric_rating = float(rating)
        if not (0.0 <= numeric_rating <= 5.0):
            raise ValueError("Rating must be between 0.0 and 5.0")
    except ValueError as e:
        raise ValueError(f"Invalid rating value: {rating}") from e

    sample_reviews = {
        "The Great Eatery": "Fantastic food and service!",
        "Quick Bites": "Good for a quick meal.",
        "Gourmet Delight": "Exquisite dining experience.",
        "Marco's Pizzaria": "The pizza had so little cheese and the crust tasted like cardboard.",
    }

    return {
        "restaurant_name": restaurant_name,
        "rating": numeric_rating,
        "review": review or sample_reviews.get(restaurant_name, "No review available."),
    }


from typing import Dict, Optional, Union


def suggest_drink(
    patron_id: Optional[str] = None,
    preferences: Optional[Dict[str, Optional[str]]] = None,
) -> Dict[str, Union[str, Dict[str, str]]]:
    """Suggest a drink based on a patron's preferences or past orders.

    Args:
        patron_id: Optional patron ID to personalize suggestions.
        preferences: Optional drink preferences, such as flavor profile
                     and alcohol preference.

    Returns:
        Dict containing:
            - drink_name: Suggested drink name
            - details: Dictionary with flavor profile and alcohol content
    """

    # Sample data for demonstration purposes
    drinks = {
        "sweet": {
            "yes": {
                "drink_name": "Mojito",
                "flavor_profile": "sweet",
                "alcohol_content": "medium",
            },
            "no": {
                "drink_name": "Virgin Pina Colada",
                "flavor_profile": "sweet",
                "alcohol_content": "none",
            },
        },
        "strong": {
            "yes": {
                "drink_name": "Old Fashioned",
                "flavor_profile": "strong",
                "alcohol_content": "high",
            },
            "no": {
                "drink_name": "Espresso",
                "flavor_profile": "strong",
                "alcohol_content": "none",
            },
        },
        "non_alcoholic": {
            "yes": {
                "drink_name": "Shirley Temple",
                "flavor_profile": "fruity",
                "alcohol_content": "none",
            },
            "no": {
                "drink_name": "Lemonade",
                "flavor_profile": "citrus",
                "alcohol_content": "none",
            },
        },
    }

    # Default preferences if none provided
    default_preferences = {"flavor_profile": "sweet", "alcohol_preference": "yes"}

    # Use provided preferences or default
    if preferences is None:
        preferences = default_preferences

    flavor_profile = preferences.get("flavor_profile", "sweet")
    alcohol_preference = preferences.get("alcohol_preference", "yes")

    # Suggest a drink based on preferences
    if flavor_profile in drinks and alcohol_preference in drinks[flavor_profile]:
        suggestion = drinks[flavor_profile][alcohol_preference]
    else:
        # Fallback suggestion
        suggestion = {
            "drink_name": "Water",
            "flavor_profile": "neutral",
            "alcohol_content": "none",
        }

    return {
        "drink_name": suggestion["drink_name"],
        "details": {
            "flavor_profile": suggestion["flavor_profile"],
            "alcohol_content": suggestion["alcohol_content"],
        },
    }


from typing import Dict, List, Union


def suggest_energy_drink(
    preferred_flavors: List[str] = [], max_caffeine_mg: float = 200
) -> Dict[str, Union[str, float]]:
    """Suggest an energy drink based on flavor preferences and caffeine tolerance.

    Args:
        preferred_flavors: List of preferred flavors.
        max_caffeine_mg: Maximum caffeine content the user is comfortable with.

    Returns:
        Dict containing:
            - name: Suggested energy drink name
            - flavor: Flavor of the suggested drink
            - caffeine_mg: Caffeine content of the suggested drink
    """
    sample_drinks = [
        {"name": "BuzzBerry", "flavor": "berry", "caffeine_mg": 150},
        {"name": "CitrusCharge", "flavor": "citrus", "caffeine_mg": 180},
        {"name": "MangoMight", "flavor": "mango", "caffeine_mg": 120},
        {"name": "TropicalThunder", "flavor": "tropical", "caffeine_mg": 200},
        {"name": "VanillaVibe", "flavor": "vanilla", "caffeine_mg": 100},
    ]

    # Filter drinks by caffeine content
    suitable_drinks = [
        drink for drink in sample_drinks if drink["caffeine_mg"] <= max_caffeine_mg
    ]

    if not suitable_drinks:
        raise ValueError("No drinks available with the specified caffeine limit.")

    # Further filter by preferred flavors if provided
    if preferred_flavors:
        suitable_drinks = [
            drink for drink in suitable_drinks if drink["flavor"] in preferred_flavors
        ]

    if not suitable_drinks:
        raise ValueError("No drinks match the preferred flavors and caffeine limit.")

    # Select the first suitable drink as a suggestion
    suggested_drink = suitable_drinks[0]

    return {
        "name": suggested_drink["name"],
        "flavor": suggested_drink["flavor"],
        "caffeine_mg": suggested_drink["caffeine_mg"],
    }


from typing import Dict, Literal


def verify_id(
    id_number: str,
    id_type: Literal["driver_license", "passport", "state_id"] = "driver_license",
) -> Dict[str, Union[bool, str]]:
    """Verify a patron's ID to confirm they are of legal drinking age.

    Args:
        id_number: The ID number or barcode to verify.
        id_type: The type of ID (e.g., 'driver_license', 'passport').

    Returns:
        Dict containing:
            - is_valid: Boolean indicating if the ID is valid and the patron is of legal age
            - message: A message providing additional information
    """

    # Sample hash-based ID verification simulation
    if not id_number:
        raise ValueError("ID number cannot be empty")

    # Simulated hash-based check for age verification
    hash_value = hash(id_number) % 100
    is_valid = hash_value >= 21  # Simulating age check

    if is_valid:
        return {
            "is_valid": True,
            "message": "ID is valid and patron is of legal drinking age.",
        }
    else:
        return {
            "is_valid": False,
            "message": "ID is invalid or patron is not of legal drinking age.",
        }


from typing import Dict, List, Optional, Union


def generate_recipe(
    ingredients: Optional[List[str]] = None,
    dietaries: Optional[List[str]] = None,
    dish_name: Optional[str] = None,
    cuisine: Optional[str] = None,
) -> Dict[str, Union[str, List[str]]]:
    """Generate a recipe based on user requirements.

    Args:
        ingredients: A list of ingredients to use in the recipe.
        dietaries: A list of dietary requirements.
        dish_name: Name or description of a dish.
        cuisine: Desired cuisine of recipe.

    Returns:
        Dict containing:
            - title: The generated recipe title.
            - ingredients: List of ingredients used in the recipe.
            - steps: List of steps to prepare the dish.
            - cuisine: The cuisine of the recipe.
            - dietaries: List of dietary requirements met by the recipe.
    """
    # Sample data generation based on input parameters
    if not ingredients:
        ingredients = ["chicken", "rice", "broccoli"]
    if not dietaries:
        dietaries = ["gluten-free"]
    if not dish_name:
        dish_name = "Delicious Dish"
    if not cuisine:
        cuisine = "Fusion"

    # Simulate recipe generation
    recipe_title = f"{cuisine} Style {dish_name}"
    steps = [
        f"Prepare the {', '.join(ingredients)}.",
        "Cook until done.",
        "Serve hot and enjoy!",
    ]

    return {
        "title": recipe_title,
        "ingredients": ingredients,
        "steps": steps,
        "cuisine": cuisine,
        "dietaries": dietaries,
    }


from typing import Dict, List, Union


def chinese_restaurant(
    lat: float, lng: float, radius_km: float = 10
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find Chinese restaurants nearby based on the current location.

    Args:
        lat: The latitude coordinate of the user's location
        lng: The longitude coordinate of the user's location
        radius_km: The distance in kilometers from the user's location

    Returns:
        Dict containing:
            - location: A string representation of the user's location
            - restaurants: A list of dictionaries, each containing:
                - name: The name of the restaurant
                - distance_km: The distance from the user's location in kilometers
                - rating: The average rating of the restaurant
    """

    # Simulated sample data based on hash of coordinates
    sample_data = {
        (42.3601, -71.0589): [
            {"name": "Golden Dragon", "distance_km": 2.5, "rating": 4.5},
            {"name": "Panda Express", "distance_km": 3.0, "rating": 4.0},
        ],
        (35.6895, 139.6917): [
            {"name": "Shanghai Delight", "distance_km": 1.2, "rating": 4.7},
            {"name": "Szechuan Palace", "distance_km": 2.8, "rating": 4.3},
        ],
    }

    location_key = (round(lat, 4), round(lng, 4))
    if location_key not in sample_data:
        raise ValueError(f"No data available for location: {location_key}")

    return {
        "location": f"Lat: {lat}, Lng: {lng}",
        "restaurants": sample_data[location_key],
    }


from typing import Dict


def book_cafe(cafe_name: str, date: str) -> Dict[str, str]:
    """Book a given cafe for a specified date.

    Args:
        cafe_name: The name of the cafe to be booked
        date: The date to book the cafe (format: YYYY-MM-DD)

    Returns:
        Dict containing:
            - cafe_name: Name of the cafe booked
            - date: Date of the booking
            - confirmation_code: A unique confirmation code for the booking
    """
    if not cafe_name or not date:
        raise ValueError("Both cafe_name and date must be provided")

    # Simulate a confirmation code generation using a hash
    confirmation_code = f"{hash(cafe_name + date) % 10000:04}"

    return {
        "cafe_name": cafe_name,
        "date": date,
        "confirmation_code": confirmation_code,
    }


from typing import Dict


def book_restaurant_reservation(people: int) -> Dict[str, Union[str, int]]:
    """Make a reservation at the restaurant for a specified number of people.

    Args:
        people: How many people the reservation is for

    Returns:
        Dict containing:
            - reservation_id: Unique identifier for the reservation
            - people: Number of people the reservation is for
            - status: Status of the reservation
    """
    if people < 1:
        raise ValueError("Number of people must be at least 1")

    # Simulate a reservation ID using a hash-based generation for consistency
    reservation_id = hash(f"reservation_{people}") % 10000

    return {
        "reservation_id": f"RES-{reservation_id}",
        "people": people,
        "status": "confirmed",
    }


from typing import Dict


def book_store_cafe(bookstore_name: str) -> Dict[str, bool]:
    """Determine if a bookstore has a cafe.

    Args:
        bookstore_name: Name of the bookstore to check (e.g. 'Barnes & Noble', 'Waterstones')

    Returns:
        Dict containing:
            - bookstore_name: Name of the bookstore
            - has_cafe: Boolean indicating if the bookstore has a cafe
    """
    sample_data = {
        "Barnes & Noble": True,
        "Waterstones": True,
        "Books-A-Million": False,
        "Powell's Books": True,
        "The Strand": False,
    }

    if bookstore_name not in sample_data:
        raise ValueError(f"Bookstore not supported: {bookstore_name}")

    return {
        "bookstore_name": bookstore_name,
        "has_cafe": sample_data[bookstore_name],
    }


from typing import Dict, Optional


def cafe_has_library(cafe_name: str, city: Optional[str] = None) -> Dict[str, bool]:
    """Determine if a given cafe has a library.

    Args:
        cafe_name: Name of the cafe to check
        city: Optional; Name of the city where the cafe is located

    Returns:
        Dict containing:
            - cafe_name: Name of the cafe
            - has_library: Boolean indicating if the cafe has a library
    """
    # Simulated data for demonstration purposes
    sample_data = {
        "The Book Nook": True,
        "Cafe Bibliotheque": True,
        "Java Junction": False,
        "Espresso Express": False,
    }

    # Generate a key for consistent hash-based lookup
    key = f"{cafe_name.lower()}_{city.lower() if city else ''}".strip("_")

    # Check if the cafe is in the sample data
    if key not in sample_data:
        raise ValueError(
            f"Cafe not found: {cafe_name} in {city if city else 'unknown city'}"
        )

    return {
        "cafe_name": cafe_name,
        "has_library": sample_data[key],
    }


from typing import Dict


def clean_table(
    table_id: str, staff_id: str, clean_complete: bool = True
) -> Dict[str, str]:
    """Cleans a table and updates its status to 'cleaned' in the booking system.

    Args:
        table_id: The unique identifier for a table.
        staff_id: The unique identifier of the staff member responsible for cleaning the table.
        clean_complete: True if the clean has been completed successfully, false otherwise.

    Returns:
        Dict containing:
            - table_id: The unique identifier for the table.
            - status: The new status of the table ('cleaned' or 'not cleaned').
            - staff_id: The unique identifier of the staff member who cleaned the table.
    """
    if not table_id or not staff_id:
        raise ValueError("Both table_id and staff_id must be provided.")

    status = "cleaned" if clean_complete else "not cleaned"

    return {"table_id": table_id, "status": status, "staff_id": staff_id}


from typing import Dict, List, Literal, Union


def create_desert(
    type: Literal[1, 2, 3],
    ingredient: Literal["D", "O", "S"],
    scoops: str,
    sprinkles: bool = False,
    cream_topper: bool = False,
    nuts: bool = False,
    sauce_flavour: Union[Literal["C", "S", "R"], bool] = False,
    chocolate_flake: int = 0,
) -> Dict[str, Union[str, int, bool, List[str]]]:
    """Create an ice cream desert with specified options.

    Args:
        type: The type of desert (1 - cone, 2 - tub, 3 - Sunday)
        ingredient: The base ingredient (D - dairy, O - oat milk, S - soya)
        scoops: Comma-separated list of flavours. One entry = 1 scoop. Max 3 scoops.
        sprinkles: Whether to add sprinkles
        cream_topper: Whether to top with whipped cream
        nuts: Whether to top with nuts
        sauce_flavour: Add sauce: C- Chocolate, S- Strawberry, R- Raspberry
        chocolate_flake: Number of flake sticks to add (0 - 2)

    Returns:
        Dict containing:
            - type: Type of desert
            - ingredient: Base ingredient
            - scoops: List of scoop flavours
            - sprinkles: Whether sprinkles are added
            - cream_topper: Whether whipped cream is added
            - nuts: Whether nuts are added
            - sauce_flavour: Sauce flavour added
            - chocolate_flake: Number of chocolate flakes added
    """
    # Validate scoops
    scoop_list = scoops.split(",")
    if len(scoop_list) > 3:
        raise ValueError("Maximum of 3 scoops allowed.")

    # Validate chocolate_flake
    if not (0 <= chocolate_flake <= 2):
        raise ValueError("Number of chocolate flakes must be between 0 and 2.")

    # Sample data generation
    desert_types = {1: "cone", 2: "tub", 3: "Sunday"}
    ingredient_types = {"D": "dairy", "O": "oat milk", "S": "soya"}
    sauce_types = {"C": "chocolate", "S": "strawberry", "R": "raspberry"}

    return {
        "type": desert_types[type],
        "ingredient": ingredient_types[ingredient],
        "scoops": scoop_list,
        "sprinkles": sprinkles,
        "cream_topper": cream_topper,
        "nuts": nuts,
        "sauce_flavour": sauce_types.get(sauce_flavour, None),
        "chocolate_flake": chocolate_flake,
    }


import hashlib
from typing import Dict, List, Union


def filter_menu(menu: str, allegens: List[str]) -> Dict[str, Union[str, List[str]]]:
    """Filter a menu to exclude items containing specified allergens.

    Args:
        menu: Raw text or URL of the cafe's menu
        allegens: List of unwanted ingredients to avoid

    Returns:
        Dict containing:
            - original_menu: Original menu text
            - filtered_items: List of menu items excluding those with allergens
    """

    # Sample menu items for demonstration purposes
    sample_menu_items = [
        "Grilled Chicken Salad",
        "Peanut Butter Sandwich",
        "Gluten-Free Pancakes",
        "Vegan Burger",
        "Seafood Pasta",
        "Chocolate Cake",
    ]

    # Hash-based generation to simulate filtering
    def contains_allergen(item: str, allergens: List[str]) -> bool:
        item_hash = hashlib.md5(item.encode()).hexdigest()
        return any(allergen.lower() in item_hash for allergen in allergens)

    filtered_items = [
        item for item in sample_menu_items if not contains_allergen(item, allegens)
    ]

    return {
        "original_menu": menu,
        "filtered_items": filtered_items,
    }


from typing import Dict, List


def find_cheapest(
    item: List[str], cafes: List[Dict[str, Dict[str, float]]]
) -> Dict[str, Union[str, float]]:
    """Find the cheapest cafe for a particular drink or food item.

    Args:
        item: List containing the name of the item user is interested in purchasing.
        cafes: List of dictionaries where each dictionary represents a cafe and contains
               item names as keys and their prices as values.

    Returns:
        Dict containing:
            - cafe: Name of the cafe with the cheapest price for the item
            - item: Name of the item
            - price: Cheapest price found for the item

    Raises:
        ValueError: If the item is not found in any of the cafes.
    """
    item_name = item[0]
    cheapest_cafe = None
    cheapest_price = float("inf")

    for cafe in cafes:
        for cafe_name, menu in cafe.items():
            if item_name in menu:
                price = menu[item_name]
                if price < cheapest_price:
                    cheapest_price = price
                    cheapest_cafe = cafe_name

    if cheapest_cafe is None:
        raise ValueError(f"Item not found in any cafe: {item_name}")

    return {"cafe": cheapest_cafe, "item": item_name, "price": cheapest_price}


from typing import Dict, List


def find_lunch_spots_at_location(location: str) -> Dict[str, List[str]]:
    """Find lunch time eateries given a location.

    Args:
        location: City or address to find lunch spots for

    Returns:
        Dict containing:
            - location: The input location
            - lunch_spots: List of lunch spots available at the location
    """
    sample_data = {
        "New York": ["Joe's Pizza", "Shake Shack", "Le Bernardin"],
        "San Francisco": ["Tartine Bakery", "The Slanted Door", "Zuni Café"],
        "Chicago": ["Portillo's", "Lou Malnati's", "Alinea"],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    return {
        "location": location,
        "lunch_spots": sample_data[location],
    }


from typing import Dict, List, Union


def find_nearby_restaurants(
    location: str, radius: float = 10, tags: Union[str, List[str]] = None
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Get the names and addresses of restaurants near a given location.

    Args:
        location: City or address about which to find restaurants.
        radius: The radius (in kilometres) within which to search from the specified location.
        tags: Tags for filtering results (e.g. ['Chinese', 'brunch']) or single tag as string.

    Returns:
        Dict containing:
            - location: The location searched
            - restaurants: List of dictionaries with restaurant names and addresses
    """
    sample_data = {
        "New York": [
            {"name": "Joe's Pizza", "address": "7 Carmine St, New York, NY 10014"},
            {
                "name": "Shake Shack",
                "address": "Madison Ave & E.23rd St, New York, NY 10010",
            },
        ],
        "San Francisco": [
            {
                "name": "Tartine Bakery",
                "address": "600 Guerrero St, San Francisco, CA 94110",
            },
            {"name": "Nopa", "address": "560 Divisadero St, San Francisco, CA 94117"},
        ],
        "Chicago": [
            {"name": "Alinea", "address": "1723 N Halsted St, Chicago, IL 60614"},
            {
                "name": "Lou Malnati's Pizzeria",
                "address": "1120 N State St, Chicago, IL 60610",
            },
        ],
        "Venice": [
            {
                "name": "Osteria alle Testiere",
                "address": "Castello 5801, 30122 Venezia VE, Italy",
            },
            {
                "name": "Antiche Carampane",
                "address": "San Polo 1911, 30125 Venezia VE, Italy",
            },
            {
                "name": "Quadri",
                "address": "Piazza San Marco 121, 30124 Venezia VE, Italy",
            },
            {
                "name": "Trattoria da Romano",
                "address": "Via Baldassarre Galuppi 221, 30142 Burano VE, Italy",
            },
            {
                "name": "Al Covo",
                "address": "Campiello de la Pescaria 3968, 30122 Venezia VE, Italy",
            },
        ],
        "Venice, Italy": [
            {
                "name": "Caffè Florian",
                "address": "Piazza San Marco 57, 30124 Venezia VE, Italy",
                "tags": ["cafe", "coffee", "vegetarian"],
            },
        ],
        "Milan": [
            {
                "name": "Trattoria Milanese",
                "address": "Via Santa Sofia 16, 20122 Milano MI, Italy",
            },
            {
                "name": "Pizzeria Da Vinci",
                "address": "Via Marco Polo 2, 20124 Milano MI, Italy",
            },
        ],
        "Split": [
            {"name": "Konoba Sv. Petar", "address": "Domina 6, 21000 Split, Croatia"},
            {
                "name": "Restaurant Grot",
                "address": "Put Sv. Dujma 1, 21000 Split, Croatia",
            },
        ],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    restaurants = sample_data[location]

    if tags:
        # Convert string to list if needed
        if isinstance(tags, str):
            tags = [tags]
        # Simulate filtering by tags
        filtered_restaurants = [
            restaurant
            for restaurant in restaurants
            if any(tag.lower() in restaurant["name"].lower() for tag in tags)
        ]
        restaurants = filtered_restaurants if filtered_restaurants else restaurants

    return {
        "location": location,
        "restaurants": restaurants,
    }


from typing import Dict, Union


def find_recipe(
    dish: str, dietary_preference: str = "none"
) -> Dict[str, Union[str, List[str]]]:
    """Find a recipe based on ingredients or dish name.

    Args:
        dish: Name of the dish or main ingredient
        dietary_preference: Dietary restrictions (e.g., 'vegetarian', 'Halal')

    Returns:
        Dict containing:
            - dish: Name of the dish
            - ingredients: List of ingredients required for the recipe
            - instructions: Step-by-step cooking instructions
    """

    recipes = {
        "spaghetti": {
            "ingredients": ["pasta", "tomato sauce", "ground beef", "parmesan"],
            "instructions": [
                "Boil pasta until al dente.",
                "Cook ground beef in a pan.",
                "Add tomato sauce to beef and simmer.",
                "Combine pasta with sauce and serve with parmesan.",
            ],
        },
        "vegetable curry": {
            "ingredients": ["mixed vegetables", "coconut milk", "curry powder", "rice"],
            "instructions": [
                "Chop vegetables and sauté in a pan.",
                "Add curry powder and stir well.",
                "Pour in coconut milk and simmer until thick.",
                "Serve with cooked rice.",
            ],
        },
        "chicken salad": {
            "ingredients": [
                "chicken breast",
                "lettuce",
                "tomatoes",
                "cucumber",
                "dressing",
            ],
            "instructions": [
                "Grill chicken breast and slice.",
                "Chop lettuce, tomatoes, and cucumber.",
                "Mix all ingredients in a bowl.",
                "Add dressing and toss before serving.",
            ],
        },
    }

    # Filter recipes based on dietary preference
    if dietary_preference == "vegetarian":
        recipes = {
            k: v
            for k, v in recipes.items()
            if "ground beef" not in v["ingredients"]
            and "chicken breast" not in v["ingredients"]
        }
    elif dietary_preference == "Halal":
        # Assuming all recipes are Halal for simplicity
        pass

    if dish not in recipes:
        raise ValueError(f"Recipe not found for dish: {dish}")

    return {
        "dish": dish,
        "ingredients": recipes[dish]["ingredients"],
        "instructions": recipes[dish]["instructions"],
    }


from typing import Dict, List, Optional


def find_restaurant(
    location: str, food_type: Optional[str] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find a restaurant near a location.

    Args:
        location: City or address to search around.
        food_type: Filter results by type of food (optional).

    Returns:
        Dict containing:
            - location: The location where the search was performed
            - restaurants: List of restaurants with:
                - name: Name of the restaurant
                - address: Address of the restaurant
                - rating: Average rating of the restaurant
                - food_type: Type of food served
    """

    sample_data = {
        "New York": [
            {
                "name": "Joe's Pizza",
                "address": "7 Carmine St",
                "rating": 4.5,
                "food_type": "Italian",
            },
            {
                "name": "Shake Shack",
                "address": "Madison Ave",
                "rating": 4.2,
                "food_type": "American",
            },
            {
                "name": "Sushi Nakazawa",
                "address": "23 Commerce St",
                "rating": 4.8,
                "food_type": "Japanese",
            },
        ],
        "San Francisco": [
            {
                "name": "Tartine Bakery",
                "address": "600 Guerrero St",
                "rating": 4.7,
                "food_type": "Bakery",
            },
            {
                "name": "La Taqueria",
                "address": "2889 Mission St",
                "rating": 4.6,
                "food_type": "Mexican",
            },
            {
                "name": "House of Prime Rib",
                "address": "1906 Van Ness Ave",
                "rating": 4.7,
                "food_type": "Steakhouse",
            },
        ],
    }

    if location not in sample_data:
        raise ValueError(f"Location not supported: {location}")

    restaurants = sample_data[location]
    if food_type:
        restaurants = [
            r for r in restaurants if r["food_type"].lower() == food_type.lower()
        ]

    return {
        "location": location,
        "restaurants": restaurants,
    }


from typing import Dict, List, Union


def find_restaurants_near_venue(
    venue_id: str,
    time_window: Dict[str, str] = None,
    party_size: int = None,
    cuisine: List[str] = None,
    only_walkable: bool = None,
    open_now: bool = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]:
    """Discover restaurants near a venue, filtered by time window, cuisine, and walkability.

    Args:
        venue_id: Venue to search around
        time_window: Desired dining time window (24h HH:MM)
        party_size: Number of diners (integer)
        cuisine: Cuisine tags, e.g., ['italian', 'mexican', 'vegan']
        only_walkable: Restrict to walking-distance options
        open_now: Only include restaurants open right now

    Returns:
        Dict containing:
            - venue_id: The ID of the venue
            - restaurants: List of restaurants with details such as name, cuisine, distance, and availability
    """
    if not venue_id:
        raise ValueError("venue_id is required")

    # Simulated sample data
    sample_restaurants = [
        {
            "name": "Pasta Palace",
            "cuisine": "italian",
            "distance": 0.3,
            "availability": "12:00-22:00",
        },
        {
            "name": "Taco Town",
            "cuisine": "mexican",
            "distance": 0.5,
            "availability": "11:00-23:00",
        },
        {
            "name": "Green Garden",
            "cuisine": "vegan",
            "distance": 0.2,
            "availability": "10:00-20:00",
        },
    ]

    # Filter by cuisine
    if cuisine:
        sample_restaurants = [r for r in sample_restaurants if r["cuisine"] in cuisine]

    # Filter by walkability
    if only_walkable:
        sample_restaurants = [r for r in sample_restaurants if r["distance"] <= 0.5]

    # Filter by open now
    if open_now:
        current_time = "14:00"  # Simulated current time
        sample_restaurants = [
            r
            for r in sample_restaurants
            if r["availability"].split("-")[0]
            <= current_time
            <= r["availability"].split("-")[1]
        ]

    # Filter by time window
    if time_window:
        start_time, end_time = time_window["start_time"], time_window["end_time"]
        sample_restaurants = [
            r
            for r in sample_restaurants
            if start_time <= r["availability"].split("-")[0]
            and end_time >= r["availability"].split("-")[1]
        ]

    return {
        "venue_id": venue_id,
        "restaurants": sample_restaurants,
    }


from typing import Dict, List


def get_beverages_menu() -> Dict[str, List[str]]:
    """Get the available beverages menu.

    Returns:
        Dict containing:
            - hot: List of available hot beverages
            - cold: List of available cold beverages
    """

    return {
        "hot": ["Coffee", "Tea", "Hot Chocolate", "Espresso"],
        "cold": ["Iced Coffee", "Lemonade", "Iced Tea", "Smoothie"],
    }


from typing import Dict, Union


def get_calories(meal_name: str, servings: float = 1) -> Dict[str, Union[str, float]]:
    """Retrieve the number of calories in a meal.

    Args:
        meal_name: Name of the meal (e.g., 'Spaghetti Bolognese', 'Caesar Salad')
        servings: Number of servings (default is 1)

    Returns:
        Dict containing:
            - meal_name: Name of the meal
            - calories_per_serving: Calories in one serving of the meal
            - total_calories: Total calories based on the number of servings
    """

    sample_calories = {
        "Spaghetti Bolognese": 350,
        "Caesar Salad": 150,
        "Grilled Chicken": 220,
        "Vegetable Stir Fry": 180,
        "Porridge": 200,
        "2 eggs": 150,
        "2 slices sourdough with butter": 350,
        "Big Mac": 550,
        "Fries": 350,
    }

    if meal_name not in sample_calories:
        raise ValueError(f"Meal not supported: {meal_name}")

    calories_per_serving = sample_calories[meal_name]
    total_calories = calories_per_serving * servings

    return {
        "meal_name": meal_name,
        "calories_per_serving": calories_per_serving,
        "total_calories": total_calories,
    }


from typing import Dict, Union


def get_cals(
    prod_name: Union[str, None] = None, barcode: Union[str, None] = None
) -> Dict[str, Union[str, int]]:
    """Retrieve calorific content for a given product.

    Args:
        prod_name: A general or specific product name to look up
        barcode: Unique product id scanned from barcode

    Returns:
        Dict containing:
            - product: Name of the product
            - calories: Calorific content of the product in kcal

    Raises:
        ValueError: If neither prod_name nor barcode is provided or if the product is not found.
    """

    if not prod_name and not barcode:
        raise ValueError("Either 'prod_name' or 'barcode' must be provided.")

    # Sample data for demonstration purposes
    sample_data = {
        "apple": 52,
        "banana": 89,
        "chocolate_bar": 230,
        "milk": 42,
        "bread": 265,
        "123456789012": 52,  # barcode for apple
        "987654321098": 89,  # barcode for banana
    }

    # Determine the key to use for lookup
    key = prod_name if prod_name else barcode

    if key not in sample_data:
        raise ValueError(f"Product not found: {key}")

    # Return the calorific content for the product
    return {
        "product": key,
        "calories": sample_data[key],
    }


from typing import Dict, Union


def get_carbs(meal_name: str, servings: float = 1) -> Dict[str, Union[str, float]]:
    """Retrieve the number of grams of carbohydrates in a meal.

    Args:
        meal_name: Name of the meal (e.g., 'pasta', 'salad')
        servings: Number of servings

    Returns:
        Dict containing:
            - meal_name: Name of the meal
            - servings: Number of servings
            - carbohydrates: Total grams of carbohydrates
    """
    sample_carbs = {
        "pasta": 75,
        "salad": 15,
        "burger": 40,
        "pizza": 80,
        "sushi": 30,
        "porridge": 35,
        "2 eggs": 1,
        "sourdough with butter": 45,
        "Big Mac": 46,
        "Fries": 45,
    }

    if meal_name not in sample_carbs:
        raise ValueError(f"Meal not supported: {meal_name}")

    carbs_per_serving = sample_carbs[meal_name]
    total_carbs = carbs_per_serving * servings

    return {
        "meal_name": meal_name,
        "servings": servings,
        "carbohydrates": total_carbs,
    }


from typing import Dict, List


def get_daily_specials_menu() -> Dict[str, List[str]]:
    """Get the daily specials menu for a restaurant.

    Returns:
        Dict containing:
            - day: List of special dishes available on that day
    """
    sample_menu = {
        "Monday": ["Grilled Salmon", "Caesar Salad", "Tomato Soup"],
        "Tuesday": ["Taco Platter", "Chicken Quesadilla", "Churros"],
        "Wednesday": ["Beef Stroganoff", "Garlic Bread", "Minestrone Soup"],
        "Thursday": ["BBQ Ribs", "Coleslaw", "Cornbread"],
        "Friday": ["Fish and Chips", "Mushy Peas", "Tartar Sauce"],
        "Saturday": ["Pasta Primavera", "Bruschetta", "Tiramisu"],
        "Sunday": ["Roast Chicken", "Mashed Potatoes", "Apple Pie"],
    }

    return sample_menu


import hashlib
from datetime import datetime, timedelta
from typing import Dict


def get_delivery_eta(
    restaurant_name: str, delivery_address: str, order_datetime_iso: str
) -> Dict[str, str]:
    """Estimate delivery arrival time for a specific restaurant to a given address.

    Args:
        restaurant_name: Exact restaurant name as displayed to the user
        delivery_address: Full delivery address or area/landmark
        order_datetime_iso: Planned order datetime in ISO 8601 (e.g., '2025-08-12T19:05:00+05:30')

    Returns:
        Dict containing:
            - restaurant_name: Name of the restaurant
            - delivery_address: Delivery address
            - estimated_arrival: Estimated delivery arrival time in ISO 8601 format
    """
    try:
        order_datetime = datetime.fromisoformat(order_datetime_iso)
    except ValueError:
        raise ValueError("Invalid ISO 8601 datetime format")

    # Generate a consistent but varied delivery time based on restaurant and address
    hash_input = f"{restaurant_name}{delivery_address}".encode()
    hash_digest = hashlib.sha256(hash_input).hexdigest()
    delivery_minutes = (
        int(hash_digest[:2], 16) % 60 + 20
    )  # Random delivery time between 20 and 79 minutes

    estimated_arrival = order_datetime + timedelta(minutes=delivery_minutes)

    return {
        "restaurant_name": restaurant_name,
        "delivery_address": delivery_address,
        "estimated_arrival": estimated_arrival.isoformat(),
    }


from typing import Dict, Literal


def get_espresso_grind(roast: str, is_ground: bool) -> Dict[str, str]:
    """Select a grind size for espresso given some bean properties.

    Args:
        roast: Roast level of beans (e.g. 'light', 'medium', 'dark')
        is_ground: Are the beans pre-ground

    Returns:
        Dict containing:
            - grind_size: Recommended grind size for espresso
            - note: Additional note regarding the grind
    """
    if is_ground:
        raise ValueError("Cannot select grind size for pre-ground beans")

    roast_to_grind = {
        "light": "fine",
        "medium": "medium-fine",
        "dark": "fine",
    }

    if roast not in roast_to_grind:
        raise ValueError(f"Unsupported roast level: {roast}")

    return {
        "grind_size": roast_to_grind[roast],
        "note": "Adjust grind size based on personal taste preference",
    }


from typing import Dict, Literal


def get_espresso_weight(origin: str, process: str) -> Dict[str, Union[str, int]]:
    """Select an end weight for espresso given some coffee properties.

    Args:
        origin: Country of origin of beans (e.g. 'Ethiopia', 'Colombia')
        process: Coffee process of beans (e.g. 'washed', 'natural')

    Returns:
        Dict containing:
            - origin: Country of origin of beans
            - process: Coffee process of beans
            - end_weight: Recommended end weight for espresso in grams
    """

    sample_weights = {
        ("Ethiopia", "washed"): 36,
        ("Ethiopia", "natural"): 38,
        ("Colombia", "washed"): 40,
        ("Colombia", "natural"): 42,
    }

    key = (origin, process)
    if key not in sample_weights:
        raise ValueError(f"Combination not supported: {origin}, {process}")

    return {
        "origin": origin,
        "process": process,
        "end_weight": sample_weights[key],
    }


from typing import Dict, List, Union


def get_flavours(preferences: Union[str, None] = None) -> Dict[str, List[str]]:
    """Gets an array of available flavours, optionally sorted by preferences.

    Args:
        preferences: Optional keywords used to sort preferred flavours to top of results

    Returns:
        Dict containing:
            - flavours: List of available flavours, sorted by preferences if provided
    """

    available_flavours = [
        "vanilla",
        "chocolate",
        "strawberry",
        "mint",
        "cookie dough",
        "pistachio",
        "caramel",
        "coffee",
    ]

    if preferences:
        sorted_flavours = sorted(
            available_flavours,
            key=lambda flavour: (preferences.lower() not in flavour.lower(), flavour),
        )
    else:
        sorted_flavours = available_flavours

    return {"flavours": sorted_flavours}


from typing import Dict, List, Union


def get_guest_details(guest_name: str) -> Dict[str, Union[str, List[str]]]:
    """Retrieve all details known about a given guest, including dietary restrictions.

    Args:
        guest_name: Name of the guest to lookup

    Returns:
        Dict containing:
            - guest_name: Name of the guest
            - dietary_restrictions: List of dietary restrictions for the guest
    """

    guest_data = {
        "Alice Johnson": ["vegetarian", "gluten-free"],
        "Bob Smith": ["vegan"],
        "Charlie Brown": ["nut allergy"],
    }

    if guest_name not in guest_data:
        raise ValueError(f"Guest not found: {guest_name}")

    return {
        "guest_name": guest_name,
        "dietary_restrictions": guest_data[guest_name],
    }


from typing import Dict, List, Union


def get_ingr(
    prod_name: Union[str, None] = None, barcode: Union[str, None] = None
) -> Dict[str, Union[str, List[str]]]:
    """Retrieve ingredient list for a given product.

    Args:
        prod_name: A general or specific product name to look up.
        barcode: Unique product id scanned from barcode.

    Returns:
        Dict containing:
            - product: Name of the product
            - ingredients: List of ingredients for the product
    """

    if prod_name is None and barcode is None:
        raise ValueError("Either 'prod_name' or 'barcode' must be provided.")

    # Sample data for demonstration purposes
    sample_data = {
        "123456789012": {
            "product": "Chocolate Bar",
            "ingredients": ["Sugar", "Cocoa Butter", "Milk", "Cocoa Mass"],
        },
        "987654321098": {
            "product": "Orange Juice",
            "ingredients": ["Water", "Orange Concentrate", "Sugar"],
        },
        "Chocolate Bar": {
            "product": "Chocolate Bar",
            "ingredients": ["Sugar", "Cocoa Butter", "Milk", "Cocoa Mass"],
        },
        "Orange Juice": {
            "product": "Orange Juice",
            "ingredients": ["Water", "Orange Concentrate", "Sugar"],
        },
    }

    key = barcode if barcode else prod_name
    if key not in sample_data:
        raise ValueError(f"Product not found for given identifier: {key}")

    return sample_data[key]


from typing import Dict, List, Optional


def get_inventory(
    category: Optional[str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Retrieve ingredient inventory based on category.

    Args:
        category: Ingredient category to filter by (e.g. 'fruits', 'vegetables')

    Returns:
        Dict containing:
            - category: The category of ingredients requested
            - items: List of dictionaries with ingredient details:
                - name: Name of the ingredient
                - quantity: Quantity available in stock
    """

    inventory = {
        "fruits": [
            {"name": "apple", "quantity": 50},
            {"name": "banana", "quantity": 30},
        ],
        "vegetables": [
            {"name": "carrot", "quantity": 100},
            {"name": "broccoli", "quantity": 75},
        ],
        "dairy": [
            {"name": "milk", "quantity": 200},
            {"name": "cheese", "quantity": 40},
        ],
    }

    if category:
        if category not in inventory:
            raise ValueError(f"Category not supported: {category}")
        return {
            "category": category,
            "items": inventory[category],
        }

    # If no category is specified, return all items
    all_items = [item for items in inventory.values() for item in items]
    return {
        "category": "all",
        "items": all_items,
    }


from typing import Dict, List


def get_meals_menu() -> Dict[str, List[str]]:
    """Get the daily meals menu.

    Returns:
        Dict containing:
            - breakfast: List of breakfast items
            - lunch: List of lunch items
            - dinner: List of dinner items
    """
    sample_menu = {
        "breakfast": ["Pancakes", "Omelette", "Fruit Salad"],
        "lunch": ["Grilled Chicken Sandwich", "Caesar Salad", "Tomato Soup"],
        "dinner": ["Spaghetti Bolognese", "Garlic Bread", "Mixed Vegetables"],
    }

    return sample_menu


from typing import Dict, List


def get_menu_item_ingredients(menu_item: str) -> Dict[str, List[str]]:
    """Retrieve the ingredient list for a given menu item.

    Args:
        menu_item: Menu item to get ingredient list for

    Returns:
        Dict containing:
            - menu_item: The name of the menu item
            - ingredients: List of ingredients for the menu item
    """

    menu_database = {
        "Margherita Pizza": ["tomato sauce", "mozzarella cheese", "basil", "olive oil"],
        "Caesar Salad": [
            "romaine lettuce",
            "croutons",
            "parmesan cheese",
            "Caesar dressing",
        ],
        "Spaghetti Carbonara": [
            "spaghetti",
            "eggs",
            "parmesan cheese",
            "pancetta",
            "black pepper",
        ],
        "Chicken Tacos": [
            "chicken breast",
            "taco shells",
            "lettuce",
            "tomato",
            "cheddar cheese",
            "sour cream",
        ],
        "Vegan Burger": [
            "vegan patty",
            "lettuce",
            "tomato",
            "vegan cheese",
            "burger bun",
        ],
    }

    if menu_item not in menu_database:
        raise ValueError(f"Menu item not found: {menu_item}")

    return {
        "menu_item": menu_item,
        "ingredients": menu_database[menu_item],
    }


from typing import Dict, List, Optional


def get_menu_items(
    dietary_restriction: Optional[str] = None, include_secret_menu: bool = False
) -> Dict[str, List[str]]:
    """Retrieve a list of all menu items.

    Args:
        dietary_restriction: Filter results to menu_items that are safe for a dietary restriction (e.g. 'vegan', 'gluten-free')
        include_secret_menu: Include items from the secret menu

    Returns:
        Dict containing:
            - menu_items: List of menu item names
    """
    all_menu_items = {
        "vegan": ["Vegan Burger", "Vegan Salad"],
        "gluten-free": ["Gluten-Free Pizza", "Gluten-Free Pasta"],
        "vegetarian": ["Vegetarian Sandwich", "Vegetarian Soup"],
        "secret": ["Secret Nachos", "Secret Smoothie"],
    }

    if dietary_restriction and dietary_restriction not in all_menu_items:
        raise ValueError(f"Dietary restriction not supported: {dietary_restriction}")

    menu_items = []
    if dietary_restriction:
        menu_items.extend(all_menu_items[dietary_restriction])
    else:
        for key in all_menu_items:
            if key != "secret":
                menu_items.extend(all_menu_items[key])

    if include_secret_menu:
        menu_items.extend(all_menu_items["secret"])

    return {"menu_items": menu_items}


from typing import Dict, Union


def get_nuts(
    prod_name: Union[str, None] = None, barcode: Union[str, None] = None
) -> Dict[str, Union[str, float, Dict[str, float]]]:
    """Retrieve nutrients for a given food product by name or barcode.

    Args:
        prod_name: A general or specific product name to look up.
        barcode: Unique product id scanned from barcode.

    Returns:
        Dict containing:
            - product: Name of the product
            - barcode: Barcode of the product
            - nutrients: Dictionary of nutrient names and their values in grams

    Raises:
        ValueError: If neither prod_name nor barcode is provided or if the product is not found.
    """

    if not prod_name and not barcode:
        raise ValueError("Either 'prod_name' or 'barcode' must be provided.")

    # Simulated database of products with nutrients
    sample_data = {
        "123456789012": {
            "product": "Apple",
            "barcode": "123456789012",
            "nutrients": {
                "calories": 52.0,
                "protein": 0.3,
                "fat": 0.2,
                "carbohydrates": 14.0,
                "fiber": 2.4,
            },
        },
        "987654321098": {
            "product": "Banana",
            "barcode": "987654321098",
            "nutrients": {
                "calories": 89.0,
                "protein": 1.1,
                "fat": 0.3,
                "carbohydrates": 23.0,
                "fiber": 2.6,
            },
        },
        "Orange": {
            "product": "Orange",
            "barcode": "112233445566",
            "nutrients": {
                "calories": 47.0,
                "protein": 0.9,
                "fat": 0.1,
                "carbohydrates": 12.0,
                "fiber": 2.4,
            },
        },
    }

    # Determine the key to search by
    key = barcode if barcode else prod_name

    # Search for the product in the sample data
    product_info = sample_data.get(key) or next(
        (v for k, v in sample_data.items() if v["product"] == prod_name), None
    )

    if not product_info:
        raise ValueError(
            f"Product not found for {'barcode' if barcode else 'prod_name'}: {key}"
        )

    return product_info


from typing import Dict, Union


def get_price_level(
    restaurant_id: str, currency: str = "USD"
) -> Dict[str, Union[str, int]]:
    """Returns the price level or cost range for a specific restaurant.

    Args:
        restaurant_id: Unique identifier for the restaurant, such as a database ID or an external service ID.
        currency: Currency code for the returned price, in ISO 4217 format (e.g., 'USD', 'EUR').

    Returns:
        Dict containing:
            - restaurant_id: The unique identifier for the restaurant
            - price_level: An integer representing the price level (1 to 5)
            - currency: The currency code used for the price level
    """
    # Simulated hash-based price level generation for consistency
    hash_value = sum(ord(char) for char in restaurant_id) % 5 + 1

    if currency not in ["USD", "EUR", "GBP"]:
        raise ValueError(f"Currency not supported: {currency}")

    return {
        "restaurant_id": restaurant_id,
        "price_level": hash_value,
        "currency": currency,
    }


from typing import Dict, Union


def get_protein(meal_name: str, servings: float = 1) -> Dict[str, Union[str, float]]:
    """Retrieve number of grams of protein in a meal.

    Args:
        meal_name: Name of the meal (e.g., 'chicken salad', 'beef stew')
        servings: Number of servings

    Returns:
        Dict containing:
            - meal_name: Name of the meal
            - protein_per_serving: Protein content per serving in grams
            - total_protein: Total protein content for the given servings in grams
    """

    # Sample protein data per serving for different meals
    protein_data = {
        "chicken salad": 30.0,
        "beef stew": 40.0,
        "vegetable stir fry": 15.0,
        "tofu curry": 20.0,
        "pasta primavera": 12.0,
        "porridge": 8,
        "2 eggs": 13,
        "sourdough with butter": 9,
        "Big Mac": 25,
        "Fries": 4,
    }

    if meal_name not in protein_data:
        raise ValueError(f"Meal not supported: {meal_name}")

    protein_per_serving = protein_data[meal_name]
    total_protein = protein_per_serving * servings

    return {
        "meal_name": meal_name,
        "protein_per_serving": protein_per_serving,
        "total_protein": total_protein,
    }


from typing import Dict, List, Union


def get_pubs(
    loc: str,
    clo_time: str = "24:00",
    op_time: str = "16:00",
    food: bool = None,
    mus: bool = None,
) -> List[Dict[str, Union[str, bool]]]:
    """Returns a list of pubs that match the description.

    Args:
        loc: Location of the pub.
        clo_time: Closing time of the pub.
        op_time: Opening time of the pub.
        food: Filters whether the pub serves food or not.
        mus: Filters whether the pub has live music or not.

    Returns:
        List of dictionaries, each containing:
            - name: Name of the pub
            - location: Location of the pub
            - opening_time: Opening time of the pub
            - closing_time: Closing time of the pub
            - serves_food: Whether the pub serves food
            - live_music: Whether the pub has live music
    """

    sample_pubs = [
        {
            "name": "The Happy Pint",
            "location": "Downtown",
            "opening_time": "15:00",
            "closing_time": "23:00",
            "serves_food": True,
            "live_music": False,
        },
        {
            "name": "The Quiet Corner",
            "location": "Uptown",
            "opening_time": "16:00",
            "closing_time": "24:00",
            "serves_food": False,
            "live_music": False,
        },
        {
            "name": "Rock & Brew",
            "location": "Downtown",
            "opening_time": "17:00",
            "closing_time": "02:00",
            "serves_food": True,
            "live_music": True,
        },
    ]

    if not loc:
        raise ValueError("Location must be specified")

    filtered_pubs = [
        pub
        for pub in sample_pubs
        if pub["location"] == loc
        and pub["closing_time"] <= clo_time
        and pub["opening_time"] >= op_time
        and (food is None or pub["serves_food"] == food)
        and (mus is None or pub["live_music"] == mus)
    ]

    return filtered_pubs


from typing import Dict


def get_recipe(name: str) -> Dict[str, str]:
    """Retrieve the full text of a recipe.

    Args:
        name: Name of the recipe to retrieve (e.g. 'Pancakes', 'Spaghetti Bolognese')

    Returns:
        Dict containing:
            - name: Name of the recipe
            - ingredients: List of ingredients required for the recipe
            - instructions: Step-by-step instructions to prepare the dish
    """

    sample_recipes = {
        "Pancakes": {
            "ingredients": "2 cups all-purpose flour, 2 tablespoons sugar, 2 teaspoons baking powder, 1/2 teaspoon salt, 2 eggs, 1 1/2 cups milk, 1/4 cup melted butter",
            "instructions": "1. In a large bowl, whisk together the flour, sugar, baking powder, and salt. 2. In another bowl, beat the eggs and then whisk in the milk and melted butter. 3. Pour the wet ingredients into the dry ingredients and stir until just combined. 4. Heat a non-stick skillet over medium heat and pour 1/4 cup of batter for each pancake. 5. Cook until bubbles form on the surface, then flip and cook until golden brown. Serve warm.",
        },
        "Spaghetti Bolognese": {
            "ingredients": "400g spaghetti, 2 tablespoons olive oil, 1 onion, chopped, 2 garlic cloves, minced, 500g minced beef, 800g canned tomatoes, 2 tablespoons tomato paste, 1 teaspoon dried oregano, salt and pepper to taste",
            "instructions": "1. Cook the spaghetti according to package instructions. 2. In a large pan, heat the olive oil over medium heat. Add the onion and garlic, and sauté until soft. 3. Add the minced beef and cook until browned. 4. Stir in the canned tomatoes, tomato paste, oregano, salt, and pepper. Simmer for 20 minutes. 5. Serve the sauce over the cooked spaghetti.",
        },
    }

    if name not in sample_recipes:
        raise ValueError(f"Recipe not found: {name}")

    return {
        "name": name,
        "ingredients": sample_recipes[name]["ingredients"],
        "instructions": sample_recipes[name]["instructions"],
    }


from typing import Dict, List, Literal


def get_recipes(
    type: Literal["cake", "cookie", "candy", "chocolate"]
) -> Dict[str, List[str]]:
    """Gets all the recipes of a given type.

    Args:
        type: Recipe type (cake/cookie/candy/chocolate).

    Returns:
        Dict containing:
            - type: The type of recipes requested
            - recipes: List of recipe names for the given type
    """

    sample_recipes = {
        "cake": ["Chocolate Cake", "Vanilla Sponge Cake", "Red Velvet Cake"],
        "cookie": [
            "Chocolate Chip Cookie",
            "Oatmeal Raisin Cookie",
            "Peanut Butter Cookie",
        ],
        "candy": ["Gummy Bears", "Caramel Toffee", "Lollipop"],
        "chocolate": [
            "Dark Chocolate Truffles",
            "Milk Chocolate Bar",
            "White Chocolate Bark",
        ],
    }

    if type not in sample_recipes:
        raise ValueError(f"Recipe type not supported: {type}")

    return {
        "type": type,
        "recipes": sample_recipes[type],
    }


from typing import Dict, List


def get_refreshments(city: str) -> Dict[str, List[str]]:
    """Returns a list of venues in a given city that offer refreshments such as water or soda.

    Args:
        city: The city to search for venues (e.g. 'New York', 'Los Angeles')

    Returns:
        Dict containing:
            - city: City name
            - venues: List of venue names offering refreshments
    """

    sample_data = {
        "New York": [
            "Central Park Kiosk",
            "Times Square Cafe",
            "Brooklyn Bridge Stand",
        ],
        "Los Angeles": [
            "Santa Monica Pier Refreshments",
            "Hollywood Snack Bar",
            "Venice Beach Drinks",
        ],
        "Chicago": ["Millennium Park Cafe", "Navy Pier Refreshments", "The Bean Kiosk"],
        "Berlin": [
            "Café Anna Blume",
            "House of Small Wonders",
            "Café Winterfeldt Schokoladen",
        ],
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    return {
        "city": city,
        "venues": sample_data.get(city, []),
    }


from typing import Dict, Union


def get_res_dishes(
    restaurant_id: str, cuisine_type: str
) -> Dict[str, Union[str, bool]]:
    """Check if the restaurant offers a specific type of cuisine.

    Args:
        restaurant_id: The unique identifier for the restaurant
        cuisine_type: The type of cuisine to check for, e.g., 'seafood'

    Returns:
        Dict containing:
            - restaurant_id: The unique identifier for the restaurant
            - offers_cuisine: Boolean indicating if the restaurant offers the specified cuisine
    """

    # Simulated database of restaurants and their offered cuisines
    restaurant_data = {
        "res_001": ["seafood", "italian", "mexican"],
        "res_002": ["chinese", "thai"],
        "res_003": ["seafood", "french"],
    }

    if restaurant_id not in restaurant_data:
        raise ValueError(f"Restaurant ID not found: {restaurant_id}")

    offers_cuisine = cuisine_type.lower() in restaurant_data[restaurant_id]

    return {"restaurant_id": restaurant_id, "offers_cuisine": offers_cuisine}


from typing import Dict, List


def get_reservation_list(service: str) -> Dict[str, List[str]]:
    """Retrieve a list of all guests with reservations for a given service.

    Args:
        service: Service to get reservations for (e.g. 'spa', 'restaurant')

    Returns:
        Dict containing:
            - service: Name of the service
            - guests: List of guest names with reservations
    """

    sample_reservations = {
        "spa": ["Alice Johnson", "Bob Smith", "Charlie Brown"],
        "restaurant": ["David Wilson", "Eve Davis", "Frank Miller"],
        "gym": ["Grace Lee", "Hannah King", "Ian Scott"],
    }

    if service not in sample_reservations:
        raise ValueError(f"Service not supported: {service}")

    return {
        "service": service,
        "guests": sample_reservations.get(service, []),
    }


from typing import Dict, List, Optional, Union


def get_restaurants(
    name: Optional[str] = None,
    cuisine: Optional[str] = None,
    opening_time: Optional[str] = None,
    closing_time: Optional[str] = None,
    rating: Optional[float] = None,
) -> List[Dict[str, Union[str, float]]]:
    """Retrieve local restaurants based on optional filters.

    Args:
        name: Name of the restaurant to filter by.
        cuisine: Type of cuisine to filter by.
        opening_time: Opening time to filter by (e.g. '09:00').
        closing_time: Closing time to filter by (e.g. '22:00').
        rating: Minimum rating to filter by.

    Returns:
        List of dictionaries, each containing:
            - name: Name of the restaurant
            - cuisine: Type of cuisine
            - opening_time: Opening time
            - closing_time: Closing time
            - rating: Rating out of 5
    """

    sample_restaurants = [
        {
            "name": "Pasta Palace",
            "cuisine": "Italian",
            "opening_time": "11:00",
            "closing_time": "23:00",
            "rating": 4.5,
        },
        {
            "name": "Sushi Central",
            "cuisine": "Japanese",
            "opening_time": "12:00",
            "closing_time": "22:00",
            "rating": 4.7,
        },
        {
            "name": "Burger Barn",
            "cuisine": "American",
            "opening_time": "10:00",
            "closing_time": "21:00",
            "rating": 4.2,
        },
        {
            "name": "Curry Corner",
            "cuisine": "Indian",
            "opening_time": "11:30",
            "closing_time": "22:30",
            "rating": 4.6,
        },
        {
            "name": "Taco Town",
            "cuisine": "Mexican",
            "opening_time": "09:00",
            "closing_time": "20:00",
            "rating": 4.3,
        },
    ]

    def matches_filters(restaurant: Dict[str, Union[str, float]]) -> bool:
        if name and name.lower() not in restaurant["name"].lower():
            return False
        if cuisine and cuisine.lower() != restaurant["cuisine"].lower():
            return False
        if opening_time and opening_time != restaurant["opening_time"]:
            return False
        if closing_time and closing_time != restaurant["closing_time"]:
            return False
        if rating and restaurant["rating"] < rating:
            return False
        return True

    return [
        restaurant for restaurant in sample_restaurants if matches_filters(restaurant)
    ]


from typing import Dict, Union


def get_step(name: str, step: int = 1) -> Dict[str, Union[str, int]]:
    """Retrieve a specific step from a recipe.

    Args:
        name: The name of the recipe to retrieve the step from.
        step: The step number to retrieve (default is 1).

    Returns:
        Dict containing:
            - name: The name of the recipe
            - step: The step number
            - instruction: The instruction for the specified step

    Raises:
        ValueError: If the recipe name is not supported or the step number is invalid.
    """

    recipes = {
        "Pancakes": [
            "Mix flour, sugar, baking powder, and salt.",
            "Whisk in milk, eggs, and melted butter.",
            "Pour batter onto a hot griddle.",
            "Cook until bubbles form, then flip and cook until golden.",
        ],
        "Spaghetti Bolognese": [
            "Heat oil in a pan and cook onions until soft.",
            "Add minced beef and cook until browned.",
            "Stir in tomato sauce and simmer for 20 minutes.",
            "Serve over cooked spaghetti.",
        ],
        "Caesar Salad": [
            "Chop lettuce and place in a bowl.",
            "Add croutons and grated parmesan cheese.",
            "Toss with Caesar dressing.",
            "Top with grilled chicken slices.",
        ],
    }

    if name not in recipes:
        raise ValueError(f"Recipe not supported: {name}")

    if step < 1 or step > len(recipes[name]):
        raise ValueError(f"Invalid step number: {step} for recipe {name}")

    return {"name": name, "step": step, "instruction": recipes[name][step - 1]}


from typing import Dict, List


def gluten_free_cafes(city: str) -> Dict[str, List[str]]:
    """Search for cafes with gluten-free options in a specified city.

    Args:
        city: Name of the city to search for cafes (e.g. 'San Francisco', 'Berlin')

    Returns:
        Dict containing:
            - city: City name
            - cafes: List of cafes with gluten-free options
    """

    sample_data = {
        "San Francisco": [
            "Cafe Gratitude",
            "The Plant Cafe Organic",
            "KitTea Cat Lounge",
        ],
        "Berlin": ["Brammibal's Donuts", "No Milk Today", "Goodies Berlin"],
        "New York": ["By the Way Bakery", "The Little Beet", "Hu Kitchen"],
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    return {
        "city": city,
        "cafes": sample_data.get(city, []),
    }


from typing import Dict, List


def map_dietary_restrictions_to_unsafe_ingredients(
    dietary_restriction: str,
) -> Dict[str, Union[str, List[str]]]:
    """Find which ingredients are unsafe for a given dietary restriction.

    Args:
        dietary_restriction: Dietary restriction for which to list unsafe ingredients

    Returns:
        Dict containing:
            - dietary_restriction: The dietary restriction queried
            - unsafe_ingredients: List of ingredients that are unsafe for the given restriction
    """

    restriction_to_ingredients = {
        "vegan": ["meat", "dairy", "eggs", "honey"],
        "vegetarian": ["meat", "fish", "poultry"],
        "gluten-free": ["wheat", "barley", "rye"],
        "nut-free": ["almonds", "walnuts", "peanuts"],
        "dairy-free": ["milk", "cheese", "butter"],
    }

    if dietary_restriction not in restriction_to_ingredients:
        raise ValueError(f"Dietary restriction not supported: {dietary_restriction}")

    return {
        "dietary_restriction": dietary_restriction,
        "unsafe_ingredients": restriction_to_ingredients[dietary_restriction],
    }


from typing import Dict, List, Union


def near_restaurants(
    city: str, is_open: Union[str, None] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Find nearby places to eat in a specified city.

    Args:
        city: The city where the festival takes place (e.g. 'New York', 'Los Angeles')
        is_open: The hour of when they want to eat, formatted as 'HH:MM' (24-hour format)

    Returns:
        Dict containing:
            - city: The city name
            - restaurants: List of dictionaries with restaurant details:
                - name: Name of the restaurant
                - cuisine: Type of cuisine offered
                - open_hour: Opening hour in 'HH:MM' format
                - close_hour: Closing hour in 'HH:MM' format
    """

    sample_data = {
        "New York": [
            {
                "name": "Joe's Pizza",
                "cuisine": "Italian",
                "open_hour": "11:00",
                "close_hour": "23:00",
            },
            {
                "name": "Shake Shack",
                "cuisine": "American",
                "open_hour": "10:00",
                "close_hour": "22:00",
            },
            {
                "name": "Sushi Nakazawa",
                "cuisine": "Japanese",
                "open_hour": "12:00",
                "close_hour": "22:00",
            },
        ],
        "Los Angeles": [
            {
                "name": "In-N-Out Burger",
                "cuisine": "American",
                "open_hour": "10:30",
                "close_hour": "01:00",
            },
            {
                "name": "Guelaguetza",
                "cuisine": "Mexican",
                "open_hour": "11:00",
                "close_hour": "22:00",
            },
            {
                "name": "Bestia",
                "cuisine": "Italian",
                "open_hour": "17:00",
                "close_hour": "23:00",
            },
        ],
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    restaurants = sample_data[city]

    if is_open:
        hour, minute = map(int, is_open.split(":"))
        is_open_minutes = hour * 60 + minute
        restaurants = [
            r
            for r in restaurants
            if int(r["open_hour"].split(":")[0]) * 60
            + int(r["open_hour"].split(":")[1])
            <= is_open_minutes
            <= int(r["close_hour"].split(":")[0]) * 60
            + int(r["close_hour"].split(":")[1])
        ]

    return {"city": city, "restaurants": restaurants}


from typing import Dict, Literal


def order_burger(
    size: Literal["S", "M", "L"] = "M", fries: bool = False, drink: bool = False
) -> Dict[str, Union[str, bool, float]]:
    """Place an order for a burger meal.

    Args:
        size: What size the burger is ('S', 'M', 'L')
        fries: Whether fries are ordered as well
        drink: Whether a drink is ordered as well

    Returns:
        Dict containing:
            - size: Size of the burger
            - fries: Whether fries are included
            - drink: Whether a drink is included
            - total_price: Total price of the meal
    """

    # Mock pricing data
    size_prices = {"S": 5.0, "M": 7.0, "L": 9.0}
    fries_price = 2.0
    drink_price = 1.5

    if size not in size_prices:
        raise ValueError(f"Unsupported size: {size}")

    total_price = size_prices[size]
    if fries:
        total_price += fries_price
    if drink:
        total_price += drink_price

    return {"size": size, "fries": fries, "drink": drink, "total_price": total_price}


from typing import Dict


def order_chinese(order: str) -> Dict[str, str]:
    """Places an order for Chinese takeaway.

    Args:
        order: The chosen menu item to order (e.g. 'Kung Pao Chicken', 'Sweet and Sour Pork')

    Returns:
        Dict containing:
            - order: The name of the ordered item
            - status: The status of the order
            - estimated_time: Estimated time for delivery
    """

    menu = {
        "Kung Pao Chicken": "available",
        "Sweet and Sour Pork": "available",
        "Spring Rolls": "unavailable",
        "Fried Rice": "available",
    }

    if order not in menu:
        raise ValueError(f"Order item not on menu: {order}")

    if menu[order] == "unavailable":
        return {
            "order": order,
            "status": "unavailable",
            "estimated_time": "N/A",
        }

    # Simulate estimated delivery time based on a hash of the order
    estimated_time = f"{(hash(order) % 30) + 10} minutes"

    return {
        "order": order,
        "status": "confirmed",
        "estimated_time": estimated_time,
    }


from typing import Dict, List, Union


def order_food(
    table_id: str,
    no_of_customers: int,
    starters: List[Dict[str, Union[str, int]]] = [],
    mains: List[Dict[str, Union[str, int]]] = [],
    desserts: List[Dict[str, Union[str, int]]] = [],
    drinks: List[Dict[str, Union[str, int]]] = [],
    order_complete: bool = False,
) -> Dict[str, Union[str, int, bool, List[Dict[str, Union[str, int]]]]]:
    """Allows a waiter to input the food order for a table.

    Args:
        table_id: The unique identifier of the table that the order is being placed for.
        no_of_customers: The number of people sat at this table.
        starters: The starters ordered by this table.
        mains: The mains ordered by this table.
        desserts: The desserts ordered by this table.
        drinks: The drinks ordered by this table.
        order_complete: Whether the table has ordered all their food already (true), or would like to add to the order later on (false).

    Returns:
        Dict containing:
            - table_id: The unique identifier of the table.
            - no_of_customers: The number of people at the table.
            - starters: List of starters ordered.
            - mains: List of mains ordered.
            - desserts: List of desserts ordered.
            - drinks: List of drinks ordered.
            - order_complete: Whether the order is complete.
    """
    if no_of_customers <= 0:
        raise ValueError("Number of customers must be greater than zero.")

    sample_data = {
        "table_id": table_id,
        "no_of_customers": no_of_customers,
        "starters": starters if starters else [{"starter_id": "s1", "quantity": 2}],
        "mains": mains if mains else [{"main_id": "m1", "quantity": 3}],
        "desserts": desserts if desserts else [{"dessert_id": "d1", "quantity": 1}],
        "drinks": drinks if drinks else [{"drink_id": "dr1", "quantity": 4}],
        "order_complete": order_complete,
    }

    return sample_data


from typing import Dict


def order_indian(order: str) -> Dict[str, str]:
    """Place an order for Indian takeaway.

    Args:
        order: The chosen dish to order (e.g. 'Chicken Tikka Masala', 'Paneer Butter Masala')

    Returns:
        Dict containing:
            - order: The name of the dish ordered
            - status: The status of the order
            - estimated_time: Estimated time for delivery
    """

    sample_menu = {
        "Chicken Tikka Masala": "Order confirmed",
        "Paneer Butter Masala": "Order confirmed",
        "Lamb Vindaloo": "Order confirmed",
        "Vegetable Biryani": "Order confirmed",
    }

    if order not in sample_menu:
        raise ValueError(f"Dish not available: {order}")

    estimated_times = {
        "Chicken Tikka Masala": "30 minutes",
        "Paneer Butter Masala": "25 minutes",
        "Lamb Vindaloo": "35 minutes",
        "Vegetable Biryani": "20 minutes",
    }

    return {
        "order": order,
        "status": sample_menu[order],
        "estimated_time": estimated_times[order],
    }


from typing import Dict, Literal


def order_pizza(
    size: Literal["M", "L", "XL", "XXL"], quantity: int = 1
) -> Dict[str, Union[str, int, float]]:
    """Place an order for a pizza.

    Args:
        size: Size of pizza ('M', 'L', 'XL', 'XXL')
        quantity: Number of pizzas being ordered

    Returns:
        Dict containing:
            - size: Size of the pizza ordered
            - quantity: Number of pizzas ordered
            - total_price: Total price of the order
    """
    price_chart = {
        "M": 8.99,
        "L": 12.99,
        "XL": 15.99,
        "XXL": 18.99,
    }

    if size not in price_chart:
        raise ValueError(f"Unsupported pizza size: {size}")

    total_price = price_chart[size] * quantity

    return {
        "size": size,
        "quantity": quantity,
        "total_price": round(total_price, 2),
    }


from datetime import datetime
from typing import Dict, Union


def release_table(
    table_id: str, time: Dict[str, Union[int, str]], is_clean: bool = False
) -> Dict[str, Union[str, bool]]:
    """Mark a table as free in the booking system.

    Args:
        table_id: The unique identifier for a table.
        time: The time at which the table has been released, with keys 'hour' and 'minute'.
        is_clean: True if the table has been cleaned, false otherwise.

    Returns:
        Dict containing:
            - table_id: The unique identifier for the table.
            - status: The status of the table, either 'free' or 'occupied'.
            - released_at: The formatted time when the table was released.
            - is_clean: True if the table has been cleaned, false otherwise.
    """
    if not isinstance(table_id, str) or not table_id:
        raise ValueError("Invalid table_id provided.")

    try:
        release_time = datetime.strptime(f"{time['hour']}:{time['minute']}", "%H:%M")
    except (KeyError, ValueError):
        raise ValueError(
            "Invalid time format provided. Expected keys: 'hour', 'minute'."
        )

    return {
        "table_id": table_id,
        "status": "free",
        "released_at": release_time.strftime("%H:%M"),
        "is_clean": is_clean,
    }


from datetime import datetime
from typing import Dict, Union


def request_booking(
    customer_id: str,
    booking_size: int = 1,
    time: Dict[str, Union[int, str]] = None,
    dietary_needs: bool = False,
) -> Dict[str, Union[str, int, bool]]:
    """Matches a suitable table to the booking customer, if one is available.

    Args:
        customer_id: The unique identifier of the customer who is making the booking.
        booking_size: The number of seats requested by the customer.
        time: The time at which the customer would like the table to be booked for.
        dietary_needs: Whether the customer or anyone in their party has any allergies or dietary needs.

    Returns:
        Dict containing:
            - customer_id: The unique identifier of the customer.
            - table_id: The identifier of the matched table.
            - booking_size: The number of seats booked.
            - time: The time of the booking.
            - dietary_needs: Whether dietary needs were considered.
            - status: The status of the booking ('confirmed' or 'waitlisted').
    """
    if not customer_id or not time:
        raise ValueError("Both 'customer_id' and 'time' are required fields.")

    # Simulated table availability based on hash of customer_id and time
    hash_value = hash(customer_id + str(time))
    available_tables = ["T1", "T2", "T3", "T4", "T5"]
    table_id = available_tables[hash_value % len(available_tables)]

    # Simulated logic for confirming or waitlisting a booking
    if booking_size <= 4 and hash_value % 3 != 0:
        status = "confirmed"
    else:
        status = "waitlisted"

    return {
        "customer_id": customer_id,
        "table_id": table_id,
        "booking_size": booking_size,
        "time": time,
        "dietary_needs": dietary_needs,
        "status": status,
    }


from typing import Dict


def reserve_restaurant(
    restaurant_name: str, city: str, date: str, time: str, people: int
) -> Dict[str, str]:
    """Reserve a table at a restaurant.

    Args:
        restaurant_name: Name of the restaurant
        city: City where the restaurant is located
        date: Reservation date in YYYY-MM-DD format
        time: Reservation time in HH:MM format
        people: Number of people in the reservation

    Returns:
        Dict containing:
            - confirmation_number: Unique confirmation number for the reservation
            - status: Status of the reservation
    """
    if people <= 0:
        raise ValueError("Number of people must be greater than zero")

    # Simulate a confirmation number generation
    confirmation_number = (
        f"{hash((restaurant_name, city, date, time, people)) % 1000000:06}"
    )

    return {"confirmation_number": confirmation_number, "status": "confirmed"}


from typing import Dict, Union


def reserve_seat(
    restaurant_id: str, tab_num: str, arrive_time: float, sets_res: int
) -> Dict[str, Union[str, int, float]]:
    """Book a table at a Chinese restaurant online.

    Args:
        restaurant_id: The unique identifier for the restaurant or name of the restaurant
        tab_num: The table number at the Chinese restaurant
        arrive_time: Reserve a time to arrive at the restaurant
        sets_res: Reserve the number of seats

    Returns:
        Dict containing:
            - restaurant_id: The unique identifier for the restaurant
            - tab_num: The table number reserved
            - arrive_time: The time of reservation
            - sets_res: The number of seats reserved
            - confirmation_code: A unique confirmation code for the reservation
    """

    if sets_res <= 0:
        raise ValueError("Number of seats reserved must be greater than zero.")
    if not (0 <= arrive_time <= 24):
        raise ValueError("Arrive time must be between 0 and 24.")

    # Simulate a confirmation code generation
    confirmation_code = (
        f"{hash((restaurant_id, tab_num, arrive_time, sets_res)) % 1000000:06}"
    )

    return {
        "restaurant_id": restaurant_id,
        "tab_num": tab_num,
        "arrive_time": arrive_time,
        "sets_res": sets_res,
        "confirmation_code": confirmation_code,
    }


import hashlib
from typing import Dict, List, Literal, Union


def reserve_table(
    restaurant_id: str,
    datetime: str,
    party_size: int,
    seating_preference: Literal["table", "bar", "patio", "booth"] = None,
    allergy_notes: List[str] = None,
    occasion: str = None,
    name: str = None,
    phone: str = None,
) -> Dict[str, Union[str, int, List[str]]]:
    """Make a dining reservation at a specified restaurant.

    Args:
        restaurant_id: Target restaurant ID
        datetime: Reservation datetime in ISO 8601 (e.g., '2025-08-12T19:30')
        party_size: Number of guests (integer)
        seating_preference: Seating preference: 'table', 'bar', 'patio', 'booth'
        allergy_notes: List of allergy or dietary notes
        occasion: Optional occasion note (e.g., 'birthday')
        name: Name for the booking
        phone: Contact phone number

    Returns:
        Dict containing:
            - reservation_id: Unique reservation identifier
            - restaurant_id: Target restaurant ID
            - datetime: Reservation datetime
            - party_size: Number of guests
            - seating_preference: Seating preference
            - allergy_notes: List of allergy or dietary notes
            - occasion: Occasion note
            - name: Name for the booking
            - phone: Contact phone number
    """
    if not restaurant_id or not datetime or not party_size:
        raise ValueError("restaurant_id, datetime, and party_size are required fields")

    # Generate a unique reservation ID using a hash
    reservation_id = hashlib.md5(
        f"{restaurant_id}{datetime}{party_size}".encode()
    ).hexdigest()

    return {
        "reservation_id": reservation_id,
        "restaurant_id": restaurant_id,
        "datetime": datetime,
        "party_size": party_size,
        "seating_preference": seating_preference or "table",
        "allergy_notes": allergy_notes or [],
        "occasion": occasion or "",
        "name": name or "Guest",
        "phone": phone or "N/A",
    }


from typing import Dict


def restaurant_rating(restaurant_name: str) -> Dict[str, Union[str, float]]:
    """Display the star rating for a given restaurant.

    Args:
        restaurant_name: The restaurant's name.

    Returns:
        Dict containing:
            - restaurant_name: The name of the restaurant
            - star_rating: The star rating of the restaurant
    """

    sample_ratings = {
        "The Gourmet Kitchen": 4.5,
        "Pizza Palace": 3.8,
        "Sushi World": 4.2,
        "Burger Haven": 4.0,
        "Pasta Paradise": 3.9,
    }

    if restaurant_name not in sample_ratings:
        raise ValueError(f"Restaurant not found: {restaurant_name}")

    return {
        "restaurant_name": restaurant_name,
        "star_rating": sample_ratings[restaurant_name],
    }


from typing import Dict


def schedule_holiday(date: str) -> Dict[str, str]:
    """Specify that the restaurant will be closed on a future date.

    Args:
        date: The date in dd/mm/yyyy format that the restaurant will be closed.

    Returns:
        Dict containing:
            - date: The date the restaurant will be closed
            - status: Confirmation message of the closure
    """
    # Validate the date format
    try:
        day, month, year = map(int, date.split("/"))
    except ValueError:
        raise ValueError("Date must be in dd/mm/yyyy format")

    if not (1 <= day <= 31 and 1 <= month <= 12 and year >= 2023):
        raise ValueError("Invalid date provided")

    # Simulate scheduling the holiday
    return {"date": date, "status": f"Restaurant will be closed on {date}"}


from typing import Dict, List, Union


def search_restaurants(
    country: str,
    city: str,
    price_range: Dict[str, float] = None,
    key_terms: List[str] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search for restaurants by city.

    Args:
        country: The country where the restaurant is located.
        city: The city where the restaurant is located.
        price_range: Price range filter with 'min' and 'max' values.
        key_terms: Key words such as cuisine or food types.

    Returns:
        Dict containing:
            - city: City name
            - country: Country name
            - restaurants: List of restaurants with details such as name, cuisine, and average price
    """

    # Sample data for demonstration purposes
    sample_data = {
        ("USA", "New York"): [
            {"name": "Joe's Pizza", "cuisine": "Italian", "average_price": 15},
            {"name": "Sushi Nakazawa", "cuisine": "Japanese", "average_price": 150},
            {"name": "Shake Shack", "cuisine": "American", "average_price": 10},
        ],
        ("France", "Paris"): [
            {"name": "Le Meurice", "cuisine": "French", "average_price": 250},
            {"name": "L'Arpège", "cuisine": "French", "average_price": 300},
            {"name": "Chez Janou", "cuisine": "Provençal", "average_price": 40},
        ],
    }

    key = (country, city)
    if key not in sample_data:
        raise ValueError(f"No data available for {city}, {country}")

    restaurants = sample_data[key]

    # Filter by price range if provided
    if price_range:
        min_price = price_range.get("min", 0)
        max_price = price_range.get("max", float("inf"))
        restaurants = [
            r for r in restaurants if min_price <= r["average_price"] <= max_price
        ]

    # Filter by key terms if provided
    if key_terms:
        key_terms_lower = [term.lower() for term in key_terms]
        restaurants = [
            r
            for r in restaurants
            if any(term in r["cuisine"].lower() for term in key_terms_lower)
        ]

    return {
        "city": city,
        "country": country,
        "restaurants": restaurants,
    }


from typing import Dict, List


def track_discounts(
    items: List[str], cafes: List[str], alert: bool = True
) -> Dict[str, Union[List[Dict[str, Union[str, float]]], str]]:
    """Track prices of nearby coffee shops to alert user when discounts become available.

    Args:
        items: List of items user is interested in tracking (e.g., 'americano', 'latte').
        cafes: List of cafes the user wants to monitor.
        alert: Boolean indicating if an alert should be sent when discounts become available.

    Returns:
        Dict containing:
            - discounts: List of dictionaries with cafe name, item, and discounted price
            - message: Notification message if alert is enabled
    """
    if not items or not cafes:
        raise ValueError("Both 'items' and 'cafes' must be provided and non-empty.")

    # Simulated discount data
    sample_discounts = {
        "Cafe Mocha": {"americano": 2.5, "latte": 3.0},
        "Java House": {"americano": 2.0, "latte": 2.8},
        "Brewed Awakenings": {"americano": 2.2, "latte": 2.9},
    }

    discounts = []
    for cafe in cafes:
        if cafe in sample_discounts:
            for item in items:
                if item in sample_discounts[cafe]:
                    discounts.append(
                        {
                            "cafe": cafe,
                            "item": item,
                            "discounted_price": sample_discounts[cafe][item],
                        }
                    )

    if not discounts:
        return {"discounts": [], "message": "No discounts available at the moment."}

    message = "Discounts available!" if alert else "Discount tracking complete."
    return {"discounts": discounts, "message": message}


def get_flavours(preferences: Optional[str] = None) -> Dict[str, Union[str, List[str]]]:
    """Gets an array of available flavours.

    Args:
        preferences: Optional keywords used to sort preferred flavours to top of results

    Returns:
        Dict containing:
            - preferences: The preferences filter used (if any)
            - available_flavours: List of available ice cream flavours
    """

    # Base flavours available at the ice cream shop
    base_flavours = [
        "vanilla",
        "chocolate",
        "strawberry",
        "mint chip",
        "cookies and cream",
        "rocky road",
        "pistachio",
        "neapolitan",
        "butter pecan",
        "coffee",
        "cherry vanilla",
        "chocolate chip",
        "caramel swirl",
        "rainbow sherbet",
    ]

    # If preferences provided, sort matching flavours to the top
    if preferences:
        preference_keywords = preferences.lower().split()
        preferred_flavours = []
        other_flavours = []

        for flavour in base_flavours:
            if any(keyword in flavour.lower() for keyword in preference_keywords):
                preferred_flavours.append(flavour)
            else:
                other_flavours.append(flavour)

        available_flavours = preferred_flavours + other_flavours
    else:
        available_flavours = base_flavours

    return {"preferences": preferences, "available_flavours": available_flavours}


def create_desert(
    type: int,
    ingredient: str,
    scoops: str,
    sprinkles: bool = False,
    cream_topper: bool = False,
    nuts: bool = False,
    sauce_flavour: Optional[str] = None,
    chocolate_flake: int = 0,
) -> Dict[str, Union[str, int, bool]]:
    """Create your ice cream desert.

    Args:
        type: Container type (1 - cone, 2 - tub, 3 - Sunday)
        ingredient: Base ingredient (D - dairy, O - oat milk, S - soya)
        scoops: Comma separated list of flavours. One entry = 1 scoop. Max 3 scoops.
        sprinkles: Add sprinkles
        cream_topper: Top with whipped cream
        nuts: Top with nuts
        sauce_flavour: Add sauce (C - Chocolate, S - Strawberry, R - Raspberry)
        chocolate_flake: Number of flake sticks to add (0-2)

    Returns:
        Dict containing:
            - desert_id: Unique identifier for the created desert
            - type: Container type description
            - ingredient: Base ingredient description
            - scoops: List of scoops added
            - toppings: List of toppings added
            - estimated_prep_time: Estimated preparation time in minutes
    """

    # Validate inputs
    if type not in [1, 2, 3]:
        raise ValueError("Type must be 1 (cone), 2 (tub), or 3 (Sunday)")

    if ingredient not in ["D", "O", "S"]:
        raise ValueError("Ingredient must be D (dairy), O (oat milk), or S (soya)")

    if sauce_flavour and sauce_flavour not in ["C", "S", "R"]:
        raise ValueError(
            "Sauce flavour must be C (Chocolate), S (Strawberry), or R (Raspberry)"
        )

    if chocolate_flake not in [0, 1, 2]:
        raise ValueError("Chocolate flake must be 0, 1, or 2")

    # Parse scoops (max 3)
    scoop_list = [s.strip() for s in scoops.split(",") if s.strip()]
    if len(scoop_list) > 3:
        raise ValueError("Maximum 3 scoops allowed")

    # Generate unique desert ID
    import hashlib

    desert_data = f"{type}{ingredient}{scoops}{sprinkles}{cream_topper}{nuts}{sauce_flavour}{chocolate_flake}"
    desert_id = hashlib.md5(desert_data.encode()).hexdigest()[:8].upper()

    # Map type to description
    type_descriptions = {1: "cone", 2: "tub", 3: "sundae"}

    # Map ingredient to description
    ingredient_descriptions = {"D": "dairy", "O": "oat milk", "S": "soya"}

    # Build toppings list
    toppings = []
    if sprinkles:
        toppings.append("sprinkles")
    if cream_topper:
        toppings.append("whipped cream")
    if nuts:
        toppings.append("nuts")
    if sauce_flavour:
        sauce_map = {
            "C": "chocolate sauce",
            "S": "strawberry sauce",
            "R": "raspberry sauce",
        }
        toppings.append(sauce_map[sauce_flavour])
    if chocolate_flake > 0:
        toppings.append(
            f"{chocolate_flake} chocolate flake{'s' if chocolate_flake > 1 else ''}"
        )

    # Estimate prep time (base 2 min + 30 sec per scoop + 30 sec per topping)
    estimated_prep_time = 2 + (len(scoop_list) * 0.5) + (len(toppings) * 0.5)

    return {
        "desert_id": desert_id,
        "type": type_descriptions[type],
        "ingredient": ingredient_descriptions[ingredient],
        "scoops": scoop_list,
        "toppings": toppings,
        "estimated_prep_time": round(estimated_prep_time, 1),
    }


def order(desert_ids: str, table_number: int) -> Dict[str, Union[str, int, List[str]]]:
    """Order your dessert.

    Args:
        desert_ids: Comma separated list of desert ids
        table_number: Number of the table you are seated at

    Returns:
        Dict containing:
            - order_id: Unique order identifier
            - table_number: Table number for the order
            - desert_ids: List of desert IDs in the order
            - status: Order status
            - estimated_total_time: Total estimated preparation time
    """

    if not desert_ids or not table_number:
        raise ValueError("Both desert_ids and table_number are required")

    # Parse desert IDs
    desert_id_list = [id.strip() for id in desert_ids.split(",") if id.strip()]

    if not desert_id_list:
        raise ValueError("At least one desert ID must be provided")

    # Generate unique order ID
    import hashlib

    order_data = f"{desert_ids}{table_number}"
    order_id = f"ORD-{hashlib.md5(order_data.encode()).hexdigest()[:6].upper()}"

    # Estimate total prep time (assume 3-5 minutes per desert)
    estimated_total_time = len(desert_id_list) * 4

    return {
        "order_id": order_id,
        "table_number": table_number,
        "desert_ids": desert_id_list,
        "status": "confirmed",
        "estimated_total_time": estimated_total_time,
    }


def progress_update(table_number: int) -> Dict[str, Union[str, int]]:
    """Find out what's happening with your order inc. estimated delivery time.

    Args:
        table_number: Number of the table you are seated at

    Returns:
        Dict containing:
            - table_number: Table number checked
            - order_status: Current status of the order
            - estimated_delivery_time: Estimated time until delivery (minutes)
            - message: Status message
    """

    if not table_number:
        raise ValueError("Table number is required")

    # Simulate order status based on table number
    status_options = ["preparing", "almost ready", "ready for pickup", "delivered"]
    status_index = (table_number - 1) % len(status_options)
    order_status = status_options[status_index]

    # Simulate estimated delivery time
    delivery_times = {
        "preparing": 8,
        "almost ready": 2,
        "ready for pickup": 0,
        "delivered": 0,
    }

    messages = {
        "preparing": "Your order is currently being prepared in the kitchen.",
        "almost ready": "Your order is almost ready! Just putting the finishing touches on it.",
        "ready for pickup": "Your order is ready! Please come to the counter to collect it.",
        "delivered": "Your order has been delivered to your table. Enjoy!",
    }

    return {
        "table_number": table_number,
        "order_status": order_status,
        "estimated_delivery_time": delivery_times[order_status],
        "message": messages[order_status],
    }


def cancel_order(
    table_number: int, desert_ids: Optional[str] = None
) -> Dict[str, Union[str, int, List[str]]]:
    """Cancel your order if you change your mind.

    Args:
        table_number: Number of the table you are seated at
        desert_ids: Optional comma separated list of desert ids, only include if you are cancelling part of an order

    Returns:
        Dict containing:
            - table_number: Table number for the cancellation
            - cancellation_type: Whether full order or partial cancellation
            - cancelled_items: List of cancelled desert IDs (if partial)
            - status: Cancellation status
            - refund_amount: Estimated refund amount
    """

    if not table_number:
        raise ValueError("Table number is required")

    if desert_ids:
        # Partial cancellation
        cancelled_items = [id.strip() for id in desert_ids.split(",") if id.strip()]
        cancellation_type = "partial"
        refund_amount = len(cancelled_items) * 5.99  # Assume $5.99 per desert
    else:
        # Full order cancellation
        cancelled_items = []
        cancellation_type = "full"
        refund_amount = 12.99  # Assume average order total

    return {
        "table_number": table_number,
        "cancellation_type": cancellation_type,
        "cancelled_items": cancelled_items,
        "status": "cancelled",
        "refund_amount": round(refund_amount, 2),
    }
