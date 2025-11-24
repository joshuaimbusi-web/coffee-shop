import pytest

from customer import Customer
from coffee import Coffee
from order import Order

def clear_all():
    Customer._all = []
    Coffee._all = []
    Order._all = []

def test_coffee_init_valid():
    clear_all()
    c = Coffee("Latte")
    assert c.name == "Latte"
    assert c in Coffee.all()

def test_coffee_name_validation():
    clear_all()
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")  # less than 3 characters

def test_orders_customers_num_average():
    clear_all()
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    alice.create_order(latte, 3.0)
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 5.0)

    # orders() returns list of Order objects
    orders = latte.orders()
    assert len(orders) == 3

    # customers() returns unique customers
    customers = latte.customers()
    assert set(customers) == {alice, bob}

    # num_orders() should be 3
    assert latte.num_orders() == 3

    # average_price() should be (3+4+5)/3 = 4.0
    assert pytest.approx(latte.average_price(), rel=1e-9) == 4.0

def test_average_price_no_orders():
    clear_all()
    c = Coffee("Americano")
    assert c.num_orders() == 0
    assert c.average_price() == 0.0
