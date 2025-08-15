from django.contrib import admin

# Register your models here.
from core.models import WorkShop, WorkshopRegistration

@admin.register(WorkShop)
class WorkShopAdmin(admin.ModelAdmin):
    list_display = ('workshop_name', 'workshop_date', 'workshop_location')
    search_fields = ('workshop_name', 'workshop_location')
    list_filter = ('workshop_date',)
    
    
@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'workshop', 'registration_date', 'will_attend_physical', 'django_experience')
    search_fields = ('user_name', 'user_email')
    list_filter = ('workshop', 'will_attend_physical', 'django_experience')
    ordering = ('-registration_date',)