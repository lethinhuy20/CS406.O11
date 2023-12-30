from django.contrib import admin
from .models import UploadImage, DatabaseImage

# Register your models here.
admin.site.register([UploadImage, DatabaseImage])

# modify admin view 
class DatabaseImageAdmin(admin.ModelAdmin):
    list_display = [
        'index',
        'category',
        'gender',
    ]
    search_fields = [
        'index',
        'category',
        'gender',
    ]

admin.site.unregister(DatabaseImage)
admin.site.register(DatabaseImage, DatabaseImageAdmin)