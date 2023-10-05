from django.contrib import admin
from .models import Image
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['Name', 'image']
    list_filter = ['Name', 'image']
    search_fields = ['Name', 'image']
    
    
admin.site.register(Image ,PostAdmin)