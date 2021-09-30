from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                                               # Home Path
    path('projects/', views.projects, name='projects'),                 # Projects Path
    path('certificates/', views.certificates, name='certificates'),     # Certificates Path

]
