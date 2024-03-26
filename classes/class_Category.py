class Category:
    name: str
    description: str
    products: list
    count_of_all_categories = 0
    set_of_all_unique_products = set()
    count_of_all_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.set_of_this_category_unique_products = set([item['name'] for item in products])

        Category.count_of_all_categories += 1
        Category.set_of_all_unique_products |= self.set_of_this_category_unique_products
        Category.count_of_all_categories += len(Category.set_of_all_unique_products)

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.products})'

    def __str__(self):
        return f'Класс "Category". Обязательные атрибуты name(str), description(str), products(list)'
