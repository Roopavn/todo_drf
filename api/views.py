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

    

#To create a new object for your model
#allows you to create a new object using a POST request.
class CandidatedirectoryCreateView(generics.CreateAPIView):
    queryset = Candidatedirectory.objects.all()
    serializer_class = CandidatedirectorySerializer  

    def create(self, request, *args, **kwargs):
            # Get the data from the request
            data = request.data

            # Validate the data using the serializer
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)

            # Check if an object with the same email or phone_number already exists in the database
            email = data.get('email')
            contact_no_primary = data.get('contact_no_primary')
            if Candidatedirectory.objects.filter(email=email).exists():
                return Response({'error': 'This email is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
            if Candidatedirectory.objects.filter(contact_no_primary=contact_no_primary).exists():
                return Response({'error': 'This phone number is already in use.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new object if data is valid and no duplicates exist
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CandidatedirectoryUpdateView(generics.UpdateAPIView):
    queryset = Candidatedirectory.objects.all()
    serializer_class = CandidatedirectorySerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the existing object
        old_data = CandidatedirectorySerializer(instance).data  # Serialize the existing object to get its data

        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'old_data': old_data, 'new_data': serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Once you've defined these views, 
# you need to wire them up to your URLs using Django's URL patterns.



