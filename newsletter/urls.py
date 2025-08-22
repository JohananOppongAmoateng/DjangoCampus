from django.urls import path
from .views import NewsletterSubscriberListCreateView, NewsletterSubscriberDetailView

app_name = 'newsletter'

urlpatterns = [
    path('api/subscribers/', NewsletterSubscriberListCreateView.as_view(), name='subscriber-list'),
    path('api/subscribers/<int:pk>/', NewsletterSubscriberDetailView.as_view(), name='subscriber-detail'),
]