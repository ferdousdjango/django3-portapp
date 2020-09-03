from django.shortcuts import render
from portapp.models import Port

def home(request):
    port= Port.objects.all()
    return render(request,'portapp/home.html',{'port':port})
def project_list(request):
    return render(request,'portapp/myprojects.html')