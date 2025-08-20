from rest_framework import serializers
from .models import (
    PartnerTier, PartnerType, Partner,
    ContributorRole, Contributor,
    SponsorLevel, Sponsor,
    Supporter
)


class PartnerTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerTier
        fields = ['id', 'name', 'description', 'badge_color']


class PartnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerType
        fields = ['id', 'name', 'description']


class PartnerSerializer(serializers.ModelSerializer):
    tier_name = serializers.CharField(source='tier.name', read_only=True)
    tier_badge_color = serializers.CharField(
        source='tier.badge_color',
        read_only=True
    )
    partner_type_name = serializers.CharField(
        source='partner_type.name',
        read_only=True
    )

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'description', 'logo', 'website',
            'tier', 'tier_name', 'tier_badge_color',
            'partner_type', 'partner_type_name',
            'partnership_date', 'is_active'
        ]


class ContributorRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorRole
        fields = ['id', 'name', 'description', 'badge_color']


class ContributorSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)
    role_badge_color = serializers.CharField(
        source='role.badge_color',
        read_only=True
    )

    class Meta:
        model = Contributor
        fields = [
            'id', 'full_name', 'role', 'role_name', 'role_badge_color',
            'photo', 'bio', 'achievements', 'linkedin', 'github',
            'twitter', 'website', 'email', 'is_active'
        ]


class SponsorLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorLevel
        fields = ['id', 'name', 'description', 'badge_color']


class SponsorSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.name', read_only=True)
    level_badge_color = serializers.CharField(
        source='level.badge_color',
        read_only=True
    )

    class Meta:
        model = Sponsor
        fields = [
            'id', 'name', 'logo', 'website', 'level',
            'level_name', 'level_badge_color', 'description',
            'sponsored_since', 'is_active'
        ]


class SupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporter
        fields = [
            'id', 'name', 'logo', 'website', 'contribution_type',
            'description', 'support_date', 'is_active'
        ]
