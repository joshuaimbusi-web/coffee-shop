import pytest

from customer import Customer
from coffee import Coffee
from order import Order

def clear_all():
    Customer._all = []
    Coffee._all = []
    Order._all = []

def test_order_init_valid():
    clear_all()
    alice = Customer("Alice")
    latte = Coffee("Latte")
    o = Order(alice, latte, 3.25)
    assert o.customer is alice
    assert o.coffee is latte
    assert o.price == pytest.approx(3.25)

def test_price_validation_type_and_range():
    clear_all()
    alice = Customer("Alice")
    latte = Coffee("Latte")

    # non-convertible price should raise TypeError
    with pytest.raises(TypeError):
        Order(alice, latte, "not-a-number")

    # below range
    with pytest.raises(ValueError):
        Order(alice, latte, 0.5)

    # above range
    with pytest.raises(ValueError):
        Order(alice, latte, 20.0)

def test_order_relationships_listed():
    clear_all()
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    alice.create_order(latte, 3.0)
    bob.create_order(latte, 4.0)

    # both orders should appear in Order.all()
    assert len(Order.all()) == 2
    # latte.orders() should show two orders
    assert len(latte.orders()) == 2
