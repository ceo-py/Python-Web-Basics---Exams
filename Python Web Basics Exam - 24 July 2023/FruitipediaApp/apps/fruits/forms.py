from django import forms

from apps.fruits.models import FruitsModel


class FruitsModelBaseForm(forms.ModelForm):
    class Meta:
        model = FruitsModel
        fields = "__all__"


class FruitsCreateForm(FruitsModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for field in self.fields.values():
            field.widget.attrs["placeholder"] = field.label
            field.label = False


class FruitsEditForm(FruitsModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_labels()

    def __set_labels(self):
        for (field, label) in zip(
            self.fields.values(), ("Name", "Image URL", "Description", "Nutrition")
        ):
            field.label = label


class FruitsDeleteForm(FruitsModelBaseForm):
    class Meta:
        model = FruitsModel
        fields = ["name", "image_url", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_labels()
        self.__set_disabled_fields()

    def __set_labels(self):
        for (field, label) in zip(
            self.fields.values(), ("Name", "Image URL", "Description")
        ):
            field.label = label

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs["disabled"] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
