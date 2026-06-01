from django.db import models

# Create your models here.
 
class MedicalHistory(models.Model):
    allergies      = models.TextField('Alergias')
    family_history = models.TextField('Histórico Familiar')
    notes          = models.CharField('Notas', max_length=200)
 
    class Meta:
        verbose_name = 'Histórico Médico'
        verbose_name_plural = 'Históricos Médicos'
        ordering = ['id']
 
    def __str__(self):
        return f'Histórico #{self.pk}'