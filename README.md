# Django Celery Demo

## Run

### Terminal 1
Prepare the DBs and the environment. Then run a Celery worker.
```shell
# PostgreSQL
$ docker run --rm -d -p 5432:5432 -e POSTGRES_PASSWORD=mypassword postgres

# RabbitMQ for the broker
$ docker run -d --rm -p 5672:5672 rabbitmq

# Redis for the backend
$ docker run --rm -d -p 6379:6379 redis

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
>>> add.delay(2, 5).get()
7
```

### Terminal 3
In another terminal, you can run Flower: a real-time Celery web-monitor
```shell
celery --app mysite flower --port=5555
```

## Demo: Worker in a different codebase

 1. Start your worker in a [different codebase](https://git.ximilar.com/getmoments/video/video-workers).
 2. In this project, execute:
    ```shell
    $ cd mysite
    $ python manage.py runserver
    ```
 3. Open your browser with the following URL: http://127.0.0.1:8000/polls/.
 4. Observe the results.