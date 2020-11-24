from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'pass123'})

def password(request):
    return render(request, 'generator/password.html', {'password':'pass123'})
    