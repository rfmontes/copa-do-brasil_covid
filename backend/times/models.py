from django.db import models

class Base(models.Model):
    votos = models.IntegerField('Votos', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)


class Time(Base):
    nome_time = models.CharField('Time', max_length=200)

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'
        ordering = ['id']

    def __str__(self):
        return self.nome_time


