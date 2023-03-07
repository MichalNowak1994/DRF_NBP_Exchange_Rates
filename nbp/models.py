from django.db import models


class ExchangeRate(models.Model):
    date = models.DateField()
    currency = models.CharField(max_length=200)
    code = models.CharField(max_length=3)
    mid = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        unique_together = ('date', 'currency', 'code', 'mid')
