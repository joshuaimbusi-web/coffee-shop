from utils import validate_string
class Customer:
    _all = []

    def __init__(self, name):
        self._name = validate_string(name, name="Customer name", min_len=1, max_len=15)
        Customer._all.append(self)

    def __repr__(self):
        return f"<Customer name={self.name!r}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_string(value, name="Customer name", min_len=1, max_len=15)

    @classmethod
    def all(cls):
        return cls._all

    def orders(self):
        from order import Order
        return [o for o in Order.all() if o.customer is self]

    def coffees(self):
        seen = []
        for o in self.orders():
            if o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        totals = {}
        for order in coffee.orders():
            totals.setdefault(order.customer, 0.0)
            totals[order.customer] += order.price

        if not totals:
            return None

        return max(totals.items(), key=lambda kv: kv[1])[0]
