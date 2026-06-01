from django.db import models
from persons.models import Person
from medicalhistories.models import MedicalHistory
 # Create your models here.

class Patient(Person):
    allergies         = models.ForeignKey(MedicalHistory, null=True, blank=True,on_delete=models.SET_NULL,verbose_name='Alergias')
    emergency_contact = models.CharField('Contato de Emergência', max_length=200)
    health_insurance  = models.CharField('Convênio', max_length=100)
 
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']
 
    def __str__(self):
        return f'Paciente: {self.name}'
 