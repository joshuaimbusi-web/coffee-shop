"""
Customer model for the coffee shop domain.
"""

from utils import validate_string


class Customer:
    _all = []

    def __init__(self, name):
        # name validation via helper; raises on invalid input
        self._name = validate_string(name, name="Customer name", min_len=1, max_len=15)
        Customer._all.append(self)

    def __repr__(self):
        return f"<Customer name={self.name!r}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # setter reuses the same validation helper
        self._name = validate_string(value, name="Customer name", min_len=1, max_len=15)

    @classmethod
    def all(cls):
        return cls._all

    def orders(self):
        """Return all Order instances for this customer."""
        # lazy import to avoid circular import at module load time
        from order import Order
        return [o for o in Order.all() if o.customer is self]

    def coffees(self):
        """Return unique Coffee instances this customer has ordered."""
        seen = []
        for o in self.orders():
            if o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee, price):
        """Create an Order for this customer.

        Arguments:
            coffee: expected to be a Coffee instance (no strict runtime isinstance
                    check here to avoid circular import).
            price: numeric value convertible to float within valid range.

        Returns:
            The newly created Order instance.

        Raises:
            TypeError/ValueError from Order constructor if inputs are invalid.
        """
        # import Order only when needed
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Return the Customer who spent the most on the given coffee.

        Returns None if there are no orders for that coffee.
        """
        totals = {}
        for order in coffee.orders():
            totals.setdefault(order.customer, 0.0)
            totals[order.customer] += order.price

        if not totals:
            return None

        return max(totals.items(), key=lambda kv: kv[1])[0]
