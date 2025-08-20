from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import (
    Partner,
     Contributor,
     Sponsor,
    Supporter
)
from .serializers import (
    PartnerSerializer,
    ContributorSerializer,
    SponsorSerializer,
    SupporterSerializer
)


# Partner views
@extend_schema_view(
    get=extend_schema(
        summary="List all strategic partners",
        description="Get a list of all active strategic partners that share our vision",
        tags=["Partners"]
    )
)
class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.filter(is_active=True).select_related(
        'tier', 'partner_type'
    )
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]

@extend_schema_view(
    get=extend_schema(
        summary="Retrieve partner details",
        description="Get detailed information about a specific strategic partner",
        tags=["Partners"]
    )
)
class PartnerDetailView(generics.RetrieveAPIView):
    queryset = Partner.objects.select_related('tier', 'partner_type')
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]
    


# Contributor views
@extend_schema_view(
    get=extend_schema(
        summary="List all contributors",
        description=(
            "Get a list of all volunteers and mentors who dedicate "
            "their time to make workshops happen"
        ),
        tags=["Contributors"]
    )
)
class ContributorListView(generics.ListAPIView):
    queryset = Contributor.objects.filter(is_active=True).select_related('role')
    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Retrieve contributor details",
        description="Get detailed information about a specific contributor",
        tags=["Contributors"]
    )
)
class ContributorDetailView(generics.RetrieveAPIView):
    queryset = Contributor.objects.select_related('role')
    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]


# Sponsor views
@extend_schema_view(
    get=extend_schema(
        summary="List all sponsors",
        description="Get a list of all active sponsors",
        tags=["Sponsors"]
    )
)
class SponsorListView(generics.ListAPIView):
    queryset = Sponsor.objects.filter(is_active=True).select_related('level')
    serializer_class = SponsorSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Get sponsor details",
        description="Retrieve details for a specific sponsor",
        tags=["Sponsors"]
    )
)
class SponsorDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.filter(is_active=True).select_related('level')
    serializer_class = SponsorSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


# Supporter views
@extend_schema_view(
    get=extend_schema(
        summary="List all supporters",
        description="Get a list of all active supporters",
        tags=["Supporters"]
    )
)
class SupporterListView(generics.ListAPIView):
    queryset = Supporter.objects.filter(is_active=True)
    serializer_class = SupporterSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Get supporter details",
        description="Retrieve details for a specific supporter",
        tags=["Supporters"]
    )
)
class SupporterDetailView(generics.RetrieveAPIView):
    queryset = Supporter.objects.filter(is_active=True)
    serializer_class = SupporterSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
