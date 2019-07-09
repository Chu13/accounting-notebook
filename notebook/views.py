from django.shortcuts import render
from notebook.models import Transaction
from .forms import TransactionForm

def history(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'history.html', context)

def transaction(request):
    if request.method == 'POST':
        filled_form = TransactionForm(request.POST)
        if filled_form.is_valid():
            created_transaction = filled_form.save()
            created_transaction_pk = created_transaction.id
            note = 'Your %s Transaction for %s has been sent!' %(filled_form.cleaned_data['type'],
            filled_form.cleaned_data['amount'])
            filled_form = TransactionForm()
        else:
            created_transaction_pk = None
            note = 'Transaction has failed. Please try again'
        return render(request, 'transaction.html', {'transactionform': filled_form, 'note': note})
    else:
        form = TransactionForm()
        return render(request, 'transaction.html', {'transactionform': form})

# def detail(reques, pk):
#     transaction = Transaction.objects.get(pk=pk)