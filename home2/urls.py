from django.urls import path
from .views import *

urlpatterns = [

    path('', Crud.as_view()),
    path('detail/<int:pk>', CrudDetail.as_view()),
    path('simple', SimpletList.as_view()),
    path('simple/<int:pk>', SimpleDetail.as_view()),
]
