from django.shortcuts import render
from django.shortcuts import HttpResponse
def home(request):
    # return HttpResponse('yes it is home')
    return render(request,'home.html')
def about(request):
    # return HttpResponse('we are goood')
    return render(request,'about.html')
