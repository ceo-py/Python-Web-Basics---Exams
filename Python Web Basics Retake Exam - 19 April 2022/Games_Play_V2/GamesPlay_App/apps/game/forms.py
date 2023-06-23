from django import forms

from apps.game.models import GameModel


class GameModelBaseForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class GameModelDeleteForm(GameModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs["disabled"] = True



