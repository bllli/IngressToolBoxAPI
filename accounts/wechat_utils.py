from django.conf import settings

from weixin.lib.wxcrypt import WXBizDataCrypt
from weixin import WXAPPAPI
from weixin.oauth2 import OAuth2AuthExchangeError

from accounts.models import User

appid = settings.WXAPP_ID
secret = settings.WXAPP_SECRET
api = WXAPPAPI(appid=appid, app_secret=secret)


class Unauthorized(Exception):
    def __init__(self, code, des=''):
        self.code = code
        self.des = des


def get_wxapp_userinfo(encrypted_data, iv, code):
    try:
        # 使用 code 换取 session key
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError as e:
        raise Unauthorized(e.code, e.description)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(appid, session_key)
    # 解密得到 用户信息
    user_info = crypt.decrypt(encrypted_data, iv)
    return user_info


def get_openid(encrypted_data, iv, code):
    from pprint import pprint
    user_info = get_wxapp_userinfo(encrypted_data, iv, code)
    pprint(user_info)
    # 获取 openid
    openid = user_info.get('openId', None)
    if openid:
        return openid
    raise Unauthorized('invalid_wxapp_code')


def verify_wxapp(encrypted_data, iv, code):
    user_info = get_wxapp_userinfo(encrypted_data, iv, code)
    # 获取 openid
    openid = user_info.get('openId', None)
    if openid:
        auth = User.get_by_wxapp(openid)
        if not auth:
            raise Unauthorized('wxapp_not_registered')
        return auth
    raise Unauthorized('invalid_wxapp_code')
