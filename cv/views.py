from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render,  get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import About, Project, Experience
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string

def index(request,idUrl):
    about = About.objects.filter(id=idUrl).first()
    projects = Project.objects.filter(about=about)
    experiences = Experience.objects.filter(about=about)
    nn=1
    if len(experiences)>0:
        nn=360/len(experiences)
    font=about.urlfont.split("~")
    return render(request, "cv/index.html",{
        "about": about,
        "fontname": font[0],
        "fontUrl": font[1],
        "projects": projects,
        "experiences":experiences,
        "nexperiences": nn 
    })
    
def contact(request):
    if request.method=="POST":
        name= request.POST["name"]
        emailt= request.POST["email"]
        email2= request.POST["email2"]
        cel= request.POST["cel"]
        messaget= request.POST["message"]
        
        subject="Correo desde la App"
        
        templ= render_to_string("cv/email_template.html",{
            'name': name,
            'email': emailt,
            'message': messaget,
            'cel': cel
        })
        
        email= EmailMessage(
            subject,
            templ,
            settings.EMAIL_HOST_USER,
            [email2,emailt]
        )
        email.fail_silently=False
        email.send()
        
        messages.success(request,"Se ha enviado tu correo.")
    
    return index(request,request.POST["id"])
        
        