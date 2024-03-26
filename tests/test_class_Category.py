import classes.class_Category


def test_init_object_category(data_for_test):
    categories = [classes.class_Category.Category(item['name'], item['description'], item['products'])
                  for item in data_for_test]
    assert categories[0].name == 'Смартфоны'
    assert type(categories[1].description) is str
    assert len(categories[0].products) == 3
    assert len(categories[1].products) == 1
    assert len(categories) == 2
    assert classes.class_Category.Category.count_of_all_categories == 9
    assert len(classes.class_Category.Category.set_of_all_unique_products) == 4

