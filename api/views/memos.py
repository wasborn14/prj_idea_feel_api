from asyncio.log import logger
from django.http import HttpResponseBadRequest, HttpResponseForbidden, JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from api.utils import login_check
from api.models import Memo

memo_fields = ('id', 'title', 'content', 'created_at', 'updated_at','create_user') 

"""
メモ一覧取得

param:request
return:JsonResponse
throws:HttpResponseForbidden
"""
@api_view(['GET'])
def index(request):
    login_check(request)
    # 作成者本人のメモのみ返す
    memos = Memo.objects.all().filter(create_user=request.user.id).values(*memo_fields).order_by('created_at').reverse()
    response = {"memoList":list(memos)}
    return JsonResponse(response, safe=False)

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
            memo.content = request.data.get('content')
            memo.created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
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
