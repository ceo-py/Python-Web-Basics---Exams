from django import forms

from game_base.auth_app.models import ProfileModel


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(ProfileModelBaseForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']


class ProfileDeleteForm(ProfileModelBaseForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
