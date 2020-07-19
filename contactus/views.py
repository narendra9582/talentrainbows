from django.shortcuts import render
from .models import ContactUs
from django.contrib import messages


def contactus(request):
    return render(request,'contact_us.html')

def contactus(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        query = request.POST.get('query')
        contact = ContactUs(firstname = firstname, lastname = lastname , email= email, contactno = contactno,query = query)
        contact.save()
        messages.success(request, 'Your query has been received we will get back to you soon! .')
    return render(request,'contact_us.html')
