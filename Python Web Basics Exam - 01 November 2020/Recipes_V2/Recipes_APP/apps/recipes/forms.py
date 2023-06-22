from django import forms

from apps.recipes.models import RecipesModel


class RecipesModelBaseForm(forms.ModelForm):
    class Meta:
        model = RecipesModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label_suffix = ''


class RecipesDeleteForm(RecipesModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs["disabled"] = True
