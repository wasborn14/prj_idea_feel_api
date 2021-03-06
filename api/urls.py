from django.urls import path
from django.conf.urls import include
from api.views.views import MemoListView, CreateUserView
from api.views import memo


# modelviewsetの登録例
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # ユーザー登録
    path('register/', CreateUserView.as_view(), name='register'),
    
    # djoserによるエンドポイント実装
    # api/auth/jwt/create/, api/auth/users/, api/auth/users/reset_passwordなどが作成される
    path('auth/', include('djoser.urls.jwt')),

    # メモ関連
    # path('memos/', memos.index, name='memos'),
    path('memo/list/', MemoListView.as_view(), name='memo_list'),
    path('memo/create/', memo.post, name='memo_create'),
    path('memo/<int:memo_id>/', memo.show, name='memos_detail'),
    # TODO:post, putなどメソッドで変えられないのか確認
    path('memo/<int:memo_id>/update/', memo.update, name='memo_update'),
    path('memo/<int:memo_id>/delete/', memo.delete, name='memo_delete'),

    # 元から設定していた内容
    # path('list-post/', PostListView.as_view(), name='list-post'),
    # path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    # path('list-task/', TaskListView.as_view(), name='list-task'),
    # path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),

    # modelviewsetの登録例
    # path('', include(router.urls)),
]