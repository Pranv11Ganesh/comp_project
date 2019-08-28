from django.shortcuts import render
import csv
from BookTicket.models import Account
import os

# Create your views here.
def seehome(request):
    return render(request,'Home_Page.html')
def seelogin(request):
    return render(request,'Login.html')
def seepnr(request):
    return render(request,'PNR status.html')
def seesearch(request):
    return render(request,'Search.html')
def seereg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['password']
        repwd=request.POST['repassword']
        age=request.POST['age']
        with open('data.csv','a') as file:
            wcs=csv.writer(file)
            wcs.writerow(["name",name])
            wcs.writerow(["email",email])
            wcs.writerow(["pwd",pwd])
            wcs.writerow(["repwd",repwd])
            wcs.writerow(["age",age])
        lst=Account()
        lst.aname=name
        lst.aemail=email
        lst.apwd=pwd
        lst.aage=age
        lst.save()
        a_list=Account.objects.all()
        return render(request,'Registered_Home.html',{'al':a_list}) 
        print(al)
    else:
        return render(request,'Register.html')