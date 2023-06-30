from django import forms

from apps.user_profile.models import ProfileModel


class ProfileModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(ProfileModelBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for field in self.fields.values():
            if 'URL' in field.label:
                field.widget.attrs["placeholder"] = 'URL'
            else:
                field.widget.attrs["placeholder"] = field.label

            field.label_suffix = ''


class ProfileDeleteForm(ProfileModelBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
