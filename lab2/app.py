import requests


def main(url=''):
    if not url:
        print("No URL passed to function")
        return False
    r = requests.get(url=url)
    d = r.json()
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError

    return True


def home_work():
    # Ваш захист
    pass


if __name__ == "__main__":
    a = "="*40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')
