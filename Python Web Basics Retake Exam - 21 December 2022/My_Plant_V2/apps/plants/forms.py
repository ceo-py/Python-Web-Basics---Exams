from django import forms

from apps.plants.models import PlantsModel


class PlantsModelBaseForm(forms.ModelForm):
    class Meta:
        model = PlantsModel
        fields = '__all__'


class PlantsDeleteForm(PlantsModelBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
