# from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Book, Note
from .serializers import BookSerializer, FeaturedSerializer, NoteSerializer


# Create your views here.

class BookView(generics.ListCreateAPIView):
    #overriding defaults, I think? setting some class attributes:
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def book_list(self, request):
        return self.get_queryset()

    def perform_create(self, serializer):
        serializer.save()


class FeaturedView(generics.ListCreateAPIView):
    featured_queryset = Book.objects.filter(featured=True)
    serializer_class = FeaturedSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = FeaturedSerializer(queryset, many=True)
        return Response(serializer.data)

class NoteView(generics.ListCreateAPIView):
    note_queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exceptions=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)