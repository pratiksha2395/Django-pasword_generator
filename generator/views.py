from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html', {'password':'dhdhscjhd'})

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if(request.GET.get('sprecial_char')):
        characters.extend(list('!@#$%^&*'))
    if(request.GET.get('numbers')):
        characters.extend(list('1234567890'))

    thepass=''
    for i in range(0,length):
        thepass += random.choice(characters)
    return render(request,'generator/password.html', {'password':thepass})

def about(request):
    return render(request, 'generator/about.html')
