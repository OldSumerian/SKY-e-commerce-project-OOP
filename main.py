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


if __name__ == '__main__':
    main()
