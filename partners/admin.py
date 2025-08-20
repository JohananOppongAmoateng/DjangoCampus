from django.contrib import admin
from .models import (
    PartnerTier, PartnerType, Partner,
    ContributorRole, Contributor,
    SponsorLevel, Sponsor,
    Supporter
)


@admin.register(PartnerTier)
class PartnerTierAdmin(admin.ModelAdmin):
    list_display = ['name', 'badge_color', 'order']
    search_fields = ['name']


@admin.register(PartnerType)
class PartnerTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'tier', 'partner_type', 'partnership_date', 'is_active']
    list_filter = ['tier', 'partner_type', 'is_active']
    search_fields = ['name', 'description']
    date_hierarchy = 'partnership_date'


@admin.register(ContributorRole)
class ContributorRoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'badge_color']
    search_fields = ['name', 'description']


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'is_active']
    list_filter = ['role', 'is_active']
    search_fields = ['full_name', 'bio', 'achievements']


@admin.register(SponsorLevel)
class SponsorLevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'badge_color', 'order']
    search_fields = ['name']


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'sponsored_since', 'is_active']
    list_filter = ['level', 'is_active']
    search_fields = ['name', 'description']
    date_hierarchy = 'sponsored_since'


@admin.register(Supporter)
class SupporterAdmin(admin.ModelAdmin):
    list_display = ['name', 'contribution_type', 'support_date', 'is_active']
    list_filter = ['contribution_type', 'is_active']
    search_fields = ['name', 'description']
    date_hierarchy = 'support_date'
