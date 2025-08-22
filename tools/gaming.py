# Gaming Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Optional, Union


def deck_search(
    deck_name: Optional[str] = None,
    deck_card: Optional[str] = None,
    deck_keyword: Optional[str] = None,
    deck_val_min: Optional[float] = None,
    deck_val_max: Optional[float] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search user-created decks for keywords or specific cards.

    Args:
        deck_name: Title of the deck to search for.
        deck_card: Search for decks containing specific cards.
        deck_keyword: Searches deck name, text, and rulings for instances of the search term.
        deck_val_min: Limits selections to decks with a value higher than the search term.
        deck_val_max: Limits selections to decks with a value lower than the search term.

    Returns:
        Dict containing:
            - query: Description of the search query
            - results: List of decks matching the search criteria, each with:
                - name: Name of the deck
                - value: Estimated value of the deck
                - cards: List of cards in the deck
    """
    sample_decks = [
        {
            "name": "Dragon's Fury",
            "value": 150.0,
            "cards": ["Red Dragon", "Fireball", "Mountain"],
        },
        {
            "name": "Ocean's Might",
            "value": 200.0,
            "cards": ["Blue Whale", "Tidal Wave", "Island"],
        },
        {
            "name": "Forest's Whisper",
            "value": 120.0,
            "cards": ["Green Elf", "Forest", "Nature's Lore"],
        },
    ]

    def matches_criteria(deck):
        if deck_name and deck_name.lower() not in deck["name"].lower():
            return False
        if deck_card and not any(
            deck_card.lower() in card.lower() for card in deck["cards"]
        ):
            return False
        if deck_keyword and not (
            deck_keyword.lower() in deck["name"].lower()
            or any(deck_keyword.lower() in card.lower() for card in deck["cards"])
        ):
            return False
        if deck_val_min is not None and deck["value"] <= deck_val_min:
            return False
        if deck_val_max is not None and deck["value"] >= deck_val_max:
            return False
        return True

    results = [deck for deck in sample_decks if matches_criteria(deck)]

    query_description = f"Search for decks with name '{deck_name}', card '{deck_card}', keyword '{deck_keyword}', value min '{deck_val_min}', value max '{deck_val_max}'"

    return {
        "query": query_description,
        "results": results,
    }


from typing import Dict, Union


def add_item(
    player_id: str, item_id: str, quantity: int = 1
) -> Dict[str, Union[str, int, bool]]:
    """Add an item to a player's inventory if they have space and meet level requirements.

    Args:
        player_id: The ID of the player receiving the item.
        item_id: The ID of the item to add.
        quantity: Number of items to add (default: 1).

    Returns:
        Dict containing:
            - player_id: The ID of the player
            - item_id: The ID of the item added
            - quantity: Number of items added
            - success: Whether the item was successfully added
    """

    # Mock player data
    players = {
        "player1": {"level": 10, "inventory_space": 5},
        "player2": {"level": 5, "inventory_space": 2},
    }

    # Mock item data
    items = {
        "itemA": {"required_level": 5, "size": 1},
        "itemB": {"required_level": 10, "size": 2},
    }

    if player_id not in players:
        raise ValueError(f"Player ID not found: {player_id}")
    if item_id not in items:
        raise ValueError(f"Item ID not found: {item_id}")

    player = players[player_id]
    item = items[item_id]

    if player["level"] < item["required_level"]:
        return {
            "player_id": player_id,
            "item_id": item_id,
            "quantity": 0,
            "success": False,
        }

    total_size = item["size"] * quantity
    if player["inventory_space"] < total_size:
        return {
            "player_id": player_id,
            "item_id": item_id,
            "quantity": 0,
            "success": False,
        }

    # Simulate adding item to inventory
    player["inventory_space"] -= total_size

    return {
        "player_id": player_id,
        "item_id": item_id,
        "quantity": quantity,
        "success": True,
    }


from typing import Dict, List


def best_teammates(
    pokemon_name: str, format: str = "gen9ou"
) -> List[Dict[str, Union[str, float]]]:
    """Return a list of the 10 Pokémon with the highest winrates when used alongside the given Pokémon.

    Args:
        pokemon_name: String containing the name of the Pokémon.
        format: The given format the user wants information about (default is 'gen9ou').

    Returns:
        List of dictionaries, each containing:
            - name: Name of the Pokémon
            - winrate: Winrate percentage when used alongside the given Pokémon
    """

    # Sample data simulating winrates for Pokémon combinations
    sample_data = {
        "Pikachu": [
            {"name": "Charizard", "winrate": 75.5},
            {"name": "Bulbasaur", "winrate": 70.2},
            {"name": "Squirtle", "winrate": 68.9},
            {"name": "Jigglypuff", "winrate": 67.4},
            {"name": "Meowth", "winrate": 66.1},
            {"name": "Pidgey", "winrate": 65.8},
            {"name": "Rattata", "winrate": 64.3},
            {"name": "Zubat", "winrate": 63.7},
            {"name": "Geodude", "winrate": 62.5},
            {"name": "Magikarp", "winrate": 61.9},
        ],
        "Charizard": [
            {"name": "Pikachu", "winrate": 75.5},
            {"name": "Blastoise", "winrate": 74.3},
            {"name": "Venusaur", "winrate": 73.1},
            {"name": "Alakazam", "winrate": 72.6},
            {"name": "Gengar", "winrate": 71.4},
            {"name": "Machamp", "winrate": 70.2},
            {"name": "Snorlax", "winrate": 69.8},
            {"name": "Dragonite", "winrate": 68.9},
            {"name": "Gyarados", "winrate": 67.5},
            {"name": "Lapras", "winrate": 66.7},
        ],
    }

    if pokemon_name not in sample_data:
        raise ValueError(f"Pokémon not supported: {pokemon_name}")

    return sorted(sample_data[pokemon_name], key=lambda x: x["winrate"], reverse=True)


from typing import Dict, List, Literal, Union


def get_runner_up_players(
    region: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Gets the ranked stats of the players ranked 1000-300 on the ladder for the given region.

    Args:
        region: The region the account is in. Options are 'North America', 'Europe', or 'Asia'.

    Returns:
        Dict containing:
            - region: The region of the players
            - players: List of dictionaries with player stats, each containing:
                - name: Player's name
                - rank: Player's rank
                - score: Player's score
    """

    if region not in ["North America", "Europe", "Asia"]:
        raise ValueError(f"Region not supported: {region}")

    # Simulate player data
    sample_players = [
        {"name": f"Player{rank}", "rank": rank, "score": 1000 - rank}
        for rank in range(300, 1001)
    ]

    return {
        "region": region,
        "players": sample_players,
    }


from typing import Dict, List, Literal


def get_top_players(
    region: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Gets the ranked stats of the top 300 players on the ladder for the given region.

    Args:
        region: The region the account is in. Options are 'North America', 'Europe', or 'Asia'.

    Returns:
        Dict containing:
            - region: The region of the players
            - players: List of dictionaries containing player stats
                - rank: Player's rank
                - name: Player's name
                - score: Player's score
    """
    if region not in ["North America", "Europe", "Asia"]:
        raise ValueError(f"Region not supported: {region}")

    # Generate mock data for top players
    players = [
        {
            "rank": i + 1,
            "name": f"Player{i + 1}_{region[:2]}",
            "score": 3000 - i * 10,  # Decreasing score for each rank
        }
        for i in range(300)
    ]

    return {"region": region, "players": players}


from typing import Dict, List, Literal


def pokemon_loadouts(
    pokemon_name: str, format: str = "gen9ou"
) -> Dict[str, Union[str, List[str], Dict[str, int]]]:
    """Returns the most popular stat spread, natures, and movesets for the given Pokémon in the specified format.

    Args:
        pokemon_name: String containing the name of the Pokémon (e.g. 'Pikachu', 'Charizard')
        format: The format for which the information is requested (default is 'gen9ou')

    Returns:
        Dict containing:
            - pokemon_name: Name of the Pokémon
            - format: The format for which the data is relevant
            - nature: Most popular nature for the Pokémon
            - stats: Dictionary of stat spread with keys as stat names and values as stat values
            - moveset: List of most popular moves for the Pokémon
    """

    sample_data = {
        "Pikachu": {
            "gen9ou": {
                "nature": "Timid",
                "stats": {
                    "HP": 35,
                    "Attack": 55,
                    "Defense": 40,
                    "Sp. Atk": 50,
                    "Sp. Def": 50,
                    "Speed": 90,
                },
                "moveset": ["Thunderbolt", "Volt Tackle", "Iron Tail", "Quick Attack"],
            },
            "gen8ou": {
                "nature": "Jolly",
                "stats": {
                    "HP": 35,
                    "Attack": 55,
                    "Defense": 40,
                    "Sp. Atk": 50,
                    "Sp. Def": 50,
                    "Speed": 90,
                },
                "moveset": ["Thunderbolt", "Volt Tackle", "Grass Knot", "Quick Attack"],
            },
        },
        "Charizard": {
            "gen9ou": {
                "nature": "Modest",
                "stats": {
                    "HP": 78,
                    "Attack": 84,
                    "Defense": 78,
                    "Sp. Atk": 109,
                    "Sp. Def": 85,
                    "Speed": 100,
                },
                "moveset": ["Flamethrower", "Dragon Pulse", "Air Slash", "Solar Beam"],
            },
            "gen8ou": {
                "nature": "Timid",
                "stats": {
                    "HP": 78,
                    "Attack": 84,
                    "Defense": 78,
                    "Sp. Atk": 109,
                    "Sp. Def": 85,
                    "Speed": 100,
                },
                "moveset": ["Fire Blast", "Hurricane", "Focus Blast", "Roost"],
            },
        },
    }

    if pokemon_name not in sample_data:
        raise ValueError(f"Pokémon not supported: {pokemon_name}")

    if format not in sample_data[pokemon_name]:
        raise ValueError(f"Format not supported for {pokemon_name}: {format}")

    data = sample_data[pokemon_name][format]
    return {
        "pokemon_name": pokemon_name,
        "format": format,
        "nature": data["nature"],
        "stats": data["stats"],
        "moveset": data["moveset"],
    }


from typing import Dict, Literal


def pokemon_tier(pokemon_name: str, format: str = "gen9ou") -> Dict[str, str]:
    """Determine the tier ranking of a Pokémon based on usage stats and winrate.

    Args:
        pokemon_name: The name of the Pokémon to evaluate.
        format: The competitive format to consider (default is 'gen9ou').

    Returns:
        Dict containing:
            - pokemon_name: Name of the Pokémon
            - format: The competitive format considered
            - tier: The tier ranking of the Pokémon (S/A/B/C/D/E/F)
    """

    # Sample data for demonstration purposes
    sample_data = {
        "gen9ou": {
            "Pikachu": "C",
            "Charizard": "A",
            "Greninja": "S",
            "Bulbasaur": "E",
        },
        "gen8ou": {
            "Pikachu": "D",
            "Charizard": "B",
            "Greninja": "A",
            "Bulbasaur": "F",
        },
    }

    if format not in sample_data:
        raise ValueError(f"Format not supported: {format}")

    if pokemon_name not in sample_data[format]:
        raise ValueError(f"Pokémon not found in format {format}: {pokemon_name}")

    return {
        "pokemon_name": pokemon_name,
        "format": format,
        "tier": sample_data[format][pokemon_name],
    }


from typing import Dict, Union


def pokemon_use_stats(
    pokemon_name: str, format: str = "gen9ou"
) -> Dict[str, Union[str, float]]:
    """Return the usage statistics of a Pokémon in a given format.

    Args:
        pokemon_name: String containing the name of the Pokémon.
        format: The given format the user wants information about (default is 'gen9ou').

    Returns:
        Dict containing:
            - pokemon_name: Name of the Pokémon
            - format: The format in which the stats are provided
            - team_percentage: Percentage of teams the Pokémon is included in
            - lead_percentage: Percentage of games the Pokémon is used as a lead
    """

    # Sample data based on hash of the Pokémon name and format for consistency
    sample_data = {
        "gen9ou": {
            "Pikachu": (15.2, 5.1),
            "Charizard": (25.4, 10.3),
            "Bulbasaur": (5.6, 2.2),
        },
        "gen8ou": {
            "Pikachu": (12.3, 4.8),
            "Charizard": (22.1, 9.7),
            "Bulbasaur": (4.9, 1.9),
        },
    }

    if format not in sample_data:
        raise ValueError(f"Format not supported: {format}")

    if pokemon_name not in sample_data[format]:
        raise ValueError(f"Pokémon not found in format {format}: {pokemon_name}")

    team_percentage, lead_percentage = sample_data[format][pokemon_name]

    return {
        "pokemon_name": pokemon_name,
        "format": format,
        "team_percentage": team_percentage,
        "lead_percentage": lead_percentage,
    }


from typing import Dict, Union


def remove_item(
    player_id: str, item_id: str, quantity: int = 1
) -> Dict[str, Union[str, int]]:
    """Remove an item from a player's inventory.

    Args:
        player_id: The ID of the player losing the item.
        item_id: The ID of the item to remove.
        quantity: Number of items to remove (default: 1).

    Returns:
        Dict containing:
            - player_id: The ID of the player
            - item_id: The ID of the removed item
            - quantity: Number of items removed

    Raises:
        ValueError: If the item is equipped, doesn't exist, or quantity is invalid.
    """

    # Mock player inventory data
    player_inventory = {
        "player123": {"sword": 2, "shield": 1, "potion": 5},
        "player456": {"axe": 1, "potion": 3},
    }

    # Mock equipped items data
    equipped_items = {
        "player123": ["sword"],
        "player456": ["axe"],
    }

    if player_id not in player_inventory:
        raise ValueError(f"Player ID not found: {player_id}")

    if item_id not in player_inventory[player_id]:
        raise ValueError(f"Item ID not found in inventory: {item_id}")

    if item_id in equipped_items.get(player_id, []):
        raise ValueError(f"Cannot remove equipped item: {item_id}")

    current_quantity = player_inventory[player_id][item_id]

    if quantity < 1 or quantity > current_quantity:
        raise ValueError(f"Invalid quantity: {quantity}")

    # Simulate item removal
    player_inventory[player_id][item_id] -= quantity
    if player_inventory[player_id][item_id] == 0:
        del player_inventory[player_id][item_id]

    return {
        "player_id": player_id,
        "item_id": item_id,
        "quantity": quantity,
    }


from typing import Dict, Literal, Union


def collection_add(
    card_name: str,
    card_quantity: int = 1,
    trade_status: Literal["trade", "display"] = "display",
) -> Dict[str, Union[str, int]]:
    """Add a card to your digital trade/display binder.

    Args:
        card_name: Card name (specific)
        card_quantity: Number of this specific card to add to the collection.
        trade_status: Is the card available to trade/sell or is it display only?

    Returns:
        Dict containing:
            - card_name: Name of the card added
            - card_quantity: Total quantity of the card in the collection
            - trade_status: Status of the card in the collection
    """
    if card_quantity < 1:
        raise ValueError("card_quantity must be at least 1")

    # Simulate a collection database with a hash-based generation
    collection = {
        "Blue-Eyes White Dragon": {"quantity": 2, "status": "display"},
        "Dark Magician": {"quantity": 1, "status": "trade"},
    }

    if card_name in collection:
        existing_card = collection[card_name]
        existing_card["quantity"] += card_quantity
        existing_card["status"] = trade_status
    else:
        collection[card_name] = {"quantity": card_quantity, "status": trade_status}

    return {
        "card_name": card_name,
        "card_quantity": collection[card_name]["quantity"],
        "trade_status": collection[card_name]["status"],
    }


from typing import Dict, Union


def collection_rem(
    card_name: str, card_quantity: int = 1
) -> Dict[str, Union[str, int]]:
    """Remove a card from your digital trade/display binder.

    Args:
        card_name: The specific name of the card to remove.
        card_quantity: The number of this specific card to remove from your collection.

    Returns:
        Dict containing:
            - card_name: Name of the card removed
            - card_quantity: Number of cards removed
            - remaining_quantity: Number of this card remaining in the collection
    """
    # Sample collection data
    collection = {
        "Blue-Eyes White Dragon": 5,
        "Dark Magician": 3,
        "Red-Eyes Black Dragon": 2,
    }

    if card_name not in collection:
        raise ValueError(f"Card not found in collection: {card_name}")

    current_quantity = collection[card_name]
    if card_quantity > current_quantity:
        raise ValueError(
            f"Cannot remove {card_quantity} cards. Only {current_quantity} available."
        )

    remaining_quantity = current_quantity - card_quantity
    collection[card_name] = remaining_quantity

    return {
        "card_name": card_name,
        "card_quantity": card_quantity,
        "remaining_quantity": remaining_quantity,
    }


from typing import Dict, List, Literal, Union


def apply_condition(condition: str, apply: bool) -> Dict[str, Union[str, List[str]]]:
    """Applies or removes a D&D condition to the character.

    Args:
        condition: The name of the condition to apply or remove (e.g. 'poisoned', 'blinded').
        apply: True to apply the condition, false to remove it.

    Returns:
        Dict containing:
            - action: Description of the action taken
            - conditions: Updated list of conditions on the character
    """
    valid_conditions = {"poisoned", "blinded", "grappled", "stunned", "charmed"}
    if condition not in valid_conditions:
        raise ValueError(f"Unsupported condition: {condition}")

    # Simulate existing conditions for demonstration purposes
    current_conditions = ["poisoned", "grappled"]

    if apply:
        if condition in current_conditions:
            action = f"Condition '{condition}' is already applied."
        else:
            current_conditions.append(condition)
            action = f"Condition '{condition}' applied."
    else:
        if condition in current_conditions:
            current_conditions.remove(condition)
            action = f"Condition '{condition}' removed."
        else:
            action = f"Condition '{condition}' is not present."

    return {
        "action": action,
        "conditions": current_conditions,
    }


from typing import Dict


def attack(attack_dice: str, level: int = 1) -> Dict[str, int]:
    """Simulate an attack based on the attack dice and level modifier.

    Args:
        attack_dice: The attack dice in the format of {number of dice}D{number of sides} (e.g., '2D4').
        level: The level modifier for the attack.

    Returns:
        Dict containing:
            - damage: The total damage dealt by the attack.
    """
    import random
    import re

    dice_pattern = r"(\d+)D(\d+)"
    match = re.match(dice_pattern, attack_dice)
    if not match:
        raise ValueError(f"Invalid attack dice format: {attack_dice}")

    num_dice, num_sides = map(int, match.groups())
    if num_dice <= 0 or num_sides <= 0:
        raise ValueError("Number of dice and sides must be positive integers")

    damage = sum(random.randint(1, num_sides) for _ in range(num_dice))
    total_damage = damage + level

    return {"damage": total_damage}


import random
from typing import Dict, Union


def calculate_attack(attack_roll: str, target_ac: float) -> Dict[str, Union[int, bool]]:
    """Calculate the result of an attack roll and determine if it hits the target.

    Args:
        attack_roll: The dice roll expression for the attack, e.g. '1d20+7'.
        target_ac: The Armor Class of the target.

    Returns:
        Dict containing:
            - total_roll: The total result of the attack roll
            - hit: Boolean indicating if the attack hits the target
    """
    try:
        dice, modifier = attack_roll.split("+")
        num_dice, dice_sides = map(int, dice.split("d"))
        modifier = int(modifier)
    except ValueError:
        raise ValueError("Invalid attack roll format. Use 'XdY+Z' format.")

    if num_dice <= 0 or dice_sides <= 0:
        raise ValueError("Number of dice and sides must be positive integers.")

    total_roll = sum(random.randint(1, dice_sides) for _ in range(num_dice)) + modifier
    hit = total_roll >= target_ac

    return {
        "total_roll": total_roll,
        "hit": hit,
    }


from datetime import datetime
from typing import Dict, Union


def check_player_availability_for_date(
    player_name: str, date_of_birth: str, check_date: str
) -> Dict[str, Union[str, bool]]:
    """Check if a player is available for a specific date.

    Args:
        player_name: Name of the player to check availability for
        date_of_birth: Player's date of birth in YYYY-MM-DD format
        check_date: Date to check availability for in YYYY-MM-DD format

    Returns:
        Dict containing:
            - player_name: Name of the player
            - available: Boolean indicating if the player is available on the check_date
            - status: Current status of the player (e.g., 'injured', 'available', 'suspended')
            - return_date: Date when the player is expected to be available, if currently unavailable
    """
    # Mock player data based on hash of name and date of birth for consistency
    player_hash = hash((player_name, date_of_birth)) % 3
    status_options = ["available", "injured", "suspended"]
    status = status_options[player_hash]

    # Mock return date for unavailable players
    if status != "available":
        return_date = (
            datetime.strptime(check_date, "%Y-%m-%d") + timedelta(days=player_hash * 7)
        ).strftime("%Y-%m-%d")
    else:
        return_date = None

    # Determine availability
    available = status == "available" or (return_date and check_date >= return_date)

    return {
        "player_name": player_name,
        "available": available,
        "status": status,
        "return_date": return_date,
    }


from typing import Dict


def craft_item(
    player_id: str, target_item_id: str, materials: Dict[str, int]
) -> Dict[str, Union[str, bool]]:
    """Craft a new item by consuming materials if the player has said materials.

    Args:
        player_id: ID of the player crafting the item.
        target_item_id: ID of the item to craft.
        materials: Key-value pairs of material item IDs and quantities.

    Returns:
        Dict containing:
            - player_id: ID of the player
            - target_item_id: ID of the crafted item
            - success: Boolean indicating if the crafting was successful
            - message: Description of the crafting result
    """

    # Mock player inventory
    player_inventory = {
        "wood": 10,
        "iron": 5,
        "cloth": 20,
    }

    # Check if player has enough materials
    for material_id, required_qty in materials.items():
        if player_inventory.get(material_id, 0) < required_qty:
            return {
                "player_id": player_id,
                "target_item_id": target_item_id,
                "success": False,
                "message": f"Insufficient {material_id} to craft {target_item_id}.",
            }

    # Simulate crafting process
    for material_id, required_qty in materials.items():
        player_inventory[material_id] -= required_qty

    return {
        "player_id": player_id,
        "target_item_id": target_item_id,
        "success": True,
        "message": f"Successfully crafted {target_item_id}.",
    }


import hashlib
import random
from typing import Dict, List, Literal, Optional, Union


def create_enemy(
    name: str,
    species: Literal["humanoid", "undead", "beast", "elemental", "construct"],
    element: Literal["earth", "water", "fire", "wind", "death"],
    description: Optional[str] = None,
    level: int = 1,
) -> Dict[str, Union[str, int, List[str]]]:
    """Create a named enemy with random stats and a list of attacks based on its element.

    Args:
        name: The name of the enemy
        species: The species of the enemy (humanoid, undead, beast, elemental or construct)
        element: The element that the enemy uses for spells and abilities (earth, water, fire, wind, death)
        description: The description of the enemy
        level: The level of the enemy

    Returns:
        Dict containing:
            - name: Name of the enemy
            - species: Species of the enemy
            - element: Element of the enemy
            - level: Level of the enemy
            - description: Description of the enemy
            - stats: Dictionary of enemy stats (health, attack, defense)
            - attacks: List of attacks based on the enemy's element
    """

    # Generate consistent random stats using a hash of the name
    hash_seed = int(hashlib.sha256(name.encode()).hexdigest(), 16)
    random.seed(hash_seed)

    # Generate stats
    stats = {
        "health": random.randint(50, 100) + level * 10,
        "attack": random.randint(10, 20) + level * 2,
        "defense": random.randint(5, 15) + level * 2,
    }

    # Define attacks based on element
    element_attacks = {
        "earth": ["Rock Throw", "Earthquake", "Mud Slide"],
        "water": ["Water Jet", "Tsunami", "Rain Dance"],
        "fire": ["Fireball", "Flame Burst", "Inferno"],
        "wind": ["Gust", "Tornado", "Air Slash"],
        "death": ["Soul Drain", "Necrotic Touch", "Deathly Howl"],
    }

    attacks = random.sample(element_attacks[element], k=2)

    return {
        "name": name,
        "species": species,
        "element": element,
        "level": level,
        "description": description
        or f"A fearsome {species} with mastery over {element} elements.",
        "stats": stats,
        "attacks": attacks,
    }


from typing import Dict, Union


def cues_used(pro_name: str) -> Dict[str, Union[str, list]]:
    """Find the type of pool cue used by a specific pool pro.

    Args:
        pro_name: Name of the pro

    Returns:
        Dict containing:
            - pro_name: Name of the pool pro
            - cue_brands: List of cue brands used by the pro
    """

    sample_data = {
        "Efren Reyes": ["Predator", "Mezz"],
        "Allison Fisher": ["Cuetec", "McDermott"],
        "Shane Van Boening": ["Cuetec", "Predator"],
        "Jeanette Lee": ["Scorpion", "Viking"],
    }

    if pro_name not in sample_data:
        raise ValueError(f"Pro name not supported: {pro_name}")

    return {
        "pro_name": pro_name,
        "cue_brands": sample_data[pro_name],
    }


from typing import Dict, List, Literal, Union


def customize_avatar(
    avatar_name: str,
    body_type: Literal[
        "human", "robot", "animal", "fantasy_creature", "abstract"
    ] = "human",
    special_abilities: List[str] = [],
    color_scheme: str = "#0066CC",
) -> Dict[str, Union[str, List[str]]]:
    """Modify user's virtual avatar appearance and abilities.

    Args:
        avatar_name: Name for this avatar configuration
        body_type: Basic avatar form ('human', 'robot', 'animal', 'fantasy_creature', 'abstract')
        special_abilities: Special powers or abilities for the avatar
        color_scheme: Primary color scheme (hex codes or names)

    Returns:
        Dict containing:
            - avatar_name: Name for this avatar configuration
            - body_type: Basic avatar form
            - special_abilities: List of special powers or abilities
            - color_scheme: Primary color scheme
            - description: A brief description of the avatar
    """
    if not avatar_name:
        raise ValueError("avatar_name is required")

    descriptions = {
        "human": "A versatile and adaptable form, perfect for any situation.",
        "robot": "A mechanical marvel with precision and strength.",
        "animal": "Embodies the spirit and agility of the wild.",
        "fantasy_creature": "A mystical being with magical powers.",
        "abstract": "An enigmatic form that defies conventional understanding.",
    }

    description = descriptions.get(body_type, "An undefined avatar form.")

    return {
        "avatar_name": avatar_name,
        "body_type": body_type,
        "special_abilities": special_abilities,
        "color_scheme": color_scheme,
        "description": description,
    }


from typing import Dict


def games_to_duo(
    rank_1: int, points_1: int, rank_2: int, points_2: int
) -> Dict[str, int]:
    """Calculate the number of consecutive games a player needs to win to duo with another player.

    Args:
        rank_1: The rank of the first player (1-20).
        points_1: The current number of points player one has within their rank.
        rank_2: The rank of the second player (1-20).
        points_2: The current number of points player two has within their rank.

    Returns:
        Dict containing:
            - games_needed: Number of games player one needs to win consecutively to duo with player two.
    """

    if not (1 <= rank_1 <= 20) or not (1 <= rank_2 <= 20):
        raise ValueError("Ranks must be between 1 and 20.")
    if not (0 <= points_1 <= 100) or not (0 <= points_2 <= 100):
        raise ValueError("Points must be between 0 and 100.")

    # Calculate the rank difference
    rank_difference = rank_2 - rank_1

    # Calculate the points difference
    points_difference = points_2 - points_1

    # Assume each win gives a fixed number of points, e.g., 20 points
    points_per_win = 20

    # Calculate total points needed to reach the target rank and points
    total_points_needed = rank_difference * 100 + points_difference

    # Calculate the number of games needed
    games_needed = max(0, (total_points_needed + points_per_win - 1) // points_per_win)

    return {"games_needed": games_needed}


from typing import Dict, List, Literal, Union


def get_best_players_for_position(
    position: Literal[
        "LeftWing",
        "LeftBack",
        "PlayMaker",
        "Pivot",
        "RightBack",
        "RightWing",
        "Goalkeeper",
    ],
    age_group: Literal["U8", "U10", "U12", "U14", "U16", "U18", "Adult"],
    gender: Literal["Male", "Female"],
    only_available: bool,
    min_skill_score: float = 0,
    max_results: int = 10,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Get the best players for a specific position based on their position-specific skill scores.

    Args:
        position: Position to find the best players for
        age_group: Filter by age group
        gender: Filter by gender
        only_available: Only return players who are currently available
        min_skill_score: Minimum skill score required for the position (0-10)
        max_results: Maximum number of players to return

    Returns:
        Dict containing:
            - position: The position queried
            - players: List of players with their details
    """
    # Sample data for demonstration purposes
    sample_players = [
        {
            "name": "Alex Johnson",
            "age": 15,
            "gender": "Male",
            "position": "LeftWing",
            "skill_score": 8.5,
            "available": True,
        },
        {
            "name": "Jamie Smith",
            "age": 17,
            "gender": "Female",
            "position": "Goalkeeper",
            "skill_score": 9.0,
            "available": False,
        },
        {
            "name": "Sam Lee",
            "age": 12,
            "gender": "Male",
            "position": "PlayMaker",
            "skill_score": 7.5,
            "available": True,
        },
        {
            "name": "Taylor Brown",
            "age": 20,
            "gender": "Female",
            "position": "Pivot",
            "skill_score": 8.0,
            "available": True,
        },
        {
            "name": "Jordan White",
            "age": 14,
            "gender": "Male",
            "position": "RightBack",
            "skill_score": 6.5,
            "available": True,
        },
    ]

    # Filter players based on the criteria
    filtered_players = [
        player
        for player in sample_players
        if player["position"] == position
        and player["age"] <= int(age_group[1:])  # Extract age limit from age_group
        and player["gender"] == gender
        and player["skill_score"] >= min_skill_score
        and (not only_available or player["available"])
    ]

    # Sort players by skill score in descending order
    sorted_players = sorted(
        filtered_players, key=lambda x: x["skill_score"], reverse=True
    )

    # Limit the number of results
    top_players = sorted_players[:max_results]

    return {"position": position, "players": top_players}


from typing import Dict, Union


def get_blu_ray_game_information(game_name: str) -> Dict[str, Union[str, List[str]]]:
    """Get information about a specific blu-ray game title.

    Args:
        game_name: The name of the game to get information about

    Returns:
        Dict containing:
            - game_name: The name of the game
            - genre: The genre of the game
            - certification: The age certification of the game
            - director: The director of the game
            - platforms: List of platforms the game is available on
    """

    sample_data = {
        "The Last of Us": {
            "genre": "Action-adventure",
            "certification": "Mature 17+",
            "director": "Neil Druckmann",
            "platforms": ["PlayStation 4", "PlayStation 5"],
        },
        "Halo Infinite": {
            "genre": "First-person shooter",
            "certification": "Teen",
            "director": "Joseph Staten",
            "platforms": ["Xbox One", "Xbox Series X/S", "PC"],
        },
        "God of War": {
            "genre": "Action-adventure",
            "certification": "Mature 17+",
            "director": "Cory Barlog",
            "platforms": ["PlayStation 4", "PlayStation 5"],
        },
    }

    if game_name not in sample_data:
        raise ValueError(f"Game not supported: {game_name}")

    game_info = sample_data[game_name]
    return {
        "game_name": game_name,
        "genre": game_info["genre"],
        "certification": game_info["certification"],
        "director": game_info["director"],
        "platforms": game_info["platforms"],
    }


from typing import Dict, Union


def get_loot(
    avg_level: float, number_of_enemies: int = 1
) -> Dict[str, Union[int, float, str]]:
    """Get loot depending on the number and level of the enemies.

    Args:
        avg_level: Average level of the encountered enemies.
        number_of_enemies: Number of encountered enemies.

    Returns:
        Dict containing:
            - gold: Amount of gold collected
            - items: Number of items collected
            - rarity: Rarity level of the loot
    """
    if avg_level < 0:
        raise ValueError("Average level must be non-negative")
    if number_of_enemies < 1:
        raise ValueError("Number of enemies must be at least 1")

    # Simulate loot generation based on avg_level and number_of_enemies
    base_gold = int(avg_level * 10)
    base_items = int(avg_level / 2)
    rarity_levels = ["common", "uncommon", "rare", "epic", "legendary"]

    gold = base_gold * number_of_enemies
    items = base_items * number_of_enemies
    rarity_index = min(int(avg_level // 10), len(rarity_levels) - 1)
    rarity = rarity_levels[rarity_index]

    return {
        "gold": gold,
        "items": items,
        "rarity": rarity,
    }


from typing import Dict, List, Literal, Union


def get_recommended_discounted_steam_games(
    genre: Literal[
        "ACTION",
        "ROLE_PLAYING",
        "STRATEGY",
        "ADVENTURE",
        "SIMULATION",
        "SPORTS_&_RACING",
    ],
    discount: float = 0,
    min_price: float = 0,
    max_price: float = 0,
    platforms: List[Literal["WINDOWS", "MACOS", "LINUX/STEAMOS"]] = ["WINDOWS"],
    players: List[Literal["SINGLEPLAYER", "ONLINE_MULTIPLAYER", "LOCAL_COOP"]] = None,
    limit: int = 50,
    sort_by: Literal["POPULARITY", "PRICE", "ALPHANUMERIC"] = "POPULARITY",
) -> Dict[str, Union[str, List[Dict[str, Union[str, float, List[str]]]]]]:
    """Gets recommended games on the Steam platform that are on Special Discount Offers.

    Args:
        genre: Game genre to filter by.
        discount: Minimum discount percentage to filter games.
        min_price: Minimum price of the games.
        max_price: Maximum price of the games.
        platforms: Platforms the games must be compatible with.
        players: Player modes the games must support.
        limit: Maximum number of games to return.
        sort_by: Criteria to sort the games by.

    Returns:
        Dict containing:
            - genre: The genre of games requested.
            - games: List of games with details such as name, price, discount, platforms, and player modes.
    """
    sample_games = [
        {
            "name": "Action Game 1",
            "price": 19.99,
            "discount": 50,
            "platforms": ["WINDOWS"],
            "players": ["SINGLEPLAYER"],
        },
        {
            "name": "RPG Adventure",
            "price": 29.99,
            "discount": 60,
            "platforms": ["WINDOWS", "MACOS"],
            "players": ["ONLINE_MULTIPLAYER"],
        },
        {
            "name": "Strategy Master",
            "price": 9.99,
            "discount": 70,
            "platforms": ["LINUX/STEAMOS"],
            "players": ["LOCAL_COOP"],
        },
        {
            "name": "Sim Life",
            "price": 14.99,
            "discount": 30,
            "platforms": ["WINDOWS", "LINUX/STEAMOS"],
            "players": ["SINGLEPLAYER", "LOCAL_COOP"],
        },
        {
            "name": "Racing Pro",
            "price": 24.99,
            "discount": 40,
            "platforms": ["WINDOWS", "MACOS"],
            "players": ["ONLINE_MULTIPLAYER", "LOCAL_COOP"],
        },
    ]

    filtered_games = [
        game
        for game in sample_games
        if game["discount"] > discount
        and (min_price == 0 or game["price"] >= min_price)
        and (max_price == 0 or game["price"] <= max_price)
        and any(platform in game["platforms"] for platform in platforms)
        and (players is None or any(player in game["players"] for player in players))
    ]

    if sort_by == "PRICE":
        filtered_games.sort(key=lambda x: x["price"])
    elif sort_by == "ALPHANUMERIC":
        filtered_games.sort(key=lambda x: x["name"])

    return {"genre": genre, "games": filtered_games[:limit]}


from typing import Dict, Union


def get_schedule_I_game_stats(player_id: int) -> Dict[str, Union[str, int, float]]:
    """Get player stats for a given player_id in Schedule I.

    Args:
        player_id: Unique identifier for the player

    Returns:
        Dict containing:
            - player_id: The player's unique identifier
            - games_played: Number of games played in Schedule I
            - average_score: Average score per game
            - total_points: Total points scored in Schedule I
    """

    # Simulate some sample data based on player_id
    sample_data = {
        101: {"games_played": 15, "average_score": 22.5, "total_points": 337},
        202: {"games_played": 18, "average_score": 19.8, "total_points": 356},
        303: {"games_played": 20, "average_score": 25.1, "total_points": 502},
    }

    if player_id not in sample_data:
        raise ValueError(f"Player ID not found in Schedule I: {player_id}")

    player_stats = sample_data[player_id]

    return {
        "player_id": player_id,
        "games_played": player_stats["games_played"],
        "average_score": player_stats["average_score"],
        "total_points": player_stats["total_points"],
    }


from typing import Dict, Union


def get_star_craft_II_game_stats(user_id: int) -> Dict[str, Union[str, int, float]]:
    """Get player stats for a given player id in StarCraft II.

    Args:
        user_id: Unique identifier for the player

    Returns:
        Dict containing:
            - user_id: Player's unique identifier
            - player_name: Player's in-game name
            - wins: Number of games won
            - losses: Number of games lost
            - win_rate: Win rate percentage
    """

    # Simulated player data based on user_id
    player_data = {
        1: {"player_name": "ZergMaster", "wins": 150, "losses": 50},
        2: {"player_name": "ProtossPro", "wins": 120, "losses": 80},
        3: {"player_name": "TerranTactician", "wins": 200, "losses": 100},
    }

    if user_id not in player_data:
        raise ValueError(f"User ID not found: {user_id}")

    data = player_data[user_id]
    win_rate = (data["wins"] / (data["wins"] + data["losses"])) * 100

    return {
        "user_id": user_id,
        "player_name": data["player_name"],
        "wins": data["wins"],
        "losses": data["losses"],
        "win_rate": round(win_rate, 2),
    }


from typing import Dict, Union


def get_star_craft_I_game_stats(user_id: int) -> Dict[str, Union[str, int, float]]:
    """Get player stats for a given player id in StarCraft I.

    Args:
        user_id: Unique identifier for the player

    Returns:
        Dict containing:
            - user_id: The player's unique identifier
            - games_played: Total number of games played
            - win_rate: Player's win rate as a percentage
            - average_apm: Average Actions Per Minute of the player
            - favorite_race: The player's most played race
    """
    if user_id <= 0:
        raise ValueError("Invalid user_id: must be a positive integer")

    # Mock data generation based on user_id
    games_played = (user_id * 3) % 1000 + 50
    win_rate = ((user_id * 7) % 100) / 100
    average_apm = (user_id * 5) % 300 + 50
    races = ["Terran", "Zerg", "Protoss"]
    favorite_race = races[user_id % len(races)]

    return {
        "user_id": user_id,
        "games_played": games_played,
        "win_rate": win_rate,
        "average_apm": average_apm,
        "favorite_race": favorite_race,
    }


from typing import Dict, List, Literal, Union


def get_steam_games(
    name: str,
    genre: Literal[
        "ACTION",
        "ROLE_PLAYING",
        "STRATEGY",
        "ADVENTURE",
        "SIMULATION",
        "SPORTS_&_RACING",
    ] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Gets games and their details on the Steam platform that match the name input.

    Args:
        name: Game name to search for
        genre: Game genre to help narrow down the search (optional)

    Returns:
        Dict containing:
            - search_name: The name used for searching
            - games: List of dictionaries with game details, each containing:
                - title: Title of the game
                - genre: Genre of the game
                - release_year: Year the game was released
                - price: Price of the game in USD
    """

    sample_games = [
        {"title": "Action Hero", "genre": "ACTION", "release_year": 2021, "price": 29},
        {
            "title": "Role Play Saga",
            "genre": "ROLE_PLAYING",
            "release_year": 2019,
            "price": 49,
        },
        {
            "title": "Strategic Minds",
            "genre": "STRATEGY",
            "release_year": 2020,
            "price": 39,
        },
        {
            "title": "Adventure Quest",
            "genre": "ADVENTURE",
            "release_year": 2018,
            "price": 19,
        },
        {
            "title": "Simulate Life",
            "genre": "SIMULATION",
            "release_year": 2022,
            "price": 59,
        },
        {
            "title": "Racing Pro",
            "genre": "SPORTS_&_RACING",
            "release_year": 2021,
            "price": 24,
        },
    ]

    filtered_games = [
        game
        for game in sample_games
        if name.lower() in game["title"].lower()
        and (genre is None or game["genre"] == genre)
    ]

    if not filtered_games:
        raise ValueError(
            f"No games found matching the criteria: name='{name}', genre='{genre}'"
        )

    return {
        "search_name": name,
        "games": filtered_games,
    }


import hashlib
from typing import Dict, List, Literal, Union


def get_xp_records(
    rsn: str,
    game: Literal["osrs", "rs3"] = "rs3",
    skills: Union[List[str], str] = [],
    start_time: Union[int, None] = None,
    end_time: Union[int, None] = None,
) -> Dict[str, Union[str, Dict[str, int]]]:
    """Retrieve XP totals over a time period for a RuneScape player.

    Args:
        rsn: Runescape player's name
        game: 'osrs' or 'rs3'; defaults to 'rs3'
        skills: Skills to include (list of skill names or single skill name), defaults to all skills
        start_time: Start time to track XP gains
        end_time: End time to track XP gains

    Returns:
        Dict containing:
            - rsn: Player's RuneScape name
            - game: Game type ('osrs' or 'rs3')
            - xp_records: Dictionary of skills and their XP totals
    """
    if not rsn:
        raise ValueError("Player's name (rsn) is required")

    # Sample skills data
    all_skills = {
        "rs3": ["Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer"],
        "osrs": ["Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer"],
    }

    # Convert string skills to list if needed
    if isinstance(skills, str):
        skills = [skills]
    
    if not skills:
        skills = all_skills[game]

    xp_records = {}
    for skill in skills:
        # Generate a consistent but varied XP total using hash
        skill_hash = hashlib.md5(f"{rsn}-{skill}-{game}".encode()).hexdigest()
        xp_total = int(skill_hash[:8], 16) % 1000000  # XP total between 0 and 999,999
        xp_records[skill] = xp_total

    return {
        "rsn": rsn,
        "game": game,
        "xp_records": xp_records,
    }


from typing import Dict, Literal


def is_pokemon_available(pokemon_name: str, format: str = "gen9ou") -> Dict[str, bool]:
    """Check if a Pokémon is available in the given format.

    Args:
        pokemon_name: String containing the name of the Pokémon
        format: The given format the user wants information about (default is 'gen9ou')

    Returns:
        Dict containing:
            - pokemon_name: Name of the Pokémon
            - format: The format checked
            - available: Boolean indicating if the Pokémon is available in the format
    """

    # Sample data simulating Pokémon availability in different formats
    availability_data = {
        "gen9ou": {"Pikachu": True, "Charizard": True, "Bulbasaur": False},
        "gen8ou": {"Pikachu": True, "Charizard": False, "Bulbasaur": True},
        "gen7ou": {"Pikachu": False, "Charizard": True, "Bulbasaur": True},
    }

    if format not in availability_data:
        raise ValueError(f"Format not supported: {format}")

    available = availability_data[format].get(pokemon_name, False)

    return {
        "pokemon_name": pokemon_name,
        "format": format,
        "available": available,
    }


from typing import Dict, List, Literal, Union


def join_texas_cash_game(
    playerID: str,
    blinds: Union[List[Literal[1, 2, 5, 10]], str],
    buyInAmount: float,
    playerBalance: float,
    ipAddress: str,
    seatPreference: int = None,
) -> Dict[str, Union[str, float, int, List[int]]]:
    """Allows a player to join an existing Texas Hold'em poker cash game.

    Args:
        playerID: The player's 8 digit identification number (e.g. 98712365)
        blinds: The small and big blind amounts in US dollars. Can be provided as a list [1, 2], a dash-separated string '1-2', or a string representation of a list '[1, 2]'
        buyInAmount: The amount of money the player wants to buy-in to the game with
        playerBalance: The player's current account balance
        ipAddress: The player's current IP address at the time they attempt to join the table
        seatPreference: The player's preferred seat position at the table

    Returns:
        Dict containing:
            - playerID: The player's identification number
            - tableID: The identification number of the table joined
            - seatNumber: The seat number assigned to the player
            - blinds: The small and big blind amounts
            - buyInAmount: The buy-in amount for the game
            - remainingBalance: The player's remaining balance after buy-in
    """

    # Convert blinds parameter if it's a string
    if isinstance(blinds, str):
        # Handle dash-separated format like '5-10'
        if '-' in blinds:
            try:
                blind_values = [int(val.strip()) for val in blinds.split('-')]
                blinds = blind_values
            except ValueError:
                raise ValueError("Invalid blinds format. Expected format like '5-10'")
        # Handle string representation of a list like '[5, 10]' or '['5', '10']'
        elif blinds.startswith('[') and blinds.endswith(']'):
            try:
                import ast
                blind_values = ast.literal_eval(blinds)
                if isinstance(blind_values, list):
                    # Convert string numbers to integers if needed
                    blinds = [int(val) if isinstance(val, str) else val for val in blind_values]
                else:
                    raise ValueError("Invalid blinds format. Expected a list.")
            except (ValueError, SyntaxError):
                raise ValueError("Invalid blinds format. Expected a valid list.")
        else:
            raise ValueError("Invalid blinds format. Expected format like '5-10' or '[5, 10]'")
    
    # Validate that all blinds values are allowed
    allowed_values = [1, 2, 5, 10]
    if not all(val in allowed_values for val in blinds):
        raise ValueError(f"Blind values must be one of {allowed_values}")

    if buyInAmount < 50 or buyInAmount > 1000:
        raise ValueError("Buy-in amount must be between $50 and $1000.")

    if playerBalance < buyInAmount:
        raise ValueError("Insufficient balance for the buy-in amount.")

    # Simulate table ID and seat assignment
    tableID = hash((playerID, blinds, ipAddress)) % 10000
    seatNumber = seatPreference if seatPreference else (hash(ipAddress) % 9) + 1

    return {
        "playerID": playerID,
        "tableID": tableID,
        "seatNumber": seatNumber,
        "blinds": blinds,
        "buyInAmount": buyInAmount,
        "remainingBalance": playerBalance - buyInAmount,
    }


from typing import Dict, Union


def league_stats(
    year: int, incl_playoffs: bool = True
) -> Dict[str, Union[int, Dict[str, Union[int, float]]]]:
    """Retrieve league-wide records for a given year.

    Args:
        year: The season year to retrieve stats for.
        incl_playoffs: Whether to include playoff stats in the results.

    Returns:
        Dict containing:
            - year: The season year
            - stats: A dictionary with league-wide statistics including:
                - total_games: Total number of games played
                - average_points: Average points scored per game
                - average_attendance: Average attendance per game
    """

    # Simulated data based on year and incl_playoffs
    base_games = 1230  # Regular season games in a typical league
    playoff_games = 82  # Example number of playoff games
    total_games = base_games + (playoff_games if incl_playoffs else 0)

    # Generate consistent but varied sample data using a hash of the year
    hash_seed = hash(year) % 100
    average_points = 100 + (hash_seed % 10)  # Average points vary slightly
    average_attendance = 17000 + (hash_seed % 2000)  # Attendance varies

    return {
        "year": year,
        "stats": {
            "total_games": total_games,
            "average_points": average_points,
            "average_attendance": average_attendance,
        },
    }


import hashlib
from typing import Dict, Literal, Union


def log_xp_gain(
    rsn: str,
    skill: str,
    gained_xp: float,
    time_stamp: str,
    game: Literal["osrs", "rs3"] = "rs3",
) -> Dict[str, Union[str, float]]:
    """Record xp gain for a Runescape account.

    Args:
        rsn: Runescape player's name
        skill: Skill name
        gained_xp: Amount of xp gained in the skill
        time_stamp: Time when xp was gained
        game: 'osrs' or 'rs3', defaults to 'rs3'

    Returns:
        Dict containing:
            - rsn: Runescape player's name
            - skill: Skill name
            - gained_xp: Amount of xp gained
            - time_stamp: Time when xp was gained
            - game: Game type ('osrs' or 'rs3')
            - log_id: Unique identifier for the log entry
    """
    if not rsn or not skill or gained_xp is None or not time_stamp:
        raise ValueError("Missing required parameters")

    # Generate a unique log ID using a hash of the input data
    log_id = hashlib.md5(
        f"{rsn}{skill}{gained_xp}{time_stamp}{game}".encode()
    ).hexdigest()

    return {
        "rsn": rsn,
        "skill": skill,
        "gained_xp": gained_xp,
        "time_stamp": time_stamp,
        "game": game,
        "log_id": log_id,
    }


from typing import Dict, Literal


def manage_spells(
    level: int, action: Literal["cast", "restore", "reset"]
) -> Dict[str, Union[int, str, Dict[int, int]]]:
    """Tracks spell slots and manages spellcasting for the character.

    Args:
        level: The spell level being cast or updated.
        action: The action to take: 'cast' to use a slot, 'restore' to regain a slot, 'reset' to refresh all slots.

    Returns:
        Dict containing:
            - action: The action performed
            - level: The spell level affected
            - slots: A dictionary of remaining slots by level
    """
    # Sample spell slots for a character
    spell_slots = {1: 4, 2: 3, 3: 3, 4: 2, 5: 1}

    if action == "cast":
        if level not in spell_slots or spell_slots[level] <= 0:
            raise ValueError(f"No available slots to cast a level {level} spell.")
        spell_slots[level] -= 1
    elif action == "restore":
        if level not in spell_slots:
            raise ValueError(f"Invalid spell level: {level}")
        spell_slots[level] += 1
    elif action == "reset":
        spell_slots = {1: 4, 2: 3, 3: 3, 4: 2, 5: 1}
    else:
        raise ValueError(f"Unsupported action: {action}")

    return {
        "action": action,
        "level": level,
        "slots": spell_slots,
    }


from typing import Dict


def moral_alignment_description(moral_alignment: str) -> Dict[str, str]:
    """Return a description of the inputted moral alignment.

    Args:
        moral_alignment: The moral alignment type that the user wants a description of.

    Returns:
        Dict containing:
            - alignment: The moral alignment type
            - description: A brief description of the moral alignment
    """

    descriptions = {
        "Lawful Good": "Acts as a good person is expected or required to act.",
        "Neutral Good": "Does the best that a good person can do.",
        "Chaotic Good": "Acts as their conscience directs, with little regard for what others expect.",
        "Lawful Neutral": "Acts as law, tradition, or a personal code directs.",
        "True Neutral": "Does what seems to be a balanced approach.",
        "Chaotic Neutral": "Follows their whims, holding their personal freedom above all else.",
        "Lawful Evil": "Methodically takes what they want within the limits of a code of conduct.",
        "Neutral Evil": "Does whatever they can get away with, without compassion or qualms.",
        "Chaotic Evil": "Acts with arbitrary violence, spurred by greed, hatred, or bloodlust.",
    }

    if moral_alignment not in descriptions:
        raise ValueError(f"Unsupported moral alignment: {moral_alignment}")

    return {
        "alignment": moral_alignment,
        "description": descriptions[moral_alignment],
    }


from typing import Dict, Union


def player_stats(
    name: str, incl_playoffs: bool = True
) -> Dict[str, Union[str, int, float]]:
    """Retrieve individual stats for a player.

    Args:
        name: Player name (e.g. 'LeBron James', 'Lionel Messi')
        incl_playoffs: Include playoff stats if True, otherwise only regular season

    Returns:
        Dict containing:
            - name: Player's name
            - games_played: Total number of games played
            - points_per_game: Average points scored per game
            - assists_per_game: Average assists made per game
            - rebounds_per_game: Average rebounds per game
    """

    # Sample data based on player name hash for consistency
    sample_data = {
        "LeBron James": {
            "games_played": 82,
            "points_per_game": 27.2,
            "assists_per_game": 7.4,
            "rebounds_per_game": 7.9,
        },
        "Lionel Messi": {
            "games_played": 50,
            "points_per_game": 1.1,
            "assists_per_game": 0.3,
            "rebounds_per_game": 0.0,  # Not applicable for soccer, but included for consistency
        },
    }

    if name not in sample_data:
        raise ValueError(f"Player not found: {name}")

    stats = sample_data[name]

    if incl_playoffs:
        # Adjust stats to include playoffs
        stats = {k: v * 1.1 for k, v in stats.items()}

    return {
        "name": name,
        "games_played": int(stats["games_played"]),
        "points_per_game": round(stats["points_per_game"], 1),
        "assists_per_game": round(stats["assists_per_game"], 1),
        "rebounds_per_game": round(stats["rebounds_per_game"], 1),
    }


from typing import Dict, List, Union


def rc_trackmeets(
    postcode: str, radius: float = 5
) -> Dict[str, Union[str, float, List[Dict[str, Union[str, float]]]]]:
    """Find radio controlled car groups and tracks near a given postcode.

    Args:
        postcode: The postcode or outcode to center the search on.
        radius: The search radius in miles around the central postcode.

    Returns:
        Dict containing:
            - postcode: The central postcode for the search
            - radius: The search radius in miles
            - tracks: List of nearby tracks with details
                - name: Name of the track
                - distance: Distance from the central postcode in miles
                - address: Address of the track
    """

    # Sample data based on hash of postcode for consistent but varied results
    sample_tracks = {
        "12345": [
            {
                "name": "Speedway RC Track",
                "distance": 3.2,
                "address": "123 RC Lane, Toytown",
            },
            {
                "name": "Fast Wheels Arena",
                "distance": 4.5,
                "address": "456 Model Ave, Toytown",
            },
        ],
        "67890": [
            {
                "name": "Mini Racers Circuit",
                "distance": 2.8,
                "address": "789 Hobby St, Modelville",
            },
            {
                "name": "RC Fun Park",
                "distance": 5.0,
                "address": "1011 Play Rd, Modelville",
            },
        ],
    }

    # Generate a hash-based key to simulate varied data
    key = str(abs(hash(postcode)) % 100000)

    if key not in sample_tracks:
        raise ValueError(f"No tracks found for postcode: {postcode}")

    return {
        "postcode": postcode,
        "radius": radius,
        "tracks": sample_tracks[key],
    }


import random
import re
from typing import Dict, Union


def roll_dice(dice: str) -> Dict[str, Union[int, str]]:
    """Roll one or more dice with an optional modifier.

    Args:
        dice: The dice expression to roll, e.g. '1d20+5', '3d6', etc.

    Returns:
        Dict containing:
            - expression: The original dice expression
            - result: The total result after rolling the dice and applying modifiers
    """
    match = re.fullmatch(r"(\d+)d(\d+)([+-]\d+)?", dice)
    if not match:
        raise ValueError(f"Invalid dice expression: {dice}")

    num_dice, dice_sides, modifier = match.groups()
    num_dice = int(num_dice)
    dice_sides = int(dice_sides)
    modifier = int(modifier) if modifier else 0

    if num_dice <= 0 or dice_sides <= 0:
        raise ValueError("Number of dice and sides must be positive integers")

    rolls = [random.randint(1, dice_sides) for _ in range(num_dice)]
    total = sum(rolls) + modifier

    return {
        "expression": dice,
        "result": total,
    }


from typing import Dict, List


def schedule_game(
    time: str, friends: List[int], game_name: str
) -> Dict[str, Union[str, List[int]]]:
    """Schedule a game invite with friends.

    Args:
        time: The time to schedule the game invite (e.g. '2023-10-15T18:00:00Z')
        friends: An array of player_ids to send invites to
        game_name: The name of the game players are invited to play

    Returns:
        Dict containing:
            - scheduled_time: The time the game is scheduled for
            - invited_friends: List of player_ids who were invited
            - game: The name of the game scheduled
    """
    if not time or not friends or not game_name:
        raise ValueError(
            "All parameters 'time', 'friends', and 'game_name' are required."
        )

    if not isinstance(friends, list) or not all(
        isinstance(friend, int) for friend in friends
    ):
        raise TypeError("Friends must be a list of player_ids (integers).")

    # Simulate scheduling logic
    scheduled_time = time
    invited_friends = friends
    game = game_name

    return {
        "scheduled_time": scheduled_time,
        "invited_friends": invited_friends,
        "game": game,
    }


from typing import Dict, List


def schedule_game_now(
    friends: List[int], game_name: str
) -> Dict[str, Union[str, List[int]]]:
    """Send out a game invite immediately to a list of friends.

    Args:
        friends: Array of player_ids to send invites to
        game_name: Game players are invited to play

    Returns:
        Dict containing:
            - game_name: Name of the game
            - invited_friends: List of player_ids who received the invite
            - status: Status of the invite process
    """

    if not friends:
        raise ValueError("Friends list cannot be empty")
    if not game_name:
        raise ValueError("Game name cannot be empty")

    # Simulate sending invites by hashing player_ids with game_name
    invited_friends = [
        friend_id for friend_id in friends if hash((friend_id, game_name)) % 2 == 0
    ]

    return {
        "game_name": game_name,
        "invited_friends": invited_friends,
        "status": "Invites sent successfully" if invited_friends else "No invites sent",
    }


from typing import Dict, List, Literal, Union


def search_players(
    age_group: Literal["U8", "U10", "U12", "U14", "U16", "U18", "Adult"],
    gender: Literal["Male", "Female"],
    position: Literal[
        "LeftWing",
        "LeftBack",
        "PlayMaker",
        "Pivot",
        "RightBack",
        "RightWing",
        "Goalkeeper",
    ] = None,
    min_skill_level: int = 1,
    min_position_skill: int = 0,
    only_available: bool = True,
    sort_by: Literal[
        "skill_level", "position_skill", "name", "availability"
    ] = "position_skill",
) -> List[Dict[str, Union[str, int, bool]]]:
    """Search for players based on age group, gender, and position criteria.

    Args:
        age_group: Target age group for the team.
        gender: Target gender for the team.
        position: Specific position to search for.
        min_skill_level: Minimum overall skill level required (1-10).
        min_position_skill: Minimum skill level required for the specific position (0-10).
        only_available: Only return players who are currently available.
        sort_by: Sort results by specific criteria.

    Returns:
        List of dictionaries, each containing:
            - name: Player's name
            - age_group: Player's age group
            - gender: Player's gender
            - position: Player's position
            - skill_level: Player's overall skill level
            - position_skill: Player's skill level for the specific position
            - available: Player's availability status
    """
    sample_players = [
        {
            "name": "Alex Johnson",
            "age_group": "U14",
            "gender": "Male",
            "position": "LeftWing",
            "skill_level": 7,
            "position_skill": 8,
            "available": True,
        },
        {
            "name": "Jamie Smith",
            "age_group": "U16",
            "gender": "Female",
            "position": "Goalkeeper",
            "skill_level": 9,
            "position_skill": 9,
            "available": False,
        },
        {
            "name": "Taylor Brown",
            "age_group": "U12",
            "gender": "Male",
            "position": "PlayMaker",
            "skill_level": 6,
            "position_skill": 7,
            "available": True,
        },
        {
            "name": "Jordan Lee",
            "age_group": "Adult",
            "gender": "Female",
            "position": "Pivot",
            "skill_level": 8,
            "position_skill": 8,
            "available": True,
        },
        {
            "name": "Morgan Davis",
            "age_group": "U18",
            "gender": "Male",
            "position": "RightBack",
            "skill_level": 5,
            "position_skill": 6,
            "available": True,
        },
    ]

    filtered_players = [
        player
        for player in sample_players
        if player["age_group"] == age_group
        and player["gender"] == gender
        and (position is None or player["position"] == position)
        and player["skill_level"] >= min_skill_level
        and player["position_skill"] >= min_position_skill
        and (not only_available or player["available"])
    ]

    return sorted(filtered_players, key=lambda x: x[sort_by])


from typing import Dict, Literal


def select_game(
    playerID: str,
    sufficientBalance: bool,
    gameSelection: Literal[
        "texas holdem", "omaha", "stud", "blackjack", "craps", "roulette", "slots"
    ],
) -> Dict[str, str]:
    """Allow the player to select a casino game to play.

    Args:
        playerID: The player's 8 digit identification number (e.g. 98712365)
        sufficientBalance: If 'True' the player has a balance greater than $10 USD so they are eligible to play
        gameSelection: The player's game selection

    Returns:
        Dict containing:
            - playerID: The player's identification number
            - gameSelected: The game the player has selected
            - status: Confirmation message about the game selection
    """
    if len(playerID) != 8 or not playerID.isdigit():
        raise ValueError("Invalid playerID: Must be an 8 digit number")

    if not sufficientBalance:
        return {
            "playerID": playerID,
            "gameSelected": gameSelection,
            "status": "Insufficient balance to play",
        }

    return {
        "playerID": playerID,
        "gameSelected": gameSelection,
        "status": f"Game '{gameSelection}' selected successfully",
    }


from typing import Dict, Literal, Optional


def send_chat_message(
    playerID: str,
    tableID: str,
    comChannel: Literal["private", "public"],
    messageContent: str,
    recipientName: Optional[str] = None,
) -> Dict[str, str]:
    """Send a chat message to other players at the poker table.

    Args:
        playerID: The player's 8-digit identification number (e.g. 98712365)
        tableID: The 4-digit alphanumeric code of the table the player is currently sitting at (e.g. AP93)
        comChannel: The player's choice of whether their message is broadcasted privately to a single player or publicly to the entire table
        messageContent: The message that the player would like to broadcast (e.g. You are going down!)
        recipientName: The username of the player that the private message will be sent to (e.g. hannibal barca)

    Returns:
        Dict containing:
            - status: Status of the message sending process
            - message: The content of the message sent
            - recipient: The recipient of the message
    """
    if comChannel == "private" and not recipientName:
        raise ValueError("Recipient name must be provided for private messages.")

    # Simulate message sending
    status = "success"
    recipient = recipientName if comChannel == "private" else "all players at the table"

    return {
        "status": status,
        "message": messageContent,
        "recipient": recipient,
    }


from typing import Dict, Literal, Union


def site_registration(
    playerName: str,
    playerEmail: str,
    playerPhone: str,
    playerDOB: str,
    playerNationality: str,
    playerVerificationMethod: Literal["driver license", "passport", "national id"],
    driverLicenseNo: str = "",
    passportNo: str = "",
    nationalIDNo: str = "",
) -> Dict[str, Union[str, bool]]:
    """Register a player for an account on the casino website.

    Args:
        playerName: The full name of the player in lowercase letters (e.g. 'julius caesar')
        playerEmail: The player's email address (e.g. 'j.caesar@yahoo.com')
        playerPhone: The player's phone number (e.g. '+64228871874')
        playerDOB: The player's date of birth in YYYY-MM-DD format (e.g. '1989-06-04')
        playerNationality: The player's nationality (e.g. 'New Zealander')
        playerVerificationMethod: Method the player would like to use to prove their identity
        driverLicenseNo: The player's driver license number (e.g. 'PW589120')
        passportNo: The player's passport number (e.g. 'RA000750')
        nationalIDNo: The player's national identification number (e.g. 'C23454390')

    Returns:
        Dict containing:
            - playerName: The registered player's name
            - registrationStatus: Boolean indicating if registration was successful
            - verificationStatus: Boolean indicating if verification was successful
    """
    if playerVerificationMethod == "driver license" and not driverLicenseNo:
        raise ValueError(
            "Driver license number is required for verification method 'driver license'."
        )
    if playerVerificationMethod == "passport" and not passportNo:
        raise ValueError(
            "Passport number is required for verification method 'passport'."
        )
    if playerVerificationMethod == "national id" and not nationalIDNo:
        raise ValueError(
            "National ID number is required for verification method 'national id'."
        )

    # Simulate registration and verification process
    registration_success = hash(playerEmail) % 2 == 0
    verification_success = hash(playerPhone) % 2 == 0

    return {
        "playerName": playerName,
        "registrationStatus": registration_success,
        "verificationStatus": verification_success,
    }


import random
from typing import Dict


def throw_dice(d: int, number_of_dice: int = 1, modifier: int = 0) -> Dict[str, int]:
    """Simulate throwing dice and calculate the total result with a modifier.

    Args:
        d: Number of sides on a die.
        number_of_dice: Number of dice to throw.
        modifier: Modifier to add to the result after all dice are thrown.

    Returns:
        Dict containing:
            - total: The total result after throwing the dice and adding the modifier.
            - rolls: The list of individual dice roll results.
            - modifier: The modifier that was added to the total.
    """
    if d <= 0:
        raise ValueError("Number of sides on a die must be positive.")
    if number_of_dice <= 0:
        raise ValueError("Number of dice must be positive.")

    rolls = [random.randint(1, d) for _ in range(number_of_dice)]
    total = sum(rolls) + modifier

    return {"total": total, "rolls": rolls, "modifier": modifier}


from typing import Dict, Union


def track_hit_points(
    change: float, max_hp: Union[float, None] = None
) -> Dict[str, Union[float, str]]:
    """Adjust and track the character's current and maximum hit points.

    Args:
        change: The amount to add or subtract from current hit points (negative for damage, positive for healing).
        max_hp: Optional new maximum hit points if they change (e.g., from level-up or effects).

    Returns:
        Dict containing:
            - current_hp: Updated current hit points after applying the change
            - max_hp: Updated maximum hit points if provided, otherwise unchanged
            - status: Status of the character ('alive' or 'unconscious')
    """
    # Sample initial hit points for demonstration
    initial_current_hp = 50.0
    initial_max_hp = 100.0

    # Update maximum hit points if a new value is provided
    if max_hp is not None:
        if max_hp < 0:
            raise ValueError("Maximum hit points cannot be negative")
        initial_max_hp = max_hp

    # Calculate new current hit points
    new_current_hp = initial_current_hp + change
    if new_current_hp > initial_max_hp:
        new_current_hp = initial_max_hp
    elif new_current_hp < 0:
        new_current_hp = 0

    # Determine character status
    status = "alive" if new_current_hp > 0 else "unconscious"

    return {
        "current_hp": new_current_hp,
        "max_hp": initial_max_hp,
        "status": status,
    }


from typing import Dict, List, Union


def trade_items(
    player1_id: str,
    player1_items: List[str],
    player2_id: str,
    player2_items: List[str],
) -> Dict[str, Union[str, List[str]]]:
    """Trade items between two players, validating ownership, rarity, and inventory space.

    Args:
        player1_id: ID of the first player in the trade.
        player1_items: Item IDs offered by the first player.
        player2_id: ID of the second player in the trade.
        player2_items: Item IDs offered by the second player.

    Returns:
        Dict containing:
            - player1_id: ID of the first player
            - player2_id: ID of the second player
            - player1_new_items: New inventory of player 1 after the trade
            - player2_new_items: New inventory of player 2 after the trade
    """

    # Mock data for player inventories and item rarities
    player_inventories = {
        "player1": ["sword", "shield", "potion"],
        "player2": ["bow", "arrow", "potion"],
    }
    item_rarities = {
        "sword": "common",
        "shield": "rare",
        "potion": "common",
        "bow": "uncommon",
        "arrow": "common",
    }
    max_inventory_size = 5

    # Validate ownership
    if not all(
        item in player_inventories.get(player1_id, []) for item in player1_items
    ):
        raise ValueError("Player 1 does not own all the items offered for trade.")
    if not all(
        item in player_inventories.get(player2_id, []) for item in player2_items
    ):
        raise ValueError("Player 2 does not own all the items offered for trade.")

    # Validate inventory space
    if (
        len(player_inventories[player1_id]) - len(player1_items) + len(player2_items)
        > max_inventory_size
    ):
        raise ValueError("Player 1 does not have enough inventory space for the trade.")
    if (
        len(player_inventories[player2_id]) - len(player2_items) + len(player1_items)
        > max_inventory_size
    ):
        raise ValueError("Player 2 does not have enough inventory space for the trade.")

    # Perform the trade
    new_player1_items = [
        item for item in player_inventories[player1_id] if item not in player1_items
    ] + player2_items
    new_player2_items = [
        item for item in player_inventories[player2_id] if item not in player2_items
    ] + player1_items

    return {
        "player1_id": player1_id,
        "player2_id": player2_id,
        "player1_new_items": new_player1_items,
        "player2_new_items": new_player2_items,
    }


import hashlib
from typing import Dict, Union


def update_player_availability(
    player_name: str,
    date_of_birth: str,
    available: bool,
    reason: str = "",
    return_date: Union[str, None] = None,
) -> Dict[str, Union[str, bool, None]]:
    """Update a player's availability status.

    Args:
        player_name: Name of the player to update
        date_of_birth: Player's date of birth in YYYY-MM-DD format
        available: Whether the player is available for selection
        reason: Reason for unavailability (injury, personal, etc.)
        return_date: Expected return date in YYYY-MM-DD format

    Returns:
        Dict containing:
            - player_name: Name of the player
            - date_of_birth: Player's date of birth
            - available: Availability status
            - reason: Reason for unavailability
            - return_date: Expected return date
    """
    # Simulate player database with a hash-based approach for consistency
    player_id = hashlib.md5(f"{player_name}{date_of_birth}".encode()).hexdigest()

    # Mock database of players
    players_db = {
        "a1b2c3d4e5f6g7h8i9j0": {
            "player_name": "John Doe",
            "date_of_birth": "1990-01-01",
            "available": True,
            "reason": "",
            "return_date": None,
        },
        "b2c3d4e5f6g7h8i9j0a1": {
            "player_name": "Jane Smith",
            "date_of_birth": "1985-05-15",
            "available": False,
            "reason": "injury",
            "return_date": "2023-11-01",
        },
    }

    if player_id not in players_db:
        raise ValueError(f"Player not found: {player_name} with DOB {date_of_birth}")

    # Update player information
    players_db[player_id].update(
        {
            "available": available,
            "reason": reason,
            "return_date": return_date,
        }
    )

    return players_db[player_id]


from typing import Dict, Literal, Union


def update_player_position_skill(
    player_name: str,
    date_of_birth: str,
    position: Literal[
        "LeftWing",
        "LeftBack",
        "PlayMaker",
        "Pivot",
        "RightBack",
        "RightWing",
        "Goalkeeper",
    ],
    skill_score: float,
) -> Dict[str, Union[str, float]]:
    """Update a player's skill score for a specific position.

    Args:
        player_name: Name of the player to update.
        date_of_birth: Player's date of birth in YYYY-MM-DD format (used for unique identification).
        position: Position to update the skill score for.
        skill_score: New skill score for this position (0-10).

    Returns:
        Dict containing:
            - player_name: Name of the player.
            - date_of_birth: Player's date of birth.
            - position: Position updated.
            - skill_score: Updated skill score.
    """
    if not (0 <= skill_score <= 10):
        raise ValueError("Skill score must be between 0 and 10.")

    # Simulate a database update operation
    # In a real scenario, this would involve database access logic
    player_data = {
        "player_name": player_name,
        "date_of_birth": date_of_birth,
        "position": position,
        "skill_score": skill_score,
    }

    # Mocked response simulating a successful update
    return player_data


from typing import Dict, List, Union


def war_model_shopper(
    postcode: str, radius: float = 5
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find retailers of miniature war figures for tabletop gaming or decoration.

    Args:
        postcode: The postcode or outcode to center the search on.
        radius: The search radius in miles around the central postcode.

    Returns:
        Dict containing:
            - postcode: The central postcode of the search
            - radius: The search radius in miles
            - retailers: List of retailers with:
                - name: Retailer name
                - address: Retailer address
                - distance: Distance from the central postcode in miles
    """

    # Sample data generation based on postcode hash
    sample_retailers = {
        "12345": [
            {
                "name": "Miniature World",
                "address": "123 Elm St, Springfield",
                "distance": 2.5,
            },
            {
                "name": "Battlefield Models",
                "address": "456 Oak St, Springfield",
                "distance": 4.0,
            },
        ],
        "67890": [
            {
                "name": "Warrior's Haven",
                "address": "789 Pine St, Shelbyville",
                "distance": 1.2,
            },
            {
                "name": "Figures & More",
                "address": "101 Maple St, Shelbyville",
                "distance": 3.8,
            },
        ],
    }

    # Hash-based selection for consistent but varied results
    postcode_hash = hash(postcode) % 2
    sample_keys = list(sample_retailers.keys())

    if postcode_hash >= len(sample_keys):
        raise ValueError(f"No retailers found for postcode: {postcode}")

    selected_key = sample_keys[postcode_hash]
    retailers = sample_retailers[selected_key]

    # Filter retailers by radius
    filtered_retailers = [
        retailer for retailer in retailers if retailer["distance"] <= radius
    ]

    if not filtered_retailers:
        raise ValueError(
            f"No retailers found within {radius} miles of postcode: {postcode}"
        )

    return {
        "postcode": postcode,
        "radius": radius,
        "retailers": filtered_retailers,
    }


from typing import Dict


def wins_to_duo(
    rank_1: int, points_1: int, rank_2: int, points_2: int
) -> Dict[str, int]:
    """Calculate the number of consecutive wins needed for a player to duo with another player of a different rank.

    Args:
        rank_1: The rank of the first player (1-20).
        points_1: The current points of the first player within their rank.
        rank_2: The rank of the second player (1-20).
        points_2: The current points of the second player within their rank.

    Returns:
        Dict containing:
            - wins_needed: Number of consecutive wins needed for player one to duo with player two.
    """
    if not (1 <= rank_1 <= 20) or not (1 <= rank_2 <= 20):
        raise ValueError("Ranks must be between 1 and 20.")
    if points_1 < 0 or points_2 < 0:
        raise ValueError("Points cannot be negative.")

    # Assume each win gives a fixed number of points, e.g., 100 points.
    points_per_win = 100

    # Calculate the total points needed for rank_1 to reach rank_2.
    rank_difference = rank_2 - rank_1
    points_needed = rank_difference * 1000 + (points_2 - points_1)

    if points_needed <= 0:
        return {"wins_needed": 0}

    # Calculate the number of wins needed.
    wins_needed = (points_needed + points_per_win - 1) // points_per_win

    return {"wins_needed": wins_needed}


from typing import Dict


def wins_to_match(
    rank_1: int, points_1: int, rank_2: int, points_2: int
) -> Dict[str, int]:
    """Calculate the number of consecutive wins needed for a player to meet or exceed another player's rank and points.

    Args:
        rank_1: The rank of the first player (1-20).
        points_1: The current points of the first player within their rank.
        rank_2: The rank to meet or beat (1-20).
        points_2: The points in the rank to meet or beat.

    Returns:
        Dict containing:
            - wins_needed: Number of consecutive wins required to meet or exceed the target rank and points.
    """
    if not (1 <= rank_1 <= 20) or not (1 <= rank_2 <= 1000):
        raise ValueError("Ranks must be between 1 and 1000.")
    if points_1 < 0 or points_2 < 0:
        raise ValueError("Points cannot be negative.")

    # Assume each win gives a fixed number of points, e.g., 10 points
    points_per_win = 10

    # Calculate total points needed to surpass the target
    total_points_1 = (20 - rank_1) * 100 + points_1
    total_points_2 = (20 - rank_2) * 100 + points_2

    if total_points_1 >= total_points_2:
        return {"wins_needed": 0}

    points_needed = total_points_2 - total_points_1
    wins_needed = (
        points_needed + points_per_win - 1
    ) // points_per_win  # Ceiling division

    return {"wins_needed": wins_needed}
