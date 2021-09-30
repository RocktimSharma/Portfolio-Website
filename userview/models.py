from django.db import models


# Create your models here.

# Creating project class
class Projects(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image1 = models.ImageField(upload_to='projectspic')
    image2 = models.ImageField(upload_to='projectspic')
    image3 = models.ImageField(upload_to='projectspic', blank=True)
    image4 = models.ImageField(upload_to='projectspic', blank=True)
    toolsAndSoftware = models.TextField()
    languageAndFrameworks = models.TextField()
    apk = models.FileField(upload_to='projectsfile', blank=True)
    exe = models.FileField(upload_to='projectsfile', blank=True)
    deb = models.FileField(upload_to='projectsfile', blank=True)
    link = models.URLField(blank=True)
    docs = models.FileField(blank=True)
    codeLink = models.URLField(blank=True)


# Creating certificate class
class Certificates(models.Model):
    certificate = models.ImageField(upload_to='certificates')
    platform = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()


# Creating Skills class
class Skills(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_percentage = models.IntegerField()
    skill_style = models.IntegerField()


# Creating Slideshow class
class Slideshow(models.Model):
    image = models.ImageField(upload_to='slideshow')


# Creating Site content class
class SiteContent(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    about_me = models.TextField(blank=True)
    copyright_text = models.CharField(max_length=50, blank=True)
    copyright_name = models.CharField(max_length=30, blank=True)
    copyright_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)


# Creating contact url class
class ContactUrls(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    url = models.URLField()
