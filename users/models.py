from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15, default='+996')
    photo = models.ImageField(upload_to='users/', blank=True, null=True)

    gender = models.CharField(max_length=10, choices=[
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE")
    ], default="MALE")

    city = models.CharField(max_length=100, default='Bishkek')
    country = models.CharField(max_length=100, default='Kyrgyzstan')
    bio = models.TextField(blank=True)

    birth_date = models.DateField(null=True, blank=True)

    job = models.CharField(max_length=100, blank=True)
    hobby = models.CharField(max_length=100, blank=True)

    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username