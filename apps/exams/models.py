from django.db import models
from consults.models import Consult
# Create your models here.

class Exam(models.Model):
    STATUS_CHOICES = [
        ('SO', 'Solicitado'),
        ('AT', 'Em Andamento'),
        ('CO', 'Concluído'),
        ('CA', 'Cancelado'),
    ]
    consult      = models.ForeignKey(Consult, on_delete=models.CASCADE,
                                      verbose_name='Consulta', related_name='exams')
    exam_type    = models.CharField('Tipo de Exame', max_length=200)
    status       = models.CharField('Status', max_length=2,
                                     choices=STATUS_CHOICES, default='SO')
    request_date = models.DateField('Data de Solicitação', auto_now_add=True)
 
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
        ordering = ['-request_date']
 
    def __str__(self):
        return f'{self.exam_type} ({self.get_status_display()})'
 