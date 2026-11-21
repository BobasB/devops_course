# AGENTS.md

Навчальний DevOps-курс (українською). Кожна лабораторна — окрема папка з `README.md` (завдання).

## Структура
- `lab1`…`lab6` — лабораторні (Git, Python/CI, моніторинг/Django, Docker, Makefile/Compose, CI/CD).
- `lab2`, `lab3` — Python 3.7 + Pipenv (`Pipfile`, `Pipfile.lock`); `lab3` — Django.
- `lab4`, `lab5` — Dockerfile / docker-compose.
- `ansible/`, `example/` — приклади; `2019`, `2020`, `2021` — архів студентів.
- `.travis.yml` — CI; `Makefile` — оновлення Pipfile.lock (`make update-pipfile`), `make clean`.

## Команди
- Lab2 тести: `cd lab2 && pipenv install && pipenv run pytest tests/tests.py`
- Lab3: `cd lab3 && pipenv install && ./scripts/travis-build.sh`
- Lab5: `cd lab5 && make` / `docker-compose up` (див. README лабораторної)

## Правила
- Один PR — одна лабораторна; у назві PR: номер роботи, прізвище, група.
- Не змінювати чужі студентські роботи в `2019`–`2021` без потреби.
- Репозиторій використовує git-crypt (`.git-crypt`); не коммітити секрети й `db.sqlite3`.
- Документація курсу — українською; зберігайте мову існуючих файлів.
- Оновлення залежностей — через Dependabot PR; після зміни `Pipfile` оновлюйте `Pipfile.lock`.
