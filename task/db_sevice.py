from task_back.task_dto import TaskDTo
class SqlContext(object):
    def create(self,model:object)->TaskDTo:
        model.save()
        data=model.__dict__
        de={}
        for k,v in data.items():
            if k in ['id','title','description']:
                de[k]=v
        return TaskDTo.parse_obj(de)
