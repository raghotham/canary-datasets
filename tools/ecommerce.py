# Ecommerce Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Union


def add_to_cart(
    product_id: str, quantity: int = 1, options: Dict[str, str] = None
) -> Dict[str, Union[str, int, Dict[str, str]]]:
    """Add a selected product to the shopping cart with quantity and variation options.

    Args:
        product_id: Unique identifier of the product.
        quantity: Number of items to add. Defaults to 1.
        options: Product variations such as size or color. Defaults to an empty dictionary.

    Returns:
        Dict containing:
            - product_id: The product identifier
            - quantity: The number of items added
            - options: The selected product variations
            - message: Confirmation message of the addition
    """
    if not product_id:
        raise ValueError("Product ID is required")

    if quantity <= 0:
        raise ValueError("Quantity must be at least 1")

    if options is None:
        options = {}

    # Simulate adding to cart with a confirmation message
    return {
        "product_id": product_id,
        "quantity": quantity,
        "options": options,
        "message": f"Added {quantity} of product {product_id} to cart with options {options}",
    }


from typing import Dict


def checkout(
    cart_id: str, notification: bool = False
) -> Dict[str, Union[str, bool, float]]:
    """Checkout with any items that are currently in the cart.

    Args:
        cart_id: Unique identifier of the shopping cart.
        notification: Send a notification to the user upon checking out.

    Returns:
        Dict containing:
            - cart_id: The cart ID used for checkout
            - total_amount: Total amount of the items in the cart
            - success: Whether the checkout was successful
            - notification_sent: Whether a notification was sent
    """

    # Simulated cart data based on cart_id hash
    cart_data = {
        "cart_123": 150.75,
        "cart_456": 89.99,
        "cart_789": 200.50,
    }

    if cart_id not in cart_data:
        raise ValueError(f"Cart ID not found: {cart_id}")

    total_amount = cart_data[cart_id]
    success = True  # Simulating a successful checkout process
    notification_sent = notification

    return {
        "cart_id": cart_id,
        "total_amount": total_amount,
        "success": success,
        "notification_sent": notification_sent,
    }


from typing import Dict, List, Optional, Union


def search_product(
    query: str,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: str = "relevance",
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]:
    """Search for products based on keywords, category, or filters such as price range.

    Args:
        query: Search term or product name.
        category: Product category to filter results (e.g., electronics, clothing).
        min_price: Minimum price filter.
        max_price: Maximum price filter.
        sort_by: Sort results by relevance, price, or rating.

    Returns:
        Dict containing:
            - query: The search query used
            - results: List of products with details such as product_name, product_id, description, price
    """
    sample_products = [
        {
            "product_name": "Wireless Mouse",
            "product_id": 101,
            "description": "Ergonomic wireless mouse",
            "price": 25.99,
            "category": "electronics",
        },
        {
            "product_name": "Bluetooth Headphones",
            "product_id": 102,
            "description": "Noise-cancelling headphones",
            "price": 89.99,
            "category": "electronics",
        },
        {
            "product_name": "Running Shoes",
            "product_id": 201,
            "description": "Comfortable running shoes",
            "price": 59.99,
            "category": "clothing",
        },
        {
            "product_name": "Smartphone",
            "product_id": 103,
            "description": "Latest model smartphone",
            "price": 699.99,
            "category": "electronics",
        },
        {
            "product_name": "T-shirt",
            "product_id": 202,
            "description": "Cotton t-shirt",
            "price": 15.99,
            "category": "clothing",
        },
    ]

    filtered_products = [
        product
        for product in sample_products
        if query.lower() in product["product_name"].lower()
        and (category is None or product["category"] == category)
        and (min_price is None or product["price"] >= min_price)
        and (max_price is None or product["price"] <= max_price)
    ]

    if sort_by == "price":
        filtered_products.sort(key=lambda x: x["price"])
    elif sort_by == "rating":
        # Assuming a mock rating system for demonstration
        filtered_products.sort(key=lambda x: hash(x["product_id"]) % 5, reverse=True)

    return {
        "query": query,
        "results": filtered_products,
    }


from typing import Dict, List, Optional, Union


