from django.db import models

# Create your models here.
class Medication(models.Model):
    medication = models.CharField('Medicamento', max_length=200)
    brand      = models.CharField('Marca', max_length=200)
 
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['medication']
 
    def __str__(self):
        return self.medication
