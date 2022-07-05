from django.http import HttpResponseForbidden, JsonResponse
from requests import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, status
from ..serializers import TaskSerializer, UserSerializer, PostSerializer
from ..models import Task, Post, Memo
from rest_framework.decorators import api_view
from users.models import User

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # allowAny jwt認証なしに行える
    permission_classes = (AllowAny,)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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