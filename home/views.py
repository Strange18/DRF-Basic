# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# class Home(APIView):

# Create Operation
# -----------------------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        testing = test.objects.all()
        serializer = TestSerializer(testing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# -----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# Update


@api_view(['GET', 'PUT'])
def update(request, pk):
    if request.method == 'GET':
        testing = test.objects.all()
        serializer = TestSerializer(testing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            testing = test.objects.get(id=pk)
        except test.DoesNotExist:
            return Response({'error': 'Test object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TestSerializer(testing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# DELETE


@api_view(['GET', 'DELETE'])
def delete(request, pk):
    if request.method == 'GET':
        testing = test.objects.all()
        serializer = TestSerializer(testing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        try:
            testing = test.objects.get(id=pk)
        except test.DoesNotExist:
            return Response({'error': 'Test object not found'}, status=status.HTTP_404_NOT_FOUND)
        testing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# -----------------------------------------------------------------------------------------------
# Read operation using API
# ------------------------------------------------------------------------------------------------


@api_view(['GET'])
def home(request):
    try:
        blog = Blog.objects.all().order_by('-publication_date')
        serialized_data = BlogSerializer(blog, many=True)
        print(serialized_data.data)
        return Response(serialized_data.data)
    except:
        return Response("No Current Entry")


@api_view(['GET'])
def each(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
        serialized_data = BlogSerializer(blog)
        print(serialized_data.data)
        return Response(serialized_data.data)
    except:
        return Response("No data found")

# -------------------------------------------------------------------------------------------------