def search_websites(
    product_id: str,
    product_name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: str = "relevance",
    specific_sites: Optional[List[str]] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search websites to find a specific product.

    Args:
        product_id: Unique identifier of the product.
        product_name: Search term or product name.
        category: Product category to filter results (e.g., electronics, clothing).
        min_price: Minimum price filter.
        max_price: Maximum price filter.
        sort_by: Sort results by relevance, price, or rating.
        specific_sites: Specifies websites to search. If left null, search all websites.

    Returns:
        Dict containing:
            - product_id: The unique identifier of the product
            - results: List of dictionaries with product details including:
                - site: Website name
                - price: Product price
                - rating: Product rating
                - availability: Availability status
    """
    if not product_id:
        raise ValueError("Product ID is required")

    # Mock data generation based on product_id hash
    hash_value = hash(product_id) % 100
    sample_sites = ["Amazon", "eBay", "Walmart", "BestBuy", "Target"]
    if specific_sites:
        sample_sites = [site for site in sample_sites if site in specific_sites]

    results = []
    for site in sample_sites:
        price = 50 + hash_value * 0.5
        if min_price and price < min_price:
            continue
        if max_price and price > max_price:
            continue

        results.append(
            {
                "site": site,
                "price": price,
                "rating": 3.5 + (hash_value % 5) * 0.1,
                "availability": "In Stock" if hash_value % 2 == 0 else "Out of Stock",
            }
        )

    # Sort results based on the sort_by parameter
    if sort_by == "price":
        results.sort(key=lambda x: x["price"])
    elif sort_by == "rating":
        results.sort(key=lambda x: x["rating"], reverse=True)

    return {"product_id": product_id, "results": results}


from typing import Dict, Optional, Union


def track_order(
    order_id: str, email: Optional[str] = None
) -> Dict[str, Union[str, bool]]:
    """Track the delivery status of an existing order using the order ID.

    Args:
        order_id: Unique identifier for the order to track.
        email: Email associated with the order (for verification).

    Returns:
        Dict containing:
            - order_id: The order ID being tracked
            - status: Current status of the order
            - estimated_delivery: Estimated delivery date
            - verified: Whether the email verification was successful
    """
    # Simulated order database
    orders = {
        "12345": {
            "status": "shipped",
            "estimated_delivery": "2023-10-15",
            "email": "customer@example.com",
        },
        "67890": {
            "status": "processing",
            "estimated_delivery": "2023-10-20",
            "email": "another@example.com",
        },
        "54321": {
            "status": "delivered",
            "estimated_delivery": "2023-10-10",
            "email": "user@example.com",
        },
    }

    if order_id not in orders:
        raise ValueError(f"Order ID not found: {order_id}")

    order_info = orders[order_id]
    verified = email is None or order_info["email"] == email

    return {
        "order_id": order_id,
        "status": order_info["status"],
        "estimated_delivery": order_info["estimated_delivery"],
        "verified": verified,
    }


from typing import Dict, Literal, Optional


def handle_fallback_delivery(
    package_id: str,
    fallback_option: Literal[
        "safe_drop", "neighbor", "locker", "pickup_point", "reschedule"
    ],
    details: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """Carries out the chosen fallback delivery option when the recipient is not home.

    Args:
        package_id: Unique package ID.
        fallback_option: Chosen fallback option (e.g. 'safe_drop', 'neighbor', 'locker', 'pickup_point', 'reschedule').
        details: Additional details for the fallback, such as neighbor contact info, locker location, locker accessibility info etc.

    Returns:
        Dict containing:
            - package_id: The unique package ID
            - status: Status of the fallback delivery
            - message: Detailed message about the delivery action
    """
    if not package_id:
        raise ValueError("Package ID must be provided.")

    if fallback_option not in [
        "safe_drop",
        "neighbor",
        "locker",
        "pickup_point",
        "reschedule",
    ]:
        raise ValueError(f"Unsupported fallback option: {fallback_option}")

    # Simulated responses based on fallback option
    responses = {
        "safe_drop": "Package safely dropped at the designated location.",
        "neighbor": f"Package left with neighbor: {details.get('neighbor_name', 'unknown')}.",
        "locker": f"Package placed in locker at location: {details.get('locker_location', 'unknown')}.",
        "pickup_point": "Package sent to the nearest pickup point.",
        "reschedule": "Delivery rescheduled for the next available date.",
    }

    status = "success" if fallback_option in responses else "failure"
    message = responses.get(fallback_option, "Fallback option not executed.")

    return {
        "package_id": package_id,
        "status": status,
        "message": message,
    }


from typing import Dict, Literal


def notify_recipient_of_fallback(
    recipient_contact: str, message: str, method: Literal["sms", "email", "push"]
) -> Dict[str, str]:
    """Send a notification to the recipient about package fallback details.

    Args:
        recipient_contact: Phone number or email of the recipient.
        message: Short message with fallback details (e.g. 'Package left with neighbor at apt. 3').
        method: Notification method ('sms', 'email', 'push').

    Returns:
        Dict containing:
            - status: Status of the notification ('success' or 'failure')
            - method: Method used for notification
            - recipient: The recipient's contact information
    """
    if not recipient_contact or not message or not method:
        raise ValueError("All parameters must be provided and non-empty")

    # Simulate sending notification
    if method == "sms" and "@" not in recipient_contact:
        status = "success"
    elif method == "email" and "@" in recipient_contact:
        status = "success"
    elif method == "push":
        status = "success"
    else:
        status = "failure"

    return {"status": status, "method": method, "recipient": recipient_contact}


from typing import Dict, List


def retrieve_recipient_preferences(address: str) -> Dict[str, Union[str, List[str]]]:
    """Retrieves stored fallback delivery preferences for a recipient.

    Args:
        address: Delivery address for the package.

    Returns:
        Dict containing:
            - address: The delivery address
            - safe_drop: Permission for safe-drop ('yes' or 'no')
            - neighbor_list: List of neighbor addresses for package drop-off
            - preferred_pickup_points: List of preferred pickup points
    """
    if not address:
        raise ValueError("Address must be provided")

    # Mock data generation based on address hash
    hash_value = hash(address)
    safe_drop = "yes" if hash_value % 2 == 0 else "no"
    neighbor_list = [f"Neighbor {i}" for i in range(1, (hash_value % 3) + 2)]
    preferred_pickup_points = [
        f"Pickup Point {i}" for i in range(1, (hash_value % 4) + 2)
    ]

    return {
        "address": address,
        "safe_drop": safe_drop,
        "neighbor_list": neighbor_list,
        "preferred_pickup_points": preferred_pickup_points,
    }


from typing import Dict, Union


def add_to_cart(
    product_id: str, user_id: str, quantity: int = 1
) -> Dict[str, Union[str, int]]:
    """Add a specified quantity of a product to the user's shopping cart.

    Args:
        product_id: The id of the product to add.
        user_id: The ID of the user.
        quantity: The number of units to add to the cart (default is 1).

    Returns:
        Dict containing:
            - product_id: The id of the product added.
            - user_id: The ID of the user.
            - quantity: The total quantity of the product in the cart.
    """
    if quantity < 1:
        raise ValueError("Quantity must be at least 1")

    # Simulate a cart database with a hash-based generation for consistent results
    cart_db = {
        "user123": {"prodA": 2, "prodB": 1},
        "user456": {"prodC": 3},
    }

    # Retrieve the user's current cart or initialize a new one
    user_cart = cart_db.get(user_id, {})

    # Update the quantity of the product in the user's cart
    current_quantity = user_cart.get(product_id, 0)
    new_quantity = current_quantity + quantity
    user_cart[product_id] = new_quantity

    # Update the cart database (simulated)
    cart_db[user_id] = user_cart

    return {
        "product_id": product_id,
        "user_id": user_id,
        "quantity": new_quantity,
    }


from typing import Dict, Union


def get_order_status(order_id: str) -> Dict[str, Union[str, int]]:
    """Gets the status of a specific order using the order ID.

    Args:
        order_id: The unique identifier for the order.

    Returns:
        Dict containing:
            - order_id: The unique identifier for the order
            - status: Current status of the order (e.g., 'pending', 'shipped', 'delivered')
            - estimated_delivery_days: Estimated number of days for delivery
    """

    # Simulated order data based on hash of order_id
    statuses = ["pending", "shipped", "delivered", "cancelled"]
    hash_value = hash(order_id)
    status_index = hash_value % len(statuses)
    estimated_delivery_days = (
        hash_value % 5
    ) + 1  # Random delivery days between 1 and 5

    return {
        "order_id": order_id,
        "status": statuses[status_index],
        "estimated_delivery_days": estimated_delivery_days,
    }


from typing import Dict, List, Union


def order_delivery(
    restaurant_name: str, selected_dishes: List[str]
) -> Dict[str, Union[str, List[str], float]]:
    """Place an order for delivery from a specified restaurant.

    Args:
        restaurant_name: The restaurant's name.
        selected_dishes: List of individual dishes to be ordered.

    Returns:
        Dict containing:
            - restaurant_name: The name of the restaurant
            - selected_dishes: List of dishes ordered
            - total_cost: Total cost of the order
    """
    if not restaurant_name:
        raise ValueError("Restaurant name must be provided.")
    if not selected_dishes:
        raise ValueError("At least one dish must be selected.")

    # Mocked dish prices for demonstration purposes
    dish_prices = {
        "Pizza": 12.99,
        "Burger": 8.99,
        "Sushi": 15.99,
        "Pasta": 10.99,
        "Salad": 7.99,
    }

    total_cost = sum(dish_prices.get(dish, 0) for dish in selected_dishes)

    if total_cost == 0:
        raise ValueError("Selected dishes are not available.")

    return {
        "restaurant_name": restaurant_name,
        "selected_dishes": selected_dishes,
        "total_cost": total_cost,
    }


from typing import Any, Dict


def place_order(
    payment_info: Dict[str, Any], shipping_address: Dict[str, Any]
) -> Dict[str, Union[str, float]]:
    """Place an order for all items in the user's shopping cart.

    Args:
        payment_info: Details for payment processing (e.g., card number, expiration date).
        shipping_address: The address where the order should be shipped.

    Returns:
        Dict containing:
            - order_id: Unique identifier for the order
            - total_amount: Total amount charged for the order
            - status: Status of the order placement
    """
    if not payment_info or not shipping_address:
        raise ValueError("Both payment_info and shipping_address are required.")

    # Mock data for demonstration purposes
    order_id = "ORD" + str(hash(frozenset(payment_info.items())) % 10000)
    total_amount = 99.99  # Mock total amount
    status = "Order placed successfully"

    return {
        "order_id": order_id,
        "total_amount": total_amount,
        "status": status,
    }


from typing import Dict, Optional


def search_products(
    query: str, category: Optional[str] = None
) -> Dict[str, Union[str, int]]:
    """Search for a product based on a query and return the product id.

    Args:
        query: The item that the user is searching for.
        category: The product category to search within (optional).

    Returns:
        Dict containing:
            - product_id: The ID of the found product
            - name: The name of the found product
            - category: The category of the found product
    """

    # Sample product database
    products = [
        {"id": 101, "name": "Wireless Mouse", "category": "Electronics"},
        {"id": 102, "name": "Bluetooth Speaker", "category": "Electronics"},
        {"id": 103, "name": "Running Shoes", "category": "Footwear"},
        {"id": 104, "name": "Coffee Maker", "category": "Appliances"},
        {"id": 105, "name": "Water Bottle", "category": "Outdoors"},
    ]

    # Filter products based on query and category
    filtered_products = [
        product
        for product in products
        if query.lower() in product["name"].lower()
        and (category is None or category.lower() == product["category"].lower())
    ]

    if not filtered_products:
        raise ValueError(
            f"No products found for query: '{query}' in category: '{category}'"
        )

    # Return the first matched product
    matched_product = filtered_products[0]
    return {
        "product_id": matched_product["id"],
        "name": matched_product["name"],
        "category": matched_product["category"],
    }


from typing import Dict


def set_back_in_stock(name: str) -> Dict[str, str]:
    """Specify that a menu item is back in stock.

    Args:
        name: The name of the menu item that is back in stock

    Returns:
        Dict containing:
            - item: Name of the menu item
            - status: Stock status of the item
    """
    if not name:
        raise ValueError("Menu item name must be provided")

    # Simulate a database of menu items
    menu_items = {
        "Burger": "out of stock",
        "Pasta": "out of stock",
        "Salad": "in stock",
        "Pizza": "out of stock",
    }

    if name not in menu_items:
        raise ValueError(f"Menu item not found: {name}")

    # Update the stock status
    menu_items[name] = "in stock"

    return {
        "item": name,
        "status": menu_items[name],
    }


from typing import Dict


def set_out_of_stock(name: str) -> Dict[str, str]:
    """Specify that a menu item is out of stock.

    Args:
        name: The name of the menu item that is out of stock

    Returns:
        Dict containing:
            - name: Name of the menu item
            - status: Status indicating the item is out of stock
    """
    if not name:
        raise ValueError("Menu item name cannot be empty")

    # Simulate a check against a menu database
    menu_items = {"Burger", "Pizza", "Salad", "Pasta"}
    if name not in menu_items:
        raise ValueError(f"Menu item not found: {name}")

    return {"name": name, "status": "out of stock"}


from typing import Dict, List


def add_to_costco_shopping_list(item_name: str) -> Dict[str, Union[str, List[str]]]:
    """Add an item to the CostCo shopping list.

    Args:
        item_name: The name of the item to add to the shopping list.

    Returns:
        Dict containing:
            - message: Confirmation message of the item added
            - shopping_list: Updated list of items in the shopping cart
    """

    # Simulated existing shopping list
    shopping_list = ["milk", "bread", "eggs"]

    if not item_name:
        raise ValueError("Item name cannot be empty.")

    # Add the new item to the shopping list
    shopping_list.append(item_name)

    return {
        "message": f"'{item_name}' has been added to your CostCo shopping list.",
        "shopping_list": shopping_list,
    }


def clear_costco_order() -> Dict[str, Union[str, List[str]]]:
    """Clear the current CostCo shopping list.

    Returns:
        Dict containing:
            - status: Status of the operation
            - cleared_items: List of items that were cleared from the shopping list
    """
    # Simulated list of items in the CostCo shopping list
    shopping_list = ["milk", "bread", "eggs", "chicken", "rice"]

    if not shopping_list:
        raise ValueError("The shopping list is already empty.")

    # Clear the shopping list
    cleared_items = shopping_list.copy()
    shopping_list.clear()

    return {
        "status": "success",
        "cleared_items": cleared_items,
    }


from typing import Dict, List, Union


def submit_costco_order() -> Dict[str, Union[str, List[str], float]]:
    """Submit items in the CostCo shopping list to order.

    Returns:
        Dict containing:
            - order_id: Unique identifier for the order
            - items: List of items submitted for order
            - total_cost: Total cost of the order
    """

    # Sample data for demonstration purposes
    sample_items = ["Toilet Paper", "Organic Milk", "Almonds", "Chicken Breasts"]
    sample_costs = {
        "Toilet Paper": 19.99,
        "Organic Milk": 8.49,
        "Almonds": 15.99,
        "Chicken Breasts": 12.99,
    }

    # Calculate total cost
    total_cost = sum(sample_costs[item] for item in sample_items)

    # Generate a mock order ID
    order_id = "ORD" + str(hash(frozenset(sample_items)) % 10000)

    return {
        "order_id": order_id,
        "items": sample_items,
        "total_cost": total_cost,
    }


from typing import Dict, List, Union


def woolworths_product_search(
    keyword: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Search the Woolworths supermarket product range based on input string.

    Args:
        keyword: A search string to find products (e.g. 'milk', 'bread')

    Returns:
        Dict containing:
            - keyword: The search keyword used
            - products: List of products matching the search keyword, each with:
                - name: Name of the product
                - price: Price of the product in AUD
                - category: Category of the product
    """

    sample_products = {
        "milk": [
            {"name": "Full Cream Milk", "price": 1.50, "category": "Dairy"},
            {"name": "Almond Milk", "price": 2.00, "category": "Dairy Alternatives"},
        ],
        "bread": [
            {"name": "Wholemeal Bread", "price": 2.50, "category": "Bakery"},
            {"name": "Sourdough Bread", "price": 3.00, "category": "Bakery"},
        ],
        "apple": [
            {"name": "Red Apple", "price": 0.50, "category": "Fruit"},
            {"name": "Green Apple", "price": 0.60, "category": "Fruit"},
        ],
    }

    if keyword not in sample_products:
        raise ValueError(f"No products found for keyword: {keyword}")

    return {
        "keyword": keyword,
        "products": sample_products[keyword],
    }


from typing import Dict, Union


def add_list_item(
    item: str, amount: float = 1, units: str = "each", category: Union[str, None] = None
) -> Dict[str, Union[str, float]]:
    """Add an item to the shopping list with specified details.

    Args:
        item: The name of the item to add to the shopping list.
        amount: The quantity of the item to add (default is 1).
        units: The measurement units for the item (default is 'each').
        category: The category of the item (e.g., 'produce', 'dairy').

    Returns:
        Dict containing:
            - item: Name of the item added
            - amount: Quantity of the item added
            - units: Measurement units for the item
            - category: Category of the item (if provided)
    """
    if not item:
        raise ValueError("Item name must be provided")

    sample_categories = {
        "apple": "produce",
        "milk": "dairy",
        "bread": "bakery",
    }
    if category is None:
        category = sample_categories.get(item.lower(), "miscellaneous")

    return {
        "item": item,
        "amount": amount,
        "units": units,
        "category": category,
    }


from typing import Dict, Literal, Union


def book_shoot(
    client: Dict[str, str],
    shoot: Dict[str, Union[str, int]],
    deposit_amount_gbp: float,
    payment_method: Literal["card_on_file", "new_card", "bank_transfer"],
    notes: str = "",
) -> Dict[str, Union[str, float, Dict[str, str]]]:
    """Confirm a booking and place a deposit for a photography shoot.

    Args:
        client: Client contact information including name and email.
        shoot: Details of the shoot including service type, start time, duration, and location.
        deposit_amount_gbp: Deposit amount in British pounds.
        payment_method: Method for payment ('card_on_file', 'new_card', 'bank_transfer').
        notes: Additional notes or requirements (optional).

    Returns:
        Dict containing:
            - confirmation_id: Unique confirmation ID for the booking
            - client: Client's name and email
            - shoot_details: Details of the shoot including service type and start time
            - deposit: Amount and payment method used
            - status: Confirmation status
    """
    if deposit_amount_gbp < 0:
        raise ValueError("Deposit amount cannot be negative")

    if "name" not in client or "email" not in client:
        raise ValueError("Client information must include name and email")

    if (
        "service_type" not in shoot
        or "start_time" not in shoot
        or "duration_minutes" not in shoot
        or "location" not in shoot
    ):
        raise ValueError(
            "Shoot details must include service type, start time, duration, and location"
        )

    confirmation_id = hash(
        f"{client['email']}-{shoot['start_time']}-{shoot['location']}"
    )

    return {
        "confirmation_id": f"CONF-{abs(confirmation_id)}",
        "client": {"name": client["name"], "email": client["email"]},
        "shoot_details": {
            "service_type": shoot["service_type"],
            "start_time": shoot["start_time"],
        },
        "deposit": {"amount_gbp": deposit_amount_gbp, "payment_method": payment_method},
        "status": "confirmed",
    }


def change_store_status() -> Dict[str, Union[str, bool]]:
    """Toggle the store status between open and closed.

    Returns:
        Dict containing:
            - status: The new status of the store ('open' or 'closed')
            - is_open: Boolean indicating if the store is open
    """
    import hashlib

    # Simulate current store status using a hash-based approach
    current_status = hashlib.md5(b"store_status").hexdigest()
    is_open = int(current_status, 16) % 2 == 0

    # Toggle the status
    new_status = "closed" if is_open else "open"

    return {
        "status": new_status,
        "is_open": not is_open,
    }


from typing import Dict, Union


def check_price(item: str, store: str) -> Dict[str, Union[str, float]]:
    """Check the price of a grocery item at a given store.

    Args:
        item: Name of the item to look up (e.g., 'apple', 'milk')
        store: The grocery store to check the price at (e.g., 'Walmart', 'Whole Foods')

    Returns:
        Dict containing:
            - item: Name of the item
            - store: Name of the store
            - price: Price of the item at the store
    """

    # Sample data for demonstration purposes
    sample_prices = {
        "Walmart": {
            "apple": 0.5,
            "milk": 3.0,
            "bread": 2.0,
        },
        "Whole Foods": {
            "apple": 0.7,
            "milk": 3.5,
            "bread": 2.5,
        },
        "Costco": {
            "apple": 0.4,
            "milk": 2.8,
            "bread": 1.8,
        },
    }

    if store not in sample_prices:
        raise ValueError(f"Store not supported: {store}")

    store_prices = sample_prices[store]

    if item not in store_prices:
        raise ValueError(f"Item not available at {store}: {item}")

    return {
        "item": item,
        "store": store,
        "price": store_prices[item],
    }


from typing import Dict, Union


def checkout(
    user_id: str, payment_details: Dict[str, str], shipping_address: str
) -> Dict[str, Union[str, float, Dict[str, Union[str, float]]]]:
    """Processes payment for all items in the cart and creates an order.

    Args:
        user_id: The ID for the user whose cart is being checked out.
        payment_details: An object containing the user's payment information.
            - method: The payment method.
            - card_number: The 16-digit credit card number.
        shipping_address: The full address where the order should be shipped.

    Returns:
        Dict containing:
            - order_id: Unique identifier for the created order
            - total_amount: Total amount charged for the order
            - payment_status: Status of the payment
            - shipping_details: Details of the shipping
                - address: The shipping address
                - estimated_delivery: Estimated delivery time in days
    """
    # Mock data for demonstration purposes
    if len(payment_details.get("card_number", "")) != 16:
        raise ValueError("Invalid card number length")

    # Simulate order processing
    order_id = f"ORD-{hash(user_id) % 10000}"
    total_amount = 99.99  # Mock total amount
    payment_status = (
        "Success" if payment_details["method"] in ["credit", "debit"] else "Failed"
    )
    estimated_delivery = 5  # Mock delivery time in days

    return {
        "order_id": order_id,
        "total_amount": total_amount,
        "payment_status": payment_status,
        "shipping_details": {
            "address": shipping_address,
            "estimated_delivery": estimated_delivery,
        },
    }


def clear_inventory() -> Dict[str, Union[str, int]]:
    """Clear all items from the warehouse inventory.

    Returns:
        Dict containing:
            - status: Status of the inventory clearance
            - items_cleared: Number of items cleared from the inventory
    """
    # Simulate clearing the inventory
    items_cleared = 1500  # Example number of items in inventory

    return {
        "status": "success",
        "items_cleared": items_cleared,
    }


from typing import Dict, List, Union


def compare_total_cost(
    listing_ids: List[str],
    region: str,
    include_tax: bool = False,
    include_shipping: bool = False,
    coupon_codes: List[str] = None,
) -> Dict[str, Union[str, float, List[Dict[str, Union[str, float]]]]]:
    """Compare effective checkout cost across marketplaces.

    Args:
        listing_ids: Candidate listings to compare
        region: Buyer region for tax/shipping rules
        include_tax: Whether to include estimated sales tax
        include_shipping: Whether to include shipping costs
        coupon_codes: Optional coupon codes to apply

    Returns:
        Dict containing:
            - region: The buyer's region
            - comparisons: List of dictionaries with:
                - listing_id: The ID of the listing
                - base_price: The base price of the listing
                - tax: The estimated tax applied
                - shipping: The estimated shipping cost
                - discount: The discount applied from coupons
                - total_cost: The total effective cost
    """
    if not listing_ids:
        raise ValueError("At least one listing ID must be provided.")

    sample_prices = {
        "listing_1": 100.0,
        "listing_2": 150.0,
        "listing_3": 200.0,
    }
    tax_rates = {
        "US": 0.07,
        "EU": 0.20,
        "JP": 0.10,
    }
    shipping_costs = {
        "US": 5.0,
        "EU": 10.0,
        "JP": 15.0,
    }
    coupon_discounts = {
        "SAVE10": 0.10,
        "FREESHIP": 5.0,
    }

    comparisons = []
    for listing_id in listing_ids:
        base_price = sample_prices.get(listing_id, 0.0)
        tax = base_price * tax_rates.get(region, 0.0) if include_tax else 0.0
        shipping = shipping_costs.get(region, 0.0) if include_shipping else 0.0
        discount = 0.0

        if coupon_codes:
            for code in coupon_codes:
                if code in coupon_discounts:
                    if code == "FREESHIP":
                        shipping = 0.0
                    else:
                        discount += base_price * coupon_discounts[code]

        total_cost = base_price + tax + shipping - discount
        comparisons.append(
            {
                "listing_id": listing_id,
                "base_price": base_price,
                "tax": tax,
                "shipping": shipping,
                "discount": discount,
                "total_cost": total_cost,
            }
        )

    return {
        "region": region,
        "comparisons": comparisons,
    }


import hashlib
from typing import Dict, Literal, Union


def compute_price_fairness(
    model: str,
    current_price: float,
    window_days: int = 30,
    condition: Literal["new", "used", "refurbished", "open-box"] = "new",
) -> Dict[str, Union[str, float, bool]]:
    """Analyze whether a current price is a good deal versus historical trends.

    Args:
        model: Product/Model
        current_price: Observed current price in USD
        window_days: Historical window to compare against
        condition: Condition of the item ('new', 'used', 'refurbished', 'open-box')

    Returns:
        Dict containing:
            - model: Product/Model name
            - current_price: Observed current price in USD
            - average_historical_price: Average price over the historical window
            - is_good_deal: Boolean indicating if the current price is a good deal
    """
    # Simulate historical price data using a hash-based approach
    hash_input = f"{model}-{condition}-{window_days}".encode()
    hash_value = int(hashlib.sha256(hash_input).hexdigest(), 16)

    # Generate a pseudo-random average historical price
    average_historical_price = (hash_value % 500) + 50  # Range: 50 to 550 USD

    # Determine if the current price is a good deal
    is_good_deal = current_price < average_historical_price * 0.9

    return {
        "model": model,
        "current_price": current_price,
        "average_historical_price": average_historical_price,
        "is_good_deal": is_good_deal,
    }


from typing import Dict, List


def count_inventory() -> Dict[str, Union[int, Dict[str, int]]]:
    """Count the number of items and their types in an inventory.

    Returns:
        Dict containing:
            - total_items: Total number of items in the inventory
            - item_types: Dictionary with item types as keys and their counts as values
    """
    inventory_sample = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12,
        "pear": 7,
    }

    total_items = sum(inventory_sample.values())
    item_types = inventory_sample

    return {
        "total_items": total_items,
        "item_types": item_types,
    }


