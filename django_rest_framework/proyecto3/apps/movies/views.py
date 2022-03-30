from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from apps.movies import serializers

from apps.movies.models import Category, Movie
from apps.movies.serializers import CategorySerializer, MovieSerializer

# Categories
class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreateApiView(CreateAPIView):
    serializer_class = CategorySerializer


# class CategoryUpdateApiView(UpdateAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()

class CategoryUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDeleteApiView(DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# Movies

class MovieListApiView(ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieRetrieveApiView(RetrieveAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieCreateApiView(CreateAPIView):
    serializer_class = MovieSerializer


class MovieUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDestroyApiView(DestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()