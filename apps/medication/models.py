from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.name}'