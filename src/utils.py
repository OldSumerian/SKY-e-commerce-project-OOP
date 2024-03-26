import json


def get_info_from_json():
    """
    Получает данные из json-файла
    :return:
    """
    with open('data/products.json', encoding='UTF-8') as data:
        full_products_info = json.load(data)
    return full_products_info
