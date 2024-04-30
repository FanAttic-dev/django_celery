# Django Celery Demo

## Run

### Terminal 1
Prepare the DBs and the environment. Then run a Celery worker.
```shell
# PostgreSQL
$ docker run --rm -d -p 5432:5432 -e POSTGRES_PASSWORD=mypassword postgres

# RabbitMQ
$ docker run -d --rm -p 5672:5672 rabbitmq

# or Redis
# $ docker run --rm -d -p 6379:6379 redis

# Venv
$ python -m venv .venv
$ pip install -r requirements.txt

# Celery
$ cd mysite
$ celery --app mysite worker --loglevel INFO
```

### Terminal 2
As a demo, you can just run the Django shell as follows:
```shell
$ python mysite/manage.py shell

>>> from polls.tasks import add
>>> res = add.delay(2, 5)
>>> res.get()
7
```

### Terminal 3
In another terminal, you can run Flower: a real-time Celery web-monitor
```shell
celery --app mysite flower --port=5555
```