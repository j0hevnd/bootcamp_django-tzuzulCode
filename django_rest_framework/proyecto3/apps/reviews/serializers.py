from rest_framework import serializers

from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')

        