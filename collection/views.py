from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def auth(request):
    return render(request,'login.html')    
def log(request):
    return render(request,'logout.html')