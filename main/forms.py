"""File where form defenitions are situated"""
from django import forms
from main.models import Profile
from django.contrib.admin.widgets import AdminDateWidget


class ProfileForm(forms.ModelForm):
    """Represent form for Profile model"""

    def __init__(self, *args, **kw):
        super(forms.ModelForm, self).__init__(*args, **kw)
        profile_fields = Profile._meta.fields[1:]
        profile_fields.reverse()
        values = []
        for field in profile_fields:
            values.append(field.get_attname())
        self.fields.keyOrder = values

    class Meta:
        """Model assigning"""
        model = Profile
        widgets = {'birth_date': AdminDateWidget()}
