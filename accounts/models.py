from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """用户model扩展 以便支持微信登陆"""
    openid = models.CharField('微信用户标识', max_length=128)
    token = models.CharField('已登录凭证', max_length=32)
    wx_name = models.CharField('微信名', max_length=128, blank=True)

    codename = models.CharField('Agent CodeName', max_length=256, null=True, blank=True)
    nickname = models.CharField('昵称', max_length=128, null=True, blank=True)
    level = models.SmallIntegerField('等级', null=True, blank=True)
    level_update_time = models.DateTimeField('等级更新时间', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.wx_name}__{self.openid}__{self.token}'

    @staticmethod
    def get_by_wxapp(openid):
        User.objects.get(openid=openid)
