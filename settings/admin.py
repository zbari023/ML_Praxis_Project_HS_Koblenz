from django.contrib import admin

# Register your models here.
from .models import Company,Image,UserData



class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
class PostAdmin(admin.ModelAdmin):
    list_display = ['image']
    list_filter = ['image']
    search_fields = ['image']
    
admin.site.register(Image ,PostAdmin)
admin.site.register(Company)
admin.site.register(UserData,UserDataAdmin)
