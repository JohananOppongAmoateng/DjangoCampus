from django.shortcuts import render
from teams.serializers import TeamSerializer, SocialSerializer
from teams.models import TeamModel, SocialModel
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter
)
from drf_spectacular.types import OpenApiTypes


@extend_schema_view(
    get=extend_schema(
        summary="List all team members",
        description=(
            "Retrieve a list of all team members with their basic "
            "information and social media links."
        ),
        tags=["Teams"]
    ),
    post=extend_schema(
        summary="Create a new team member",
        description="Add a new team member to the organization.",
        tags=["Teams"]
    )
)
class TeamListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing all team members and creating new ones.
    """
    queryset = TeamModel.objects.prefetch_related('socials').filter(
        is_active=True
    )
    serializer_class = TeamSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Retrieve a team member",
        description=(
            "Get detailed information about a specific team member "
            "including their social media links."
        ),
        tags=["Teams"]
    ),
    put=extend_schema(
        summary="Update a team member",
        description="Update all information for a specific team member.",
        tags=["Teams"]
    ),
    patch=extend_schema(
        summary="Partially update a team member",
        description="Update specific fields of a team member.",
        tags=["Teams"]
    ),
    delete=extend_schema(
        summary="Delete a team member",
        description="Remove a team member from the organization.",
        tags=["Teams"]
    )
)
class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting individual
    team members.
    """
    queryset = TeamModel.objects.prefetch_related('socials').all()
    serializer_class = TeamSerializer


@extend_schema_view(
    get=extend_schema(
        summary="List active team members only",
        description="Retrieve a list of only active team members.",
        tags=["Teams"]
    )
)
class ActiveTeamMembersView(generics.ListAPIView):
    """
    API endpoint for listing only active team members.
    """
    queryset = TeamModel.objects.prefetch_related('socials').filter(
        is_active=True
    )
    serializer_class = TeamSerializer


@extend_schema_view(
    get=extend_schema(
        summary="List all social media links",
        description="Retrieve all social media links for all team members.",
        tags=["Social Media"]
    ),
    post=extend_schema(
        summary="Create a new social media link",
        description="Add a new social media link for a team member.",
        tags=["Social Media"]
    )
)
class SocialListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating social media links.
    """
    queryset = SocialModel.objects.select_related('team').all()
    serializer_class = SocialSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Retrieve a social media link",
        description="Get details of a specific social media link.",
        tags=["Social Media"]
    ),
    put=extend_schema(
        summary="Update a social media link",
        description="Update a social media link completely.",
        tags=["Social Media"]
    ),
    patch=extend_schema(
        summary="Partially update a social media link",
        description="Update specific fields of a social media link.",
        tags=["Social Media"]
    ),
    delete=extend_schema(
        summary="Delete a social media link",
        description="Remove a social media link.",
        tags=["Social Media"]
    )
)
class SocialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting social media links.
    """
    queryset = SocialModel.objects.select_related('team').all()
    serializer_class = SocialSerializer


@extend_schema(
    summary="Get social media links for a specific team member",
    description=(
        "Retrieve all social media links for a specific team member "
        "by their ID."
    ),
    parameters=[
        OpenApiParameter(
            name='team_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description='ID of the team member'
        )
    ],
    tags=["Social Media"]
)
class TeamMemberSocialsView(generics.ListAPIView):
    """
    API endpoint for getting all social media links of a specific
    team member.
    """
    serializer_class = SocialSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return SocialModel.objects.filter(team_id=team_id)


@extend_schema(
    summary="Get team members by platform",
    description=(
        "Retrieve all team members who have a specific "
        "social media platform."
    ),
    parameters=[
        OpenApiParameter(
            name='platform',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.PATH,
            description=(
                'Social media platform '
                '(e.g., linkedin, twitter, github)'
            )
        )
    ],
    tags=["Social Media"]
)
class TeamMembersByPlatformView(generics.ListAPIView):
    """
    API endpoint for getting team members by social media platform.
    """
    serializer_class = TeamSerializer

    def get_queryset(self):
        platform = self.kwargs['platform']
        return TeamModel.objects.filter(
            socials__platform=platform,
            is_active=True
        ).prefetch_related('socials').distinct()


@extend_schema(
    summary="Get team statistics",
    description=(
        "Get statistics about the team including total members, "
        "active members, and platform counts."
    ),
    tags=["Teams"]
)
@api_view(['GET'])
def team_stats(request):
    """
    API endpoint for getting team statistics.
    """
    total_members = TeamModel.objects.count()
    active_members = TeamModel.objects.filter(is_active=True).count()
    inactive_members = total_members - active_members
    
    # Platform statistics
    platform_stats = {}
    platforms = [
        'linkedin', 'twitter', 'github', 'instagram',
        'facebook', 'portfolio', 'email'
    ]
    
    for platform in platforms:
        count = SocialModel.objects.filter(platform=platform).count()
        platform_stats[platform] = count
    
    return Response({
        'total_members': total_members,
        'active_members': active_members,
        'inactive_members': inactive_members,
        'platform_statistics': platform_stats
    }, status=status.HTTP_200_OK)

