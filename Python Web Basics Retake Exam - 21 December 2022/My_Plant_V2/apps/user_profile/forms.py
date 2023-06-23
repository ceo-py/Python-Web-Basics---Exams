from django import forms

from apps.user_profile.models import ProfileModel


class ProfilesModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(ProfilesModelBaseForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'first_name', 'last_name']
