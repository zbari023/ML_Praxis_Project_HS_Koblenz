from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NameuploadForm, ImageUploadForm
from .models import Image
from .forms import ContactForm

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

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["barry450643@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "settings/email.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")