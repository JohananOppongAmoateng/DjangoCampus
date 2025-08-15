from secrets import choice
from django.db import models

# Create your models here.


# Models to to add what you'll learn 

    
# Model to add workshops
class WorkShop(models.Model):
    workshop_name = models.CharField(max_length=255, verbose_name="Workshop Name", null=False, blank=False)
    workshop_date = models.DateField(verbose_name="Workshop Date", null=False, blank=False)
    workshop_location = models.CharField(max_length=255, verbose_name="Workshop Location", null=False, blank=False)
    workshop_description = models.TextField(verbose_name="Workshop Description", null=True, blank=True)
    
    
    class Meta:
        verbose_name = "Workshop"
        verbose_name_plural = "Workshops"
        ordering = ['workshop_date']
        table_name = 'workshops'
        
    def __str__(self):
        return f"{self.workshop_name} - {self.workshop_date}"
    
    
    

#Experience in django

class DjangoExperience(choice.Choices):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'

# Model to let users register for workshops
class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE, related_name='registrations', verbose_name="Workshop")
    user_name = models.CharField(max_length=255, verbose_name="User Name", null=False, blank=False)
    user_email = models.EmailField(verbose_name="User Email", null=False, blank=False)
    will_attend_physical = models.BooleanField(default=True, verbose_name="Will Attend Physically")
    django_experience = models.CharField(
        max_length=20,
        choices=DjangoExperience.choices,
        default=DjangoExperience.BEGINNER,
        verbose_name="Django Experience Level"
    )
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")
    
    class Meta:
        verbose_name = "Workshop Registration"
        verbose_name_plural = "Workshop Registrations"
        ordering = ['registration_date']
        table_name = 'workshop_registrations'
        
    def __str__(self):
        return f"{self.user_name} registered for {self.workshop.workshop_name}"
