from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from cids.models import Cid
# Create your models here.

 
class Consult(models.Model):
    STATUS_CHOICES = [
        ('AG', 'Agendada'),
        ('AT', 'Em Atendimento'),
        ('CO', 'Concluída'),
        ('CA', 'Cancelada'),
    ]
    patient          = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente', related_name='consults')
    doctor           = models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name='Médico', related_name='consults')
    cid              = models.ManyToManyField(Cid, blank=True, verbose_name='CIDs')
    appointment_date = models.DateTimeField('Data/Hora da Consulta')
    anamnesis        = models.TextField('Anamnese', blank=True)
    status           = models.CharField('Status', max_length=2,choices=STATUS_CHOICES, default='AG')
 
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['-appointment_date']
 
    def __str__(self):
        return f'Consulta #{self.pk} — {self.patient} com {self.doctor}'
 