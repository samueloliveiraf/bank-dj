from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from apps.account.views import home

from apps.account import urls as urls_accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts-banck/', include(urls_accounts)),

    path('', home, name='home')
]
