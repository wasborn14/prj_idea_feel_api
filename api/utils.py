from django.http import HttpResponseForbidden

"""
ログイン状態を確認するためトークンをチェックする
param:request
return:none
throw:HttpResponseForbidden
"""
def login_check(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    if token is None:
        return HttpResponseForbidden()
    return