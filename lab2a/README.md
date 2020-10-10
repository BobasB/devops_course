## Lab_2a: Основи роботи з Python.
### Pre-requirements:
- встановлено програми Python 3.8, git, [PIP](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/);
- робоче середовище: IntelIJ або PyCharm;
### What to do.
1. Python однай з найлегших на найпоширеніших мов програмування. В Інтернеті можна знайти безліч курсів по його вивченняю, але ми звернемся до [офіційної документації](https://docs.python.org/3.8/index.html);
1. Створіть Python файл `*.py` в якому будете виконувати базові приклади. Застосовуючи команду `print` виконайте наступне:
    1. Виведіть [вбудовані константи](https://docs.python.org/3.8/library/constants.html), (2-3 на вибір), наприклад:
       ```python
       print("Перша константа", False)
       ```
    1. Виведіть результат роботи [вбудованих функцій](https://docs.python.org/3.8/library/functions.html#func-repr) (2-3 на вибір), наприклад:
       ```python
       print(abs(-12.5), f"є рівним {abs(12.5)}")
       ``` 
    1. Познайомтесь з [циклами](https://docs.python.org/3.8/reference/compound_stmts.html#the-for-statement) та [розгалуженнями](https://docs.python.org/3.8/reference/compound_stmts.html#the-if-statement). Напишіть будь-який код який демонструє роботу циклу або розгалужень, (2-3 на вибір), наприклад:
       ```python
       A = True
       print("Значить А=True" if A else "Значить А=False")
       ```
    1. Конструкція `try`->`except`->`finally`. У мові Python код не компілюється а виконується зразу. Можливі помилки нам треба виловлювати самим. Напишіть свій варіант коду з помилкою. Наприклад:
       ```python
       A = 0
       try:
           print("Що буде якщо", 10/A, "?")
       except Exception as e:
           print(e)
       finally:
           print("А вот воно що!")
       ```
    1. Контекс-менеджер `with`. Можете почитата [тут](https://python-scripts.com/contextlib). Напишіть свій код, наприклад:
       ```python
       with open("README.md", "r") as f:
           for line in f:
               print(line)
       ```
1. Створіть у Власному репозиторію такі ж файли як і у цьому:
    ```text
    lab2a/
    ├── modules/
    │   └── common.py
    ├── __init__.py
    └── app.py
    ```
1. Після успішного виконання роботи відредагуйте Ваш персональний _README.md_ у цьому репозиторію. Створіть таблицю яка ставить у відповідність номер лабораторної роботи та URL посилання на папку з виконаною роботою у Вашому персональному репозиторію. Створіть пул-реквест до основного репозиторію.
