from django.utils import timezone

from rest_framework import serializers, mixins, viewsets

from .models import PassCode


class DateTimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        if value:
            value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)


class PassCodeSerializer(serializers.ModelSerializer):
    created = DateTimeTzAwareField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = PassCode
        exclude = ('modified',)


class PassCodeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PassCodeSerializer
    queryset = PassCode.objects.all()
