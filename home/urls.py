
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home),
    path('<int:pk>/',each),
    path('create/',create),
    path('update/<int:pk>/',update),
    path('delete/<int:pk>/',delete),


]