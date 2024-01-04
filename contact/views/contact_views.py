
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
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

    context = {"contacts": contacts, "site_title": 'Contacts - '}
    return render(
        request,
        'contact/index.html',
        context,)


def search(request):
    # if request.method == "GET":     # q - name do input do html!!
    searched_value = request.GET.get("q", '').strip()  # query

    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

    if searched_value == '':
        # if none back to first page
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=searched_value) |
        Q(last_name__icontains=searched_value) |
        Q(phone__icontains=searched_value) |
        Q(email__icontains=searched_value))  # Q - allows or

    # print(contacts.query)
    contacts = contacts.order_by('-id')

    context = {"contacts": contacts,
               "site_title": 'Contacts (search) - '}

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

    context = {"contact": contacts, "site_title": f'{
        contacts.first_name} {contacts.last_name} - '}
    return render(
        request,
        'contact/contact.html',
        context,)
