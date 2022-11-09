from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    #specifying h
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date', 'genre', 'featured' ]