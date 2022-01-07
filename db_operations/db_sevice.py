# from task_back.task_dto import TaskDTo,TaskDToGet
from application.task.task_dto import TaskDTo

from application.task.task_dto import TaskDToGet


class SqlContext(object):
    def create(self,model:object)->TaskDTo:
        model.save()
        data=model.__dict__
        de={}
        for k,v in data.items():
            if k in ['id','title','description']:
                de[k]=v
        return TaskDTo.parse_obj(de)

    def get_list(self,model:object) -> [TaskDToGet]:
        data = model.objects.all()
        l = []
        for i in data:
            de = {}
            for j,v in i.__dict__.items():
                if j in ['id', 'title', 'description']:
                    de[j] = v
            l.append(TaskDToGet(**de))
        return l