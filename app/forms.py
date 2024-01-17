from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import User

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','date_of_birth', 'profile_picture', 'phone_number', 'gender', 'occupation', 'company' ,'receive_newsletter' ]
    widgets = {
        'date_of_birth': forms.TextInput(attrs={'type': 'date'}),
    }

