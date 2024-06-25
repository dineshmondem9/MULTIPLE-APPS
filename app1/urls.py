from django.urls import path
app_name='anything'
from app1.views import *

urlpatterns = [
    path('app11/',app11,name='app11'),
    path('app12/',app12,name='app12'),
    
]