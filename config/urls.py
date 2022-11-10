"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from library import views
from library.models import Book, Note
from library.serializers import BookSerializer, FeaturedSerializer, NoteSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('books/', views.BookListView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='book-list'),
    path('featured/', views.FeaturedListView.as_view(queryset=Book.objects.filter(featured=True), serializer_class=FeaturedSerializer), name='featured-list'),
    path('notes/', views.NoteListView.as_view(queryset=Note.objects.all(), serializer_class=NoteSerializer), name='note-list'),
    path('create/', views.BookViewSet.as_view({'get': 'list'}), name='book-create')
]
