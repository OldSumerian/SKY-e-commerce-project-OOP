import classes.class_Product


class Grass(classes.class_Product.Product):
    made_by_country: str
    germination_period: int

    def __init__(self, name, description, price, quantity, color, made_by_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.made_by_country = made_by_country
        self.germination_period = germination_period

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError('Add only one-typed objects')
        return self.price * self.quantity + other.price * other.quantity
