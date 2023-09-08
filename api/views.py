from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.views import exception_handler

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CandidatedirectorySerializer

from .models import Candidatedirectory

# Django REST framework API view that 
# provides an overview of the available API endpoints 
# and their corresponding URLs. 

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/candidatedirectory-list/',
		'Detail View':'/candidatedirectory-detail/<str:pk>/',
		'Create':'/candidatedirectory-create/',
		'Update':'/candidatedirectory-update/<str:pk>/',
		'Delete':'/candidatedirectory-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def custom_exception_handling_view(request):
    try:
        # Your code that may raise exceptions
        result = perform_some_operation()
        return Response({'result': result})
    except SomeCustomException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#To retrieve a list of objects from your model
# This view allows you to retrieve a list of objects using a GET request.
class CandidatedirectoryListView(generics.ListCreateAPIView):
    queryset = Candidatedirectory.objects.all()
    serializer_class = CandidatedirectorySerializer  

#To retrieve, update, or delete a single object from your model
#This view supports GET (retrieve), PUT (update), PATCH (partial update), and DELETE (delete) requests for a single object.
class CandidatedirectoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidatedirectory.objects.all()
    serializer_class = CandidatedirectorySerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except SomeCustomException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#To create a new object for your model
#allows you to create a new object using a POST request.
class CandidatedirectoryCreateView(generics.CreateAPIView):
    queryset = Candidatedirectory.objects.all()
    serializer_class = CandidatedirectorySerializer  


#Once you've defined these views, 
# you need to wire them up to your URLs using Django's URL patterns.



