import class_Product


class Grass(class_Product.Product):
    made_by_country: str
    germination_period: int

    def __init__(self, made_by_country, germination_period):
        super().__init__(name=str, description=str, price=float, quantity=int,color=None)
        self.made_by_country = made_by_country
        self.germination_period = germination_period

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.quantity + other.quantity
        raise TypeError
