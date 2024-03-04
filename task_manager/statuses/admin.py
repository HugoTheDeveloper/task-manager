from django.contrib import admin
from .models import Status
# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('pk', 'name', 'created_at')
