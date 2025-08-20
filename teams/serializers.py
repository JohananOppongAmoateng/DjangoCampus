from rest_framework import serializers
from teams.models import TeamModel, SocialModel
from drf_spectacular.utils import extend_schema_field


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialModel
        fields = ['id', 'platform', 'url', 'is_primary']


class TeamSerializer(serializers.ModelSerializer):
    socials = SocialSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    
    @extend_schema_field(serializers.URLField)
    def get_image_url(self, obj):
        """Get the full URL for the team member's profile image."""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    class Meta:
        model = TeamModel
        fields = [
            'id', 'fullName', 'position', 'bio', 'image', 'image_url',
            'is_active', 'join_date', 'socials'
        ]
        read_only_fields = ['join_date']


class TeamCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating team members without nested socials.
    """
    
    class Meta:
        model = TeamModel
        fields = [
            'id', 'fullName', 'position', 'bio', 'image',
            'is_active', 'join_date'
        ]
        read_only_fields = ['join_date']


class SocialCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating social media links."""
    
    class Meta:
        model = SocialModel
        fields = ['id', 'team', 'platform', 'url', 'is_primary']
        
    def validate_team(self, value):
        """Ensure the team member exists and is active."""
        if not value.is_active:
            raise serializers.ValidationError(
                "Cannot add social media links to inactive team members."
            )
        return value
    
    def validate(self, data):
        """Ensure only one primary social per team member."""
        if data.get('is_primary', False):
            team = data.get('team')
            if team:
                # Check if there's already a primary social for this team
                existing_primary = SocialModel.objects.filter(
                    team=team,
                    is_primary=True
                ).exclude(pk=self.instance.pk if self.instance else None)
                
                if existing_primary.exists():
                    raise serializers.ValidationError(
                        "This team member already has a primary "
                        "social media link."
                    )
        return data