from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, RetrieveUpdateAPIView

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer


class ReviewUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()