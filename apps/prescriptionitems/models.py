from django.db import models
from prescriptions.models import Prescription
from medications.models import Medication

# Create your models here.
 
class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE,
                                      verbose_name='Receita', related_name='items')
    medication   = models.ForeignKey(Medication, on_delete=models.CASCADE,
                                      verbose_name='Medicamento')
    quantity     = models.CharField('Quantidade', max_length=50)
    dosage       = models.CharField('Dosagem', max_length=100)
    frequency    = models.CharField('Frequência', max_length=100)
    duration     = models.CharField('Duração', max_length=100)
 
    class Meta:
        verbose_name = 'Item de Receita'
        verbose_name_plural = 'Itens de Receita'
 
    def __str__(self):
        return f'{self.medication} — {self.dosage}'