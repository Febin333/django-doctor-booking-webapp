from django.shortcuts import render
from .models import Department,Doctors
from .forms import Bookingform
# Create your views here.
def index(request):
    dep_list=Department.objects.all()
    return render(request,'index.html',{'dep':dep_list})
def doctors(request):
    doc_list=Doctors.objects.all()
    return render(request,'doctors.html',{'doctors':doc_list})
def booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form=Bookingform
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
