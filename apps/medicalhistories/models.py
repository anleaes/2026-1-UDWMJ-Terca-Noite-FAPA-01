from django.db import models

# Create your models here.
 
class MedicalHistory(models.Model):
    allergies      = models.TextField('Alergias')
    family_history = models.TextField('Histórico Familiar')
    patient_name   = models.CharField('Nome do Paciente', max_length=200)

    class Meta:
        verbose_name = 'Histórico Médico'
        verbose_name_plural = 'Históricos Médicos'
        ordering = ['id']

    def __str__(self):
        return self.patient_name if self.patient_name else f'Histórico #{self.pk}'