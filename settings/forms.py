
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
        
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
