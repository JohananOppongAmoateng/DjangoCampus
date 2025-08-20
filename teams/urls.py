from django.urls import path
from . import views

urlpatterns = [
    # Team API endpoints
    path('api/teams/',
         views.TeamListCreateView.as_view(),
         name='team-list-create'),
    path('api/teams/<int:pk>/',
         views.TeamRetrieveUpdateDestroyView.as_view(),
         name='team-detail'),
    path('api/teams/active/',
         views.ActiveTeamMembersView.as_view(),
         name='team-active-list'),
    
    # Social Media API endpoints
    path('api/socials/',
         views.SocialListCreateView.as_view(),
         name='social-list-create'),
    path('api/socials/<int:pk>/',
         views.SocialRetrieveUpdateDestroyView.as_view(),
         name='social-detail'),
    
    # Team member socials
    path('api/teams/<int:team_id>/socials/',
         views.TeamMemberSocialsView.as_view(),
         name='team-socials'),
    
    # Teams by platform
    path('api/teams/platform/<str:platform>/',
         views.TeamMembersByPlatformView.as_view(),
         name='teams-by-platform'),
    
    # Statistics
    path('api/teams/stats/',
         views.team_stats,
         name='team-stats'),
]
