from django.contrib.auth.forms import UserCreationForm
from hackathon.models import User, Merchant, MerchantRating
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
        fields = ('username', 'place', 'phone_number', 'email', 'password')


class RatingForm(forms.ModelForm):
    class Meta:
        model = MerchantRating
        fields = ("rating_ontime", "rating_value", "rating_reliability", "rating_quality", "text")
