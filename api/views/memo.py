from asyncio.log import logger
from django.http import HttpResponseBadRequest, HttpResponseForbidden, JsonResponse, HttpResponse
from django.db.models import Q
from rest_framework import serializers
from rest_framework.decorators import api_view
from api.utils import login_check
from api.models import Memo

ZERO = 0
memo_fields = ('id', 'title', 'content', 'created_at', 'updated_at','create_user', 'parent', 'icon_id') 

"""
メモ一覧取得

param:request
return:JsonResponse
throws:HttpResponseForbidden
"""
# @api_view(['GET'])
# def index(request):
#     login_check(request)
#     # 作成者本人のメモのみ返す
#     memo = Memo.objects.all().filter(id=35).values().first()
#     children = memo.memo_set

#     logger.debug('memo')
#     # memos = memo.memo_set

#     # memos = Memo.objects.all()
#     # for memo in memos:
#     #     for child in memos.memo_set.all():
#     #         print(f'[{memo.id} {child.name}]')


#     memos = Memo.objects.all().filter(create_user=request.user.id)\
#     .filter(Q(parent_id__isnull=True) | Q(parent_id__exact=ZERO))\
#     .select_related('memo').values()\
#     .order_by('created_at').reverse()
#     # logger.debug('memos',list(memos))
#     response = {"memoList":list(memos)}
#     # logger.debug('memos',response)
#     if memos is None:
#         return JsonResponse([], safe=False)
#     return JsonResponse(memo, safe=False)

"""
メモ詳細取得

param:request, memo_id
return:JsonResponse
throws:HttpResponseForbidden
"""
@api_view(['GET'])
def show(request, memo_id):
    login_check(request)
    memo = Memo.objects.all().filter(id=memo_id).values(*memo_fields).first()
    # メモが存在しない場合
    if memo is None:
        return HttpResponseBadRequest()
    # ログインユーザーと作成者が違う場合
    if memo.get('create_user') is not request.user.id:
        return HttpResponseBadRequest()
    return JsonResponse(memo)

"""
メモ作成

param:request
return:HttpResponse
throws:HttpResponseForbidden, HttpResponseBadRequest
"""
@api_view(['POST'])
def post(request):
    try:
        login_check(request)
        if "title" in request.data:
            # ログイン中のユーザーを作成者として登録
            memo = Memo(create_user=request.user)
            memo.title = request.data.get('title')
            # 最初はcontentを仕様していたが削除
            # memo.content = request.data.get('content')
            memo.created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
            memo.updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
            memo.parent = request.data.get('parent')
            # iconの変更は後に実装
            # memo.icon_id = 1
            memo.save()
            response = {"id":memo.id}
            return JsonResponse(response)
        else:
            return HttpResponseForbidden()

    except Exception as e:
        logger.info(e)
        return HttpResponseBadRequest()

"""
メモ編集

param:request, memo_id
return:HttpResponse
throws:HttpResponseForbidden, HttpResponseBadRequest
"""
@api_view(['PUT'])
def update(request, memo_id):
    try:
        login_check(request)
        if "title" in request.data:
            # memo_idから該当のメモを参照。作成者自身でなければエラーを返す
            memo = Memo.objects.all().filter(id=memo_id).filter(create_user=request.user.id).first()
            if memo is None:
                return HttpResponseBadRequest()
            memo.title = request.data.get('title')
            memo.content = request.data.get('content')
            memo.updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
            memo.save()
            response = {"id":memo.id}
            return JsonResponse(response)
        else:
            return HttpResponseForbidden()

    except Exception as e:
        logger.info(e)
        return HttpResponseBadRequest()

"""
メモ削除

param:request, memo_id
return:HttpResponse
throws:HttpResponseBadRequest
"""
@api_view(['DELETE'])
def delete(request, memo_id):
    try:
        login_check(request)
        # memo_idから該当のメモを参照。作成者自身でなければエラーを返す
        memo = Memo.objects.all().filter(id=memo_id).filter(create_user=request.user.id).first()
        if memo is None:
            return HttpResponseBadRequest()
        memo.delete()
        return HttpResponse()

    except Exception as e:
        logger.info(e)
        return HttpResponseBadRequest()
