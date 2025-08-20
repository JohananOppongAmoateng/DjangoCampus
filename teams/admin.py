from django.contrib import admin
from .models import TeamModel, SocialModel


class SocialInline(admin.TabularInline):
    model = SocialModel
    extra = 1
    fields = ['platform', 'url', 'is_primary']


@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = [
        'fullName', 'position', 'is_active', 'join_date'
    ]
    list_filter = ['is_active', 'position', 'join_date']
    search_fields = ['fullName', 'position', 'bio']
    readonly_fields = ['join_date']
    inlines = [SocialInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('fullName', 'position', 'bio')
        }),
        ('Profile', {
            'fields': ('image', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('join_date',),
            'classes': ('collapse',)
        }),
    )


@admin.register(SocialModel)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = ['team', 'platform', 'is_primary']
    list_filter = ['platform', 'is_primary']
    search_fields = ['team__fullName', 'url']
    list_select_related = ['team']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('team')
