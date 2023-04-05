from django import forms

from base.auth_app.models import ProfileModel
from base.music_app.forms import generate_placeholders


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"
        widgets = generate_placeholders(ProfileModel._meta.get_fields())


class ProfileDeleteForm(ProfileModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
