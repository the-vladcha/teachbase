Запуск сервиса:

1) Создать виртуальное окружение
2) Установить библиотека: 
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
4) Запустить сервис из корневой директории ```src```:
```
python manage.py runserver
```