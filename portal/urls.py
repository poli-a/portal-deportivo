# Django
from django.urls import path, include

# Django REST Framework
from rest_framework import routers

# Views
from portal import views as portal_views

router = routers.DefaultRouter() # P/ generar path automaticos
router.register(r'noticias', portal_views.NoticiaViewset, basename='noticias')

urlpatterns = [
    path('', include(router.urls))   
]