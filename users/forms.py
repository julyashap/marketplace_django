from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class EmailConfirmForm(forms.Form):
    code = forms.CharField(max_length=4, label='Email-код')
