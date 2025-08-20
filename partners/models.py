from django.db import models
from django.utils.translation import gettext_lazy as _


class PartnerTier(models.Model):
    """Partner tiers (Platinum, Gold, Silver, etc.)"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    badge_color = models.CharField(max_length=20, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order']
        verbose_name = _("Partner Tier")
        verbose_name_plural = _("Partner Tiers")
    
    def __str__(self):
        return self.name


class PartnerType(models.Model):
    """Partner types (Academic, Community, Technology, etc.)"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = _("Partner Type")
        verbose_name_plural = _("Partner Types")
    
    def __str__(self):
        return self.name


class Partner(models.Model):
    """Strategic partners that share our vision"""
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="Short description of what the partner does")
    logo = models.ImageField(upload_to='partners/logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    tier = models.ForeignKey(
        PartnerTier,
        on_delete=models.SET_NULL,
        related_name="partners",
        blank=True, 
        null=True
    )
    partner_type = models.ForeignKey(
        PartnerType,
        on_delete=models.SET_NULL,
        related_name="partners",
        blank=True,
        null=True
    )
    partnership_date = models.DateField(
        help_text="Date when the partnership started"
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")
    
    def __str__(self):
        return self.name


class ContributorRole(models.Model):
    """Contributor roles (Lead Volunteer, Technical Mentor, Community Manager)"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    badge_color = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        verbose_name = _("Contributor Role")
        verbose_name_plural = _("Contributor Roles")
    
    def __str__(self):
        return self.name


class Contributor(models.Model):
    """Key contributors who dedicate time to make workshops happen"""
    full_name = models.CharField(max_length=100)
    role = models.ForeignKey(
        ContributorRole,
        on_delete=models.SET_NULL,
        related_name="contributors",
        blank=True,
        null=True
    )
    photo = models.ImageField(upload_to='contributors/photos/', blank=True, null=True)
    bio = models.TextField(help_text="Short bio about the contributor", blank=True, null=True)
    achievements = models.CharField(
        max_length=255,
        help_text="Brief highlight of achievements (e.g., 'Organized 5 workshops')",
        blank=True,
        null=True
    )
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'full_name']
        verbose_name = _("Contributor")
        verbose_name_plural = _("Contributors")
    
    def __str__(self):
        return self.full_name


class SponsorLevel(models.Model):
    """Sponsor levels (Diamond, Platinum, Gold, etc.)"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    badge_color = models.CharField(max_length=20, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order']
        verbose_name = _("Sponsor Level")
        verbose_name_plural = _("Sponsor Levels")
    
    def __str__(self):
        return self.name


class Sponsor(models.Model):
    """Financial sponsors who support the initiative"""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    level = models.ForeignKey(
        SponsorLevel,
        on_delete=models.SET_NULL,
        related_name="sponsors",
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    sponsored_since = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")
    
    def __str__(self):
        return self.name


class Supporter(models.Model):
    """Recent supporters who contribute in various ways"""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='supporters/logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    contribution_type = models.CharField(
        max_length=100,
        help_text="Type of contribution (e.g., 'Venue Provider', 'Equipment Donor')",
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    support_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-support_date', 'name']
        verbose_name = _("Supporter")
        verbose_name_plural = _("Supporters")
    
    def __str__(self):
        return self.name
