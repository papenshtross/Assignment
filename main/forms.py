"""File where form defenitions are situated"""
from django import forms
from main.models import Profile
from main.widgets import DateTimeWidget


class ProfileForm(forms.ModelForm):
    """Represent form for Profile model"""
    class Meta:
        """Model assigning"""
        model = Profile
        widgets = {'birth_date': DateTimeWidget}
