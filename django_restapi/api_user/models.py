from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)