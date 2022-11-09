from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=50)
    featured = models.BooleanField()
    # status = 
    # user = 
    # notes = 


