"""Defining application models"""
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete


class Profile(models.Model):
    """My profile model"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    birth_date = models.DateField()
    skype = models.CharField(max_length=30)
    icq = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    cell = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Request(models.Model):
    """Http Request model"""
    request = models.TextField()

    def __unicode__(self):
        return self.request


class TransactionSignal(models.Model):
    """Signal processor db model"""
    model = models.TextField()
    action = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.model, self.action)


@receiver(post_save)
def saved(sender, created, **kwargs):
    """post_save signal handler"""
    if sender is not TransactionSignal:
        if created:
            action = 'create'
        else:
            action = 'update'
        TransactionSignal.objects.create(model=sender.__name__,
                                         action=action)


@receiver(post_delete)
def deleted(sender, **kwargs):
    """post_delete signal handler"""
    TransactionSignal.objects.create(model=sender.__name__,
                                         action='delete')
