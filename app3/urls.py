from django.urls import path
from app3.views import *
app_name='anything'
urlpatterns=[
    path('app31/',app31,name='app31'),
    path('app32/',app32,name='app32'),
]
