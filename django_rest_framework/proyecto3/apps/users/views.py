from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny

from apps.users.serializers import UserSerializer, UserLoginSerializer


class RegisterCreateApiView(CreateAPIView):
    """
    Register user
    """
    permission_classes = [AllowAny]
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


class LoginApiView(APIView):
    """
    Authenticating user
    """
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        """User log-in"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        login(request, user)

        data = {
            'user': UserSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
    Deauthenticated user
    """
    
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'msg': "Logout success"}, status=status.HTTP_200_OK)




