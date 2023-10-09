
from django.shortcuts import render, redirect
from .forms import NameuploadForm, ImageUploadForm

# Create your views here.


def home(request):
    
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
    return render(request,'settings/base.html',{'form': form,'imgform': imgform})