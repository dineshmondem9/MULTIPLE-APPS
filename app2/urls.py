from django.urls import path
from app2.views import *
app_name='anything'
urlpatterns = [
    path('app21/',app21,name='app21'),
    path('app22/',app22,name='app22'),
]