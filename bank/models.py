from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    account_no = models.IntegerField()
    balance = models.IntegerField()  

class CustomerHistory(models.Model) :
    
    senders_name = models.CharField(max_length=50)
    receivers_name = models.CharField(max_length=50)
    amount = models.IntegerField()