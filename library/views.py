# from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Book, Note
from .serializers import BookSerializer, FeaturedSerializer, NoteSerializer, BookDetailSerializer


# Create your views here.

# trying out ListCreateAPIView for books >>>>
#this is now superfluous, but keeping it to check out in Insomnia:
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #this is to GET a list of books by user
        #by overriding the get_querset method built in to ListCreateAPIView, I can filter habits by the logged-in user
        return self.request.user.books.all()

    def perform_create(self, serializer):
        #this is to POST a new book
        #by overriding this perform_create method built in to ListCreateAPIView, I can associate the user who is creating this habit
        serializer.save(user=self.request.user)
  

#trying out Model View Set for books >>>
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

    # def create(self, request, *args, **kwargs):
    #     try:
    #         return super().create(request, *args, **kwargs)
    #     except IntegrityError:
    #         error_data = {
    #             "error": "Unique constraint violation: there is already a book with this title by this author."
    #         }
    #         return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

#using this view because it's for retrieving, updating or deleting a ~single instance~ of a model
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

#ohhh okay, so this ListCreateAPITView is explicitly for listing a queryset or creating a model instance.
# Used for read-write endpoints to represent a collection of model instances.
class FeaturedView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(featured=True)
    serializer_class = FeaturedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.books.filter(featured=True)

    #trying to add book that already exists to featured, but not working
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    

class NoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notes.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

