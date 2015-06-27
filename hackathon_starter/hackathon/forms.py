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
        fields = ('username','first_name','last_name', 'place', 'phone_number', 'email','talent', 'password')


class RatingForm(forms.ModelForm):
    rating_ontime = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    rating_value = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    rating_reliability = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    rating_quality = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    class Meta:
        model = MerchantRating
        fields = ("rating_ontime", "rating_value", "rating_reliability", "rating_quality", "text")
