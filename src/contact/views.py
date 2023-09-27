from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, "contact/index.html")



def send_email(request):
    subject = request.POST['subject']
    message = request.POST['message']
    from_email = request.POST['from_email']

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['ellabihoundou@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
