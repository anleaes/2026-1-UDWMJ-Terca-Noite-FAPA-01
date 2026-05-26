from django.urls import path
from . import views

app_name = 'medication'

urlpatterns = [
    path('adicionar/', views.add_medication, name='add_medication'),
    path('listar/', views.list_medication, name='list_medication'),
    path('editar/<int:id_medication>/', views.edit_medication, name='edit_medication'),
    path('excluir/<int:id_medication>/', views.delete_medication, name='delete_medication'),
]