from django.db import models

# Create your models here.

class filter_model(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()