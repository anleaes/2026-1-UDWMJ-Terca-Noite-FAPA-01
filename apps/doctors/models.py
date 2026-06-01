from django.db import models
from persons.models import Person
 # Create your models here.

class Doctor(Person):
    crm       = models.CharField('CRM', max_length=20, unique=True)
    specialty = models.CharField('Especialidade', max_length=100)
 
    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['name']
 
    def __str__(self):
        return f'Dr(a). {self.name} — {self.specialty}'
 