from modules import common

if __name__ == '__main__':
    print(f"We are in the {__name__}")
    print(common.get_current_date().now())
    print(common.get_current_platform())

