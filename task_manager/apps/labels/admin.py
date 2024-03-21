from django.contrib import admin
from .models import Label
# Register your models here.


@admin.register(Label)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('pk', 'name', 'created_at')
