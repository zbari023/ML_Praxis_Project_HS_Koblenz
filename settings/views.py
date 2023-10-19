from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import NameuploadForm, ImageUploadForm ,ContactForm
from .models import Image

# Create your views here.


def home(request):
    if Image.objects.exists():
        image = Image.objects.latest('id')
        context = {'image': image}
    else:
        context = {'image': None}
    
    if request.method == 'POST':
        form = NameuploadForm(request.POST)
        imgform = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a page displaying uploaded images
        if imgform.is_valid():
            imgform.save()
            return redirect('/') 
    else:
        form = NameuploadForm()
        imgform = ImageUploadForm()
        
    context.update({'form': form, 'imgform': imgform})
    return render(request, 'settings/base.html', context)

def contact(request):
    if request.method == 'POST':
        eform = ContactForm(request.POST)
        if eform.is_valid(): 
            eform.save()
            subject = "Welcome to Imagiolib"
            message = "Our team will contact you within 24hrs."
            email_from = settings.EMAIL_HOST_USER
            email = eform.cleaned_data['email']
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list])
            return render(request, 'settings/success.html') 
    eform = ContactForm()
    context = {'eform': eform}
    return render(request, 'settings/contact.html', context)