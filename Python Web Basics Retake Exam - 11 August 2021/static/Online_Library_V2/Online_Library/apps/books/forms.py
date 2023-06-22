from django import forms

from apps.books.models import BookModel


class BookModelBaseForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label == 'Type':
                field.widget.attrs['placeholder'] = 'Fiction, Novel, Crime..'
            else:
                field.widget.attrs['placeholder'] = field.label
