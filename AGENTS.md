# AGENTS.md

Навчальний DevOps-курс (українською). Кожна лабораторна — окрема папка з `README.md` (завдання).

## Структура
- `lab1`…`lab6` — лабораторні (Git, Python/CI, моніторинг/Django, Docker, Makefile/Compose, CI/CD).
- `lab2`, `lab3` — Python 3.7 + Pipenv (`Pipfile`, `Pipfile.lock`); `lab3` — Django.
- `lab4`, `lab5` — Dockerfile / docker-compose.
- `ansible/` — playbook налаштування Ubuntu 26 (див. `ansible/README.md`); `example/` — зразок README для здачі лабораторної; `2019`, `2020`, `2021` — архів студентів.
- `.travis.yml` — CI; `Makefile` — оновлення Pipfile.lock (`make update-pipfile`), `make clean`.

## Команди
- Корінь: `make update-pipfile` (виконує `pipenv lock --clear` лише у `lab2` і `lab3`), `make clean` (видаляє `.pytest_cache`).
- Lab2 тести: `cd lab2 && pipenv install && pipenv run pytest tests/tests.py`. У `.travis.yml` цей крок має `|| true`, тож CI не падає від помилок тестів.
- Lab2 `Makefile` — шаблон для студентів (`# Ваш код тут`); цілі навмисно порожні, не «виправляйте» їх.
- Lab3: `cd lab3 && pipenv install && ./scripts/travis-build.sh`.
- Lab4: `cd lab4 && docker build -t bobas/lab4-examples:django-travis .` (Travis пушить образ лише поза PR, через секрети `DOCKER_USERNAME`/`DOCKER_PASSWORD`).
- Lab5 (Makefile): `cd lab5 && make app && make tests && make run && make test-app`; голий `make` збирає образ `app`, але не запускає контейнер. `make docker-prune` примусово видаляє всі контейнери, невикористані томи й мережі та лише висячі образи (не всі образи) — команда руйнівна, не запускати без потреби.
- Lab5 (Compose): `cd lab5 && docker-compose up --build` (`hits` на порту 80, `redis`, `tests`).
- Для lab4/lab5 потрібен запущений Docker daemon. `lab4/Dockerfile` клонує `lab3` з GitHub (не з локальної копії), тож локальні зміни lab3 в образ не потраплять. `make run` у lab5 падає, якщо мережа `appnet` уже існує.

## CI
Лише Travis (`.travis.yml`), збирається тільки гілка `master`; етапи: lab2, lab3, lab4, lab5. GitHub Actions немає.

## Правила
- Один PR — одна лабораторна; у назві PR: номер роботи, прізвище, група.
- Не змінювати чужі студентські роботи в `2019`–`2021` без потреби.
- Репозиторій використовує git-crypt (`.git-crypt`); не коммітити секрети й `db.sqlite3`.
- Документація курсу — українською; зберігайте мову існуючих файлів.
- Після зміни `Pipfile` оновлюйте `Pipfile.lock` (`make update-pipfile`). Залежності також оновлює Dependabot; студентські PR з лабораторними — не залежності.
- Логи, `.DS_Store`, `.env` ігноруються через `.gitignore` — не додавайте їх у коміти.
- Шаблон PR: `.github/PULL_REQUEST_TEMPLATE.md`; інструкції для Copilot: `.github/copilot-instructions.md`.
