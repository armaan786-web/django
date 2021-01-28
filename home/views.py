from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
   
    return render(request,'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    return render(request,'about.html')
 

def sad(request):
    return render(request,'sad/sad.html')
 
def base(request):
    return render(request,'base.html')


def page2(request):
    return render(request,'sad/page2.html')

def page3(request):
    return render(request,'sad/page3.html')

def page4(request):
    return render(request,'sad/page4.html')


def romantic(request):
    return render(request,'romantic/romantic.html')

def rom_page2(request):
    return render(request,'romantic/rom_pg2.html')

def rom_page3(request):
    return render(request,'romantic/rom_pg3.html')

def rom_page4(request):
    return render(request,'romantic/rom_pg4.html')

def urdu(request): 
    return render(request,'urdu/urdu.html')

def urdu_pg2(request):
    return render(request,'urdu/urdu_pg2.html')

def girl(request):
    return render(request,'girl/girl_pg1.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        query = request.POST.get("query")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, query=query, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request,'contact.html')
