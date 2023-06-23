from django import forms

from base.music_app.models import AlbumModel


def generate_placeholders(fields):
    placeholders = {}
    for att in list(fields)[1:]:
        placeholders[att.attname] = forms.TextInput(
            attrs={
                "placeholder": (" ").join(
                    x.capitalize() if x != "URL" else x for x in att.attname.split("_")
                )
            }
        )
    return placeholders


class AlbumModelBaseForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = "__all__"
        widgets = generate_placeholders(AlbumModel._meta.get_fields())


class AlbumDeleteForm(AlbumModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"
