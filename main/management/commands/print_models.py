"""Print models command module"""
from django.db.models import get_models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command that prints all project models and
     the count of objects in every model"""
    def handle(self, *args, **options):
        print 'Models:'
        for model in get_models():
            print model.__name__ + '\n' + 'Objects count: ' +\
                  str(len(model.objects.all()))
