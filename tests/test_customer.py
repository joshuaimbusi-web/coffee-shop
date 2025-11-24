import pytest

from customer import Customer
from coffee import Coffee
from order import Order

def clear_all():
    Customer._all = []
    Coffee._all = []
    Order._all = []

def test_customer_init_valid():
    clear_all()
    c = Customer("Alice")
    assert c.name == "Alice"
    assert c in Customer.all()

def test_customer_name_validation():
    clear_all()
    with pytest.raises(TypeError):
        Customer(123)  # not a string
    with pytest.raises(ValueError):
        Customer("")   # empty after strip
    with pytest.raises(ValueError):
        Customer("x" * 16)  # too long (>15)

def test_create_order_and_orders_and_coffees():
    clear_all()
    alice = Customer("Alice")
    latte = Coffee("Latte")
    esp = Coffee("Espresso")

    # create orders via Customer.create_order
    o1 = alice.create_order(latte, 3.5)
    o2 = alice.create_order(esp, 2.0)

    # orders() should list both orders
    orders = alice.orders()
    assert o1 in orders and o2 in orders
    assert len(orders) == 2

    # coffees() should be unique list of Coffee objects
    coffees = alice.coffees()
    assert latte in coffees and esp in coffees
    assert len(coffees) == 2

def test_most_aficionado():
    clear_all()
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    # Alice orders twice
    alice.create_order(latte, 3.0)
    alice.create_order(latte, 4.0)

    # Bob orders once
    bob.create_order(latte, 2.0)

    # Alice spent 7.0, Bob 2.0 => Alice is top
    top = Customer.most_aficionado(latte)
    assert top is alice

    # If no orders for a coffee, returns None
    mocha = Coffee("Mocha")
    assert Customer.most_aficionado(mocha) is None
