import pinject
from .db_sevice import SqlContext
from .models import Task
from .validators import Validators
# Create your views here.

class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('sqlContext', to_class=SqlContext)
        bind('model', to_class=Task)
        bind('validators',to_class=Validators)


obj_graph=pinject.new_object_graph(binding_specs=[MyBindingSpec()])
