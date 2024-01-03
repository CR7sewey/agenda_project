
from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404, HttpRequest, HttpResponse

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


def contact(request: HttpRequest, contact_id: int) -> HttpResponse:
    contacts: Contact | None = None
    '''
    try:
        contacts = Contact.objects.get(pk=contact_id)  # return only one value
    except:
        raise Http404('This contact does not exists!')'''

    # could do with try, except, with filter(...).first()
    # or like bellow (get_object_or_404(Contact.objects or .objects.filter(pk=contact_id), pk=contact_id))
    contacts = get_object_or_404(
        Contact, pk=contact_id, show=True)  # pk and show

    context = {"contact": contacts}
    return render(
        request,
        'contact/contact.html',
        context,)
