from django.contrib import admin
from .models import MediaItem

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_type', 'upload_date')
    search_fields = ('title',)
    list_filter = ('upload_date',)