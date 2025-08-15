from django.urls import path
from . import views

urlpatterns = [
    # Workshop API endpoints
    path('api/workshops/',
         views.WorkshopListView.as_view(),
         name='workshop-list'),
    path('api/workshops/<int:pk>/',
         views.WorkshopDetailView.as_view(),
         name='workshop-detail'),
    path('api/workshops/create/',
         views.WorkshopCreateView.as_view(),
         name='workshop-create'),

    # Workshop Registration API endpoints
    path('api/registrations/',
         views.WorkshopRegistrationListView.as_view(),
         name='registration-list'),
    path('api/registrations/create/',
         views.WorkshopRegistrationCreateView.as_view(),
         name='register-workshop'),
    path('api/registrations/<int:pk>/',
         views.WorkshopRegistrationDetailView.as_view(),
         name='registration-detail'),
    path('api/workshops/<int:workshop_id>/registrations/',
         views.WorkshopRegistrationsForWorkshopView.as_view(),
         name='workshop-registrations'),
]
