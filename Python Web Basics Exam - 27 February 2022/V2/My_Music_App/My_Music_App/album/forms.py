from django import forms

from My_Music_App.album.models import Album


class AlbumModelBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            # if field.label != 'Genre':
            field.widget.attrs['placeholder'] = field.label


class AlbumModelDelete(AlbumModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs["disabled"] = True
