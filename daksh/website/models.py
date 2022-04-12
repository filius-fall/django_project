import datetime
from django.db import models


# Create your models here.

class Expenses(models.Model):
    expense = models.IntegerField()
    date = models.DateTimeField('date_added')

    def __str__(self):
        return self.expense
    

class ExpDetails(models.Model):
    expenses = models.ForeignKey(Expenses,on_delete=models.CASCADE)
    cause = models.TextField(max_length=400)
    pub_data = models.DateTimeField('pub_date')

    def __str__(self):
        return self.cause
    