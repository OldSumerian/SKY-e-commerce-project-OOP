import class_Product


class Smartphone(class_Product.Product):
    power: float
    model: str
    memory: str

    def __init__(self, power, model, memory):
        super().__init__(name=str, description=str, price=float, quantity=int, color=None)
        self.power = power
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.quantity + other.quantity
        raise TypeError('Add only one-typed objects')
