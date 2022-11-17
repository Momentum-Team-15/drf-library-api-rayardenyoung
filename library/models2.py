from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    featured = models.BooleanField(default=False)
    published_date = models.DateField()
    genre = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    book = models.ForeignKey(Book, related_name='notes')
    user = models.ForeignKey(User, related_name='notes')
    private = models.BooleanField(default=False)
    entry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Tracking(models.Model):
    UNTRACKED = 'NA'
    WANTTOREAD = 'WTR'
    READING = 'RDG'
    READ = 'RD'
    STATUS_CHOICES = [
        (UNTRACKED, 'n/a'),
        (WANTTOREAD, 'want-to-read'),
        (READING, 'reading'),
        (READ, 'read'),
        ]
    book = models.ForeignKey(Book, related_name='tracking')
    user = models.ForeignKey(User, related_name='tracking')
    status = models.CharField(choices=STATUS_CHOICES, default=UNTRACKED)