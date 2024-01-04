from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404, HttpRequest, HttpResponse

# Create your views here.


def create(request):

    # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
    return render(
        request,
        'contact/create.html',
        {}
    )
