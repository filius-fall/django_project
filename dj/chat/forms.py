from django import forms

import datetime

class ExpensesForm(forms.Form):
    amount = forms.IntegerField()
    date = forms.DateField(initial=datetime.date.today)
    category = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)