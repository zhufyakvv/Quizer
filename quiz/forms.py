# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 27.06.2017
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=64)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=64)
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_repeat = forms.CharField(label='Password repeat', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_repeat")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password does not match."
            )

class ProfileEditForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=64)
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Second Name')
    image = forms.ImageField(label='Profile pic')


class ProfilePasswordEditForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_repeat = forms.CharField(label='One more time password', widget=forms.PasswordInput())
