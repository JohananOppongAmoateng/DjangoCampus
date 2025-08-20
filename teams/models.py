from django.db import models

# Create your models here.

TEAM_MEMBER_IMAGE="/media/team/"

#Model  for team 
class TeamModel(models.Model):
    fullName = models.CharField(max_length=100,blank=False, null=False, verbose_name="Full Name")
    position = models.CharField(max_length=100,blank=False, null=False, verbose_name="Position")
    bio = models.TextField(blank=True, null=True, verbose_name="Bio")
    image = models.ImageField(upload_to='team_images/', blank=True, null=True, verbose_name="Profile Image")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    join_date = models.DateField(auto_now_add=True, verbose_name="Join Date")
    
    def __str__(self):
        return f"{self.fullName} - {self.position}"
    
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['id']




#Models for Socials
class SocialModel(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('portfolio', 'Portfolio'),
        ('email', 'Email'),
    ]
    
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name="socials")
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, verbose_name="Platform")
    url = models.URLField(max_length=200, blank=False, null=False, verbose_name="URL")
    is_primary = models.BooleanField(default=False, verbose_name="Primary Social")
    
    def __str__(self):
        return f"{self.team.fullName} - {self.get_platform_display()}"
    
    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media Links"
        unique_together = ('team', 'platform')  # Prevent 
