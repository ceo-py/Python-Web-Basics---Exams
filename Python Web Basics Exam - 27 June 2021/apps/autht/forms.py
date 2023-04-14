from django import forms

from apps.autht.models import ProfileModel


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
