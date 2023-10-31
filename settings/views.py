from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import NameuploadForm, ImageUploadForm ,ContactForm
from .models import Image, UserData ,Contact

# Create your views here.

# home function with many goals for sending the data like images or userdata to the admin and database
def home(request):
    images = Image.objects.all().count()       # given the counter of the images in the project
    user = UserData.objects.all().count()      # given the counter of the users in the project
    contacting = Contact.objects.all().count() # given the counter of the contacting in the project
    if Image.objects.exists():                 # to display just the current image in html
        image = Image.objects.latest('id')
        context = {'image': image}
    else:
        context = {'image': None}
    
    if request.method == 'POST':
        form = NameuploadForm(request.POST)    # gitting the request data from the form-class, which content the userdata
        imgform = ImageUploadForm(request.POST, request.FILES) # gitting the request data from the form-class, which content the image data
        eform = ContactForm(request.POST)      # gitting the request data from the form-class, which content the contact data
        if form.is_valid():
            form.save()                        # saving the request data in db
            return redirect('answeruser/')         # Redirect to a page to make sure for the user, that his image is uploaded
        if imgform.is_valid():
            imgform.save()
            return redirect('answerimg/')
        if eform.is_valid(): 
            eform.save()
            subject = "Welcome to Imagiolib"
            message = "Our team will contact you within 24hrs."
            email_from = settings.EMAIL_HOST_USER
            email = eform.cleaned_data['email']
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list]) # sending the answer-E-mail to the user
            return redirect('answer/')  
    else:
        form = NameuploadForm()
        imgform = ImageUploadForm()
        eform = ContactForm()
     # sending the data with the context proccessor to html 
    context.update({'form': form, 'imgform': imgform,'eform': eform,'images':images ,'user': user ,'contacting': contacting })
    return render(request, 'settings/index.html', context)

# make the dashboard function data 
def dashboard(request):
    images = Image.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'settings/dashboard.html',{
        'images':images ,                 # some context data, that used in django-html
        'user': user , 
        'contacting': contacting 
    })
    
# create the answer page for making sure, that the user his data is uploaded
def answeruser(request):
    images = Image.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'settings/answeruser.html',{
        'images':images , 
        'user': user , 
        'contacting': contacting 
    })
    
# create the answer page for making sure, that the user his data is uploaded
def answerimg(request):
    images = Image.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'settings/answerimg.html',{
        'images':images , 
        'user': user , 
        'contacting': contacting 
    })
    
    
