from django.db import models

# Create your models here
class User(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(null=True)
    name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(blank=False)

    def __str__(self):
        return self.username