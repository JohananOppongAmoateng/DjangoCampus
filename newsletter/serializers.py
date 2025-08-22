from rest_framework import serializers
from newsletter.models import NewsletterSubscriber


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
    
    def validate_email(self, value):
        if NewsletterSubscriber.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already subscribed to our newsletter."
            )
        return value

