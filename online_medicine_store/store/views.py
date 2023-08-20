from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')
def buy(request):
    return render(request,'buy.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def medicine(request):
    return render(request,'medicine.html')
def news(request):
    return render(request,'news.html')