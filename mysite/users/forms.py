from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import Profile

class user_reg_form(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=['username','email','password1','password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserProfileUpdateForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label="Password", widget=forms.HiddenInput(),
                                                help_text="Password Field Hidden")
    class Meta:
        model = User
        fields = ['username', 'email']
