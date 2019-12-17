FROM python:3.7-alpine
LABEL author="Bohdan Buhyl"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apk update \
    && apk upgrade \
    && apk add git \
    && pip install pipenv

WORKDIR /app

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY my_app/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо наш додаток
COPY my_app/ ./

# Створюємо папку для логів
RUN mkdir logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py