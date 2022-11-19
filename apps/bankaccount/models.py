from django.db import models
from apps.account.models import User


class BankAccount(models.Model):
    number_account = models.IntegerField(verbose_name='Número da conta')
    balance = models.PositiveIntegerField(verbose_name='Saldo')
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    name_complete = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.account.email}'
