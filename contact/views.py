# contact/views.py
from django.shortcuts import render
from .models import Contact

# Create your views here.
def contactlist_view(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "contact/contactlist.html", context)