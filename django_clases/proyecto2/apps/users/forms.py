from cProfile import label
from django import forms
from django.contrib.auth.forms import AuthenticationForm

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'