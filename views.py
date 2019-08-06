from django.shortcuts import render

# Create your views here.
def seehome(request):
    return render(request,'Home_Page.html')
def seelogin(request):
    return render(request,'Login.html')
def seepnr(request):
    return render(request,'PNR status.html')
def seesearch(request):
    return render(request,'Search.html')