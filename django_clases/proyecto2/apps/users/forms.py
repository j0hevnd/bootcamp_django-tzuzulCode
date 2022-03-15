from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

    
    def clean(self):
        cd = super().clean()
        password = cd['password']
        password2 = cd['password2']
        print(len(password))
        if len(password) < 7 or len(password) > 15:
            self.add_error('password', 'this password is too short. It must contain al least 8 characters and max lenght 15 characters')
        
        if len(password2) < 7 or len(password2) > 15:
            self.add_error('password2', 'this password is too short. It must contain al least 8 characters and max lenght 15 characters')

        return cd

    def clean_password2(self):
        """ validate that the passwords match """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match', code='invalid')

        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    
class CustomUserCreationForm(UserCreationForm):
    """ Create a user form inherited from UserCreationForm with fields that we specify """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
