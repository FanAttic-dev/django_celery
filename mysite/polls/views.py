from django.http import HttpResponse
from mysite.celery import app


def index(request):
    task = app.send_task("workers.concatenator.tasks.concat_scenes", (["video1", "video2"],))
    res = task.get()
    return HttpResponse("Worker finished with result: " + str(res))
