from django.db import models

# 🏞 Местность (тур)
class Location(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='locations/', null=True, blank=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


# 👤 Человек (1 к 1 связь)
class Person(models.Model):
    name = models.CharField(max_length=100)
    tour = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 💬 Комментарии (1 ко многим)
class Comment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


# 🏷 Категории (многие ко многим)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name