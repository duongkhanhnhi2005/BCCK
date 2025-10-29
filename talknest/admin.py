from django.contrib import admin
from .models import Topic
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at','description')
    search_fields = ('title',)

# Register your models here.
