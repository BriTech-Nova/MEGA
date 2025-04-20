from django.contrib import admin
from .models import ContactMessage
'''
Admin interface for managing contact messages.
This admin interface allows administrators to view, search, and filter contact messages.
'''

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'