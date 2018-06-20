from django.db import models

from model_utils.models import TimeStampedModel


class TagOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-weight')


class Tag(models.Model):
    """标签Model"""
    name = models.CharField('名称', max_length=64)
    weight = models.SmallIntegerField('权重', default=1)
    hide = models.BooleanField('隐藏', default=False)

    objects = TagOrderManager()  # 替换默认Manager

    class Mete:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        # ordering = ('-weight',)  # 不生效 不知道为啥

    def __str__(self):
        return f'{self.name}'


# class ItemType(models.Model):
#     """道具类型"""
#     name = models.CharField(max_length=128, verbose_name='名称')
#
#     class Meta:
#         verbose_name = '道具类型'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class Item(models.Model):
#     """道具 Model"""
#     RARITY_COMMON = 0x01
#     RARITY_RARE = 0x02
#     RARITY_VERY_RARE = 0x04
#     RARITY_LIST = [RARITY_COMMON, RARITY_RARE, RARITY_VERY_RARE]
#
#     name = models.CharField(max_length=128, verbose_name='名称')
#     # amount = models.IntegerField(null=True, verbose_name='数量')
#
#     level = models.SmallIntegerField(null=True, verbose_name='等级')
#     rarity = models.SmallIntegerField(choices=(
#         (RARITY_COMMON, '普通'),
#         (RARITY_RARE, '稀有'),
#         (RARITY_VERY_RARE, '非常稀有'),
#     ), default=RARITY_COMMON, verbose_name='稀有度')
#
#     item_type = models.ForeignKey(ItemType, null=True, verbose_name='道具类型', on_delete=models.DO_NOTHING)
#
#     class Meta:
#         verbose_name = '道具'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return f'{self.name}'


# class PassCodePublicManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().exclude(tags__hide=True)


class PassCode(TimeStampedModel):
    """PassCode Model"""
    code = models.CharField(max_length=128, verbose_name='pass code')
    message = models.CharField(max_length=512, verbose_name='信息')
    checked = models.BooleanField(default=False, verbose_name='已验证')

    tags = models.ManyToManyField(Tag)
    # items = models.ManyToManyField(Item)  # 这样不行 中间表还需要存道具数量

    objects = models.Manager()
    # public = PassCodePublicManager()

    class Meta:
        verbose_name = 'PassCode'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.code}'
