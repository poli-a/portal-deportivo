# Django
from django.urls import path, include

# Views
from competiciones.views import *

urlpatterns = [
    path('competiciones/', competicion_api_view, name = 'competicion'),
    path('competiciones/<int:pk>/', competicion_detail_api_view, name = 'competicion'),
    path('fixtures/', fixture_api_view, name = 'fixture'),
    path('fixtures/<int:pk>/', fixture_detail_api_view, name = 'fixture'),
    path('tabla-posiciones/', tabla_posiciones_api_view, name = 'tabla posiciones'),
    path('tabla-posiciones/<int:pk>/', tabla_posiciones_detail_api_view, name = 'tabla posiciones')
]