from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    bio = models.TextField(max_length=100, blank=True)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)