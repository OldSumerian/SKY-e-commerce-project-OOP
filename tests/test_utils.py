import src.utils


def test_get_info_from_json():
    assert len(src.utils.get_info_from_json()) == 2
    assert type(src.utils.get_info_from_json()) is list

