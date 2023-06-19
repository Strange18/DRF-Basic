from rest_framework.serializers import ModelSerializer
from .models import *


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'

class TestSerializer(ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'
