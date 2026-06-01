from django.urls import path
from . import views
 
app_name = 'medicalhistories'
 
urlpatterns = [
    path('listar/',                                  views.list_medicalhistories,  name='list_medicalhistories'),
    path('adicionar/',                               views.add_medicalhistory,     name='add_medicalhistory'),
    path('editar/<int:id_medicalhistory>/',          views.edit_medicalhistory,    name='edit_medicalhistory'),
    path('excluir/<int:id_medicalhistory>/',         views.delete_medicalhistory,  name='delete_medicalhistory'),
]