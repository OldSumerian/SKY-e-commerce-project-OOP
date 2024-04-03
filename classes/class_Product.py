class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def make_product(cls, product):
        name, description, price, quantity = product.split()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print('Price is not correct')
        elif price < self.__price:
            answer = input('Do you agree new price? (press "y" or any key to disagree)')
            if answer.lower() == 'y':
                self.__price = price
        else:
            self.__price = price

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'
    def __len__(self):
        return len(self.description)

    def __add__(self, other):
        return self.__price * self.quantity + other.price * other.quantity
