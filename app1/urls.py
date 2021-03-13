  
from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet



router = routers.DefaultRouter()
router.register("customer", CustomerViewSet)
urlpatterns =[
    
]+ router.urls