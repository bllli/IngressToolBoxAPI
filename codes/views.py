from rest_framework import serializers, mixins, viewsets

from .models import PassCode
from .serializers import PassCodeSerializer


class PassCodeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PassCodeSerializer
    queryset = PassCode.objects.all()
