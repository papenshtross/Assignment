"""Defining application models"""
from django.db import models

"""My profile model"""
class Profile(models.Model):       
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    skype = models.CharField(max_length=30)
    icq = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    cell = models.CharField(max_length=30)

"""Http Request model"""
class Request(models.Model):
    request = models.TextField()