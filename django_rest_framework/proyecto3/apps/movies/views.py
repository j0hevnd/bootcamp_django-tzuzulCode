from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework.permissions import AllowAny

from apps.movies.models import Category, Movie
from apps.movies.serializers import CategorySerializer, MovieSerializer, MovieDetailSerializer, MovieShareSerializer

# Categories
class CategoryListApiView(ListAPIView):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieRetrieveApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def post(self, request, pk):
        """ 
        Send emails
        """
        if request.user.is_authenticated:
            movie = self.queryset.get(id=pk)

            request.data['id'] = pk
            share_serializer = MovieShareSerializer(request.data)
            share_serializer.is_valid(raise_exception=True)
            sh = share_serializer.data

            # Build send email


class MovieCreateApiView(CreateAPIView):
    serializer_class = MovieSerializer


class MovieUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDestroyApiView(DestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()