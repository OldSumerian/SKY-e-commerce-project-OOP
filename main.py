from src.utils import get_info_from_json

def main():
    base = get_info_from_json()
    for item in base:
        print(item)


if __name__ == '__main__':
    main()
