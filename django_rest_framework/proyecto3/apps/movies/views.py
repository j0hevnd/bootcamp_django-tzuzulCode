from django.conf import settings
from django.core.mail import send_mail

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
            share_serializer = MovieShareSerializer(data=request.data)
            share_serializer.is_valid(raise_exception=True)
            sh = share_serializer.data

            # We obtain the complete url for the movie
            movie_url = request.build_absolute_uri(movie.get_absolute_url())

            # Build our message for the send email
            subject = f"{sh['name']} recommends you to watch movie {movie.movie_name}"
            message = f"\nWatch the movie {movie.movie_name} at {movie_url}\n"\
                      f"{sh['name']} comments: {sh['comments']}"

            # send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [sh["email"]])
            return Response({"msg": "Email send successful"}, status=status.HTTP_200_OK)

        return Response({"msg_error": "First you log-in, please."}, status=status.HTTP_401_UNAUTHORIZED)


class MovieCreateApiView(CreateAPIView):
    serializer_class = MovieSerializer


class MovieUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDestroyApiView(DestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()