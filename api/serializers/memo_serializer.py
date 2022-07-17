
from rest_framework import serializers
from api.models import Memo

# class SubMemoListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Memo
#         fields = ['id', 'title']

# class MemoListSerializer(serializers.ModelSerializer):
#     memo_list = SubMemoListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Memo
#         fields = ['id', 'title', 'memo_list']

# class MemoSerializer(serializers.ModelSerializer):
#     memo_list = MemoListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Memo
#         fields = ['id', 'title', 'create_user', 'memo_list']

class SecondSubMemoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id', 'title']
class FirstSubMemoListSerializer(serializers.ModelSerializer):
    children = SecondSubMemoListSerializer(many=True, read_only=True)
    class Meta:
        model = Memo
        fields = ['id', 'title', 'children']

class MemoListSerializer(serializers.ModelSerializer):
    children = FirstSubMemoListSerializer(many=True, read_only=True)
    class Meta:
        model = Memo
        fields = ['id', 'title', 'create_user', 'children']
