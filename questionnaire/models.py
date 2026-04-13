from django.db import models

class Questionnaire(models.Model):
    name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    favorite_actress = models.CharField(max_length=100)
    favorite_actress_photo = models.ImageField(upload_to='images/')
    favorite_singer = models.CharField(max_length=100)
    favorite_singer_photo = models.ImageField(upload_to='images/')
    team_name = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    birth_date = models.DateField()

    profile_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

# Create your models here.
