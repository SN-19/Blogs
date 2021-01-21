from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username *','class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name *','class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name *','class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email *','class':'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type':'password','placeholder': 'Password *',
                                                              'class':'form-control'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type':'password','placeholder': 'Confirm Password *',
                                                              'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone *','class':'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('phone',)

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username *', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password *',
                                                              'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username','password',)