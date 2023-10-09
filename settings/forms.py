
from django import forms 
from .models import UserData , Image

class NameuploadForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name','email','phone']
        
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']