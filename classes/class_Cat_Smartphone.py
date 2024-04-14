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
        if not isinstance(other, type(self)):
            raise TypeError('Add only one-typed objects')
        return self.quantity + other.quantity

    # def __repr__(self):
    #     return (f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, '
    #             f'{self.quantity}, {self.color}, {self.power}, {self.model}, {self.memory})')
