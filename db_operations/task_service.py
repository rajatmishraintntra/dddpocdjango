
from application.task.task_dto import TaskDTo
# from dddpocdjango.db_operations.db_sevice import SqlContext
# from dddpocdjango.task.models import Task
# from dddpocdjango.task.validators import Validators
from db_operations.db_sevice import SqlContext
from task.models import Task

from task.validators import Validators


class TaskS:
    def __init__(self,sqlContext:SqlContext,model:Task,validators:Validators) -> None:
        self.sql=sqlContext
        self.model=model
        self.validators=validators
    def create_task(self,task:TaskDTo):
        for k,v in task.dict().items():
            if k=="title":
                self.validators.unique(model=self.model._meta.model,title=v)
                setattr(self.model,k,v)
            else:
                setattr(self.model,k,v)
        return self.sql.create(self.model)

    def task_list(self):
        model = self.model._meta.model
        return self.sql.get_list(model)
