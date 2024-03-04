from django.contrib import admin
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name']
    list_display = ('pk', 'username', 'first_name', 'last_name')
    list_filter = (('date_joined', admin.DateFieldListFilter),)
