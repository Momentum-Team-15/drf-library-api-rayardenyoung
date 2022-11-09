from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=50)
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book_author')
        ]
class Status(models.Model):
    read_status = models.CharField(max_length=50)
    book_status = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="statuses", null=True, blank=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.read_status

class Notes(models.Model):
    entry = models.TextField(max_length=500, null=True, blank=True)
    note_date = models.DateField(blank=True, null=True)
    book_note = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="notes", null=True, blank=True)