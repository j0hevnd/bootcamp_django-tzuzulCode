from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     username = forms.TextInput(
#         label='Username'
#     )
#     password = forms.PasswordInput(
#         label='Password'
#     )

#     def clean(self):
#         return super().clean()

class LoginForm(AuthenticationForm):
    """ User login form """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class UserRegistrationForm(forms.ModelForm):
    """ Form for user registration """
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password2(self):
        """ validate that the passwords match """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match', code='invalid')

        return cd['password2']