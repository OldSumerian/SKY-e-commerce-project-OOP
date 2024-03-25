class Category:
    name: str
    description: str
    products: list
    count_of_all_categories = 0
    count_of_unique_products = set()

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.count_of_all_categories += 1

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.products})'

    def __str__(self):
        return f'Класс "Category". Обязательные атрибуты name(str), description(str), products(list)'