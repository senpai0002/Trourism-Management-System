from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'type':'text',
            'name':"name",
            'id':"username",
            'class': 'form-control',
            'placeholder': 'Choose a username',
        }), required = True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type':'password',
            'name':"password1",
            'id':"password",
            'placeholder': 'Enter your password',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type':'password',
            'name':"password2",
            'id':"confirm_password",
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })
    )

    genderChoices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = forms.ChoiceField(
        choices = genderChoices,
        widget = forms.RadioSelect(attrs = {
                'class':"form-check-input",
                'type':"radio",
                'name':"gender",
                'id':"male",
                'value':"male",
            }),
            required = True
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','gender']