from typing import Dict, List, Optional


def filter_books(
    author: Optional[List[str]] = None,
    genre: Optional[List[str]] = None,
    available: bool = True,
) -> Dict[str, List[Dict[str, str]]]:
    """Filter books from a catalog according to user preference.

    Args:
        author: List of authors that the user is interested in
        genre: List of genres that the user is interested in
        available: Whether the book is not on loan

    Returns:
        Dict containing:
            - books: List of books matching the criteria, each with:
                - title: Title of the book
                - author: Author of the book
                - genre: Genre of the book
                - available: Availability status of the book
    """
    catalog = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Fiction",
            "available": True,
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian",
            "available": False,
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "genre": "Fiction",
            "available": True,
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "genre": "Fiction",
            "available": True,
        },
        {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "genre": "Dystopian",
            "available": True,
        },
    ]

    def matches_criteria(book):
        if author and book["author"] not in author:
            return False
        if genre and book["genre"] not in genre:
            return False
        if available and not book["available"]:
            return False
        return True

    filtered_books = [book for book in catalog if matches_criteria(book)]

    return {"books": filtered_books}


from typing import Dict, List, Union


def find_used_car_parts(
    make: str,
    model: str,
    part_type: str,
    year: Union[int, None] = None,
    city: Union[str, None] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    """Find sellers with available used car parts of specified type based on make, model, and year.

    Args:
        make: Make of the car.
        model: Model of the car.
        part_type: The type of part to find.
        year: Year of manufacture of the car (optional).
        city: If specified, limits the search to that city (optional).

    Returns:
        Dict containing:
            - make: Make of the car.
            - model: Model of the car.
            - part_type: The type of part being searched.
            - sellers: List of sellers with available parts, each containing:
                - name: Seller's name
                - city: City where the seller is located
                - price: Price of the part
    """

    # Sample data based on hash of make, model, and part_type
    sample_sellers = {
        ("Toyota", "Camry", "engine"): [
            {"name": "Auto Parts Co", "city": "New York", "price": 1200},
            {"name": "Parts R Us", "city": "Los Angeles", "price": 1150},
        ],
        ("Ford", "F-150", "transmission"): [
            {"name": "Truck Parts Depot", "city": "Houston", "price": 900},
            {"name": "Gear Masters", "city": "Chicago", "price": 950},
        ],
        ("Hilux", "Hilux", "radiator"): [
            {"name": "Wellington Auto Parts", "city": "Wellington", "price": 350},
            {"name": "Kiwi Car Components", "city": "Wellington", "price": 375},
            {"name": "NZ Truck Parts", "city": "Auckland", "price": 320},
            {"name": "South Island Auto", "city": "Christchurch", "price": 340},
        ],
    }

    key = (make, model, part_type)
    if key not in sample_sellers:
        raise ValueError(f"No sellers found for {make} {model} {part_type}")

    sellers = sample_sellers[key]

    if city:
        sellers = [seller for seller in sellers if seller["city"] == city]
        if not sellers:
            raise ValueError(
                f"No sellers found in {city} for {make} {model} {part_type}"
            )

    return {"make": make, "model": model, "part_type": part_type, "sellers": sellers}


from typing import Dict


def finish_delivery(id: int) -> Dict[str, Union[int, str]]:
    """End delivery in system by marking the package as delivered.

    Args:
        id: The tracking id number of the package

    Returns:
        Dict containing:
            - id: The tracking id number of the package
            - status: The delivery status of the package
            - message: Confirmation message of the delivery completion
    """
    if id <= 0:
        raise ValueError("Invalid tracking id number")

    # Simulate a hash-based generation for consistent sample data
    status = "delivered" if id % 2 == 0 else "pending"
    message = (
        "Package successfully delivered."
        if status == "delivered"
        else "Package delivery is still pending."
    )

    return {
        "id": id,
        "status": status,
        "message": message,
    }


from typing import Dict, List, Literal, Union


def generate_quote(
    service_type: Literal["boudoir", "portrait", "wedding", "commercial", "fashion"],
    hours: float,
    add_ons: List[
        Literal["retouching", "prints", "album", "hair_makeup", "express_delivery"]
    ] = [],
    licence: Literal["personal", "commercial", "editorial"] = "personal",
    deliverables: List[
        Literal["online_gallery", "usb_drive", "contact_sheet", "proof_book"]
    ] = [],
    discount_code: str = "",
) -> Dict[str, Union[float, str, List[str]]]:
    """Create a price quote for a photography shoot.

    Args:
        service_type: Type of photography service
        hours: Duration of the shoot in hours
        add_ons: Additional services to include
        licence: Usage rights for the photos
        deliverables: How photos will be delivered
        discount_code: Promotional code for discount

    Returns:
        Dict containing:
            - total_cost: Total cost of the shoot
            - breakdown: List of cost breakdown items
            - discount_applied: Discount applied if any
    """
    base_rates = {
        "boudoir": 150,
        "portrait": 100,
        "wedding": 300,
        "commercial": 250,
        "fashion": 200,
    }
    add_on_rates = {
        "retouching": 50,
        "prints": 30,
        "album": 100,
        "hair_makeup": 75,
        "express_delivery": 40,
    }
    licence_rates = {
        "personal": 0,
        "commercial": 200,
        "editorial": 100,
    }
    discount_codes = {
        "SUMMER21": 0.1,  # 10% discount
        "NEWCLIENT": 0.15,  # 15% discount
    }

    if hours < 1:
        raise ValueError("Hours must be at least 1.")

    base_cost = base_rates[service_type] * hours
    add_on_cost = sum(add_on_rates[add_on] for add_on in add_ons)
    licence_cost = licence_rates[licence]
    total_cost = base_cost + add_on_cost + licence_cost

    discount_applied = 0
    if discount_code in discount_codes:
        discount_applied = discount_codes[discount_code]
        total_cost *= 1 - discount_applied

    breakdown = [
        f"Base cost for {hours} hours of {service_type}: ${base_cost:.2f}",
        f"Add-ons cost: ${add_on_cost:.2f}",
        f"Licence cost: ${licence_cost:.2f}",
    ]

    if discount_applied:
        breakdown.append(f"Discount applied: {discount_applied * 100:.0f}%")

    return {
        "total_cost": round(total_cost, 2),
        "breakdown": breakdown,
        "discount_applied": (
            f"{discount_applied * 100:.0f}%" if discount_applied else "None"
        ),
    }


from typing import Dict, List, Union


def genre_search(
    genre: str, city: str, strictness_measure: int = 3
) -> Dict[str, Union[str, List[str]]]:
    """Search for bookstores in a city that have a specific genre of books.

    Args:
        genre: Genre of books to look for (e.g. 'Science Fiction', 'Mystery')
        city: Name of the city to search in (e.g. 'New York', 'San Francisco')
        strictness_measure: Measure of how strictly the genre should be followed (1 - 5)

    Returns:
        Dict containing:
            - city: Name of the city
            - genre: Genre searched for
            - bookstores: List of bookstore names that match the criteria
    """

    # Sample data simulating bookstores in different cities
    sample_data = {
        "New York": {
            "Science Fiction": ["Galactic Reads", "Future Pages"],
            "Mystery": ["Whodunit Books", "Enigma Emporium"],
        },
        "San Francisco": {
            "Science Fiction": ["Space Odyssey", "Cosmic Tales"],
            "Mystery": ["Detective's Den", "Mystery Mansion"],
        },
        "Chicago": {
            "Science Fiction": ["Interstellar Books", "Astro Archives"],
            "Mystery": ["Clue Corner", "Puzzle Pages"],
        },
    }

    if city not in sample_data:
        raise ValueError(f"City not supported: {city}")

    if genre not in sample_data[city]:
        raise ValueError(f"Genre not available in {city}: {genre}")

    # Simulate strictness by filtering the list based on the strictness_measure
    bookstores = sample_data[city][genre]
    filtered_bookstores = bookstores[
        : max(1, len(bookstores) - (5 - strictness_measure))
    ]

    return {
        "city": city,
        "genre": genre,
        "bookstores": filtered_bookstores,
    }


from typing import Dict, List, Optional, Union


def get_blu_rays_for_sale(
    search_by_title: Optional[str] = None,
    search_by_director: Optional[str] = None,
    released_after: Optional[str] = None,
    in_stock: bool = False,
    is_4k: bool = False,
    filter_by_certification: Optional[List[str]] = None,
    filter_by_edition: Optional[List[str]] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, bool]]]]]:
    """Find blu-ray discs available for sale.

    Args:
        search_by_title: The name of the blu-ray movie to search for.
        search_by_director: The name of the director to search for.
        released_after: Filter titles released after this date (YYYY-MM-DD).
        in_stock: Filter by titles currently in stock.
        is_4k: Filter by titles available in 4k format.
        filter_by_certification: Filter by title's certification.
        filter_by_edition: Filter by title's edition.

    Returns:
        Dict containing:
            - search_criteria: Description of the applied search filters.
            - blu_rays: List of blu-ray titles matching the criteria, each with:
                - title: Title of the blu-ray.
                - director: Director of the movie.
                - release_date: Release date of the blu-ray.
                - in_stock: Availability status.
                - is_4k: Whether the blu-ray is in 4k format.
                - certification: Certification of the blu-ray.
                - edition: Edition type of the blu-ray.
    """

    # Sample data for demonstration purposes
    sample_blu_rays = [
        {
            "title": "Inception",
            "director": "Christopher Nolan",
            "release_date": "2010-07-16",
            "in_stock": True,
            "is_4k": True,
            "certification": "PG",
            "edition": "special edition",
        },
        {
            "title": "The Matrix",
            "director": "Lana Wachowski",
            "release_date": "1999-03-31",
            "in_stock": False,
            "is_4k": False,
            "certification": "R18+",
            "edition": "steelbook",
        },
        {
            "title": "Avatar",
            "director": "James Cameron",
            "release_date": "2009-12-18",
            "in_stock": True,
            "is_4k": True,
            "certification": "PG",
            "edition": "3d",
        },
    ]

    # Filter logic
    filtered_blu_rays = []
    for blu_ray in sample_blu_rays:
        if search_by_title and search_by_title.lower() not in blu_ray["title"].lower():
            continue
        if (
            search_by_director
            and search_by_director.lower() not in blu_ray["director"].lower()
        ):
            continue
        if released_after and blu_ray["release_date"] <= released_after:
            continue
        if in_stock and not blu_ray["in_stock"]:
            continue
        if is_4k and not blu_ray["is_4k"]:
            continue
        if (
            filter_by_certification
            and blu_ray["certification"] not in filter_by_certification
        ):
            continue
        if filter_by_edition and blu_ray["edition"] not in filter_by_edition:
            continue
        filtered_blu_rays.append(blu_ray)

    return {
        "search_criteria": "Filtered blu-rays based on provided criteria",
        "blu_rays": filtered_blu_rays,
    }


