from django import forms
from .models import Transaction

# class TransactionForm(forms.Form):
#     type = forms.ChoiceField(label="Type", choices=[('Debit', 'debit'), ('Credit','credit')])
#     amount = forms.IntegerField(label="amount")

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount']
        labels = {'type':'Type', 'amount':'Amount'}
        CHOICES = (('Debit', 'debit'), ('Credit', 'credit'),)
        widgets = {'type':forms.Select(choices=CHOICES)}