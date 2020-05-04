### Manual 
Запуск контейнера с Redis

__docker run -d --name <имя_контейнера_redis> -p 8080:6379 redis__

Собрать образ

__docker build -t <имя_образа>__

Запуск контейнера с собранным образом

__docker run -ti --name <имя_контейнера> -p 80:80 --link <имя_контейнера_redis> <имя_образа>__

