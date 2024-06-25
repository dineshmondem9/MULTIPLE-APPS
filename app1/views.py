from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app11(request):
    return HttpResponse('This is My app-1 Function')
def app12(request):
    return render(request,'app1.html')
