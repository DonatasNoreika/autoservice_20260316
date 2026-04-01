from django.contrib.auth.models import User
from .models import OrderComment, CarComment, Profile
from django import forms

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']

class CarCommentForm(forms.ModelForm):
    class Meta:
        model = CarComment
        fields = ['content']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

