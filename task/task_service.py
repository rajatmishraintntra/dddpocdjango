
from task_back.task_dto import TaskDTo
from .db_sevice import SqlContext
from .models import Task
from .validators import Validators

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
