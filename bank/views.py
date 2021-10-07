from django.contrib  import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from bank.models import CustomerHistory, Data

# Create your views here.
def index(request):
    return render(request, 'index.html')

def customers(request):
    datas = Data.objects.all()
    return render(request, 'customers.html', {'datas': datas})

def payments(request):
    
     return render(request, 'make_payments.html')

def history(request):

    if request.method == 'POST':

        senders_name = request.POST['sender']
        receivers_name = request.POST['receiver']

        amount = request.POST['amount']
        amount = int(amount)

        payment_data = Data.objects.all()

        for dp in payment_data:
            if dp.name == senders_name:
                for dp2 in payment_data:
                    if dp2.name == receivers_name:
                     
                        if (dp.balance - amount >= 0):
                            new_bal = dp.balance - amount

                            h = CustomerHistory(senders_name=senders_name, receivers_name=receivers_name, amount=amount)

                            a = Data.objects.get(id = dp.id)
                            a.balance = new_bal
                            a.save()

                            a2 = Data.objects.get(id = dp2.id )
                            new_bal2 = a2.balance + amount
                            a2.balance = new_bal2
                            a2.save()

                            h.save()

                            messages.success(request, "transaction succesful....!")
                            return redirect('/payments')

                        else:
                            messages.error(request, "balance is low")
                            return redirect('/payments') 

                messages.error(request, "name not found")
                return redirect('/payments') 

        messages.error(request, "name not found")
        return redirect('/payments')  


    else:
        history_data = CustomerHistory.objects.all()
        return render(request, 'history.html', {'history_data': history_data})

