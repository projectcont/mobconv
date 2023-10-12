from django.db import models
from django.urls import reverse
from django.db import models

# ----valuta------------------

class Valuta (models.Model):

    time_create = models.DateTimeField(verbose_name='Создано')
    time_write = models.DateTimeField(auto_now=True, verbose_name='Добавлено')
    usd = models.DecimalField (max_digits=60, decimal_places=10,  blank=False, verbose_name='Курс USD к рублю')
    eur = models.DecimalField(max_digits=60, decimal_places=10, blank=False, verbose_name='Курс EUR к рублю')

    def get_absolute_url (self):
        return reverse('/kurs/0',kwargs={'day':0})

    def __str__(self):
        return  f"Курс USD={self.usd} Курс EUR={self.eur}"

    class Meta:
        verbose_name='Курс валют '
        verbose_name_plural= 'Курсы валют'
        ordering=['time_create']




