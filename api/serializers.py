from requests import request
from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Task, Post, Memo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.fields import CurrentUserDefault

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'content', 'created_at')

class UserDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username')