## Lab_1: Автоматизація. Знайомство з CI/CD.
### Pre-requirements:
- віртуальна машина на основі Ubuntu 18.04;
- встановлено програми git, make, Python 3.7, [PIP](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/);
### What to do.
1. Створіть папку lab_2 з _README.md_ файлом. Уданому файлі опишіть відповіді на запитання кожного пункту роботи.
2. За допомогою пакетного менеджера PIP інсталюйте pipenv та створіть ізольоване середовище для Python.
```bash
pip install pipenv
pipenv --python 3.7
pipenv shell
```
3. Встановіть бібліотеку `requests` у Вашому середовищі. Дана бібліотека дозволить створювати HTTP запити до заданих Web сторінок.
```bash
pipenv install requests
```
4. Створіть файл `__main__.py`. Це буде програма яку потрібно протестити та запустити. Скопіюйте код програми із даного репозиторію до себе. Для кращого розуміння програми ознайомтесь з [Python tutorial](https://www.tutorialspoint.com/python/index.htm)
5. 
. Встановіть бібліотеку `pytest`. Тестування - це процес перевірки правильності відпрацювання коду. Для кращого розуміння ознайомтесь з [документацією pytest](https://docs.pytest.org/en/latest/#)
```bash
pipenv install pytest
```

. Склонуйте git репозиторій на віртуальну машину Ubuntu.
