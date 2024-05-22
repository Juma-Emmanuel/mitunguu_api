from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        # upload_to='uploads/'
        )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    location =  models.CharField(max_length=200)
    mobile =  models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
