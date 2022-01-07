from pydantic import BaseModel

class TaskDTo(BaseModel):
    title:str
    description:str

class TaskDToGet(TaskDTo):
    id:int