from django import forms

from CarApp.models import ProfileModel, CarModel


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CarModelBaseForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class ProfileCreateForm(ProfileModelBaseForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'email', 'age', 'password']


class ProfileEditForm(ProfileModelBaseForm):
    pass


class ProfileDeleteForm(ProfileModelBaseForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()


class CarCreateForm(CarModelBaseForm):
    pass


class CarEditForm(CarModelBaseForm):
    pass


class CarDeleteForm(CarModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
