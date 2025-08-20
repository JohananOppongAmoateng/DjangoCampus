from django.urls import path
from . import views

urlpatterns = [
    # Partner URLs
    path(
        'api/partners/',
        views.PartnerListView.as_view(),
        name='partner-list'
    ),
    path(
        'api/partners/<int:pk>/',
        views.PartnerDetailView.as_view(),
        name='partner-detail'
    ),
    
    # Contributor URLs
    path(
        'api/contributors/',
        views.ContributorListView.as_view(),
        name='contributor-list'
    ),
    path(
        'api/contributors/<int:pk>/',
        views.ContributorDetailView.as_view(),
        name='contributor-detail'
    ),
    
    # Sponsor URLs
    path(
        'api/sponsors/',
        views.SponsorListView.as_view(),
        name='sponsor-list'
    ),
    path(
        'api/sponsors/<int:pk>/',
        views.SponsorDetailView.as_view(),
        name='sponsor-detail'
    ),
    
    # Supporter URLs
    path(
        'api/supporters/',
        views.SupporterListView.as_view(),
        name='supporter-list'
    ),
    path(
        'api/supporters/<int:pk>/',
        views.SupporterDetailView.as_view(),
        name='supporter-detail'
    ),
]
