from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().order_by('-publication_date')
    serializer_class = BlogSerializer
