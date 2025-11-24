"""
Order model for the coffee shop domain.
"""

from utils import validate_price


class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        # minimal runtime assignment for customer/coffee; price validated here
        self._customer = customer
        self._coffee = coffee
        # use helper to validate price — raises if invalid
        self._price = validate_price(price, name="Order price", minimum=1.0, maximum=10.0)
        Order._all.append(self)

    def __repr__(self):
        return (
            f"<Order customer={getattr(self.customer, 'name', None)!r} "
            f"coffee={getattr(self.coffee, 'name', None)!r} price={self.price:.2f}>"
        )

    @classmethod
    def all(cls):
        return cls._all

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        # We keep assignment simple (no circular import). You can add stronger checks
        # here if you prefer to import Customer and verify type.
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        # see note in customer setter
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # re-validate via helper
        self._price = validate_price(value, name="Order price", minimum=1.0, maximum=10.0)
