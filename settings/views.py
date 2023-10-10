
from django.shortcuts import render, redirect
from .forms import NameuploadForm, ImageUploadForm
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