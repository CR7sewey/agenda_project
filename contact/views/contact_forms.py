from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404, HttpRequest, HttpResponse

# Create your views here.


def create(request):

    if request.method == 'POST':  # pq pode ser get a vir de la tmb!
        # From form in create.html
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('first_name', '').strip()

        # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
        return render(
            request,
            'contact/create.html',
            {}
        )
    else:  # GET!
        ...
