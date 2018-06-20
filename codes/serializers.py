from django.utils import timezone
from rest_framework import serializers

from .models import PassCode, Tag


class DateTimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        if value:
            value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        # fields = '__all__'
        exclude = ('hide',)


class PassCodeSerializer(serializers.ModelSerializer):
    created = DateTimeTzAwareField(format='%Y-%m-%d %H:%M')
    tags = TagSerializer(many=True)

    class Meta:
        model = PassCode
        exclude = ('modified',)
