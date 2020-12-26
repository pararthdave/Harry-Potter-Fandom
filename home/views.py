from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Pb1
from home.models import Pb2
from home.models import Pb3
from home.models import Pb4
from home.models import Pb5
from home.models import Pb6
from home.models import Pb7
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")
    #return HttpResponse("This is Home page")

def about(request):
     return render(request, "about.html")

def books(request):
     return render(request, "books.html")

def ff(request):
     return render(request,"ff.html")


def contact(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          subject=request.POST.get('subject')
          message=request.POST.get('message')
          contact= Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
          contact.save()
          messages.success(request, 'Message has been sent.')
     return render(request, "contact.html")

def pb1(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb1= Pb1(name=name, email=email, remarks=remarks, date=datetime.today())
          pb1.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb1.html")

def pb2(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb2= Pb2(name=name, email=email, remarks=remarks, date=datetime.today())
          pb2.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb2.html")

def pb3(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb3= Pb3(name=name, email=email, remarks=remarks, date=datetime.today())
          pb3.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb3.html")

def pb4(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb4= Pb4(name=name, email=email, remarks=remarks, date=datetime.today())
          pb4.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb4.html")

def pb5(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb5= Pb5(name=name, email=email, remarks=remarks, date=datetime.today())
          pb5.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb5.html")

def pb6(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb6= Pb6(name=name, email=email, remarks=remarks, date=datetime.today())
          pb6.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb6.html")

def pb7(request):
     if request.method == "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          remarks=request.POST.get('remarks')
          pb7= Pb7(name=name, email=email, remarks=remarks, date=datetime.today())
          pb7.save()
          messages.success(request, 'Message has been sent. Our team will get back to you within 2 working days.')
     return render(request, "pb7.html")