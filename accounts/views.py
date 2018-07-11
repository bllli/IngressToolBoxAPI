from django.contrib import auth
from django.http import JsonResponse
from rest_framework import status

from accounts.models import User
from utils.utils import get_request_param_as_json
from accounts.wechat_utils import get_wxapp_userinfo, get_openid


def login(request):
    """登陆"""
    params = get_request_param_as_json(request)
    # print(params)
    try:
        user_info = get_wxapp_userinfo(
            encrypted_data=params['encrypted_data'],
            iv=params['iv'],
            code=params['code']
        )
    except Exception as e:
        return JsonResponse({
            'msg': e,
        }, status=status.HTTP_401_UNAUTHORIZED)

    openid = user_info.get('openId')
    user, _ = User.objects.get_or_create(openid=openid)
    auth.login(request, user)
    return JsonResponse({
        'msg': 'ok',
        'jwt': '1'
    })


def test(request):
    return JsonResponse({
        'status': request.user.nickname if request.user.is_authenticated else 'nope'
    })


def logout(request):
    """登出"""
    return JsonResponse({
        'msg': 'ok'
    })