from typing import Dict, List


def get_cart_contents(
    user_id: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]:
    """Retrieves all items currently in the user's shopping cart.

    Args:
        user_id: The unique identifier for the user.

    Returns:
        Dict containing:
            - user_id: The unique identifier for the user
            - items: List of items in the cart, each with:
                - item_id: Unique identifier for the item
                - name: Name of the item
                - quantity: Quantity of the item in the cart
                - price: Price per unit of the item
    """
    # Mock data generation based on user_id hash
    sample_items = {
        0: [
            {"item_id": "101", "name": "Laptop", "quantity": 1, "price": 999.99},
            {"item_id": "102", "name": "Mouse", "quantity": 2, "price": 25.50},
        ],
        1: [
            {"item_id": "103", "name": "Keyboard", "quantity": 1, "price": 45.00},
            {"item_id": "104", "name": "Monitor", "quantity": 2, "price": 150.00},
        ],
        2: [
            {"item_id": "105", "name": "USB Cable", "quantity": 3, "price": 5.99},
        ],
    }

    # Determine which sample to use based on user_id hash
    user_hash = hash(user_id) % len(sample_items)

    return {
        "user_id": user_id,
        "items": sample_items[user_hash],
    }


from typing import Dict, List


def get_cart_items() -> Dict[str, List[Dict[str, Union[str, int, float]]]]:
    """Retrieves all items currently in the user's shopping cart.

    Returns:
        Dict containing:
            - items: List of items in the cart, each with:
                - id: Unique identifier for the item
                - name: Name of the item
                - quantity: Quantity of the item in the cart
                - price: Price per unit of the item
    """

    # Sample data simulating items in a shopping cart
    cart_items = [
        {"id": "A123", "name": "Laptop", "quantity": 1, "price": 999.99},
        {"id": "B456", "name": "Headphones", "quantity": 2, "price": 199.99},
        {"id": "C789", "name": "Coffee Mug", "quantity": 3, "price": 12.99},
    ]

    return {"items": cart_items}


