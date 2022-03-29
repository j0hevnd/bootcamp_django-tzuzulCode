from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
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
