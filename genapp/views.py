from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    #return HttpResponse("<h1>we did that</h1>")
    return render(request,'genapp/home.html')

def eggs(request):
    return HttpResponse("<h1> eggs are oval hi hi </h1>")


def ani(request):
    #return HttpResponse("<h2> hii therere olaaf its ani !! </h2>")
    return render(request,'genapp/ani.html',{'password':'^n!password'})

def password(request):
    return render(request,'genapp/pass.html')

def about(request):
    return render(request,'genapp/about.html')
    

def anspass(request):
    
    characters = [chr(i) for i in range(97,123)]
    length = int(request.GET.get('length',10))

    upper = [chr(i) for i in range(65,91)]

    if request.GET.get('uppercase'):
        characters.extend(upper)
    if request.GET.get('numbers'):
        characters.extend(list('123567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+~'))
    

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)


    return render(request,'genapp/password.html',{'password':thepassword})