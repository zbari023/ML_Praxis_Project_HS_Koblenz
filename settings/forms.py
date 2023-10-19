
from django import forms 
from .models import UserData , Image , Contact

class NameuploadForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name','email','phone']
        
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
