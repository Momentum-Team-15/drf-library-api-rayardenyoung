from rest_framework import serializers
from .models import Book, Note, Status

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #these fields are the bits of data that will populate in insomnia
        fields = ['title', 'author', 'published_date', 'genre', 'featured' ]

class BookDetailSerializer(serializers.ModelSerializer):
    #accessing foreign keys.
    statuses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #using stringrelatedfield so notes will show up as string instead of pk
    notes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'featured', 'statuses', 'notes']

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

    # def create(self, validated_data):
    #     # return models.Notes.objects.create(**validated_data)
    #     # # or 
    #     return super(BookSerializer, self).create(validated_data)

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['read_status', 'book', 'user']