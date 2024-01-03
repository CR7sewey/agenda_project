
from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def index(request):

    # to get all the contacts!using the Model!
    contacts = Contact.objects.all().order_by('-id')
    context = {"contacts": contacts}
    return render(
        request,
        'contact/index.html',
        context,)
