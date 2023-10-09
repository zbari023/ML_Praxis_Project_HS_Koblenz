
from django.shortcuts import render, redirect
from .forms import NameuploadForm

# Create your views here.


def home(request):
    
    if request.method == 'POST':
        form = NameuploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a page displaying uploaded images
    else:
        form = NameuploadForm()
    return render(request,'settings/base.html',{'form': form})