from django.db import models

# Create your models here.

class filter_model(models.Model):
    name = models.CharField(max_length=100)
    father = models.CharField(max_length=100,null=True,blank=True)
    mother = models.CharField(max_length=100,null=True,blank=True)
    occupation = models.CharField(max_length=50,null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name