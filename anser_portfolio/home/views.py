from django.shortcuts import render
from home.models import Clients
from .forms import Client_message
# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = Client_message(request.POST)
        if fm.is_valid():
            nam = fm.cleaned_data['name']
            emal = fm.cleaned_data['email']
            mesag = fm.cleaned_data['message']
            insert = Clients(c_name=nam,c_email = emal,c_message=mesag)
            insert.save()
            return render(request,'home/msgsent.html')
            
    else:
        print('this was get request')
        fm = Client_message(auto_id = 'client_%s')

    return render(request,"home/index.html",{'clientform':fm})


def manager(request):
    client = Clients.objects.all()
    # print('my output',client)
    return render(request,'home/managers.html',{'cli': client})