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
    products = [
        [classes.class_Product.Product(product['name'], product['description'], product['price'], product['quantity'])
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

    # Проверки по ДЗ № 15.1
    # Создание экземпляра класса-наследника
    any_smart = classes.class_Cat_Smartphone.Smartphone('ExampleSmart', 'Powerful smart',
                                                        100000, 5, 'black', 3000,
                                                        'S22 Ultra', '512 Gb')
    print(any_smart)
    print(repr(any_smart))
    print()

    # Создание экземпляра другого класса-наследника
    any_grass = classes.class_Cat_Grass.Grass('SomeGrass', 'Very good grass', 5000,
                                              6, 'green', 'Russia', 2)
    print(any_grass)
    print(repr(any_grass))
    print()

    # Создание экземпляра класса-родителя
    any_product = classes.class_Product.Product('MyTV', 'Must Have!', 70000, 1, 'white')
    print(any_product)
    print(repr(any_product))
    print()

    # Создание еще одного экземпляра класса-наследника (для проверки методов)
    second_smart = classes.class_Cat_Smartphone.Smartphone('AnotherSmart', 'New Powerful smart',
                                                           150000, 20, 'black', 3000,
                                                           'S24 Ultra', '512 Gb')
    print(second_smart)
    print(repr(second_smart))
    print()

    # Создание категории
    # smart_category = classes.class_Category.Category('Smartphones', 'Many good smarts', [any_smart])
    # print(smart_category)
    # print(smart_category.products)
    # print(repr(smart_category))
    # Добавление продукта в категорию
    # smart_category.products = second_smart
    # print(smart_category)
    # print(repr(smart_category))
    # print()

    print(f'Реализация сложения однотипных продуктов: {any_smart + second_smart}')
    print(any_smart + any_product)  # Вызовется ошибка при складывании класса наследника и родителя
    print()
    print(any_smart + any_grass) # Вызовется ошибка при складывании разных классов-наследников
    # Это проверки по ДЗ 15.2
    # Реализация метода предусмотренного в абстрактном базовом классе
    # print(any_smart.about_product())
    # print(any_smart.__dict__.values())
    # Работа мискина видна по выводу при каждом создании экземпляра класса

if __name__ == '__main__':
    main()
