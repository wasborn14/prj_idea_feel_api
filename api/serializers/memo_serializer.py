
from rest_framework import serializers
from api.models import Memo

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

# class SubMemoListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Memo
#         fields = ['id', 'title']

# class MemoListSerializer(serializers.ModelSerializer):
#     children = SubMemoListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Memo
#         fields = ['id', 'title', 'children']

# class MemoSerializer(serializers.ModelSerializer):
#     children = MemoListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Memo
#         fields = ['id', 'title', 'create_user', 'children']

# class MemoListSerializer(serializers.ModelSerializer):
#     memolist = MemoListSerializer()

#     class Meta:
#         model = Memo
#         fields = ['memo_list']