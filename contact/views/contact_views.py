
from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def index(request):

    # to get all the contacts!using the Model!
    # contacts = Contact.objects.all().order_by('-id') # show all!
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]  # show only show=True

    print(contacts.query)  # just to see the query! check terminal!

    context = {"contacts": contacts}
    return render(
        request,
        'contact/index.html',
        context,)
