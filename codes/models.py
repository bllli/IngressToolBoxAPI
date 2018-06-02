from django.db import models

from model_utils.models import TimeStampedModel


class PassCode(TimeStampedModel):
    code = models.CharField(max_length=128, verbose_name='pass code')
    message = models.CharField(max_length=512, verbose_name='信息')
    checked = models.BooleanField(default=False, verbose_name='已验证')

    class Meta:
        verbose_name = 'PassCode'
        verbose_name_plural = verbose_name
