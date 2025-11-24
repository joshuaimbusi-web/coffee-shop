"""
Interactive debug script for the coffee shop models.

Run with:
    python debug.py
or use it as a starting point for interactive experiments.
"""

from customer import Customer
from coffee import Coffee
from order import Order

def reset_state():
    """Clear in-memory registries for a clean debug run."""
    Customer._all = []
    Coffee._all = []
    Order._all = []

def demo():
    """Small demo illustrating features and validations."""
    reset_state()

    print("Creating customers and coffees...")
    a = Customer("Alice")
    b = Customer("Bob")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    print("Creating orders...")
    a.create_order(latte, 3.5)
    a.create_order(espresso, 2.5)
    b.create_order(latte, 4.0)

    print("\nState:")
    print("Customers:", Customer.all())
    print("Coffees:", Coffee.all())
    print("Orders:", Order.all())

    print("\nQueries:")
    print("Latte .num_orders():", latte.num_orders())
    print("Latte .average_price():", latte.average_price())
    print("Latte .customers():", latte.customers())
    print("Alice .orders():", a.orders())
    print("Alice .coffees():", a.coffees())
    print("Most aficionado for Latte:", Customer.most_aficionado(latte))

def check_invalid_inputs():
    """Show how exceptions are raised for invalid inputs."""
    reset_state()
    try:
        print("Attempt invalid customer name (too long)...")
        Customer("x" * 20)
    except Exception as e:
        print("  Caught:", type(e).__name__, e)

    try:
        print("Attempt invalid coffee name (too short)...")
        Coffee("ab")
    except Exception as e:
        print("  Caught:", type(e).__name__, e)

    try:
        print("Attempt invalid order price (not a number)...")
        c = Customer("C")
        cf = Coffee("Mocha")
        Order(c, cf, "not-a-number")
    except Exception as e:
        print("  Caught:", type(e).__name__, e)

if __name__ == "__main__":
    demo()
    print("\n--- invalid input checks ---")
    check_invalid_inputs()
