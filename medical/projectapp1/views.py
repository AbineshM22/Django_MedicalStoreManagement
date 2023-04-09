

# Create your views here.
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import MedicalstoreForm
from .models import Medicalstore

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def Home(request):
    form=MedicalstoreForm()
    if request.method=='POST':
        form=MedicalstoreForm(request.POST)
        form.save()
        form=MedicalstoreForm()
    
    data=Medicalstore.objects.all()

    


    context={
        'form':form,
        'data':data,
    }
    return render(request,'index.html',context)

# Delete View
@login_required(login_url='login')
def Delete_record(request,id):
    a=Medicalstore.objects.get(pk=id)
    a.delete()
    return redirect("homepage")
    

# Update View

@login_required(login_url='/login/')
def Update_Record(request,id):
    data=Medicalstore.objects.get(id=id)
    form=MedicalstoreForm(instance=data)

    if request.method=='POST':
        form=MedicalstoreForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context={
        'form':form
    }
    return render(request,'update.html',context)

from .models import *
@login_required(login_url='login')
def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Medicalstore.objects.filter(Medicine__contains=query_name)
            return render(request, 'search.html', {"results":results})

    return render(request, 'search.html')



    