from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'required': True},
        }

    def create(self, validated_data):
        """
        Создание пользователя.
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Устанавливаем зашифрованный пароль
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Обновление пользователя.
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # Хэшируем новый пароль
        instance.save()
        return instance
