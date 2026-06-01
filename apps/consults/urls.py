from django.urls import path
from . import views
 
app_name = 'consults'
 
urlpatterns = [
    path('listar/',                        views.list_consults,  name='list_consults'),
    path('adicionar/',                     views.add_consult,    name='add_consult'),
    path('editar/<int:id_consult>/',       views.edit_consult,   name='edit_consult'),
    path('excluir/<int:id_consult>/',      views.delete_consult, name='delete_consult'),
]