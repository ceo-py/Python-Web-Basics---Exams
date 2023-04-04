from django import forms

from base.auth_app.models import ProfileModel


class ProfileModelBaseModel(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateModel(ProfileModelBaseModel):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']


class ProfileDeleteModel(ProfileModelBaseModel):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
