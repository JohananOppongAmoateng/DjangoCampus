from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from core.serializers import (
    WorkShopSerializer,
    WorkshopRegistrationSerializer,
    WorkShopListSerializer
)
from core.models import WorkShop, WorkshopRegistration

# Create your views here.


class WorkshopListView(generics.ListAPIView):
    """
    API view to retrieve list of all workshops.
    """
    queryset = WorkShop.objects.all()
    serializer_class = WorkShopListSerializer


class WorkshopDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single workshop by ID.
    """
    queryset = WorkShop.objects.all()
    serializer_class = WorkShopSerializer


class WorkshopCreateView(generics.CreateAPIView):
    """
    API view to create a new workshop.
    """
    queryset = WorkShop.objects.all()
    serializer_class = WorkShopSerializer


class WorkshopRegistrationCreateView(generics.CreateAPIView):
    """
    API view to register for a workshop.
    """
    queryset = WorkshopRegistration.objects.all()
    serializer_class = WorkshopRegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if user is already registered for this workshop
            workshop_id = serializer.validated_data.get('workshop').id
            user_email = serializer.validated_data.get('user_email')
            
            if WorkshopRegistration.objects.filter(
                workshop_id=workshop_id,
                user_email=user_email
            ).exists():
                return Response(
                    {'error': 'You are already registered for this workshop.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkshopRegistrationListView(generics.ListAPIView):
    """
    API view to retrieve list of all workshop registrations.
    """
    queryset = WorkshopRegistration.objects.all()
    serializer_class = WorkshopRegistrationSerializer


class WorkshopRegistrationDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single workshop registration by ID.
    """
    queryset = WorkshopRegistration.objects.all()
    serializer_class = WorkshopRegistrationSerializer


class WorkshopRegistrationsForWorkshopView(generics.ListAPIView):
    """
    API view to retrieve all registrations for a specific workshop.
    """
    serializer_class = WorkshopRegistrationSerializer
    
    def get_queryset(self):
        workshop_id = self.kwargs['workshop_id']
        return WorkshopRegistration.objects.filter(workshop_id=workshop_id)

