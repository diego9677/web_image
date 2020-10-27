from django.db import models


class Prevision(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(upload_to='prevision', verbose_name='Imagen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'previsión'
        verbose_name_plural = 'previsión'


class Futuro(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(upload_to='futuro', verbose_name='Imagen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'futuro'
        verbose_name_plural = 'futuro'
