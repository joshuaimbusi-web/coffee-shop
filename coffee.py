from utils import validate_string
class Coffee:
    _all = []

    def __init__(self, name):
        self._name = validate_string(name, name="Coffee name", min_len=3)
        Coffee._all.append(self)

    def __repr__(self):
        return f"<Coffee name={self.name!r}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_string(value, name="Coffee name", min_len=3)

    @classmethod
    def all(cls):
        return cls._all

    def orders(self):
        from order import Order
        return [o for o in Order.all() if o.coffee is self]

    def customers(self):
        seen = []
        for o in self.orders():
            if o.customer not in seen:
                seen.append(o.customer)
        return seen

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        ords = self.orders()
        if not ords:
            return 0.0
        total = sum(o.price for o in ords)
        return total / len(ords)
