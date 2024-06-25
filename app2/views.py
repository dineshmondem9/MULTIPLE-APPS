from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app21(request):
    return HttpResponse('<h1>This my function in application-2</h1>')
def app22(request):
    return render(request,'app2.html')
