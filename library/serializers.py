from rest_framework import serializers
from .models import Book, Note

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #these fields are the bits of data that will populate in insomnia
        fields = ['title', 'author', 'published_date', 'genre', 'featured' ]

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre']

class NoteSerializer(serializers.ModelSerializer):
    #direct it to source so that 'book' will show up as a string instead of pk
    book = serializers.CharField(source='book.title')
    class Meta:
        model = Note
        fields = ['entry_name', 'book', 'date', 'entry']


class BookDetailSerializer(serializers.ModelSerializer):
    #accessing foreign keys
    statuses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'featured', 'statuses', 'notes']