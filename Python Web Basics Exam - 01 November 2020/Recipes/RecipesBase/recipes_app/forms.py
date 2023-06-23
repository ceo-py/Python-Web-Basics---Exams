from django import forms

from RecipesBase.recipes_app.models import RecipeModel


class RecipeModelBaseForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = '__all__'


class RecipeDeleteForm(RecipeModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            