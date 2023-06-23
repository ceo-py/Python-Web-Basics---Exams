from django import forms

from My_Music_App.user_profile.models import ProfileModel


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


