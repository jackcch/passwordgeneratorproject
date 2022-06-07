import re
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword=''
    length=int(request.GET.get('passlength',10))
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('numbers'):
        characters.extend(list('01234567890'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDFGHHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'passfield':thepassword})


def aboutpage(request):
    return render(request, 'generator/about.html')
    