import requests


def main(url):
    r = requests.get(url=url)
    d = r.json()
    if "date" in d.keys():
        print(d['date'])

    if "time" in d.keys():
        print(d['time'])

    return True


if __name__ == "__main__":
    main('http://date.jsontest.com/')
