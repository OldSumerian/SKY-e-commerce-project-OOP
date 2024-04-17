import classes.class_Product


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

        # set_of_this_category_unique_products = set([item['name'] for item in self.__products])

        classes.class_Category.Category.count_of_all_categories += 1
        # classes.class_Category.Category.count_of_unique_products += len(set_of_this_category_unique_products)

    # @classmethod
    # def add_product(cls, product):
    #     cls.__products.append(product)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, product):
        if not isinstance(product, classes.class_Product.Product):
            raise TypeError('You must added only one-typed products')
        self.products.append(product)

    @property
    def display_products(self):
        list_of_products = ""
        for i in self.__products:
            list_of_products += f"{i['name']}, {i['price']} руб. Остаток: {i['quantity']} шт.\n"
        return list_of_products

    def get_average_cost(self):
        try:
            cost = 0
            for i in self.__products:
                cost += i.price
            return cost/len(self)
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.products})'

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __add__(self):
        pass

    def __len__(self):
        return len(self.__products)
