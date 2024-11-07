from django.urls import path
from . import views

urlpatterns = [
    path('ejemplo/', views.mi_vista, name='mi_vista'),
    # path('mensaje/', views.mensajes, name='mensajes'),
    path('ver_mensajes/', views.ver_mensajes, name='ver_mensajes'),
    path('mensaje-actualizado/', views.mensaje_actualizado, name='mensaje_actualizado'),
    path('crear-mensaje/', views.crear_mensaje, name='crear_mensaje'),
]
