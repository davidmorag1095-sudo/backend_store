from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    active = models.BooleanField(default=True)

    #To string 
    def __str__(self):
        return self.name

