
from django import forms 
from .models import UserData , Image , Contact

class NameuploadForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name','email','phone']
        
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','result']
        widgets = {
                'image': forms.ClearableFileInput(attrs={'onclick': 'init()', 'onchange': 'handleImageUpload(event)'})
                
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
