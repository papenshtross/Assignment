"""File where form defenitions are situated"""
from django import forms
from main.models import Profile, Request
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


    # This describes "form" - on the server side.

class ContactForm(forms.Form):
    """Simple contact form"""
    subject = forms.CharField(label="Subject", max_length=80)
    text = forms.CharField(label="Your query", widget=forms.Textarea)

    class Media:
        """Plug in the javascript we will need:"""
        js = ("http://code.jquery.com/jquery-1.4.4.js",
              "https://github.com/malsup/form/raw/master/jquery.form.js")
