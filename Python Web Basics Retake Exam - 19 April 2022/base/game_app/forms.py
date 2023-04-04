from django import forms

from base.auth_app.models import ProfileModel
from base.game_app.models import GameModel


class GameModelBaseForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class GameDeleteForm(GameModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
