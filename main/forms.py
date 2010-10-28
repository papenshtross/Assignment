"""File where form defenitions are situated"""
from django.forms import ModelForm
from main.models import Profile


class ProfileForm(ModelForm):
    """Represent form for Profile model"""
    class Meta:
        """Model assigning"""
        model = Profile
