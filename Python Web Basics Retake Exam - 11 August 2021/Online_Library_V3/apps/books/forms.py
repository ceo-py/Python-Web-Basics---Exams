from django import forms

from apps.books.models import BooksModel


class BooksModelBaseForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = '__all__'


class BooksCreateForm(BooksModelBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for field in self.fields.values():
            if 'Type' in field.label:
                field.widget.attrs["placeholder"] = 'Fiction, Novel, Crime..'
            else:
                field.widget.attrs["placeholder"] = field.label

            field.label_suffix = ''

