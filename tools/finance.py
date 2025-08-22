# Finance Tools
# Auto-generated implementations from cached categorization

from typing import Any, Dict, List, Optional, Union


def card_search(
    card_name: Optional[str] = None,
    card_text: Optional[str] = None,
    card_type: Optional[str] = None,
    card_rulings: Optional[str] = None,
    card_cost: Optional[str] = None,
) -> Dict[str, Union[str, None]]:
    """Search for a card in the database based on various parameters.

    Args:
        card_name: A unique name given to each card.
        card_text: Text explaining how this card alters the normal game rules.
        card_type: Type of the card (e.g., 'Door', 'Monster', 'Treasure').
        card_rulings: List of rulings involving this card.
        card_cost: Resources needed to play the card.

    Returns:
        Dict containing:
            - card_name: Name of the card
            - card_text: Description of the card's effect
            - card_type: Type of the card
            - card_rulings: Rulings related to the card
            - card_cost: Cost to play the card
    """
    # Sample card database
    sample_cards = {
        "Dragon Slayer": {
            "card_text": "Defeat any dragon instantly.",
            "card_type": "Monster",
            "card_rulings": "Can only be used once per game.",
            "card_cost": "3 Mana",
        },
        "Treasure Chest": {
            "card_text": "Gain 5 gold.",
            "card_type": "Treasure",
            "card_rulings": "Cannot be used if you have more than 10 gold.",
            "card_cost": "1 Mana",
        },
    }

    # Search logic
    for name, details in sample_cards.items():
        if (
            (card_name is None or card_name == name)
            and (card_text is None or card_text in details["card_text"])
            and (card_type is None or card_type == details["card_type"])
            and (card_rulings is None or card_rulings in details["card_rulings"])
            and (card_cost is None or card_cost == details["card_cost"])
        ):
            return {
                "card_name": name,
                "card_text": details["card_text"],
                "card_type": details["card_type"],
                "card_rulings": details["card_rulings"],
                "card_cost": details["card_cost"],
            }

    raise ValueError("No matching card found in the database.")


from typing import Dict, Literal, Union


def close_position(
    stock_name: str, amount: float, type: Literal["long", "short"]
) -> Dict[str, Union[str, float, bool]]:
    """Closes an existing open position for a given stock.

    Args:
        stock_name: The name or ticker symbol of the stock to close the position for.
        amount: The amount of the stock to close. Use full position size to fully close.
        type: Specifies whether the position being closed is 'long' or 'short'.

    Returns:
        Dict containing:
            - stock_name: The name of the stock
            - amount_closed: The amount of stock closed
            - position_type: The type of position closed ('long' or 'short')
            - success: Boolean indicating if the position was successfully closed
    """

    # Simulated data for existing positions
    positions = {
        "AAPL": {"long": 50, "short": 20},
        "GOOGL": {"long": 30, "short": 10},
        "TSLA": {"long": 40, "short": 15},
    }

    if stock_name not in positions:
        raise ValueError(f"Stock not found: {stock_name}")

    if type not in positions[stock_name]:
        raise ValueError(f"Invalid position type: {type}")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    current_position = positions[stock_name][type]

    if amount > current_position:
        raise ValueError("Amount exceeds current position size")

    # Simulate closing the position
    positions[stock_name][type] -= amount
    success = True

    return {
        "stock_name": stock_name,
        "amount_closed": amount,
        "position_type": type,
        "success": success,
    }


import hashlib
from typing import Dict, Union


def convert_currency(
    amount: float, from_currency: str, to_currency: str, date: str = None
) -> Dict[str, Union[float, str]]:
    """Convert an amount from one currency to another.

    Args:
        amount: The amount of money to convert
        from_currency: The currency code to convert from (e.g., 'USD', 'AUD')
        to_currency: The currency code to convert to (e.g., 'USD', 'AUD')
        date: Optional historical date in ISO format (YYYY-MM-DD) for conversion rate

    Returns:
        Dict containing:
            - amount: Converted amount in the target currency
            - currency: Target currency code
    """
    if from_currency == to_currency:
        return {"amount": amount, "currency": to_currency}

    # Simulate exchange rates using a hash-based approach for consistency
    hash_input = f"{from_currency}-{to_currency}-{date}".encode()
    hash_value = int(hashlib.sha256(hash_input).hexdigest(), 16)
    exchange_rate = (hash_value % 10000) / 10000 + 0.5  # Rate between 0.5 and 1.5

    converted_amount = amount * exchange_rate
    return {"amount": round(converted_amount, 2), "currency": to_currency}


import hashlib
from typing import Dict, Literal, Union


