from .models import OrderComment, CarComment
from django import forms

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']

class CarCommentForm(forms.ModelForm):
    class Meta:
        model = CarComment
        fields = ['content']
