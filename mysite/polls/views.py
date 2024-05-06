from django.http import HttpResponse
from mysite.celery import app


def index(request):
    res = app.send_task("workers.concatenator.tasks.concat_scenes", (["video1", "video2"],)).get()
    return HttpResponse("Worker finished with result: " + str(res))
