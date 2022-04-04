from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer users and create user
    """

    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'password', 'confirm_password')

    def validate(self, data):
        """
        Passwords match validate
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(dict(password='Passwords no match'))
        return data

    def create(self, validated_data):
        """
        Create user
        """
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
        )
        user.set_password(validated_data['password'])
        user.save() # model

        return user

    def to_representation(self, instance):
        return {
            'username': instance.username,
            'email': instance.email,
            'first_name': instance.first_name
        }


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """
        User authentication
        """
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Las credenciales no son validas")

        self.context['user'] = user
        return data

    def create(self, validated_data):
        """ Generate user token"""
        token = Token.objects.create(user=self.context['user'])
        return self.context['user'], token.key
