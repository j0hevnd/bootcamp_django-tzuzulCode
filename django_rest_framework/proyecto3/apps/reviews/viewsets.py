from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# model
from apps.reviews.models import Review

# serializer
from apps.reviews.serializers import ReviewSerializer, ReviewCreateSerializer


class ReviewViewSet(viewsets.ViewSet):
    
    def get_permissions(self):
        """
        Permissions for each action
        """
        if self.action=='list' or self.action == "retrieve": 
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
        

    def list(self, request):
        queryset = Review.objects.all()
        if not queryset:
            return Response({'msg': 'No comments found'}, status=status.HTTP_200_OK)

        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        try:
            serializer = ReviewCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {'msg': 'Comment uploaded successfully', 'data':serializer.data}, 
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response({'msg_error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """
        Detail of comment
        """
        instance = get_object_or_404(Review, pk=pk)
        instance = get_object_or_404(Review, pk=pk)
        seralizer = ReviewSerializer(instance)
        return Response(seralizer.data, status=status.HTTP_200_OK)

    
    def update(self, request, pk=None):
        instance = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        """
        delete a comment
        """
        instance = get_object_or_404(Review, pk=pk)
        instance.delete()
        return Response({'msg': 'Comment has been delete'}, status=status.HTTP_204_NO_CONTENT)