from django.contrib.auth.forms import UserCreationForm
from hackathon.models import User, Merchant
from django import forms
from hackathon.models import UserProfile, MerchantProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'area', 'phone_number', 'email', 'password')


class MerchantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Merchant
        fields = ('username', 'area', 'phone_number', 'email', 'password')
