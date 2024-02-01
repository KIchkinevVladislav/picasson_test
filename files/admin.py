from django.contrib import admin

from .models import File

"""
Register the created models 
for their processing by the administrator
"""
@admin.register(File)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', 'processed',)
    readonly_fields = ('uploaded_at', 'processed',)
    list_filter = ('uploaded_at', 'processed',)
    search_fields = ('uploaded_at',)
    ordering = ('id', 'uploaded_at',)

