import classes.class_Category
import classes.class_Product


def test_make_list_of_categories(data_for_test):
    categories = [classes.class_Category.Category(item['name'], item['description'], item['products'])
                  for item in data_for_test]
    assert type(categories) is list
    assert len(categories) == 2

def test_make_list_of_products(data_for_test):
    categories = [classes.class_Category.Category(item['name'], item['description'], item['products'])
                  for item in data_for_test]
    products = [[classes.class_Product.Product(product['name'], product['description'], product['price'],
                product['quantity']) for product in category.products] for category in categories]
    assert type(products) is list
    assert len(products[0]) == 3

