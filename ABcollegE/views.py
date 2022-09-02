from re import search
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import scholarship
from .models import postinternship
from .models import events
# Create your views here.
def home(request):
    return render(request,"home.htm")
def search(request):
    if request.method =='GET':
        search = request.GET['search']
        if search=='GALGOTIAS UNIVERSITY':
            return render(request,"galgotias.html")
        elif  search == 'sharda university':
            return HttpResponse('''
            <html>
            <title>Sharda University</title>
            <head><a href="https://www.sharda.ac.in/">link</head>
            </html>
            ''')

        
#about Us page
def about(request):
    return render(request,"aboutus.htm")

#Login Page
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate (username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials..')
            return redirect('index')
    else:
        return render(request,"index.html")

#Register page
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        #phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Already Exist..')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Address Already Exist..')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')
                return redirect('index')
        else:
            messages.info(request,'password Not Matching.')
            return redirect('register')
        return redirect('/') 

    else:
        return render(request,"register.htm")

#Scholarship Page
def internship(request):
    scholars = scholarship.objects.all()
    return render(request,"internship.htm",{'scholars':scholars})
    return render(request,"internship.htm")

#galgotias University Page
def galgotias(request):
    return render(request,"galgotias.html")

#logout Page
def logout(request):
    auth.logout(request)
    return redirect('/')

#Internship Page
def intern(request):
    dests = postinternship.objects.all()
    return render(request,"intern.html",{'dests':dests})

#Internship Form to Apply
def internform(request):
    return render(request,"internform.html")

#LMS Page
def lms(request):
    return render(request,"lms.html")

#Notes page
def notes(request):
    return render(request,"notes.html")

#Scholarship Form page to Apply
def scholarform(request):
    return render(request,"scholarform.html")

#After success of form fillup for Scholarship form
def successscholar1(request):
           if request.method=='POST':
             d=request.POST
             f=open("successscholar1.csv",'a')
             for k in d.keys():
                f.write(k)
                f.write(',')
                f.write(d[k])
                f.write(',,')
             f.write('\n')
             f.close()
             return render(request,"successscholar1.html")

#After success of form fillup for Internship form
def successintern1(request):
           if request.method=='POST':
             d=request.POST
             f=open("successinternship.csv",'a')
             for k in d.keys():
                f.write(k)
                f.write(',')
                f.write(d[k])
                f.write(',,')
             f.write('\n')
             f.close()
             return render(request,"successintern1.html")


#Events Page
def events(request):
    data = events.objects.all()
    return render(request,"events.html",{'data':data})