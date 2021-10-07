from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('customers', views.customers, name='customers'),
    path('history', views.history, name='history'),
    path('payments', views.payments, name='payments')

]