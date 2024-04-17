import classes.class_Product


class Smartphone(classes.class_Product.Product):
    power: float
    model: str
    memory: str

    def __init__(self, name, description, price, quantity, color, power, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.power = power
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError('Add only one-typed objects')
        return self.price * self.quantity + other.price * other.quantity
