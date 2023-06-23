from django import forms

from library_base.auth_app.models import ProfileModel


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'first_Name': forms.TextInput(
                attrs={
                    "placeholder": 'First Name'}),
            'last_Name': forms.TextInput(
                attrs={
                    "placeholder": 'Last Name'}),
            'image_URL': forms.TextInput(
                attrs={
                    "placeholder": 'URL'}),
        }


class ProfileDeleteForm(ProfileModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
