from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from apps.users.serializers import UserSerializer


class RegisterCreateApiView(CreateAPIView):
    """
    Register user
    """
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Create user
        """
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user_serializer = serializer.save() # return instance user

            data = {
                'msg': 'User create successful',
                'user': self.serializer_class(user_serializer).data
            }

            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e, "errorashfk")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
