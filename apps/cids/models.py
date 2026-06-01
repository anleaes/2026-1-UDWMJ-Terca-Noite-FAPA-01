from django.db import models

# Create your models here.
 
class Cid(models.Model):
    name        = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')
 
    class Meta:
        verbose_name = 'CID'
        verbose_name_plural = 'CIDs'
        ordering = ['name']
 
    def __str__(self):
        return self.name
 