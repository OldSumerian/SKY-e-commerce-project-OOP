import classes.class_Product


def test_init_object_product():
    obj_test = classes.class_Product.Product('Samsung', 'Smartphone', 20_000.00, 5)
    assert obj_test.name == 'Samsung'
    assert type(obj_test.description) is str
    assert obj_test.price == 20_000.00
    assert type(obj_test.quantity) is int
