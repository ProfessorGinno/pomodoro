from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    advance_percentage = models.FloatField()

    def __str__(self):
        return f"Name: {self.name}.Creation date: {self.creation_date}.Update date: {self.update_date}.Advance percentage: {self.advance_percentage}. ID: {self.id}."

class Activity(models.Model):
    description = models.CharField(max_length=100)
    creation_date = models.DateField()
    advance_percentage = models.FloatField()