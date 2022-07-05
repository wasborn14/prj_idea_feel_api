
from requests import request
from rest_framework import serializers, status
from rest_framework.response import Response
from api.models import Memo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.fields import CurrentUserDefault

class MemoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    create_user = serializers.ForeignKey(default=serializers.CurrentUserDefault())

    class Meta:
        model = Memo
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'create_user')
        read_only_fields = ('id',)