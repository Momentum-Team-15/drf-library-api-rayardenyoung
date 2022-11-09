from rest_framework import serializers
from .models import Book, Note

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'featured' ]

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['entry_name', 'entry', 'date', 'book']