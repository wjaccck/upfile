from django.conf.urls import patterns, url
from api import views,signals
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'upfile', views.Up_fileViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'azure_key', views.Azure_keyViewSet)
router.register(r'dirs', views.DirsViewSet)
router.register(r'recode_list', views.Recode_dirsViewSet)


urlpatterns = router.urls
