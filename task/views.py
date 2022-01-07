from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
from application.task.task_dto import TaskDTo
from db_operations.task_service import TaskS
from repository.inject import obj_graph


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

