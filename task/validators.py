from django.apps import AppConfig
class Validators:
    def unique(self,model=None,**kwargs):
        print(kwargs)
        try:
            model.objects.get(**kwargs)
        except model.DoesNotExist:
            return kwargs
        raise ValueError(dict(errors=list(kwargs.keys())[0]+' already exists'))