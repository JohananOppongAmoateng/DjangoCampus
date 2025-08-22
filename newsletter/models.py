from django.db import models

# Create your models here.


##Newsletter

class NewsletterSubscriber(models.Model):
    name  = models.CharField(max_length=100, blank=True, null=True, verbose_name="Full Name")
    email = models.EmailField(max_length=254, unique=True, verbose_name="Email Address")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"

    def __str__(self):
        return f"{self.email} - {self.name}"