from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer users and create user
    """

    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'password', 'confirm_password')

    def validate(self, data):
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