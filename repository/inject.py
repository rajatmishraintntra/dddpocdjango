import pinject
# from dddpocdjango.db_operations.db_sevice import SqlContext
# from dddpocdjango.task.models import Task
# from dddpocdjango.task.validators import Validators
# Create your views here.
from db_operations.db_sevice import SqlContext
from task.models import Task

from task.validators import Validators


class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('sqlContext', to_class=SqlContext)
        bind('model', to_class=Task)
        bind('validators',to_class=Validators)


obj_graph=pinject.new_object_graph(binding_specs=[MyBindingSpec()])