def currency_converter(
    amount: float,
    from_currency: str,
    to_currency: str,
    operation: Literal["convert", "get_conversion_rate"],
    date: str = None,
) -> Dict[str, Union[float, str]]:
    """Convert amounts between different currencies or retrieve exchange rates.

    Args:
        amount: The amount of money to convert
        from_currency: The currency of the amount
        to_currency: The currency for the amount to be converted into
        operation: The operation to perform ('convert' or 'get_conversion_rate')
        date: The date of the conversion (optional)

    Returns:
        Dict containing:
            - converted_amount: Converted amount of money (if operation is 'convert')
            - exchange_rate: Exchange rate used for conversion (if operation is 'convert')
            - rate: Exchange rate between currencies (if operation is 'get_conversion_rate')
            - from_currency: Original currency
            - to_currency: Target currency
    """

    # Simulate exchange rates using a hash-based approach for consistency
    def get_mock_exchange_rate(from_currency: str, to_currency: str) -> float:
        hash_input = f"{from_currency}_{to_currency}".encode()
        hash_value = hashlib.md5(hash_input).hexdigest()
        return (int(hash_value[:8], 16) % 5000) / 100 + 0.5  # Rate between 0.5 and 50.5

    if from_currency == to_currency:
        raise ValueError("from_currency and to_currency must be different")

    exchange_rate = get_mock_exchange_rate(from_currency, to_currency)

    if operation == "convert":
        converted_amount = amount * exchange_rate
        return {
            "converted_amount": converted_amount,
            "exchange_rate": exchange_rate,
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
    elif operation == "get_conversion_rate":
        return {
            "rate": exchange_rate,
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
    else:
        raise ValueError(
            "Unsupported operation. Use 'convert' or 'get_conversion_rate'."
        )


from typing import Dict, Union


def set_long_order(
    stock_name: str,
    amount: float,
    stop_loss: float,
    take_profit: float,
    leverage: float,
    price: Union[float, None] = None,
) -> Dict[str, Union[str, float, bool]]:
    """Places a long order for a stock with specified parameters.

    Args:
        stock_name: The name or ticker symbol of the stock to buy.
        amount: The amount of the stock to purchase, in units or currency depending on broker settings.
        price: The price per unit for the order. If omitted, a market order will be placed.
        stop_loss: The stop loss price to limit downside risk.
        take_profit: The take profit price to automatically close the trade in profit.
        leverage: Leverage multiplier for the trade.

    Returns:
        Dict containing:
            - stock_name: The name or ticker symbol of the stock.
            - amount: The amount of stock purchased.
            - price: The price per unit for the order.
            - stop_loss: The stop loss price set for the order.
            - take_profit: The take profit price set for the order.
            - leverage: Leverage used for the trade.
            - order_placed: Boolean indicating if the order was successfully placed.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if stop_loss >= take_profit:
        raise ValueError("Stop loss must be less than take profit.")
    if leverage <= 0:
        raise ValueError("Leverage must be greater than zero.")

    # Simulate order placement
    order_placed = True

    # Mocked sample data
    sample_price = 100.0 if price is None else price

    return {
        "stock_name": stock_name,
        "amount": amount,
        "price": sample_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "leverage": leverage,
        "order_placed": order_placed,
    }


from typing import Dict, Union


def set_short_order(
    stock_name: str,
    amount: float,
    stop_loss: float,
    take_profit: float,
    leverage: float,
    price: Union[float, None] = None,
) -> Dict[str, Union[str, float]]:
    """Place a short order for a stock with specified parameters.

    Args:
        stock_name: The name or ticker symbol of the stock to sell short.
        amount: The amount of the stock to sell short, in units or currency.
        stop_loss: The stop loss price to limit upside risk.
        take_profit: The take profit price to automatically close the trade in profit.
        leverage: Leverage multiplier for the trade.
        price: The price per unit for the order. If omitted, a market order will be placed.

    Returns:
        Dict containing:
            - stock_name: The name or ticker symbol of the stock.
            - amount: The amount of the stock to sell short.
            - price: The price per unit for the order.
            - stop_loss: The stop loss price.
            - take_profit: The take profit price.
            - leverage: Leverage multiplier for the trade.
            - order_type: 'market' if price is None, otherwise 'limit'.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if leverage <= 0:
        raise ValueError("Leverage must be greater than zero.")
    if stop_loss <= 0 or take_profit <= 0:
        raise ValueError("Stop loss and take profit must be greater than zero.")
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than zero if specified.")

    order_type = "market" if price is None else "limit"

    return {
        "stock_name": stock_name,
        "amount": amount,
        "price": price if price is not None else 100.0,  # Mocked market price
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "leverage": leverage,
        "order_type": order_type,
    }


from typing import Dict, Literal, Union


def add_funds(
    amount: float,
    paymentMethod: Literal["credit/debit", "bank transfer", "paypal", "cryptocurrency"],
    cardDetails: Dict[str, str] = None,
    bankDetails: Dict[str, str] = None,
    paypalDetails: Dict[str, str] = None,
    cryptoDetails: Dict[str, str] = None,
) -> Dict[str, Union[str, float]]:
    """Add funds to a player's account using various payment methods.

    Args:
        amount: The amount of money to add to the account in US dollars. Must be at least $10.
        paymentMethod: The payment method to use ('credit/debit', 'bank transfer', 'paypal', 'cryptocurrency').
        cardDetails: The player's credit/debit card details. Required if paymentMethod is 'credit/debit'.
        bankDetails: The player's bank account details. Required if paymentMethod is 'bank transfer'.
        paypalDetails: The player's PayPal details. Required if paymentMethod is 'paypal'.
        cryptoDetails: The player's cryptocurrency wallet details. Required if paymentMethod is 'cryptocurrency'.

    Returns:
        Dict containing:
            - status: The status of the transaction ('success' or 'failure').
            - transactionId: A unique identifier for the transaction.
            - message: A message describing the result of the transaction.
    """
    if amount < 10:
        raise ValueError("Amount must be at least $10.")

    if paymentMethod == "credit/debit":
        if not cardDetails:
            raise ValueError(
                "Card details are required for credit/debit payment method."
            )
        # Simulate card processing
        transaction_id = hash(f"{cardDetails['cardNumber']}{amount}") % 1000000
        return {
            "status": "success",
            "transactionId": f"CC-{transaction_id}",
            "message": f"Added ${amount} to your account using credit/debit card.",
        }

    if paymentMethod == "bank transfer":
        if not bankDetails:
            raise ValueError(
                "Bank details are required for bank transfer payment method."
            )
        # Simulate bank transfer processing
        transaction_id = hash(f"{bankDetails['accountNumber']}{amount}") % 1000000
        return {
            "status": "success",
            "transactionId": f"BT-{transaction_id}",
            "message": f"Added ${amount} to your account via bank transfer.",
        }

    if paymentMethod == "paypal":
        if not paypalDetails:
            raise ValueError("PayPal details are required for PayPal payment method.")
        # Simulate PayPal processing
        transaction_id = hash(f"{paypalDetails['paypalEmail']}{amount}") % 1000000
        return {
            "status": "success",
            "transactionId": f"PP-{transaction_id}",
            "message": f"Added ${amount} to your account using PayPal.",
        }

    if paymentMethod == "cryptocurrency":
        if not cryptoDetails:
            raise ValueError(
                "Cryptocurrency details are required for cryptocurrency payment method."
            )
        # Simulate cryptocurrency processing
        transaction_id = hash(f"{cryptoDetails['walletAddress']}{amount}") % 1000000
        return {
            "status": "success",
            "transactionId": f"CR-{transaction_id}",
            "message": f"Added ${amount} to your account using cryptocurrency.",
        }

    raise ValueError("Unsupported payment method.")


from datetime import datetime
from typing import Dict, Literal, Optional, Union


def add_transaction(
    amount: float,
    type: Literal["income", "expense"],
    date: str,
    category: Optional[
        Literal["groceries", "dining", "rent", "entertainment", "misc"]
    ] = None,
    notes: Optional[str] = None,
) -> Dict[str, Union[float, str, None]]:
    """Add a new transaction to the ledger.

    Args:
        amount: The dollar amount of the transaction
        type: The type of the transaction ('income' or 'expense')
        date: The date and time of the transaction in ISO 8601 format
        category: The category of the transaction (optional)
        notes: Note about the transaction (optional)

    Returns:
        Dict containing:
            - amount: The dollar amount of the transaction
            - type: The type of the transaction
            - date: The date and time of the transaction
            - category: The category of the transaction
            - notes: Note about the transaction

    Raises:
        ValueError: If the date is not in a valid ISO 8601 format
    """
    try:
        # Validate date format
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError(f"Invalid date format: {date}")

    # Mocked transaction storage
    transaction_id = hash((amount, type, date, category, notes)) % 10000

    return {
        "transaction_id": transaction_id,
        "amount": amount,
        "type": type,
        "date": date,
        "category": category,
        "notes": notes,
    }


import math
import statistics
from typing import Dict, List, Union


def analyze_portfolio_risk(
    portfolio_config: Dict[str, Union[List[float], int, float]]
) -> Dict[str, Union[float, str]]:
    """Calculate portfolio risk metrics including volatility, Sharpe ratio, and value at risk.

    Args:
        portfolio_config: Object containing:
            - holdings: List of daily returns of the portfolio
            - period: Analysis time period in days
            - confidence_level: Confidence level for VaR (e.g., 0.95 for 95%)
            - risk_free_rate: Risk-free rate as a decimal (e.g., 0.01 for 1%)

    Returns:
        Dict containing:
            - volatility: Annualized volatility of the portfolio
            - sharpe_ratio: Sharpe ratio of the portfolio
            - value_at_risk: Value at Risk (VaR) of the portfolio
    """
    holdings = portfolio_config.get("holdings", [])
    period = portfolio_config.get("period", 252)
    confidence_level = portfolio_config.get("confidence_level", 0.95)
    risk_free_rate = portfolio_config.get("risk_free_rate", 0.01)

    if not holdings:
        raise ValueError("Portfolio holdings cannot be empty")

    # Calculate daily returns volatility using standard library
    daily_volatility = statistics.stdev(holdings)
    annualized_volatility = daily_volatility * math.sqrt(period)

    # Calculate Sharpe ratio
    average_return = statistics.mean(holdings)
    excess_return = average_return - risk_free_rate / period
    sharpe_ratio = excess_return / daily_volatility

    # Calculate Value at Risk (VaR)
    sorted_returns = sorted(holdings)
    var_index = int((1 - confidence_level) * len(sorted_returns))
    value_at_risk = -sorted_returns[var_index]

    return {
        "volatility": round(annualized_volatility, 4),
        "sharpe_ratio": round(sharpe_ratio, 4),
        "value_at_risk": round(value_at_risk, 4),
    }


from typing import Dict, Optional, Union


def authenticate_payment_account(
    username: Optional[str] = None,
    password: Optional[str] = None,
    o_auth_token: Optional[str] = None,
    is_single_use: bool = True,
    expiration_time: Optional[float] = None,
) -> Dict[str, Union[str, bool, float]]:
    """Authenticate a payment account and return an authentication token.

    Args:
        username: Username for the payment account.
        password: Password for the payment account.
        o_auth_token: OAuth token which can be used to authenticate in place of username and password.
        is_single_use: If true, the authentication token returned can only be used for one transaction.
        expiration_time: A custom expiration time for the payment authentication token.

    Returns:
        Dict containing:
            - token: The authentication token.
            - is_single_use: Whether the token is single-use.
            - expiration_time: The expiration time of the token.

    Raises:
        ValueError: If neither username/password nor o_auth_token is provided.
    """
    if not (username and password) and not o_auth_token:
        raise ValueError("Either username/password or o_auth_token must be provided.")

    # Simulate token generation
    token = "auth_" + (username or "oauth") + "_token"

    # Default expiration time if not provided
    if expiration_time is None:
        expiration_time = 3600.0  # Default to 1 hour

    return {
        "token": token,
        "is_single_use": is_single_use,
        "expiration_time": expiration_time,
    }


from typing import Dict


def business_netincome(city: str, income: int, expenses: int) -> Dict[str, int]:
    """Determine the net income of a business after expenses and taxes.

    Args:
        city: City to determine taxes and other fees for
        income: Input for income
        expenses: Input for expenses, not including fees or taxes

    Returns:
        Dict containing:
            - income: Total income
            - expenses: Total expenses
            - taxes: Calculated taxes based on city
            - net_income: Net income after expenses and taxes
    """

    # Sample tax rates by city
    tax_rates = {
        "New York": 0.08,
        "Los Angeles": 0.09,
        "Chicago": 0.07,
        "Houston": 0.06,
        "Phoenix": 0.05,
    }

    if city not in tax_rates:
        raise ValueError(f"City not supported: {city}")

    # Calculate taxes
    taxes = int(income * tax_rates[city])

    # Calculate net income
    net_income = income - expenses - taxes

    return {
        "income": income,
        "expenses": expenses,
        "taxes": taxes,
        "net_income": net_income,
    }


from typing import Dict, Optional, Union


def calculate_compound_interest(
    investment_data: Dict[str, Union[float, int, Optional[str]]]
) -> Dict[str, Union[float, str]]:
    """Calculate compound interest over a specified time period with options for different compounding frequencies.

    Args:
        investment_data: Object containing:
            - principal: Initial amount of money (float)
            - rate: Annual interest rate as a decimal (float)
            - time: Time in years (int)
            - frequency: Compounding frequency ('annually', 'semiannually', 'quarterly', 'monthly', 'daily') (optional, default is 'annually')

    Returns:
        Dict containing:
            - total_amount: Total amount after interest (float)
            - interest_earned: Interest earned over the period (float)
    """
    principal = investment_data.get("principal")
    rate = investment_data.get("rate")
    time = investment_data.get("time")
    frequency = investment_data.get("frequency", "annually")

    if principal is None or rate is None or time is None:
        raise ValueError(
            "Missing required investment data: 'principal', 'rate', and 'time' must be provided."
        )

    frequencies = {
        "annually": 1,
        "semiannually": 2,
        "quarterly": 4,
        "monthly": 12,
        "daily": 365,
    }

    if frequency not in frequencies:
        raise ValueError(f"Unsupported compounding frequency: {frequency}")

    n = frequencies[frequency]
    total_amount = principal * (1 + rate / n) ** (n * time)
    interest_earned = total_amount - principal

    return {
        "total_amount": round(total_amount, 2),
        "interest_earned": round(interest_earned, 2),
    }


from typing import Dict, List, Union


def calculate_loan_payment(
    loan_details: Dict[str, Union[float, int, bool]]
) -> Dict[str, Union[float, List[Dict[str, Union[int, float]]]]]:
    """Calculate monthly loan payments and generate amortization schedule details.

    Args:
        loan_details: Object containing:
            - loan_amount: Total loan amount
            - annual_interest_rate: Annual interest rate as a decimal
            - loan_term_years: Loan term in years
            - extra_payment: Optional extra payment amount per month
            - generate_schedule: Flag to indicate if amortization schedule should be generated

    Returns:
        Dict containing:
            - monthly_payment: Calculated monthly payment amount
            - amortization_schedule: List of dictionaries with amortization details per month (if requested)
    """
    loan_amount = loan_details.get("loan_amount", 0)
    annual_interest_rate = loan_details.get("annual_interest_rate", 0)
    loan_term_years = loan_details.get("loan_term_years", 0)
    extra_payment = loan_details.get("extra_payment", 0)
    generate_schedule = loan_details.get("generate_schedule", False)

    if loan_amount <= 0 or annual_interest_rate < 0 or loan_term_years <= 0:
        raise ValueError("Invalid loan details provided.")

    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / number_of_payments
    else:
        monthly_payment = (
            loan_amount
            * monthly_interest_rate
            / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        )

    monthly_payment += extra_payment

    amortization_schedule = []
    remaining_balance = loan_amount

    for month in range(1, number_of_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        if generate_schedule:
            amortization_schedule.append(
                {
                    "month": month,
                    "interest_payment": round(interest_payment, 2),
                    "principal_payment": round(principal_payment, 2),
                    "remaining_balance": round(max(remaining_balance, 0), 2),
                }
            )

        if remaining_balance <= 0:
            break

    return {
        "monthly_payment": round(monthly_payment, 2),
        "amortization_schedule": amortization_schedule if generate_schedule else [],
    }


from typing import Dict


def check_balance(account_id: str) -> Dict[str, Union[str, float]]:
    """Get the current balance for a specific bank account.

    Args:
        account_id: Internal account ID or last-4 (e.g., '****4321')

    Returns:
        Dict containing:
            - account_id: The account ID or last-4 digits
            - balance: Current balance of the account in USD
    """
    sample_accounts = {
        "****1234": 1500.75,
        "****4321": 2450.50,
        "****5678": 320.00,
    }
    if account_id not in sample_accounts:
        raise ValueError(f"Account ID not found: {account_id}")

    return {
        "account_id": account_id,
        "balance": sample_accounts[account_id],
    }


from typing import Dict, Literal, Union


def collect_payment(
    invoice_id: str,
    amount_gbp: float,
    payment_method: Literal["card_on_file", "new_card", "bank_transfer"],
    reference: str = "",
) -> Dict[str, Union[str, float, bool]]:
    """Take payment for an invoice or balance.

    Args:
        invoice_id: Unique identifier for the invoice
        amount_gbp: Payment amount in British pounds
        payment_method: Method for payment ('card_on_file', 'new_card', 'bank_transfer')
        reference: Payment reference or note

    Returns:
        Dict containing:
            - invoice_id: The invoice identifier
            - amount_gbp: The amount paid in GBP
            - payment_method: The method used for payment
            - reference: The payment reference or note
            - success: Boolean indicating if the payment was successful
    """
    if amount_gbp < 0:
        raise ValueError("Payment amount cannot be negative")

    # Simulate payment processing
    success = hash(invoice_id + payment_method) % 2 == 0

    return {
        "invoice_id": invoice_id,
        "amount_gbp": amount_gbp,
        "payment_method": payment_method,
        "reference": reference,
        "success": success,
    }


import hashlib
from typing import Dict, List, Union


def compare_stocks(
    tickers: Union[List[str], str], days: int = 30
) -> Dict[str, Union[Dict[str, float], str]]:
    """Compare stock performance over a specified number of days.

    Args:
        tickers: List of stock ticker symbols to compare, or comma-separated string.
        days: Number of calendar days to look back (must be non-negative).

    Returns:
        Dict containing:
            - percentage_changes: A dictionary with tickers as keys and their percentage change as values.
            - top_performer: The ticker symbol of the stock with the highest percentage increase.
    """
    if days < 0:
        raise ValueError("Number of days must be non-negative")

    # Handle both list and comma-separated string input
    if isinstance(tickers, str):
        ticker_list = [ticker.strip() for ticker in tickers.split(",")]
    else:
        ticker_list = tickers

    def generate_percentage_change(ticker: str, days: int) -> float:
        """Generate a mock percentage change for a given ticker and days."""
        hash_input = f"{ticker}{days}".encode()
        hash_value = hashlib.sha256(hash_input).hexdigest()
        return (int(hash_value, 16) % 2000 - 1000) / 10.0  # Range: -100.0% to +100.0%

    percentage_changes = {
        ticker: generate_percentage_change(ticker, days) for ticker in ticker_list
    }
    top_performer = max(percentage_changes, key=percentage_changes.get)

    return {
        "percentage_changes": percentage_changes,
        "top_performer": top_performer,
    }


from typing import Dict


def confirm_applicant(name: str, school: str) -> Dict[str, bool]:
    """Check if the applicant is valid for the given school.

    Args:
        name: The name of the applicant
        school: School the applicant is applying to

    Returns:
        Dict containing:
            - valid: Boolean indicating if the applicant is valid
    """
    if not name or not school:
        raise ValueError("Both name and school must be provided.")

    # Simulated hash-based validation logic
    valid_schools = {
        "Harvard": "Alice",
        "MIT": "Bob",
        "Stanford": "Charlie",
    }

    is_valid = valid_schools.get(school) == name

    return {
        "valid": is_valid,
    }


from typing import Dict


def delete_transaction(transaction_id: str) -> Dict[str, str]:
    """Delete an existing transaction.

    Args:
        transaction_id: The ID of the transaction to delete

    Returns:
        Dict containing:
            - transaction_id: The ID of the deleted transaction
            - status: Status message indicating the result of the deletion
    """
    # Simulated database of transactions
    transactions = {
        "txn_001": {"amount": 100, "currency": "USD"},
        "txn_002": {"amount": 200, "currency": "EUR"},
        "txn_003": {"amount": 300, "currency": "JPY"},
    }

    if transaction_id not in transactions:
        raise ValueError(f"Transaction ID not found: {transaction_id}")

    # Simulate deletion
    del transactions[transaction_id]

    return {
        "transaction_id": transaction_id,
        "status": "Transaction successfully deleted",
    }


from typing import Dict


def dispute_transaction(
    account_id: str, transaction_id: str, reason: str
) -> Dict[str, str]:
    """Open a dispute for a posted transaction.

    Args:
        account_id: Account ID or last-4
        transaction_id: Provider transaction identifier
        reason: Reason for dispute

    Returns:
        Dict containing:
            - status: Status of the dispute process
            - dispute_id: Unique identifier for the dispute
            - message: Confirmation message
    """
    if not account_id or not transaction_id or not reason:
        raise ValueError("All parameters must be provided and non-empty.")

    # Simulate a hash-based generation for dispute_id
    dispute_id = f"DISP-{hash((account_id, transaction_id, reason)) % 10000:04}"

    return {
        "status": "success",
        "dispute_id": dispute_id,
        "message": f"Dispute opened successfully for transaction {transaction_id}.",
    }


from typing import Dict, List


def find_nearest_atm(
    postal_code: str,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Find nearby in-network ATMs based on a postal code.

    Args:
        postal_code: ZIP/postal code to search for nearby ATMs

    Returns:
        Dict containing:
            - postal_code: The input postal code
            - atms: List of nearby ATMs with details including:
                - name: Name of the ATM
                - address: Address of the ATM
                - distance: Distance from the postal code in miles
    """

    sample_data = {
        "10001": [
            {"name": "ATM A", "address": "123 Main St, New York, NY", "distance": 0.5},
            {"name": "ATM B", "address": "456 Elm St, New York, NY", "distance": 1.2},
        ],
        "94105": [
            {
                "name": "ATM C",
                "address": "789 Market St, San Francisco, CA",
                "distance": 0.3,
            },
            {
                "name": "ATM D",
                "address": "101 Pine St, San Francisco, CA",
                "distance": 0.8,
            },
        ],
    }

    if postal_code not in sample_data:
        raise ValueError(f"No ATMs found for postal code: {postal_code}")

    return {
        "postal_code": postal_code,
        "atms": sample_data[postal_code],
    }


from typing import Dict


def freeze_card(card_last4: str) -> Dict[str, str]:
    """Temporarily lock a debit/credit card.

    Args:
        card_last4: Last-4 digits of the card

    Returns:
        Dict containing:
            - card_last4: Last-4 digits of the card
            - status: Status of the card after the operation
            - message: Confirmation message
    """
    if len(card_last4) != 4 or not card_last4.isdigit():
        raise ValueError("Invalid card_last4: Must be exactly 4 digits")

    # Simulate card status based on a hash of the card_last4
    status = "frozen" if hash(card_last4) % 2 == 0 else "already frozen"

    return {
        "card_last4": card_last4,
        "status": status,
        "message": f"Card ending in {card_last4} is now {status}.",
    }


from typing import Dict, List, Union


def get_campaign_donors(
    candidate_name: str, sort_by_amount: bool = False, limit: Union[int, None] = None
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Retrieve public campaign donor information for a candidate.

    Args:
        candidate_name: Name of the candidate whose donor records are being requested.
        sort_by_amount: Whether to sort the donor list by amount given (highest to lowest).
        limit: Maximum number of donors to return.

    Returns:
        Dict containing:
            - candidate_name: Name of the candidate
            - donors: List of donor information with:
                - name: Donor's name
                - amount: Amount donated
    """

    # Sample donor data
    sample_donors = {
        "Alice Johnson": [
            {"name": "John Doe", "amount": 250.0},
            {"name": "Jane Smith", "amount": 150.0},
            {"name": "Emily Davis", "amount": 300.0},
        ],
        "Bob Smith": [
            {"name": "Michael Brown", "amount": 500.0},
            {"name": "Chris Green", "amount": 200.0},
            {"name": "Patricia White", "amount": 100.0},
        ],
    }

    if candidate_name not in sample_donors:
        raise ValueError(f"Candidate not supported: {candidate_name}")

    donors = sample_donors[candidate_name]

    if sort_by_amount:
        donors = sorted(donors, key=lambda x: x["amount"], reverse=True)

    if limit is not None:
        donors = donors[:limit]

    return {
        "candidate_name": candidate_name,
        "donors": donors,
    }


from datetime import datetime
from typing import Dict, List, Optional, Union


def get_campaign_expenditures(
    candidate_name: str,
    categories: Optional[List[str]] = None,
    date_range: Optional[Dict[str, str]] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """Retrieve public campaign expenditure information, optionally filtered by category.

    Args:
        candidate_name: Name of the candidate whose expenditures are being requested.
        categories: List of expenditure categories to filter by (e.g., advertising, travel, staff salaries).
        date_range: Optional date range to filter expenditures with 'start_date' and 'end_date' in YYYY-MM-DD format.

    Returns:
        Dict containing:
            - candidate_name: Name of the candidate
            - expenditures: List of expenditures with 'category', 'amount', and 'date'
    """

    # Sample data for demonstration purposes
    sample_expenditures = [
        {"category": "advertising", "amount": 5000.0, "date": "2023-01-15"},
        {"category": "travel", "amount": 2000.0, "date": "2023-02-20"},
        {"category": "staff salaries", "amount": 3000.0, "date": "2023-03-10"},
        {"category": "advertising", "amount": 1500.0, "date": "2023-04-05"},
    ]

    # Filter by categories if provided
    if categories:
        sample_expenditures = [
            exp for exp in sample_expenditures if exp["category"] in categories
        ]

    # Filter by date range if provided
    if date_range:
        start_date = datetime.strptime(
            date_range.get("start_date", "1900-01-01"), "%Y-%m-%d"
        )
        end_date = datetime.strptime(
            date_range.get("end_date", "2100-01-01"), "%Y-%m-%d"
        )
        sample_expenditures = [
            exp
            for exp in sample_expenditures
            if start_date <= datetime.strptime(exp["date"], "%Y-%m-%d") <= end_date
        ]

    return {
        "candidate_name": candidate_name,
        "expenditures": sample_expenditures,
    }


from datetime import datetime
from typing import Dict, Literal


def get_category_total(
    category: Literal["groceries", "dining", "rent", "entertainment", "misc"],
    start_date: str,
    end_date: str,
) -> Dict[str, Union[str, float]]:
    """Get the total amount for a category within a date range.

    Args:
        category: The category to calculate the total for
        start_date: Start date of the range in 'YYYY-MM-DD' format
        end_date: End date of the range in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - category: The category name
            - total: Total amount spent in the category within the date range
    """
    # Sample data representing transactions
    transactions = [
        {"date": "2023-01-15", "category": "groceries", "amount": 150.75},
        {"date": "2023-02-10", "category": "dining", "amount": 60.00},
        {"date": "2023-03-05", "category": "rent", "amount": 1200.00},
        {"date": "2023-03-15", "category": "entertainment", "amount": 200.00},
        {"date": "2023-04-01", "category": "misc", "amount": 75.50},
        {"date": "2023-04-10", "category": "groceries", "amount": 130.00},
        {"date": "2023-05-20", "category": "dining", "amount": 45.25},
    ]

    # Convert string dates to datetime objects for comparison
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    if start > end:
        raise ValueError("Start date must be before or equal to end date.")

    # Calculate the total amount for the specified category and date range
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["category"] == category
        and start <= datetime.strptime(transaction["date"], "%Y-%m-%d") <= end
    )

    return {
        "category": category,
        "total": total,
    }


from typing import Dict, Union


def get_company_profile(registration_number: str) -> Dict[str, Union[str, int]]:
    """Returns the company profile for a given company registration number.

    Args:
        registration_number: Registered company number

    Returns:
        Dict containing:
            - company_name: Name of the company
            - registration_number: Registered company number
            - year_established: Year the company was established
            - industry: Industry sector of the company
    """

    sample_data = {
        "12345678": {
            "company_name": "Tech Innovators Inc.",
            "year_established": 2001,
            "industry": "Technology",
        },
        "87654321": {
            "company_name": "Green Energy Solutions",
            "year_established": 2010,
            "industry": "Renewable Energy",
        },
        "11223344": {
            "company_name": "Global Finance Corp.",
            "year_established": 1998,
            "industry": "Finance",
        },
    }

    if registration_number not in sample_data:
        raise ValueError(f"Registration number not found: {registration_number}")

    profile = sample_data[registration_number]
    return {
        "company_name": profile["company_name"],
        "registration_number": registration_number,
        "year_established": profile["year_established"],
        "industry": profile["industry"],
    }


from typing import Dict, Union


def get_currency_exchange_rate(currency_pair: str) -> Dict[str, Union[str, float]]:
    """Gets the current exchange rate between two currencies.

    Args:
        currency_pair: The currency pair to get the exchange rate for (e.g. 'USD/EUR', 'GBP/JPY')

    Returns:
        Dict containing:
            - currency_pair: The currency pair
            - exchange_rate: The current exchange rate
    """

    sample_rates = {
        "USD/EUR": 0.85,
        "EUR/USD": 1.18,
        "GBP/JPY": 151.23,
        "JPY/GBP": 0.0066,
    }

    if currency_pair not in sample_rates:
        raise ValueError(f"Currency pair not supported: {currency_pair}")

    return {
        "currency_pair": currency_pair,
        "exchange_rate": sample_rates[currency_pair],
    }


from typing import Dict, Union


def get_current_stock_price(
    ticker_symbol: str,
    is_market_open: bool,
    is_end_of_day_price: bool,
    time_date: str,
    fetch_ticker_name: Union[str, None] = None,
) -> Dict[str, Union[str, float, bool]]:
    """Fetch the current stock price of a publicly traded company.

    Args:
        ticker_symbol: Ticker symbol of the publicly traded company.
        is_market_open: If between 09:30 AM and 4 PM Monday-Friday, then true.
        is_end_of_day_price: If is_market_open is false then end_of_day is true.
        time_date: Current time and date in format YYYY-MM-DD HH:MM:SS.
        fetch_ticker_name: Optional; return full name of the same publicly traded company.

    Returns:
        Dict containing:
            - ticker_symbol: The ticker symbol of the company.
            - company_name: Full name of the company if requested.
            - current_price: Current stock price.
            - is_market_open: Whether the market is currently open.
            - is_end_of_day_price: Whether the price is an end-of-day price.
            - time_date: The time and date of the price retrieval.
    """

    # Sample data for demonstration purposes
    sample_data = {
        "AAPL": {"name": "Apple Inc.", "price": 150.00},
        "GOOGL": {"name": "Alphabet Inc.", "price": 2800.00},
        "AMZN": {"name": "Amazon.com, Inc.", "price": 3400.00},
        "KO": {"name": "Coca Cola Corporation", "price": 42.00},
    }

    if ticker_symbol not in sample_data:
        raise ValueError(f"Ticker symbol not supported: {ticker_symbol}")

    company_data = sample_data[ticker_symbol]
    company_name = company_data["name"] if fetch_ticker_name else None
    current_price = company_data["price"]

    return {
        "ticker_symbol": ticker_symbol,
        "company_name": company_name,
        "current_price": current_price,
        "is_market_open": is_market_open,
        "is_end_of_day_price": is_end_of_day_price,
        "time_date": time_date,
    }


import hashlib
from typing import Dict, Union


def get_eod_stock_price(
    ticker_symbol: str, date: str, fetch_ticker_name: Union[str, None] = None
) -> Dict[str, Union[str, float]]:
    """Fetch the end of day stock price of a publicly traded company.

    Args:
        ticker_symbol: The ticker symbol of the publicly traded company (e.g. 'AAPL', 'GOOGL')
        date: The date of the end of day price in format YYYY-MM-DD
        fetch_ticker_name: Optional; if provided, return the full name of the company

    Returns:
        Dict containing:
            - ticker_symbol: The ticker symbol of the company
            - date: The date of the stock price
            - eod_price: The end of day stock price
            - company_name: The full name of the company (if fetch_ticker_name is provided)
    """

    # Sample data for company names
    company_names = {
        "AAPL": "Apple Inc.",
        "GOOGL": "Alphabet Inc.",
        "MSFT": "Microsoft Corporation",
        "KO": "Coca Cola Corporation",
    }

    if ticker_symbol not in company_names:
        raise ValueError(f"Ticker symbol not supported: {ticker_symbol}")

    # Generate a mock end of day price using a hash of the ticker and date
    hash_input = f"{ticker_symbol}-{date}".encode()
    hash_value = hashlib.sha256(hash_input).hexdigest()
    eod_price = round(
        int(hash_value[:8], 16) % 1000 + 100, 2
    )  # Price between 100 and 1099.99

    result = {
        "ticker_symbol": ticker_symbol,
        "date": date,
        "eod_price": eod_price,
    }

    if fetch_ticker_name:
        result["company_name"] = company_names[ticker_symbol]

    return result


from typing import Dict, Union


def get_latest_rates(base: str = "USD") -> Dict[str, Union[str, Dict[str, float]]]:
    """Returns all the rates for a specific currency.

    Args:
        base: The 3 letters currency name (e.g. 'USD', 'EUR')

    Returns:
        Dict containing:
            - base: The base currency
            - rates: A dictionary with currency codes as keys and exchange rates as values
    """

    sample_rates = {
        "USD": {"EUR": 0.85, "JPY": 110.0, "GBP": 0.75},
        "EUR": {"USD": 1.18, "JPY": 129.53, "GBP": 0.88},
        "JPY": {"USD": 0.0091, "EUR": 0.0077, "GBP": 0.0068},
        "GBP": {"USD": 1.33, "EUR": 1.14, "JPY": 147.0},
    }

    if base not in sample_rates:
        raise ValueError(f"Base currency not supported: {base}")

    return {
        "base": base,
        "rates": sample_rates.get(base, {}),
    }


from typing import Dict


def get_registration_number(company_name: str) -> Dict[str, str]:
    """Returns the registration number for a registered company name.

    Args:
        company_name: Registered company name

    Returns:
        Dict containing:
            - company_name: The name of the company
            - registration_number: The registration number of the company
    """
    if not company_name:
        raise ValueError("Company name must be provided")

    # Simulate a hash-based registration number generation
    registration_number = f"REG-{abs(hash(company_name)) % 1000000:06}"

    return {
        "company_name": company_name,
        "registration_number": registration_number,
    }


from typing import Dict, List, Union


def get_stock_symbol(query: str) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Search for stock symbols for companies matching the given query.

    Args:
        query: The search term to look up ticker symbols for (the company name).

    Returns:
        Dict containing:
            - query: The original search query
            - results: List of dictionaries with:
                - symbol: Ticker symbol of the company
                - name: Full name of the company
                - exchange: Stock exchange where the company is listed
    """

    sample_data = {
        "Apple": [
            {"symbol": "AAPL", "name": "Apple Inc.", "exchange": "NASDAQ"},
        ],
        "Microsoft": [
            {"symbol": "MSFT", "name": "Microsoft Corporation", "exchange": "NASDAQ"},
        ],
        "Amazon": [
            {"symbol": "AMZN", "name": "Amazon.com, Inc.", "exchange": "NASDAQ"},
        ],
        "Google": [
            {"symbol": "GOOGL", "name": "Alphabet Inc.", "exchange": "NASDAQ"},
            {"symbol": "GOOG", "name": "Alphabet Inc.", "exchange": "NASDAQ"},
        ],
        "Tesla": [
            {"symbol": "TSLA", "name": "Tesla, Inc.", "exchange": "NASDAQ"},
        ],
    }

    results = []
    for company, data in sample_data.items():
        if query.lower() in company.lower():
            results.extend(data)

    if not results:
        raise ValueError(f"No stock symbols found for query: {query}")

    return {
        "query": query,
        "results": results,
    }


from typing import List


def get_supported_codes() -> List[str]:
    """Returns the list of currencies that are supported.

    Returns:
        List of currency codes that are currently supported.
    """
    supported_currencies = [
        "USD",
        "EUR",
        "JPY",
        "GBP",
        "AUD",
        "CAD",
        "CHF",
        "CNY",
        "SEK",
        "NZD",
    ]
    return supported_currencies


from typing import Dict, Literal, Union


def job_salary(
    job_title: str,
    location: str,
    location_type: Literal["ANY", "CITY", "STATE", "COUNTRY"] = "ANY",
    years_of_experience: Literal[
        "ALL",
        "LESS_THAN_ONE",
        "ONE_TO_THREE",
        "FOUR_TO_SIX",
        "SEVEN_TO_NINE",
        "TEN_TO_FOURTEEN",
        "ABOVE_FIFTEEN",
    ] = "ALL",
) -> Dict[str, Union[str, int]]:
    """Estimate salary by job title, location, and experience.

    Args:
        job_title: Job title for which to get salary estimation.
        location: Free-text location/area in which to get salary information.
        location_type: Specify the type of the location for additional accuracy.
        years_of_experience: Get job estimation for a specific experience level range (years).

    Returns:
        Dict containing:
            - job_title: The job title provided
            - location: The location provided
            - estimated_salary: Estimated salary in USD
    """

    # Hash-based generation for consistent sample data
    base_salaries = {
        "Software Engineer": 80000,
        "Data Scientist": 90000,
        "Product Manager": 95000,
    }

    location_modifiers = {
        "CITY": 1.1,
        "STATE": 1.05,
        "COUNTRY": 1.0,
        "ANY": 1.0,
    }

    experience_modifiers = {
        "LESS_THAN_ONE": 0.8,
        "ONE_TO_THREE": 0.9,
        "FOUR_TO_SIX": 1.0,
        "SEVEN_TO_NINE": 1.2,
        "TEN_TO_FOURTEEN": 1.4,
        "ABOVE_FIFTEEN": 1.6,
        "ALL": 1.0,
    }

    if job_title not in base_salaries:
        raise ValueError(f"Job title not supported: {job_title}")

    base_salary = base_salaries[job_title]
    location_modifier = location_modifiers.get(location_type, 1.0)
    experience_modifier = experience_modifiers.get(years_of_experience, 1.0)

    estimated_salary = int(base_salary * location_modifier * experience_modifier)

    return {
        "job_title": job_title,
        "location": location,
        "estimated_salary": estimated_salary,
    }


from typing import Dict, List, Optional


def list_company_filings(
    registration_number: str, filing_type: Optional[str] = None
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Returns a list of the filings submitted by a company.

    Args:
        registration_number: Registered company number
        filing_type: Select a category of filings to return (e.g., 'accounts', 'tax returns')

    Returns:
        Dict containing:
            - registration_number: The company registration number
            - filings: List of filings with details such as type and date
    """

    # Sample data based on registration_number hash
    sample_filings = {
        "12345678": [
            {"type": "accounts", "date": "2023-01-15"},
            {"type": "tax returns", "date": "2023-02-20"},
            {"type": "officers", "date": "2023-03-10"},
        ],
        "87654321": [
            {"type": "people with significant control", "date": "2023-01-25"},
            {"type": "trading status", "date": "2023-02-15"},
            {"type": "insolvency", "date": "2023-03-05"},
        ],
        "REG-962933": [
            {"type": "accounts", "date": "2023-12-15"},
            {"type": "tax returns", "date": "2024-01-20"},
            {"type": "officers", "date": "2024-02-10"},
            {"type": "people with significant control", "date": "2024-03-05"},
            {"type": "trading status", "date": "2024-04-18"},
        ],
    }

    if registration_number not in sample_filings:
        raise ValueError(f"Registration number not found: {registration_number}")

    filings = sample_filings[registration_number]

    if filing_type:
        filings = [filing for filing in filings if filing["type"] == filing_type]
        if not filings:
            raise ValueError(f"No filings found for type: {filing_type}")

    return {
        "registration_number": registration_number,
        "filings": filings,
    }


from typing import Dict, List, Union


def list_company_officers(
    registration_number: str, active_only: bool = True
) -> Dict[str, Union[str, List[Dict[str, Union[str, bool]]]]]:
    """Returns a list of the current and former officers declared for a company.

    Args:
        registration_number: Registered company number
        active_only: Return only active officers if true

    Returns:
        Dict containing:
            - registration_number: The company registration number
            - officers: List of officers with their details
    """

    # Mock data based on registration_number hash
    sample_data = {
        "123456": [
            {"name": "Alice Johnson", "position": "CEO", "active": True},
            {"name": "Bob Smith", "position": "CFO", "active": False},
            {"name": "Charlie Brown", "position": "CTO", "active": True},
        ],
        "789012": [
            {"name": "David Wilson", "position": "Director", "active": True},
            {"name": "Eva Green", "position": "COO", "active": False},
        ],
        "REG-962933": [
            {"name": "Sarah Mitchell", "position": "CEO", "active": True},
            {"name": "James Rodriguez", "position": "CFO", "active": True},
            {"name": "Emily Chen", "position": "CTO", "active": True},
            {"name": "Michael Thompson", "position": "COO", "active": False},
            {"name": "Lisa Wang", "position": "Director", "active": True},
        ],
    }

    if registration_number not in sample_data:
        raise ValueError(
            f"Company not found for registration number: {registration_number}"
        )

    officers = sample_data[registration_number]
    if active_only:
        officers = [officer for officer in officers if officer["active"]]

    return {
        "registration_number": registration_number,
        "officers": officers,
    }


from datetime import datetime
from typing import Dict, List


def list_transaction_by_category(
    category: str, start_date: str, end_date: str
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """List all transactions within a category by date range.

    Args:
        category: The category of the transactions to list
        start_date: Start date of the range in 'YYYY-MM-DD' format
        end_date: End date of the range in 'YYYY-MM-DD' format

    Returns:
        Dict containing:
            - category: The category of the transactions
            - transactions: List of transactions within the date range
                Each transaction contains:
                    - date: Date of the transaction
                    - amount: Amount of the transaction
                    - description: Description of the transaction
    """
    # Sample transactions data
    transactions_data = [
        {"date": "2023-01-15", "amount": 150.75, "description": "Grocery shopping"},
        {"date": "2023-02-20", "amount": 200.00, "description": "Electronics purchase"},
        {"date": "2023-03-05", "amount": 50.25, "description": "Bookstore"},
        {"date": "2023-04-10", "amount": 75.00, "description": "Restaurant"},
        {"date": "2023-05-22", "amount": 120.00, "description": "Clothing"},
    ]

    # Validate date format
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    if start > end:
        raise ValueError("Start date must be before end date.")

    # Filter transactions by date range
    filtered_transactions = [
        transaction
        for transaction in transactions_data
        if start <= datetime.strptime(transaction["date"], "%Y-%m-%d") <= end
    ]

    return {
        "category": category,
        "transactions": filtered_transactions,
    }


from datetime import datetime
from typing import Dict, List, Optional, Union


def list_transactions(
    account_id: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    min_amount: Optional[float] = None,
) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """List recent transactions for an account, optionally filtered by dates or amount.

    Args:
        account_id: Account ID or last-4
        start_date: Start date in 'YYYY-MM-DD' format
        end_date: End date in 'YYYY-MM-DD' format
        min_amount: Minimum absolute amount to include

    Returns:
        Dict containing:
            - account_id: The account identifier
            - transactions: List of transactions with:
                - date: Transaction date
                - amount: Transaction amount
                - description: Transaction description
    """

    # Sample transactions data
    sample_transactions = [
        {"date": "2023-10-01", "amount": 150.0, "description": "Grocery Store"},
        {"date": "2023-10-05", "amount": 20.0, "description": "Coffee Shop"},
        {"date": "2023-10-10", "amount": 200.0, "description": "Electronics"},
        {"date": "2023-10-15", "amount": 50.0, "description": "Restaurant"},
        {"date": "2023-10-20", "amount": 75.0, "description": "Gas Station"},
    ]

    # Filter transactions by date range
    if start_date:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        sample_transactions = [
            txn
            for txn in sample_transactions
            if datetime.strptime(txn["date"], "%Y-%m-%d") >= start_date_obj
        ]

    if end_date:
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        sample_transactions = [
            txn
            for txn in sample_transactions
            if datetime.strptime(txn["date"], "%Y-%m-%d") <= end_date_obj
        ]

    # Filter transactions by minimum amount
    if min_amount is not None:
        sample_transactions = [
            txn for txn in sample_transactions if abs(txn["amount"]) >= min_amount
        ]

    return {
        "account_id": account_id,
        "transactions": sample_transactions,
    }


from typing import Dict, Union


def pay_invoice(
    invoice_id: str,
    amount: float,
    payment_token: str,
    agree_to_terms: bool,
    email: Union[str, None] = None,
) -> Dict[str, Union[str, float, bool]]:
    """Submit payment for an invoice using a tokenized payment method and receive a receipt.

    Args:
        invoice_id: Invoice identifier
        amount: Payment amount; must match or be less than invoice balance per policy
        payment_token: Tokenized payment method
        agree_to_terms: Must be true to authorize payment
        email: Email address to receive the receipt (optional)

    Returns:
        Dict containing:
            - invoice_id: The invoice identifier
            - amount_paid: The amount that was paid
            - payment_status: Status of the payment ('success' or 'failure')
            - receipt_id: Unique identifier for the payment receipt
            - email_sent: Boolean indicating if the receipt was emailed
    """
    if not agree_to_terms:
        raise ValueError("Terms must be agreed to authorize payment.")

    # Mock invoice balances for validation
    invoice_balances = {
        "INV123": 100.0,
        "INV456": 250.0,
        "INV789": 50.0,
    }

    if invoice_id not in invoice_balances:
        raise ValueError(f"Invoice ID not found: {invoice_id}")

    if amount > invoice_balances[invoice_id]:
        raise ValueError("Payment amount exceeds invoice balance.")

    # Mock payment processing
    payment_status = "success" if payment_token.startswith("tok_") else "failure"

    # Mock receipt generation
    receipt_id = f"RCT{hash(invoice_id + payment_token) % 10000}"

    # Simulate email sending
    email_sent = email is not None

    return {
        "invoice_id": invoice_id,
        "amount_paid": amount,
        "payment_status": payment_status,
        "receipt_id": receipt_id,
        "email_sent": email_sent,
    }


from typing import Dict


def replace_card(account_id: str, reason: str) -> Dict[str, str]:
    """Order a replacement card for a given account.

    Args:
        account_id: Account ID or last-4
        reason: Reason for replacement (e.g., 'Lost', 'Stolen', 'Damaged')

    Returns:
        Dict containing:
            - account_id: The account ID for which the card is replaced
            - status: Status of the replacement request
            - new_card_id: A mock new card ID generated for the replacement
    """
    if not account_id or len(account_id) < 4:
        raise ValueError("Invalid account ID provided.")
    if reason.lower() not in ["lost", "stolen", "damaged"]:
        raise ValueError(
            "Invalid reason provided. Must be 'Lost', 'Stolen', or 'Damaged'."
        )

    # Mock new card ID generation using a hash-based approach
    new_card_id = f"NC-{hash(account_id + reason) % 1000000:06}"

    return {
        "account_id": account_id,
        "status": "Replacement Ordered",
        "new_card_id": new_card_id,
    }


from typing import Dict


def summarize_stock_performance(ticker: str, days: int = 30) -> str:
    """Fetch the last 'days' days of daily price/volume data for the given stock ticker.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL").
        days: Number of calendar days to look back.

    Returns:
        CSV-formatted string containing:
            - date: Date of the stock data
            - open: Opening price of the stock
            - close: Closing price of the stock
            - volume: Trading volume of the stock
    """
    if not ticker.isalpha():
        raise ValueError(f"Invalid ticker symbol: {ticker}")

    import datetime
    import random

    today = datetime.date.today()
    data = []

    for i in range(days):
        date = today - datetime.timedelta(days=i)
        open_price = round(random.uniform(100, 500), 2)
        close_price = round(open_price + random.uniform(-10, 10), 2)
        volume = random.randint(1000000, 5000000)
        data.append(f"{date},{open_price},{close_price},{volume}")

    return "\n".join(data)


from typing import Dict, List, Literal


def symbols_headlines(
    symbolSource: str = "NASDAQ:TSLA",
    lang: Literal[
        "en",
        "in",
        "de_DE",
        "fr",
        "it",
        "es",
        "pl",
        "br",
        "tr",
        "ru",
        "id",
        "ms_MY",
        "th_TH",
        "vi_VN",
        "ja",
        "kr",
        "zh_CN",
        "zh_TW",
        "he_IL",
        "ar_AE",
    ] = "en",
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Retrieve headlines information for a specific financial symbol.

    Args:
        symbolSource: Symbol identifier including exchange (e.g., 'NASDAQ:TSLA').
        lang: The language for the headlines (default is 'en').

    Returns:
        Dict containing:
            - symbol: The financial symbol queried
            - language: The language of the headlines
            - headlines: List of dictionaries with headline information
    """

    sample_headlines = {
        "NASDAQ:TSLA": [
            {"title": "Tesla's New Model Breaks Records", "date": "2023-10-01"},
            {
                "title": "Elon Musk Announces New Battery Technology",
                "date": "2023-09-25",
            },
        ],
        "NYSE:IBM": [
            {"title": "IBM Reports Strong Quarterly Earnings", "date": "2023-10-02"},
            {"title": "IBM Expands Cloud Services", "date": "2023-09-20"},
        ],
        "NASDAQ:AAPL": [
            {
                "title": "Apple Unveils New iPhone with Advanced Features",
                "date": "2023-09-12",
            },
            {"title": "Apple Reports Strong Q3 Earnings", "date": "2023-07-25"},
        ],
        "NASDAQ:GOOGL": [
            {
                "title": "Alphabet Expands AI Capabilities with New Partnerships",
                "date": "2023-10-05",
            },
            {
                "title": "Google Announces Updates to Android and Wear OS",
                "date": "2023-08-15",
            },
        ],
    }

    if symbolSource not in sample_headlines:
        raise ValueError(f"Symbol not supported: {symbolSource}")

    return {
        "symbol": symbolSource,
        "language": lang,
        "headlines": sample_headlines[symbolSource],
    }


from typing import Dict, Optional


def verify_insurance_coverage(
    insurance_provider: str,
    healthcare_provider: str,
    treatment_type: Optional[str] = None,
    patient_id: Optional[str] = None,
) -> Dict[str, Union[str, bool]]:
    """Verify if insurance covers treatment with a specific provider.

    Args:
        insurance_provider: Insurance company name
        healthcare_provider: Healthcare provider or practice name
        treatment_type: Type of treatment or service
        patient_id: Patient's insurance ID number

    Returns:
        Dict containing:
            - insurance_provider: Name of the insurance company
            - healthcare_provider: Name of the healthcare provider
            - treatment_type: Type of treatment or service
            - covered: Boolean indicating if the treatment is covered
    """

    # Mocked data for demonstration purposes
    coverage_data = {
        ("HealthPlus", "City Hospital"): ["surgery", "consultation"],
        ("MediCare", "Downtown Clinic"): ["consultation"],
        ("HealthPlus", "Downtown Clinic"): ["surgery", "therapy"],
    }

    # Check if the insurance and healthcare provider combination exists
    if (insurance_provider, healthcare_provider) not in coverage_data:
        raise ValueError(
            "Combination of insurance and healthcare provider not supported"
        )

    # Determine if the treatment type is covered
    covered_treatments = coverage_data[(insurance_provider, healthcare_provider)]
    is_covered = treatment_type in covered_treatments if treatment_type else True

    return {
        "insurance_provider": insurance_provider,
        "healthcare_provider": healthcare_provider,
        "treatment_type": treatment_type if treatment_type else "any",
        "covered": is_covered,
    }


from typing import Dict, Literal, Union


def withdraw_funds(
    amount: float,
    withdrawalMethod: Literal["paypal", "cryptocurrency"],
    paypalDetails: Dict[str, str] = None,
    cryptoDetails: Dict[
        str, Union[str, Literal["bitcoin", "ethereum", "litecoin"]]
    ] = None,
) -> Dict[str, Union[str, float]]:
    """Withdraw funds from the player's account to PayPal or a cryptocurrency wallet.

    Args:
        amount: The amount of money to withdraw in US dollars. Must be at least $10.
        withdrawalMethod: The method to use for withdrawal ('paypal' or 'cryptocurrency').
        paypalDetails: The player's PayPal details, required if withdrawalMethod is 'paypal'.
        cryptoDetails: The player's cryptocurrency wallet details, required if withdrawalMethod is 'cryptocurrency'.

    Returns:
        Dict containing:
            - status: Status of the withdrawal ('success' or 'failure')
            - method: The method used for withdrawal
            - amount: The amount withdrawn
            - transactionId: A mock transaction ID for the withdrawal
    """
    if amount < 10:
        raise ValueError("Amount must be at least $10.")

    if withdrawalMethod == "paypal":
        if (
            not paypalDetails
            or "paypalEmail" not in paypalDetails
            or "paypalAccountName" not in paypalDetails
        ):
            raise ValueError("PayPal details are required for PayPal withdrawals.")
        transaction_id = f"PP-{hash(paypalDetails['paypalEmail']) % 1000000}"
        return {
            "status": "success",
            "method": "paypal",
            "amount": amount,
            "transactionId": transaction_id,
        }

    if withdrawalMethod == "cryptocurrency":
        if (
            not cryptoDetails
            or "currencyType" not in cryptoDetails
            or "walletAddress" not in cryptoDetails
        ):
            raise ValueError(
                "Cryptocurrency details are required for cryptocurrency withdrawals."
            )
        transaction_id = f"CR-{hash(cryptoDetails['walletAddress']) % 1000000}"
        return {
            "status": "success",
            "method": "cryptocurrency",
            "amount": amount,
            "transactionId": transaction_id,
        }

    raise ValueError("Unsupported withdrawal method.")


def get_stock_price(ticker: str) -> Dict[str, Union[str, float]]:
    """
    Returns the current stock price for the given ticker symbol.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL", "GOOG")

    Returns:
        Dict with:
            - ticker
            - price_usd
    """
    sample_prices = {"AAPL": 210.15, "GOOG": 2850.50, "META": 320.75, "TSLA": 720.10}
    symbol = ticker.upper()
    if symbol not in sample_prices:
        raise ValueError(f"Ticker not found: {symbol}")
    return {"ticker": symbol, "price_usd": sample_prices[symbol]}


def deposit(account: str, amount: float) -> Dict[str, Union[str, float, bool]]:
    """Deposits funds into a bank account.

    Args:
        account: Bank account name
        amount: Amount of funds to deposit

    Returns:
        Dict containing:
            - account: Bank account name
            - amount: Amount deposited
            - success: Boolean indicating if deposit was successful
            - new_balance: New account balance after deposit
    """
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero")

    # Mock account balances
    account_balances = {
        "savings": 500.00,
        "checking": 1200.00,
        "emergency": 2500.00,
    }

    if account not in account_balances:
        raise ValueError(f"Account not found: {account}")

    # Simulate deposit
    new_balance = account_balances[account] + amount

    return {
        "account": account,
        "amount": amount,
        "success": True,
        "new_balance": new_balance,
    }


def get_accounts() -> Dict[str, List[Dict[str, Union[str, float]]]]:
    """List all bank accounts with their current balances.

    Returns:
        Dict containing:
            - accounts: List of accounts with name and balance
    """
    accounts = [
        {"name": "savings", "balance": 500.00, "type": "savings"},
        {"name": "checking", "balance": 1200.00, "type": "checking"},
        {"name": "emergency", "balance": 2500.00, "type": "savings"},
    ]

    return {"accounts": accounts}


def transfer_funds(
    from_account: str, to_account: str, amount: float
) -> Dict[str, Union[str, float, bool]]:
    """Transfer funds between bank accounts.

    Args:
        from_account: Source bank account name
        to_account: Destination bank account name
        amount: Amount of funds to transfer

    Returns:
        Dict containing:
            - from_account: Source account name
            - to_account: Destination account name
            - amount: Amount transferred
            - success: Boolean indicating if transfer was successful
    """
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero")

    if from_account == to_account:
        raise ValueError("Cannot transfer to the same account")

    # Mock account balances
    account_balances = {
        "savings": 500.00,
        "checking": 1200.00,
        "emergency": 2500.00,
    }

    if from_account not in account_balances:
        raise ValueError(f"Source account not found: {from_account}")

    if to_account not in account_balances:
        raise ValueError(f"Destination account not found: {to_account}")

    if account_balances[from_account] < amount:
        raise ValueError("Insufficient funds in source account")

    # Simulate transfer
    return {
        "from_account": from_account,
        "to_account": to_account,
        "amount": amount,
        "success": True,
    }


def get_last_transaction(account: str) -> Dict[str, Union[str, float]]:
    """Get the last transaction for a specific bank account.

    Args:
        account: Bank account name

    Returns:
        Dict containing:
            - account: Bank account name
            - amount: Amount of the last transaction
            - date: Date of the last transaction
            - description: Description of the transaction
    """
    # Mock last transactions for different accounts
    last_transactions = {
        "savings": {
            "amount": 75.50,
            "date": "2023-10-20",
            "description": "ATM Deposit",
        },
        "checking": {
            "amount": 150.00,
            "date": "2023-10-21",
            "description": "Direct Deposit",
        },
        "emergency": {
            "amount": 500.00,
            "date": "2023-10-15",
            "description": "Transfer In",
        },
    }

    if account not in last_transactions:
        raise ValueError(f"Account not found: {account}")

    transaction = last_transactions[account]
    return {
        "account": account,
        "amount": transaction["amount"],
        "date": transaction["date"],
        "description": transaction["description"],
    }
