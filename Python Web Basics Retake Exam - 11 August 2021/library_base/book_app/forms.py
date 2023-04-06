from django import forms

from library_base.book_app.models import BookModel


class BookModelBaseForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    "placeholder": 'Title'}),
            'description': forms.TextInput(
                attrs={
                    "placeholder": 'Description'}),
            'image': forms.TextInput(
                attrs={
                    "placeholder": 'Image'}),
            'type': forms.TextInput(
                attrs={
                    "placeholder": 'Fiction, Novel, Crime..'}),
        }
