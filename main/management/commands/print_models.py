"""Print models command module"""
from main import models
import inspect
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command that prints all project models and
     the count of objects in every model"""
    def handle(self, *args, **options):
        print 'Models:'
        for name, obj in inspect.getmembers(models):
            if inspect.isclass(obj):
                print obj.__name__ + '\n' + 'Objects count: ' +\
                      str(len(obj.objects.all()))
