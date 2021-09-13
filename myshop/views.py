from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshop.models import Quotecall, Request_Form, newsletter, happyclient, projectimage
from blog.models import article
from django.contrib import messages
# for email
from django.core.mail import EmailMultiAlternatives
# for getting templates from templates folder
from django.template.loader import render_to_string
# modules for email sending
import smtplib
from email.message import EmailMessage
from string import Template
import string
from smtplib import SMTP
import os
import sys
import random
# Create your views here.


def index(request):
    clients = happyclient.objects.all()
    projectimages = list(projectimage.objects.all())
    my_projectimages = random.sample(projectimages, 4)
    articles = list(article.objects.all())
    my_objects = random.sample(articles, 3)
    return render(request, 'myshop/index.html', {'clients': clients, 'projectimages': my_projectimages, 'articles': my_objects})


def about(request):
    clients = happyclient.objects.all()
    return render(request, 'myshop/about.html', {'clients': clients})


def team(request):
    return render(request, 'myshop/team.html')


def project(request):
    projectimages = list(projectimage.objects.all())
    my_projectimages = random.sample(projectimages, 4)
    return render(request, 'myshop/project.html', {'projectimages': my_projectimages})


def privacy(request):
    return render(request, 'myshop/privacy.html')


def termsandconditions(request):
    return render(request, 'myshop/terms.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        subjects = request.POST.get('subject', '')
        msg = request.POST.get('message', '')
        msgg = request.POST.get('message', '')
        formsaver = Request_Form(
            name=name, email=email, subject=subject, msg=msg)
        formsaver.save()
        try:
            subj = f'From {name} Contact form'
            subject = render_to_string("myshop/emailsubject.txt")
            text_body = render_to_string("myshop/emailbody.txt")
            html_body = render_to_string("myshop/quoterequest.html")
            msg = EmailMultiAlternatives(subject=subj, from_email="bbsbecteam@upatmastaff.com", to=[
                                         "bbsbecteam@upatmastaff.com"], body=text_body)
            s = Template(html_body).safe_substitute(
                name=name, email=email, subject=subjects, msg=msgg)
            msg.attach_alternative(s, "text/html")
            # msg.send()
            messages.success(request, "We will contact you soon")
            return render(request, 'myshop/contact.html')
        except Exception as e:
            messages.warning(request, "message sent with some errors")
            return render(request, 'myshop/contact.html')
        messages.error(request, "Please try again")
        return render(request, 'myshop/contact.html')
    return render(request, 'myshop/contact.html')


def callrequest(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            subject = request.POST.get('subject', '')
            subjects = request.POST.get('subject', '')
            msg = request.POST.get('message', 'Blank')
            msgg = request.POST.get('message', 'Blank')
            datasaver = Quotecall(name=name, email=email,
                                  phone=phone, subject=subject, msg=msg)
            datasaver.save()
            # email sending system
            try:
                subj = f'From {name} call request'
                subject = render_to_string("myshop/emailsubject.txt")
                text_body = render_to_string("myshop/emailbody.txt")
                html_body = render_to_string("myshop/quoterequest.html")
                msg = EmailMultiAlternatives(subject=subject, from_email="bbsbecteam@upatmastaff.com", to=[
                                             "bbsbecteam@upatmastaff.com"], body=text_body)
                s = Template(html_body).safe_substitute(
                    name=name, email=email, phone=phone, subject=subjects, msg=msgg)
                msg.attach_alternative(s, "text/html")
                # msg.send()
                saved_response = 1
                return HttpResponse(saved_response)
            except Exception as e:
                return HttpResponse(0)
    except Exception as e:
        return HttpResponse(0)


def newsletters(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('nemail', '')
            already_exists = newsletter.objects.filter(email=email)
            if len(already_exists) > 0:
                messages.warning(request, "You are already our member thanks for registering")
                return redirect('/')
            saveemail = newsletter(email=email)
            saveemail.save()
            messages.success(request, "You have subscribed to our newsletters")
            return redirect('/')
        except Exception as e:
            messages.warning(request, "You are already our member thanks for registering")
            return redirect('/')
