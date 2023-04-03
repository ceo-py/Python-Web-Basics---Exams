from django import forms

from CarApp.models import ProfileModel, CarModel


class ProfileModelBase(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CarModelBase(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class ProfileCreateModel(ProfileModelBase):
    class Meta:
        model = ProfileModel
        fields = ['username', 'email', 'age', 'password']


class ProfileEditModel(ProfileModelBase):
    pass


class ProfileDeleteModel(ProfileModelBase):
    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class CarCreateModel(CarModelBase):
    pass


class CarEditModel(CarModelBase):
    pass


class CarDeleteModel(CarModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            # field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'

        # list(self.fields.values())[0].widget.attrs['disabled'] = 'disabled'
