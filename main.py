# Подключение функции чтения данных из json-файла
from src.utils import get_info_from_json

# Подключение классов
import classes.class_Category
import classes.class_Product
import classes.class_Cat_Smartphone
import classes.class_Cat_Grass


def main():
    """
    Функция, содержащая основной код программы
    """

    # Создание переменной, содержащей данные, полученные из json-файла
    base = get_info_from_json()

    # Создание списка, содержащего экземпляры класса 'Category' по данным, полученным из json-файла
    categories = [classes.class_Category.Category(item['name'], item['description'], item['products']) for item in base]

    # Создание списка, содержащего экземпляры класса 'Product' по данным, полученным из json-файла
    products = [[classes.class_Product.Product(product['name'], product['description'], product['price'], product['quantity'])
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

    # print(categories[0])
    # print(products[0][0])
    # print()
    # print(categories[0].display_products)
    # print()
    # print(products[0][0] + products[0][1])

    any_smart = classes.class_Cat_Smartphone.Smartphone('ExampleSmart', 'Powerful smart',
                                                        100000, 5, 'black', 3000,
                                                        'S22 Ultra', '512 Gb')
    print(any_smart)
    print(repr(any_smart))
    print()

    any_grass = classes.class_Cat_Grass.Grass('SomeGrass', 'Very good grass', 5000,
                                              6, 'green', 'Russia', 2)
    print(any_grass)
    print(repr(any_grass))
    print()

    any_product = classes.class_Product.Product('MyTV', 'Must Have!', 70000, 1, 'white')
    print(any_product)
    print(repr(any_product))
    print()

    second_smart = classes.class_Cat_Smartphone.Smartphone('AnotherSmart', 'New Powerful smart',
                                                        150000, 20, 'black', 3000,
                                                        'S24 Ultra', '512 Gb')
    print(second_smart)
    print(repr(second_smart))
    print()

    print(any_smart + second_smart)
    # print(any_smart + any_product) # Вызовется ошибка при складывании разных классов

    smart_category = classes.class_Category.Category('Smartphones', 'Many good smarts', [any_smart])
    print(smart_category)
    print(smart_category.products)
    print(repr(smart_category))
    smart_category.products(second_smart) # ВОТ ТУТ НЕ РАБОТАЕТ СЕТТЕР
    print(smart_category)

if __name__ == '__main__':
    main()
