from django.urls import path
from .views import account_destiny, find_account, transfer, my_transfer


urlpatterns = [
    path('account-destiny/', account_destiny, name='account_destiny'),
    path('find-account/', find_account, name='find_account'),
    path('transfer-account/<int:number_account>/', transfer, name='transfer'),
    path('my-transfers/', my_transfer, name='my_transfer')
]
