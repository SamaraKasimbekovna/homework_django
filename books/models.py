from django.db import models
from django.utils import timezone

class Books(models.Model):
    title = models.CharField(max_length=200)  # название
    author = models.CharField(max_length=100)  # автор
    genre = models.CharField(max_length=100)  # жанр
    pages = models.IntegerField()  # количество страниц
    description = models.TextField(default='', blank=True)  # короткое описание
    image = models.ImageField(upload_to='books/')  # фото книги
    rating = models.FloatField()  # рейтинг
    review = models.TextField(max_length=150, blank=True) # отзыв о книге
    created_at = models.DateTimeField(default= timezone.now)  # дата добавления

    def __str__(self):
        return self.title
    
    
    

# Create your models here.
