from django.http import HttpResponse
from .task_service import TaskS
from task_back.task_dto import TaskDTo
from .inject import obj_graph

def index(request):
    create_tas=obj_graph.provide(TaskS)
    dto=TaskDTo(title="title",description="des")
    res=create_tas.create_task(dto)
    return HttpResponse(str(res.dict()))

