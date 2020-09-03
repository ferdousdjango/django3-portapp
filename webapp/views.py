from django.shortcuts import render
import random

def webapp(request):
    return render(request,'webapp/webhome.html')

def password_generator(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''
    length = int(request.GET.get('length',10))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('£$%%^&*&*_'))
    
    for x in range(length):
        thepassword +=random.choice(characters)

    return render(request,'webapp/password.html',{'password':thepassword})
    