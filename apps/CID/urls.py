from django.urls import path
from . import views

app_name = 'CID'

urlpatterns = [
    path('adicionar/', views.add_CID, name='add_CID'),
    path('listar/', views.list_CID, name='list_CID'),
    path('editar/<int:id_CID>/', views.edit_CID, name='edit_CID'),
    path('excluir/<int:id_CID>/', views.delete_CID, name='delete_CID'),
]