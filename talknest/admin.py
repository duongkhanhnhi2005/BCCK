from django.contrib import admin
from .models import Community
@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at','description')
    search_fields = ('name',)

# Register your models here.
