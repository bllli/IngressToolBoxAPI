from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tags', views.TagViewSet, base_name='tags')
router.register(r'codes', views.PassCodeViewSet, base_name='codes')

urlpatterns = [] + router.urls
