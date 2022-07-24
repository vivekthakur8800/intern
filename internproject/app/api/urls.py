from django.urls import path,include
from app.api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',views.apiview,basename='api')
urlpatterns=[
    path('',include(router.urls)),
]