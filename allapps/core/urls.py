from django.urls import path, include
from . import views, viewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', viewsets.TodoViewset)
router.register('users', viewsets.UserViewset)

# 'basename' required when queryset is replaced with get_queryset() in viewsets.py
# router.register('users', viewsets.UserViewset, basename='user')

# app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/todos/', include(router.urls)),
]
