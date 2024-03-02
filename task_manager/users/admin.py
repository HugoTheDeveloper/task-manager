from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name']
    list_display = ('pk', 'username', 'first_name', 'last_name')
    list_filter = (('date_joined', admin.DateFieldListFilter),)
