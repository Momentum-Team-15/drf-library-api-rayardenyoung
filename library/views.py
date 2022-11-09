# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class BookListView(generics.ListCreateAPIView):
    #overriding defaults, I think? setting some class attributes:
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        # because of generic views? have to use `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)