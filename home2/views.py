from django.shortcuts import render
from .models import Animal
from rest_framework import generics, mixins
from .serializers import *

# Create your views here.

# here we will be using class based view for performing the CRUD operations


# -----------------------------------------------------------------------------------------------------
# Use of mixins and generics for CRUD operation
# better and faster than FBV

class Crud(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CrudDetail(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# -----------------------------------------------------------------------------------------------------

class SimpletList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class SimpleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


# -----------------------------------------------------------------------------------------------------
