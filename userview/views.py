# Create your views here.
from django.shortcuts import render
from .forms import *
# Importing classes from models.py
from .models import Projects, Certificates, SiteContent, ContactUrls, Skills, Slideshow
# Importing mail_admins from django.core.mail
from django.core.mail import mail_admins


# -------------------------------------------Method to render Home Page----------------------------------------------- #
def home(request):
    site_content = SiteContent.objects.all()        # Fetching all objects from Site Content
    contact_urls = ContactUrls.objects.all()        # Fetching all objects from ContactUrls
    skills = Skills.objects.all()                   # Fetching all objects from Skills
    slideshow = Slideshow.objects.all()             # Fetching all objects from Slideshow
    submitted = False
    if request.method == 'POST':                    # Checking if the request method is POST
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]                        # Getting the Enter Name in Contact Form
            email = form.cleaned_data["email"]                      # Getting the Enter Email in Contact Form
            message = form.cleaned_data["message"]                  # Getting the Enter Message in Contact Form
            subject = 'Portfolio Mail'                              # Mail Subject
            email_text = f'Name: {name} \nEmail: {email} \n\nMessage: \n {message}'    # Concatenating the email message
            mail_admins(subject, email_text, fail_silently=False, connection=None,
                        html_message=None)                          # Sending Mail to Admin
            submitted = True

            return render(request, 'index.html',
                          context={'form': form, 'submitted': submitted, 'site_content': site_content,
                                   'contact_urls': contact_urls, 'skills': skills, 'slideshow': slideshow})

    else:
        form = ContactForm()                                        # Initializing ContactForm class
        return render(request, 'index.html',
                      context={'form': form, 'site_content': site_content, 'contact_urls': contact_urls,
                               'skills': skills, 'slideshow': slideshow})


# ---------------------------------------- Method to render Project Page---------------------------------------------- #
def projects(request):
    project = Projects.objects.all()          # Fetching all objects from Projects
    contact_urls = ContactUrls.objects.all()  # Fetching all objects from ContactUrls
    return render(request, 'projects.html', {'projects': project,'contact_urls': contact_urls})


# ----------------------------------------Method to render Certificate Page------------------------------------------- #
def certificates(request):
    certificate = Certificates.objects.all()    # Fetching all objects from Certificates
    contact_urls = ContactUrls.objects.all()    # Fetching all objects from ContactUrls
    return render(request, 'certificates.html', {'certificates': certificate,'contact_urls': contact_urls})
