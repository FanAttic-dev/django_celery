# Django Celery Demo


## Run

### Terminal 1
Prepare the DBs and the environment. Then run a Celery worker.
```shell
# PostgreSQL
$ docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=mypassword postgres

# Redis
$ docker run -d -p 6379:6379 redis

# Venv
$ python -m venv .venv
$ pip install -r requirements.txt

# Celery
$ celery --app mysite worker --loglevel INFO
```

### Terminal 2
Run Django app for producing tasks.
```shell
$ python mysite/manage.py runserver
```

As a demo, you can just run the Django shell as follows:
```shell
$ python mysite/manage.py shell

>>> from polls.tasks import add
>>> res = add.delay(2, 5)
>>> res.get()
7
```