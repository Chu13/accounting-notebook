from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
    effectiveDate = models.DateTimeField(default=timezone.now)