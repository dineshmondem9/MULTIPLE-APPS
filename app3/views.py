from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app31(request):
    return HttpResponse('This is My Function in Application-3')

def app32(request):
    return render(request,'app3.html')