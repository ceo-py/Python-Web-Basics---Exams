from django import forms

from apps.notes.models import NotesModel


class NotesModelBaseForm(forms.ModelForm):
    class Meta:
        model = NotesModel
        fields = ['title', 'content', 'image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label_suffix = ''


class NotesDeleteForm(NotesModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
