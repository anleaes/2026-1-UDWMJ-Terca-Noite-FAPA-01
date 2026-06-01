from django.db import models
from consults.models import Consult
from patients.models import Patient
from doctors.models import Doctor
# Create your models here.

class Prescription(models.Model):
    consult      = models.ForeignKey(Consult, on_delete=models.CASCADE,verbose_name='Consulta', related_name='prescriptions')
    patient      = models.ForeignKey(Patient, on_delete=models.CASCADE,verbose_name='Paciente', related_name='prescriptions')
    doctor       = models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name='Médico', related_name='prescriptions')
    issue_date   = models.DateField('Data de Emissão', auto_now_add=True)
    instructions = models.TextField('Instruções', blank=True)
 
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-issue_date']
 
    def __str__(self):
        return f'Receita #{self.pk} — {self.patient}'
 