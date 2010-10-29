"""File where form defenitions are situated"""
from django import forms
from main.models import Profile
from django.contrib.admin.widgets import AdminDateWidget


class ProfileForm(forms.ModelForm):
    """Represent form for Profile model"""
    class Meta:
        """Model assigning"""
        model = Profile
        widgets = {'birth_date': AdminDateWidget()}
