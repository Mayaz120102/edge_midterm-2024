from .models import CustomUser 
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re




class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_password(self, value):
        password_complexity = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        if not password_complexity.match(value):
            raise serializers.ValidationError(
                "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character."
            )
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


