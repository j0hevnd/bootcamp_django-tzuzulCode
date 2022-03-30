from rest_framework import serializers

from apps.movies.models import Category, Movie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """ List, Create, Update """

    class Meta:
        model = Movie
        fields = '__all__'


