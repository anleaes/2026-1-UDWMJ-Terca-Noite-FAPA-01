from django.db import models

# Create your models here. 
class Person(models.Model):
    SEX_CHOICES = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')]
    name       = models.CharField('Nome', max_length=200)
    cpf        = models.CharField('CPF', max_length=14, unique=True)
    birth_date = models.DateField('Data de Nascimento')
    email      = models.EmailField('E-mail')
    sex        = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
 
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['name']
 
    def __str__(self):
        return self.name