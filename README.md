# Django Celery Demo

Terminal 1
```shell
$ cd mysite

# Venv
$ python -m venv .venv
$ pip install -r requirements.txt

# PostgreSQL
$ docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=mypassword postgres

# Redis
$ docker run -d -p 6379:6379 redis

# Celery
$ celery --app mysite worker --loglevel INFO
```

Terminal 2
```shell
$ python mysite/manage.py runserver
```

Terminal 3
```shell
$ python mysite/manage.py shell

>>> from polls.tasks import add
>>> res = add.delay(2, 5)
>>> res.get()
7
```