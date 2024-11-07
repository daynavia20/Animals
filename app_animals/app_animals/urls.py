from django.urls import path
from . import views

urlpatterns = [
    path('mensaje/', views.mensaje, name='mensaje'),
    path('lista_animal/', views.lista_animal, name='mostrar'),
    path('animal/<int:id>/', views.animal, name='animal'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>/', views.actualizar, name='actualizar')
]



