Запуск сервиса:

1) Создать виртуальное окружение
2) Установить библиотеки: 
```
pip install -r requirements.txt
```
3) Создать ```.env``` файл с переменными окружения:
```
SECRET_KEY
TEACHBASE_CLIENT_ID
TEACHBASE_SECRET_KEY
DEBUG
DB_ENGINE
DB_DB
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```
3) Запустить сервис из корневой директории ```src```:
```
python manage.py migrate
```
4) Запустить сервис из корневой директории ```src```:
```
python manage.py runserver
```


Запуск сервиса через Docker:
1) Создать ```.env``` файл с переменными окружения:
```
SECRET_KEY
TEACHBASE_CLIENT_ID
TEACHBASE_SECRET_KEY
DEBUG
DB_ENGINE
DB_DB
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```
2) Создать ```db.env``` файл с переменными окружения:
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```
3) Из корневой папки проекта выполнить команду:
```
docker-compose up --build -d
```

Приложение будет доступно по адресу:
```http://localhost:1337```