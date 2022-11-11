# from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Book, Note
from .serializers import BookSerializer, FeaturedSerializer, NoteSerializer, BookDetailSerializer


# Create your views here.

# trying out ListCreateAPIView for books >>>>
#this is now superfluous, but keeping it to check out in Insomnia:
class BookView(generics.ListCreateAPIView):
    #overriding defaults, I think? setting some class attributes:
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def book_list(self, request):
    #     return self.get_queryset()

    # def perform_create(self, serializer):
    #     serializer.save()


#trying out Model View Set for books >>>
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # http_method_names = ["get","post"]
    permission_classes = [AllowAny]

    # def create(self, request, *args, **kwargs):
    #     try:
    #         return super().create(request, *args, **kwargs)
    #     except IntegrityError:
    #         error_data = {
    #             "error": "Unique constraint violation: there is already a book with this title by this author."
    #         }
    #         return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exceptions=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#using this view because it's for retrieving, updating or deleting a ~single instance~ of a model
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

#ohhh okay, so this ListCreateAPITView is explicitly for listing a queryset or creating a model instance.
# Used for read-write endpoints to represent a collection of model instances.
class FeaturedView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(featured=True)
    serializer_class = FeaturedSerializer
    
    # def featured_list(self, request):
    #     return self.filter_queryset()

class NoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # def note_list(self, request):
    #     return self.get_queryset()