import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Union


def get_history(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: Optional[int] = 10,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Retrieves the user's past purchase history with optional filters.

    Args:
        start_date: The start date for the history search (e.g., '2025-01-01').
        end_date: The end date for the history search (e.g., '2025-12-31').
        limit: The maximum number of history items to retrieve (defaults to 10).

    Returns:
        Dict containing:
            - start_date: The start date used for filtering
            - end_date: The end date used for filtering
            - purchases: List of purchase history items, each containing:
                - item: Name of the purchased item
                - price: Price of the item
                - date: Date of purchase
    """

    def generate_purchase_data(index: int) -> Dict[str, Union[str, float]]:
        item_name = f"Item-{index}"
        price = int(hashlib.md5(item_name.encode()).hexdigest()[-3:], 16) % 100 + 1
        purchase_date = datetime(2025, 1, 1).strftime("%Y-%m-%d")
        return {"item": item_name, "price": price, "date": purchase_date}

    if start_date:
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid start_date format: {start_date}")

    if end_date:
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid end_date format: {end_date}")

    if limit is not None and (not isinstance(limit, int) or limit <= 0):
        raise ValueError(f"Limit must be a positive integer, got: {limit}")

    purchases = [generate_purchase_data(i) for i in range(limit)]
    return {
        "start_date": start_date or "N/A",
        "end_date": end_date or "N/A",
        "purchases": purchases,
    }


from typing import Dict, Union


def get_item_details(item_name: str) -> Dict[str, Union[str, int, float]]:
    """Retrieve details of a specific item in the warehouse.

    Args:
        item_name: The name of the item to retrieve details for.

    Returns:
        Dict containing:
            - item_name: Name of the item
            - quantity: Quantity of the item in stock
            - price: Price of the item per unit
            - location: Warehouse location of the item
    """

    sample_data = {
        "Widget": {"quantity": 150, "price": 2.99, "location": "Aisle 3, Shelf B"},
        "Gadget": {"quantity": 75, "price": 5.49, "location": "Aisle 1, Shelf A"},
        "Doodad": {"quantity": 200, "price": 1.99, "location": "Aisle 5, Shelf C"},
    }

    if item_name not in sample_data:
        raise ValueError(f"Item not found in warehouse: {item_name}")

    item_details = sample_data[item_name]
    return {
        "item_name": item_name,
        "quantity": item_details["quantity"],
        "price": item_details["price"],
        "location": item_details["location"],
    }


from typing import Dict, Union


def get_listing_details(listing_id: str) -> Dict[str, Union[str, float, int]]:
    """Fetch information for a listing by ID.

    Args:
        listing_id: Provider-specific listing identifier

    Returns:
        Dict containing:
            - listing_id: The identifier of the listing
            - title: The title of the listing
            - price: The price of the listing
            - bedrooms: Number of bedrooms in the listing
            - location: Location of the listing
    """

    # Simulated data based on hash of the listing_id
    sample_data = {
        "title": f"Cozy Apartment #{hash(listing_id) % 1000}",
        "price": round((hash(listing_id) % 100000) / 100, 2),
        "bedrooms": (hash(listing_id) % 5) + 1,
        "location": f"City-{hash(listing_id) % 100}",
    }

    if not listing_id:
        raise ValueError("Listing ID cannot be empty")

    return {
        "listing_id": listing_id,
        "title": sample_data["title"],
        "price": sample_data["price"],
        "bedrooms": sample_data["bedrooms"],
        "location": sample_data["location"],
    }


from typing import Dict, Literal, Union


def get_postage_information(
    post_code: str,
    shipping_type: Literal["standard", "express", "overnight"] = "standard",
) -> Dict[str, Union[str, float, int]]:
    """Get information about the postage of an order.

    Args:
        post_code: The post code the order is to be shipped to
        shipping_type: The type of shipping the user has requested ('standard', 'express', 'overnight')

    Returns:
        Dict containing:
            - post_code: The destination post code
            - shipping_type: The type of shipping selected
            - cost: Estimated cost of shipping in USD
            - delivery_days: Estimated delivery time frame in days
    """

    # Mock data based on shipping type
    shipping_data = {
        "standard": {"cost": 5.0, "delivery_days": 5},
        "express": {"cost": 10.0, "delivery_days": 2},
        "overnight": {"cost": 20.0, "delivery_days": 1},
    }

    if shipping_type not in shipping_data:
        raise ValueError(f"Unsupported shipping type: {shipping_type}")

    # Simulate cost and delivery days based on post code hash
    base_data = shipping_data[shipping_type]
    hash_modifier = hash(post_code) % 3  # Simple hash-based variation

    return {
        "post_code": post_code,
        "shipping_type": shipping_type,
        "cost": base_data["cost"] + hash_modifier,
        "delivery_days": base_data["delivery_days"] + hash_modifier,
    }


import hashlib
from typing import Dict, List, Union


def get_price_history(
    model: str, region: str = "US", window_days: int = 30
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Retrieve historical prices for a product/model.

    Args:
        model: Product/Model, e.g., 'NVIDIA GeForce RTX 5070'
        region: Region for historical pricing (default is 'US')
        window_days: How many days of history to include (default is 30)

    Returns:
        Dict containing:
            - model: Product/Model name
            - region: Region for the pricing data
            - history: List of dictionaries with 'date' and 'price' keys
    """

    # Generate a consistent but varied price history using a hash of the model
    hash_seed = int(hashlib.sha256(model.encode()).hexdigest(), 16)
    base_price = 500 + (hash_seed % 100)  # Base price between 500 and 599

    history = []
    for day in range(window_days):
        # Simulate price fluctuation
        fluctuation = ((hash_seed >> day) % 20) - 10  # Fluctuation between -10 and +9
        price = base_price + fluctuation
        date = f"2023-09-{30 - day:02d}"  # Simulate dates in September 2023
        history.append({"date": date, "price": price})

    return {
        "model": model,
        "region": region,
        "history": history,
    }


from typing import Dict, Union


def get_product_details(product_id: str) -> Dict[str, Union[str, float, int]]:
    """Retrieves detailed information about a specific product using its ID.

    Args:
        product_id: The unique identifier of the product.

    Returns:
        Dict containing:
            - product_id: The unique identifier of the product
            - name: The name of the product
            - price: The price of the product in USD
            - stock: The number of items available in stock
            - description: A brief description of the product
    """

    # Simulated product database
    product_database = {
        "P001": {
            "name": "Wireless Mouse",
            "price": 29.99,
            "stock": 150,
            "description": "A high-precision wireless mouse with ergonomic design.",
        },
        "P002": {
            "name": "Mechanical Keyboard",
            "price": 89.99,
            "stock": 85,
            "description": "A durable mechanical keyboard with customizable RGB lighting.",
        },
        "P003": {
            "name": "USB-C Hub",
            "price": 49.99,
            "stock": 200,
            "description": "A versatile USB-C hub with multiple ports for connectivity.",
        },
    }

    if product_id not in product_database:
        raise ValueError(f"Product ID not found: {product_id}")

    product_info = product_database[product_id]
    return {
        "product_id": product_id,
        "name": product_info["name"],
        "price": product_info["price"],
        "stock": product_info["stock"],
        "description": product_info["description"],
    }


from typing import Dict, List, Optional


def get_shopping_list(category: Optional[str] = None) -> Dict[str, List[str]]:
    """Retrieve a shopping list based on the specified category.

    Args:
        category: The category of items to retrieve (e.g. 'fruits', 'vegetables').
                  If not specified, returns a list of all items.

    Returns:
        Dict containing:
            - category: The category of items
            - items: List of items in the specified category
    """

    sample_data = {
        "fruits": ["apples", "bananas", "oranges"],
        "vegetables": ["carrots", "broccoli", "spinach"],
        "dairy": ["milk", "cheese", "yogurt"],
        "bakery": ["bread", "croissants", "bagels"],
    }

    if category:
        if category not in sample_data:
            raise ValueError(f"Category not supported: {category}")
        return {
            "category": category,
            "items": sample_data[category],
        }

    all_items = [item for items in sample_data.values() for item in items]
    return {
        "category": "all",
        "items": all_items,
    }


from typing import Dict, List


def get_stores(county_name: str, state_name: str) -> Dict[str, List[str]]:
    """Get a list of stores in a given county.

    Args:
        county_name: Name of the county to find stores in
        state_name: Name of the US state the county is in

    Returns:
        Dict containing:
            - county: Name of the county
            - state: Name of the state
            - stores: List of store names in the county
    """

    sample_data = {
        ("Los Angeles", "California"): ["Store A", "Store B", "Store C"],
        ("Cook", "Illinois"): ["Store D", "Store E"],
        ("Harris", "Texas"): ["Store F", "Store G", "Store H", "Store I"],
    }

    key = (county_name, state_name)
    if key not in sample_data:
        raise ValueError(
            f"No store data available for {county_name} County, {state_name}"
        )

    return {
        "county": county_name,
        "state": state_name,
        "stores": sample_data[key],
    }


from typing import Dict, List


def get_user_recommendations(user_id: str, count: int = 5) -> Dict[str, List[str]]:
    """Provides a list of recommended products for a user based on their history.

    Args:
        user_id: The unique identifier for the user.
        count: The maximum number of recommendations to return.

    Returns:
        Dict containing:
            - user_id: The unique identifier for the user.
            - recommendations: List of recommended product names.
    """

    # Mock user purchase history and product recommendations
    user_purchase_history = {
        "user_123": ["Laptop", "Smartphone", "Headphones"],
        "user_456": ["Book", "Pen", "Notebook"],
        "user_789": ["Shoes", "Socks", "T-shirt"],
    }

    product_recommendations = {
        "Laptop": ["Mouse", "Keyboard", "Monitor"],
        "Smartphone": ["Phone Case", "Screen Protector", "Charger"],
        "Headphones": ["Earbuds", "Bluetooth Adapter", "Headphone Stand"],
        "Book": ["Bookmark", "Reading Light", "Book Cover"],
        "Pen": ["Notebook", "Pencil", "Eraser"],
        "Notebook": ["Sticky Notes", "Highlighter", "Binder"],
        "Shoes": ["Shoe Cleaner", "Socks", "Shoe Laces"],
        "Socks": ["Laundry Bag", "Foot Cream", "Shoe Inserts"],
        "T-shirt": ["Jacket", "Cap", "Sunglasses"],
    }

    if user_id not in user_purchase_history:
        raise ValueError(f"User ID not found: {user_id}")

    # Generate recommendations based on purchase history
    recommendations = []
    for item in user_purchase_history[user_id]:
        recommendations.extend(product_recommendations.get(item, []))

    # Ensure unique recommendations and limit to the requested count
    unique_recommendations = list(dict.fromkeys(recommendations))
    return {
        "user_id": user_id,
        "recommendations": unique_recommendations[:count],
    }


from typing import Dict, Literal, Union


def input_delivery(
    destination: str, service: str = "ground"
) -> Dict[str, Union[str, int]]:
    """Input delivery information into the system.

    Args:
        destination: Address where the package will arrive.
        service: Type of service the delivery will have (e.g., 'ground', 'air', 'express').

    Returns:
        Dict containing:
            - destination: The delivery address
            - service: The type of delivery service
            - estimated_days: Estimated delivery time in days
    """

    if not destination:
        raise ValueError("Destination address is required.")

    service_options = {"ground": 5, "air": 3, "express": 1}

    if service not in service_options:
        raise ValueError(f"Unsupported service type: {service}")

    estimated_days = service_options[service]

    return {
        "destination": destination,
        "service": service,
        "estimated_days": estimated_days,
    }


from typing import Dict, Union


def keyword_rank_checker(url: str, keyword: str) -> Dict[str, Union[str, int]]:
    """Check specified keyword rankings for a given URL.

    Args:
        url: URL for which to get keyword rankings.
        keyword: Keyword to get rankings for.

    Returns:
        Dict containing:
            - url: The URL for which the ranking is checked
            - keyword: The keyword for which the ranking is checked
            - rank: The rank of the keyword for the given URL
    """
    # Simulated hash-based ranking generation for consistency
    hash_value = hash((url, keyword)) % 100
    rank = hash_value + 1  # Rank is 1-based

    return {
        "url": url,
        "keyword": keyword,
        "rank": rank,
    }


from typing import Dict, List, Union


def miniature_car_parts(
    postcode: str, radius: float = 5
) -> Dict[str, Union[str, float, List[Dict[str, Union[str, float]]]]]:
    """Find retailers of miniature, RC, car parts within a specified radius of a postcode.

    Args:
        postcode: The postcode or outcode to center the search on.
        radius: The search radius in miles around the central postcode.

    Returns:
        Dict containing:
            - postcode: The central postcode for the search.
            - radius: The search radius in miles.
            - retailers: List of retailers with:
                - name: Retailer's name.
                - address: Retailer's address.
                - distance: Distance from the central postcode in miles.
    """

    # Simulated retailer data based on hash of postcode for consistent results
    sample_retailers = {
        "12345": [
            {
                "name": "Miniature Motors",
                "address": "123 Elm St, Springfield",
                "distance": 2.5,
            },
            {"name": "RC World", "address": "456 Oak St, Springfield", "distance": 4.0},
        ],
        "67890": [
            {
                "name": "Tiny Car Parts",
                "address": "789 Pine St, Shelbyville",
                "distance": 1.2,
            },
            {
                "name": "RC Emporium",
                "address": "101 Maple St, Shelbyville",
                "distance": 3.8,
            },
        ],
    }

    # Generate a hash-based key for consistent sample data retrieval
    key = str(abs(hash(postcode)) % 100000)

    if key not in sample_retailers:
        raise ValueError(f"No retailers found for postcode: {postcode}")

    return {
        "postcode": postcode,
        "radius": radius,
        "retailers": sample_retailers[key],
    }


from typing import Dict, List, Literal, Union


def order_parts(
    model_number: str,
    part_numbers: List[str],
    shipping_address: str,
    quantity_map: Dict[str, int] = None,
    delivery_speed: Literal["standard", "expedited", "overnight"] = "standard",
    budget_max: float = None,
) -> Dict[str, Union[str, float, List[Dict[str, Union[str, int]]]]]:
    """Order replacement parts for an appliance/system with optional fast shipping.

    Args:
        model_number: Appliance/system model number.
        part_numbers: One or more manufacturer part numbers.
        shipping_address: Delivery address.
        quantity_map: Map of part_number -> quantity.
        delivery_speed: Shipping speed: 'standard', 'expedited', 'overnight'.
        budget_max: Maximum total spend.

    Returns:
        Dict containing:
            - order_id: Unique identifier for the order.
            - total_cost: Total cost of the order.
            - parts_ordered: List of parts with details.
            - delivery_estimate: Estimated delivery date.
    """
    if not model_number or not part_numbers or not shipping_address:
        raise ValueError(
            "model_number, part_numbers, and shipping_address are required"
        )

    if quantity_map is None:
        quantity_map = {part_number: 1 for part_number in part_numbers}

    sample_prices = {
        "1234": 15.99,
        "5678": 25.50,
        "91011": 5.75,
    }

    total_cost = 0
    parts_ordered = []

    for part_number in part_numbers:
        if part_number not in sample_prices:
            raise ValueError(f"Part number not supported: {part_number}")
        quantity = quantity_map.get(part_number, 1)
        cost = sample_prices[part_number] * quantity
        total_cost += cost
        parts_ordered.append(
            {
                "part_number": part_number,
                "quantity": quantity,
                "cost": cost,
            }
        )

    if budget_max is not None and total_cost > budget_max:
        raise ValueError("Total cost exceeds budget_max")

    delivery_estimates = {
        "standard": "5-7 business days",
        "expedited": "2-3 business days",
        "overnight": "1 business day",
    }

    return {
        "order_id": "ORD123456",
        "total_cost": total_cost,
        "parts_ordered": parts_ordered,
        "delivery_estimate": delivery_estimates[delivery_speed],
    }


from typing import Dict, Literal, Union


def process_delivery(
    destination: str, service: str = "ground"
) -> Dict[str, Union[str, int]]:
    """Start the delivery process in the system.

    Args:
        destination: Address where the package will arrive.
        service: Type of service the delivery will have ('ground', 'air', 'express').

    Returns:
        Dict containing:
            - tracking_id: Unique identifier for the delivery.
            - destination: Address where the package will arrive.
            - service: Type of service the delivery will have.
            - estimated_days: Estimated number of days for delivery.
    """
    if not destination:
        raise ValueError("Destination address is required.")

    if service not in ["ground", "air", "express"]:
        raise ValueError(f"Unsupported service type: {service}")

    # Simulate a hash-based tracking ID generation
    tracking_id = hash((destination, service)) % 1000000

    # Simulate estimated delivery days based on service type
    service_days = {
        "ground": 5,
        "air": 3,
        "express": 1,
    }
    estimated_days = service_days.get(service, 5)

    return {
        "tracking_id": tracking_id,
        "destination": destination,
        "service": service,
        "estimated_days": estimated_days,
    }


from typing import Dict, List, Union


def rcbay(
    postcode: str, q: str, max_price: float = 999, radius: float = 10
) -> Dict[str, Union[str, float, List[Dict[str, Union[str, float]]]]]:
    """Search for radio control cars and parts by price, description, and distance.

    Args:
        postcode: Postcode or outcode to center the search on
        q: Search string with logical operators (e.g., 'car AND battery OR wheels')
        max_price: Maximum price in pounds to consider
        radius: Search radius in miles around the central postcode

    Returns:
        Dict containing:
            - postcode: The central postcode for the search
            - radius: The search radius in miles
            - max_price: The maximum price considered
            - results: List of matching items with details
    """
    if not postcode or not q:
        raise ValueError("Both 'postcode' and 'q' are required parameters.")

    # Mock data generation based on hash of the query
    import hashlib

    hash_seed = int(hashlib.md5(q.encode()).hexdigest(), 16)

    # Generate mock results
    items = [
        {"name": "RC Car Model A", "price": 150.0, "description": "Fast and durable"},
        {"name": "RC Car Model B", "price": 250.0, "description": "Sleek design"},
        {"name": "RC Battery Pack", "price": 50.0, "description": "Long-lasting"},
        {"name": "RC Wheels Set", "price": 30.0, "description": "All-terrain"},
    ]

    # Filter items based on max_price
    filtered_items = [item for item in items if item["price"] <= max_price]

    # Simulate search logic based on query
    if "AND" in q or "OR" in q:
        # Simple logic to simulate AND/OR processing
        if "AND" in q:
            tokens = q.split(" AND ")
            filtered_items = [
                item
                for item in filtered_items
                if all(token.lower() in item["description"].lower() for token in tokens)
            ]
        elif "OR" in q:
            tokens = q.split(" OR ")
            filtered_items = [
                item
                for item in filtered_items
                if any(token.lower() in item["description"].lower() for token in tokens)
            ]
    else:
        filtered_items = [
            item for item in filtered_items if q.lower() in item["description"].lower()
        ]

    # Randomly shuffle results for variety
    import random

    random.seed(hash_seed)
    random.shuffle(filtered_items)

    return {
        "postcode": postcode,
        "radius": radius,
        "max_price": max_price,
        "results": filtered_items,
    }


from typing import Dict, Union


def remove_from_cart(user_id: str, product_id: str) -> Dict[str, Union[str, bool]]:
    """Remove a product from the user's shopping cart.

    Args:
        user_id: The unique identifier for the user.
        product_id: The unique identifier for the product to remove.

    Returns:
        Dict containing:
            - user_id: The unique identifier for the user.
            - product_id: The unique identifier for the product.
            - removed: Boolean indicating if the product was successfully removed.
    """

    # Simulated cart data for demonstration purposes
    cart_data = {
        "user_123": ["prod_001", "prod_002", "prod_003"],
        "user_456": ["prod_004", "prod_005"],
    }

    if user_id not in cart_data:
        raise ValueError(f"User ID not found: {user_id}")

    if product_id not in cart_data[user_id]:
        return {
            "user_id": user_id,
            "product_id": product_id,
            "removed": False,
        }

    cart_data[user_id].remove(product_id)

    return {
        "user_id": user_id,
        "product_id": product_id,
        "removed": True,
    }


from typing import Dict, List, Literal, Union


def search_listings(
    query: str,
    category: Literal["cpu", "gpu", "ram", "ssd", "psu", "case", "motherboard"],
    condition: Literal["new", "used", "refurbished", "open-box"] = "new",
    marketplaces: List[str] = None,
    max_price: float = None,
    region: str = "US",
) -> Dict[str, Union[str, float, list]]:
    """Search product listings across supported marketplaces and conditions.

    Args:
        query: Free-text query, e.g., 'RTX 5070'
        category: Component category
        condition: Desired item condition
        marketplaces: Marketplaces to include, e.g., ['Amazon','Newegg','eBay','Facebook Marketplace']
        max_price: Maximum acceptable price in USD
        region: Buyer region for filtering

    Returns:
        Dict containing:
            - query: The search query used
            - category: The category of the product
            - results: List of dictionaries with product details
    """
    if marketplaces is None:
        marketplaces = ["Amazon", "Newegg", "eBay", "Facebook Marketplace"]

    sample_data = {
        "RTX 5070": [
            {"marketplace": "Amazon", "price": 499.99, "condition": "new"},
            {"marketplace": "eBay", "price": 450.00, "condition": "used"},
            {"marketplace": "Newegg", "price": 475.00, "condition": "refurbished"},
        ],
        "Ryzen 9": [
            {"marketplace": "Amazon", "price": 399.99, "condition": "new"},
            {"marketplace": "eBay", "price": 350.00, "condition": "used"},
        ],
    }

    if query not in sample_data:
        raise ValueError(f"No listings found for query: {query}")

    results = [
        item
        for item in sample_data[query]
        if item["marketplace"] in marketplaces
        and item["condition"] == condition
        and (max_price is None or item["price"] <= max_price)
    ]

    return {
        "query": query,
        "category": category,
        "results": results,
    }


from typing import Dict, List, Literal, Optional, Union


def search_monitors(
    size: Optional[float] = None,
    pixel_type: Optional[Literal["VA", "TN", "IPS", "OLED", "QD-OLED"]] = None,
    refresh_rate: Optional[float] = None,
    resolution: Optional[
        Literal[
            "1280x720", "1280x1024", "1920x1080", "2560x1440", "3840x2160", "5120x2880"
        ]
    ] = None,
) -> List[Dict[str, Union[str, float]]]:
    """Search for monitors that fit the given parameter values.

    Args:
        size: The size of the monitor, in inches.
        pixel_type: The type of pixel used in the monitor.
        refresh_rate: The maximum refresh rate of the monitor, in hertz.
        resolution: The native resolution of the monitor, in pixels.

    Returns:
        List of dictionaries, each containing:
            - model: Model name of the monitor
            - size: Size of the monitor in inches
            - pixel_type: Type of pixel used in the monitor
            - refresh_rate: Maximum refresh rate in hertz
            - resolution: Native resolution of the monitor
    """
    sample_monitors = [
        {
            "model": "Dell UltraSharp",
            "size": 27,
            "pixel_type": "IPS",
            "refresh_rate": 60,
            "resolution": "2560x1440",
        },
        {
            "model": "Samsung Odyssey",
            "size": 32,
            "pixel_type": "VA",
            "refresh_rate": 144,
            "resolution": "3840x2160",
        },
        {
            "model": "LG UltraFine",
            "size": 24,
            "pixel_type": "IPS",
            "refresh_rate": 60,
            "resolution": "1920x1080",
        },
        {
            "model": "Asus ROG Swift",
            "size": 27,
            "pixel_type": "TN",
            "refresh_rate": 240,
            "resolution": "1920x1080",
        },
        {
            "model": "Acer Predator",
            "size": 34,
            "pixel_type": "OLED",
            "refresh_rate": 120,
            "resolution": "5120x2880",
        },
    ]

    def matches_criteria(monitor: Dict[str, Union[str, float]]) -> bool:
        return (
            (size is None or monitor["size"] == size)
            and (pixel_type is None or monitor["pixel_type"] == pixel_type)
            and (refresh_rate is None or monitor["refresh_rate"] == refresh_rate)
            and (resolution is None or monitor["resolution"] == resolution)
        )

    results = [monitor for monitor in sample_monitors if matches_criteria(monitor)]

    if not results:
        raise ValueError("No monitors found matching the given criteria.")

    return results


from datetime import datetime
from typing import Dict, Union


def set_price_alert(
    model: str, target_price: float, region: str = "US", expire_date: str = None
) -> Dict[str, Union[str, float, bool]]:
    """Create a price alert for a model when it drops to a target price.

    Args:
        model: Product/Model to set the alert for
        target_price: Notify when price is at or below this amount (USD)
        region: Region for alert (default is 'US')
        expire_date: Expiration date for the alert in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - model: The model for which the alert is set
            - target_price: The target price for the alert
            - region: The region for the alert
            - expire_date: The expiration date of the alert
            - alert_set: Boolean indicating if the alert was successfully set
    """
    # Validate expiration date format
    if expire_date:
        try:
            datetime.strptime(expire_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("expire_date must be in 'YYYY-MM-DD' format")

    # Simulate setting the alert
    alert_set = hash((model, target_price, region, expire_date)) % 2 == 0

    return {
        "model": model,
        "target_price": target_price,
        "region": region,
        "expire_date": expire_date if expire_date else "No expiration",
        "alert_set": alert_set,
    }


from typing import Dict, Union


def track_delivery(id: int) -> Dict[str, Union[int, str, List[str]]]:
    """See where a package is in transit.

    Args:
        id: The id of the package

    Returns:
        Dict containing:
            - id: The package id
            - status: Current status of the package
            - location: Current location of the package
            - history: List of locations the package has been through
    """
    if id <= 0:
        raise ValueError("Package id must be a positive integer")

    # Simulated package data
    package_data = {
        1: {
            "status": "In Transit",
            "location": "New York",
            "history": ["Los Angeles", "Chicago"],
        },
        2: {
            "status": "Delivered",
            "location": "San Francisco",
            "history": ["Seattle", "Portland"],
        },
        3: {"status": "Pending", "location": "Houston", "history": ["Dallas"]},
    }

    if id not in package_data:
        raise ValueError(f"Package id not found: {id}")

    package_info = package_data[id]

    return {
        "id": id,
        "status": package_info["status"],
        "location": package_info["location"],
        "history": package_info["history"],
    }


from typing import Dict, Union


def update_item(item_name: str, new_quantity: float) -> Dict[str, Union[str, float]]:
    """Update the details of an item in the warehouse inventory.

    Args:
        item_name: The name of the item to update.
        new_quantity: The new quantity of the item.

    Returns:
        Dict containing:
            - item_name: The name of the updated item
            - new_quantity: The updated quantity of the item
            - status: Status message indicating success or failure
    """
    inventory = {
        "widget": 100,
        "gadget": 200,
        "doohickey": 50,
    }

    if item_name not in inventory:
        raise ValueError(f"Item not found in inventory: {item_name}")

    if new_quantity < 0:
        raise ValueError("New quantity cannot be negative")

    inventory[item_name] = new_quantity

    return {
        "item_name": item_name,
        "new_quantity": new_quantity,
        "status": "Update successful",
    }
