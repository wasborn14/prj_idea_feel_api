from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView,\
    PostListView, PostRetrieveView
from api.views import memos

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # ユーザー登録
    path('register/', CreateUserView.as_view(), name='register'),
    
    # djoserによるエンドポイント実装
    # api/auth/jwt/create/, api/auth/users/, api/auth/users/reset_passwordなどが作成される
    path('auth/', include('djoser.urls.jwt')),

    # メモ関連
    path('memos/', memos.index, name='memos'),
    path('memos/create/', memos.post, name='memos-create'),
    path('memos/<int:memo_id>/', memos.show, name='memos-detail'),
    # TODO:post, putなどメソッドで変えられないのか確認
    path('memos/<int:memo_id>/update/', memos.update, name='memos-update'),
    path('memos/<int:memo_id>/delete/', memos.delete, name='memos-delete'),

    # 元から設定していた内容
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),

    path('', include(router.urls)),
]