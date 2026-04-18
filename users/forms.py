from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from .models import CustomUser

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    photo = forms.ImageField(required=False)
    gender = forms.ChoiceField(choices=[
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE")
    ])
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    captcha = CaptchaField()  

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit=True):
        user = super().save(commit=True)

        CustomUser.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            photo=self.cleaned_data.get('photo'),
            gender=self.cleaned_data['gender'],
            city=self.cleaned_data['city'],
            country=self.cleaned_data['country'],
        )

        return user