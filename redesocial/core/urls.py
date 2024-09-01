from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postagem/<int:id>/', views.post_detail, name='post_detail'),
    path('perfil/<int:id>/', views.perfil_detail, name='perfil_detail'),
]
