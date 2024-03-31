class Category:
    name: str
    description: str
    __products: list
    count_of_all_categories = 0
    count_of_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        set_of_this_category_unique_products = set([item['name'] for item in self.__products])

        Category.count_of_all_categories += 1
        Category.count_of_unique_products += len(set_of_this_category_unique_products)

    @classmethod
    def add_product(cls, product):
        cls.__products.append(product)

    @property
    def products(self):
        return self.__products

    @property
    def display_products(self):
        for i in self.__products:
            print(f"{i['name']}, {i['price']} руб. Остаток: {i['quantity']} шт.")
        return self.__products

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.products})'

    def __str__(self):
        return f'Класс "Category". Обязательные атрибуты name(str), description(str), products(list)'
