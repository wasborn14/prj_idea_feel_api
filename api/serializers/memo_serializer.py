
from requests import request
from rest_framework import serializers, status
from rest_framework.response import Response
from api.models import Memo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.fields import CurrentUserDefault

class SubMemoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id', 'title']

class MemoListSerializer(serializers.ModelSerializer):
    memolist = SubMemoListSerializer(many=True, read_only=True)
    class Meta:
        model = Memo
        fields = ['id', 'title', 'memolist']

class MemoSerializer(serializers.ModelSerializer):
    memolist = MemoListSerializer(many=True, read_only=True)
    class Meta:
        model = Memo
        fields = ['id', 'title', 'create_user', 'memolist']