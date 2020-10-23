from django.shortcuts import render
from portapp.models import Port
from django.core.mail import send_mail

def home(request):
    port= Port.objects.all()
    return render(request,'portapp/home.html',{'port':port})
def project_list(request):
    return render(request,'portapp/myprojects.html')
#contact area start
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #send an email
        send_mail(
            message_name,#subject
            message,#message
        
            
            message_email,#from email
            ['helloferdous@gmail.com'],#to email
        )

        return render(request,'portapp/contact.html',{'message_name':message_name})
    else:
        return render(request,'portapp/contact.html',{})