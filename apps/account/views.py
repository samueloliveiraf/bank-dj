from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from apps.bankaccount.models import BankAccount
from apps.logs.models import LogTransfer


@login_required(login_url='/accounts/login/')
def home(request):
    conta = BankAccount.objects.get(account=request.user)
    context = {'conta': conta}
    return render(request, 'home.html', context)


@login_required(login_url='/accounts/login/')
def account_destiny(request):
    return render(request, 'account_destiny.html')


@login_required(login_url='/accounts/login/')
def find_account(request):
    number_account = request.POST.get('number_account')
    conta = BankAccount.objects.get(number_account=number_account)
    if conta:
        context = {'conta': conta}
        return render(request, 'find_account.html', context)
    return render(request, 'transfer.html')


@login_required(login_url='/accounts/login/')
def transfer(request, number_account):
    balance = request.POST.get('balance')
    conta_origem = BankAccount.objects.get(account=request.user)
    conta_destiny = BankAccount.objects.get(number_account=number_account)
    balance = int(balance)

    if 0 < balance <= conta_origem.balance:
        conta_origem.balance = conta_origem.balance - balance
        conta_origem.save()
        conta_destiny.balance = conta_destiny.balance + balance
        conta_destiny.save()

        log = LogTransfer(
            id_account=int(request.user.id),
            balance_transfer=balance,
            email_destinatary=request.user.email,
            account_destiny=conta_destiny.number_account,
            name_destinatary=conta_destiny.name_complete
        )
        log.save()

        if conta_destiny and conta_origem:
            context = {'success_or_error': 'Transferencia realizada!'}
            return render(request, 'success_or_error.html', context)

    context = {'success_or_error': 'Erro ao realiza transferencia'}
    return render(request, 'success_or_error.html', context)


@login_required(login_url='/accounts/login/')
def my_transfer(request):
    my_transfers = LogTransfer.objects.filter(id_account=request.user.id)
    context = {'my_transfers': my_transfers}
    return render(request, 'my_transfer.html', context)
