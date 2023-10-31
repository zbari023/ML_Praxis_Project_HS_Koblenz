
from django import forms  # load the forms-bibliothek from django
from .models import UserData , Image , Contact  # load the classes from the model

class NameuploadForm(forms.ModelForm):   # This form-class is responsible to get the data from the user like name,email and phone
    class Meta:
        model = UserData
        fields = ['name','email','telefonnummer']

class ImageUploadForm(forms.ModelForm): # This form-class is responsible to get the data from the image in html page
    class Meta:
        model = Image
        fields = ['image','result']
        widgets = {              # this method will given the fields some function and customization for the in and output
                'image': forms.ClearableFileInput(attrs={'onclick': 'init()', 'onchange': 'handleImageUpload(event)'}),
                'result': forms.Textarea(attrs={'id': 'label-container', 'readonly': True})
        }
        
class ContactForm(forms.ModelForm):  # This form-class is responsible to get the data from the user, when he send his data in message type in html-area
    class Meta:
        model = Contact
        fields = '__all__'
