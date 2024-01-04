from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction
# Create your views here.
def home(request):
    form = TransactionForm(data=request.POST or None) # retrieve transaction form
    # checks if request method == POST
    if request.method == 'POST':
        pk = request.POST['account'] # if form is submitted, retrieve which account user wants to view
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

def create_account(request):
    form = AccountForm(data=request.POST or None) # retrieve the account form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # check to see if the submitted form is valid and if so, save form
            form.save() # saves the new account
            return render(request, 'checkbook/CreateNewAccount.html') # returns back to homepage
    content = {'form':form} # saves content to the template as a dictionary
    # adds content fo form to page
    return redirect('index') # returns back to homepage

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve requested account using Primary Key
    transactions = Transaction.Transactions.filter(account=pk) # retrieve all account's transactions
    current_total = account.initial_deposit # create account total variable, starting with initial deposit value
    table_contents = {} # creates dictionary into which transaction information will be placed
    for t in transactions: # loop thru transactions and determine which is deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount # if deposit add amount to balance
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
        else:
            current_total -= t.amount # if withdrawal subtract amount from balance
            table_contents.update({t: current_total}) # add transaction and total to dictionary
    #pass account, account total and transaction info to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

def transaction(request):
    form = TransactionForm(data=request.POST or None) # retrieve transaction form
    # checks if request method is post
    if request.method == 'POST':
        if form.is_valid(): #checks to see if submitted form is valid and if so save form
            pk = request.POST['account'] # retrieve which account transaction was for
            form.save() # saves transaction
            return balance(request, pk) # renders balance of accounts balance sheet
    content={'form':form}
    return render(request, 'checkbook/AddTransaction.html', content)
