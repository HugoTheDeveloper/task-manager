from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'author']
    list_display = ('pk', 'name', 'description', 'author', 'executor')
    list_filter = (('created_at', admin.DateFieldListFilter),)
