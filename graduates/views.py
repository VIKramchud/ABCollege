from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,"first.htm",{'university':'Shivam'})
def login(request):
    return render(request,"login.htm")
def second(request):
    return render(request,"second.htm")
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res = val1+val2
    return render(request,"result.htm",{'result':res})
def about(request):
    return render(request,"aboutus.htm")
