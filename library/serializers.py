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

#accessing foreign key
class BookDetailSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    statuses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'featured', 'notes', 'statuses']