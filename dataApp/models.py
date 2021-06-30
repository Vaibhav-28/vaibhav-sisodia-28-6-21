from django.db import models


class Ticker(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    date = models.CharField(max_length=20)
    open_val = models.DecimalField(decimal_places=2, max_digits=100)
    high_val = models.DecimalField(decimal_places=2, max_digits=100)
    low_val = models.DecimalField(decimal_places=2, max_digits=100)
    close_val = models.DecimalField(decimal_places=2, max_digits=100)
