"""File where form defenitions are situated"""
from django import forms
from main.models import Profile
from main.widgets import DateTimeWidget


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
        widgets = {'birth_date': DateTimeWidget}

    class Media:
        """Plug in the javascript we will need:"""
        js = ("/site_media/js/jquery-1.4.4.js",
                "/site_media/js/jquery.form.js",
                "/site_media/js/progress.js",
                "/site_media/js/progress.dialog.js")
