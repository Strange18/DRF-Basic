from django.urls import path, include
from .views import *
from rest_framework import routers
from .viewsets import *

routers = routers.DefaultRouter()
routers.register('author', AuthorViewSet)
routers.register('category', CategoryViewSet)
routers.register('blog', BlogViewSet)


urlpatterns = [
    # path('',home),
    # path('<int:pk>/',each),
    # path('create/',create),
    # path('update/<int:pk>/',update),
    # path('delete/<int:pk>/',delete),
    path('', include(routers.urls))
]
