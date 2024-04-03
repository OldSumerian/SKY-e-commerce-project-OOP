# Подключение функции чтения данных из json-файла
from src.utils import get_info_from_json

# Подключение классов
from classes.class_Category import Category
from classes.class_Product import Product


def main():
    """
    Функция, содержащая основной код программы
    """

    # Создание переменной, содержащей данные, полученные из json-файла
    base = get_info_from_json()

    # Создание списка, содержащего экземпляры класса 'Category' по данным, полученным из json-файла
    categories = [Category(item['name'], item['description'], item['products']) for item in base]

    # Создание списка, содержащего экземпляры класса 'Product' по данным, полученным из json-файла
    products = [[Product(product['name'], product['description'], product['price'], product['quantity'])
                 for product in category.products] for category in categories]

    # def display():
    #     print(categories)
    #     print(products)
    #     print(Category.count_of_all_categories)
    #     print(Category.count_of_unique_products)
    #
    # display()

    # categories[0].display_products
    # print(products[0][0].price)
    # products[0][0].price = -50
    # print(products[0][0].price)
    # products[0][0].price = 200_000
    # print(products[0][0].price)
    # products[0][0].price = 100_000
    # print(products[0][0].price)

    print(categories[0])
    print(products[0][0])
    print()
    print(categories[0].display_products)
    print()
    print(products[0][0] + products[0][1])

if __name__ == '__main__':
    main()
