from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import NewsletterSubscriber
from .serializers import NewsletterSubscriberSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Subscribe to newsletter",
        description="Subscribe to the newsletter with email and optional name",
        tags=["Newsletter"]
    ),
    get=extend_schema(
        summary="List all subscribers",
        description="Get a list of all newsletter subscribers",
        tags=["Newsletter"]
    )
)
class NewsletterSubscriberListCreateView(generics.ListCreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Get subscriber details",
        description="Retrieve details for a specific newsletter subscriber",
        tags=["Newsletter"]
    ),
    delete=extend_schema(
        summary="Unsubscribe from newsletter",
        description="Remove a subscriber from the newsletter list",
        tags=["Newsletter"]
    )
)
class NewsletterSubscriberDetailView(generics.RetrieveDestroyAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    permission_classes = [AllowAny]
