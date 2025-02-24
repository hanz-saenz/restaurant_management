from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'typology', 'restaurant']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'phone', 'typology', 'restaurant']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # La contraseña no se devuelve en la respuesta

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone', 'typology', 'restaurant']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
            phone=validated_data.get('phone', ''),
            typology=validated_data.get('typology', 'customer'),
            restaurant=validated_data.get('restaurant', None)
        )
        return user