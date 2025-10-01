## Clean Hub

Cоздать файл .env
```dotenv
SECRET_KEY=your_key
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=remote_db_host
DB_PORT=5432
```


собираем образ
```commandline
docker build -t myapp .
```

запускаем
```commandline
docker run -p 8000:8000 --env-file .env myapp
```
