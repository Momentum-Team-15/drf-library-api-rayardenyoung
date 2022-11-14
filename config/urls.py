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
    path('books/', views.BookView.as_view(), name='book-list'),
    path('bookviewset/', views.BookViewSet.as_view({'get': 'list'}), name='book-list'),
    path('featured/', views.FeaturedView.as_view(), name='featured-list'),
    path('featured/edit/<int:pk>/', views.FeaturedView.as_view(), name='featured-edit'),
    path('notes/', views.NoteView.as_view(), name='note-list'),
    path('notes/add/', views.NoteView.as_view(), name='note-add'),
    path('books/add/', views.BookViewSet.as_view({'post': 'create'}), name='book-add'),
    path('books/detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]