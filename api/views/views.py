from django.http import HttpResponseForbidden, JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import generics
from api.serializers.memo_serializer import MemoListSerializer

from api.serializers.serializers import UserSerializer
from ..models import Memo
from rest_framework.decorators import api_view
from users.models import User
from django.db.models import Q

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # allowAny jwt認証なしに行える
    permission_classes = (AllowAny,)

# 元の設定内容
# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (AllowAny,)

# class PostRetrieveView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (AllowAny,)

# class TaskListView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = (AllowAny,)

# class TaskRetrieveView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = (AllowAny,)

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

def get_token(request):
    """
    リクエストからトークンを取得して返す
    :param request: リクエスト
    :return:トークン
    """
    return request.META.get('HTTP_AUTHORIZATION', None)

user_fields = ('username')

@api_view(['GET'])
def index(request):
    token = get_token(request)
    if token is None:
        return HttpResponseForbidden()
    users = User.objects.all().values(user_fields)
    data = {
        "users": list(users)
    }
    return JsonResponse(list(data), safe=False)
class MemoListView(generics.ListAPIView):
    # prefetch_relatedがあればserializer複数なくても再帰的にできると思ったがうまくいっていないのでいらないかもしれない
    # いずれこちらのようにできるか検討：https://qiita.com/sin_tanaka/items/1d5932fd8e393f432651
    # queryset = Memo.objects.filter(Q(memos_id__isnull=True) | Q(memos_id__exact=0)).prefetch_related('memolist')
    serializer_class = MemoListSerializer

    def get_queryset(self):
        return Memo.objects.filter(Q(parent__isnull=True) | Q(parent__exact=0))\
            .filter(create_user=self.request.user.id).prefetch_related('children')