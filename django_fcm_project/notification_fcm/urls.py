from django.urls import path, include
from django.conf.urls import url

from . import views
from fcm_django.api.rest_framework import FCMDeviceViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    url(r'^docs/', include_docs_urls(title='FCM django web demo')),
    url(r'^', include(router.urls)),
]
