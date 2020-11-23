# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from users import views as user_views

router = DefaultRouter() # P/ generar path automaticos
router.register(r'users', user_views.UserViewSet, basename='users')

# Incluyendo todas las rutas del router
urlpatterns = [
    path('', include(router.urls))
]