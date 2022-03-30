from rest_framework import viewsets, status
from rest_framework.response import Response

# model
from apps.reviews.models import Review

# serializer
from apps.reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Review.objects.all()
        if not queryset:
            return Response({'msg': 'No comments found'}, status=status.HTTP_200_OK)

        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)