from rest_framework import serializers

from apps.reviews.models import Review
from apps.movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')

        depth = 2


class ReviewCreateSerializer(serializers.Serializer):
    """
    Comment movie
    """
    comment = serializers.CharField(max_length=200)
    movie_review = serializers.CharField(max_length=200)

    def create(self, validated_data):
        movie_review = Movie.objects.filter(movie_name=validated_data['movie_review']).first()
        Review.objects.create(
            comment = validated_data['comment'],
            movie_review = movie_review
        )
        return validated_data
        