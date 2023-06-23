from django import forms
from myPlantApp.models import ProfileModel, PlantModel


class ProfileModelCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'first_name', 'last_name']


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileModelEditForm(ProfileModelBaseForm):
    pass


class ProfileModelDeleteForm(ProfileModelBaseForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class PlantModelBaseForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantModelCreateForm(PlantModelBaseForm):
    pass


class PlantModelEditForm(PlantModelBaseForm):
    pass


class PlantModelDeleteForm(PlantModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'


