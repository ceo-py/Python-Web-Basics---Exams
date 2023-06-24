from django import forms

from apps.user_profile.models import ProfileModel


class ProfilesModelBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"


class ProfileCreateForm(ProfilesModelBaseForm):
    class Meta:
        model = ProfileModel
        fields = ["first_name", "last_name", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()
        self.__set_password_field_hidden()

    def __set_placeholders(self):
        for field in self.fields.values():
            field.widget.attrs["placeholder"] = field.label
            field.label = False

    def __set_password_field_hidden(self):
        if "password" in self.fields:
            self.fields["password"].widget = forms.PasswordInput(
                render_value=False, attrs={"placeholder": "Password"}
            )


class ProfileEditForm(ProfilesModelBaseForm):
    class Meta:
        model = ProfileModel
        fields = ["first_name", "last_name", "image_url", "age"]
