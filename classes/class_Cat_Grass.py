import classes.class_Product


class Grass(classes.class_Product.Product):
    made_by_country: str
    germination_period: int

    def __init__(self, name, description, price, quantity, color, made_by_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.made_by_country = made_by_country
        self.germination_period = germination_period

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.quantity + other.quantity
        raise TypeError('Add only one-typed objects')

    def __repr__(self):
        return (f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, '
                f'{self.quantity}, {self.color}, {self.made_by_country}, {self.germination_period})')