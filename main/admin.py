"""Default administration class"""
from django.contrib import admin
from main.models import Profile

# Register Profile for administration purposes
admin.site.register(Profile)
