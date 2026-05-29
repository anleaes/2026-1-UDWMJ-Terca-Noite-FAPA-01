from django.urls import path
from . import views

app_name = 'cids'

urlpatterns = [
    path('adicionar/', views.add_cid, name='add_cid'),
    path('listar/', views.list_cids, name='list_cids'),
    path('editar/<int:id_cid>/', views.edit_cid, name='edit_cid'),
    path('excluir/<int:id_cid>/', views.delete_cid, name='delete_cid'),
]