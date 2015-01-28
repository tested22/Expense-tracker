from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=65, decimal_places=2)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='expenses')


