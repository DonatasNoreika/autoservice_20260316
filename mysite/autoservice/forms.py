from django.contrib.auth.models import User
from .models import OrderComment, CarComment, Profile, Order
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

# class OrderCreateUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['car', 'deadline', 'status']
#         widgets = {'deadline': forms.DateInput(attrs={'type': 'datetime-local'})}

class OrderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'deadline', 'status']
        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Kad POST metu ir validacijoje naudotų tą patį datetime-local formatą
        self.fields['deadline'].input_formats = ['%Y-%m-%dT%H:%M']