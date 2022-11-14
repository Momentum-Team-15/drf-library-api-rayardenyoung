from django.contrib import admin
from .models import User, Book, Status, Note
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Status)
admin.site.register(Note)