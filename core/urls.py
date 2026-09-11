from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('contacto/', views.contacto, name='contacto'),
    path('proyecto/<slug:slug>/', views.detalle_proyecto, name='detalle_proyecto')
]