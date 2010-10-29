"""Defining application models"""
from django.db import models


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
