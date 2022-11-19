from django.db import models


class LogTransfer(models.Model):
    id_account = models.IntegerField(verbose_name='Id Identificação')
    balance_transfer = models.PositiveIntegerField(verbose_name='Saldo Transferido')
    account_destiny = models.IntegerField(verbose_name='Conta transferida')
    name_destinatary = models.CharField(verbose_name='Nome destinatário', max_length=250)
    email_destinatary = models.EmailField(verbose_name='Email destinatário', max_length=250)

    def __str__(self):
        return f'{self.id_account}'
