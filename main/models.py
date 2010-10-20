from django.db import models

class Profile(models.Model):       
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    skype = models.CharField(max_length=30)
    icq = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    cell = models.CharField(max_length=30)