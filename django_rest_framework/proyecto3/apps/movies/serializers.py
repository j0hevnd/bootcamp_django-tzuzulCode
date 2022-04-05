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
        depth = 1

    def to_representation(self, instance):
        """
        Data to send to the view
        """
        data = super().to_representation(instance)
        
        return {
            'id': instance.id,
            'movie_name': data['movie_name'],
            'desciption':instance.description
        }

class MovieDetailSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1


class MovieShareSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=20)
    email = serializers.EmailField(required=True)
    comments = serializers.CharField(required=True, max_length=200)