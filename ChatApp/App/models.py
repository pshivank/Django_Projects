from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 16)