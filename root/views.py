from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'root/index.html')

def service_detail(request):
    return render(request,'root/service-details.html')

def protfolio_detail(request):
    return render(request,'root/portfolio-details.html')