from django.contrib import admin

# Register your models here.
from .models import Company,Image,UserData, Contact
# customazation the classes in Admin panel
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telefonnummer']
class PostAdmin(admin.ModelAdmin):
    list_display = ['image','result']
    list_filter = ['image']
    search_fields = ['image']
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

# models-class Registeration in Admin panel 

admin.site.register(Image ,PostAdmin)        
admin.site.register(Company)
admin.site.register(UserData,UserDataAdmin)
admin.site.register(Contact,ContactDataAdmin)
