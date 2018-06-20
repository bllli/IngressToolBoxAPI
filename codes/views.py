from rest_framework import serializers, mixins, viewsets

from .models import PassCode, Tag
from .serializers import PassCodeSerializer, TagContentSerializer


class PassCodeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PassCodeSerializer
    queryset = PassCode.objects.all()


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    serializer_class = TagContentSerializer
    queryset = Tag.objects.all()

