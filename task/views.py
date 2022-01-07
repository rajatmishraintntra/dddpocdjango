from django.http import HttpResponse
from .task_service import TaskS
from task_back.task_dto import TaskDTo
from .inject import obj_graph
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json


# Create your views here.


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all Task, or create a new Task.
    """
    if request.method == 'GET':
        gettask = obj_graph.provide(TaskS)
        res = gettask.task_list()
        i=[]
        for ik in res:
            i.append(ik.dict())
        return Response({"data":i})

    elif request.method == 'POST':
        create_tas = obj_graph.provide(TaskS)
        dto = TaskDTo(title=request.POST.get('title'), description=request.POST.get('description'))
        res = create_tas.create_task(dto)
        return Response(res.dict())
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

