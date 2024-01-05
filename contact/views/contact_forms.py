from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpRequest, HttpResponse
from contact.forms import ContactForm

# Create your views here.


def create(request):

    if request.method == 'POST':  # pq pode ser get a vir de la tmb!
        # From form in create.html
        # first_name = request.POST.get('first_name').strip()
        # last_name = request.POST.get('last_name', '').strip()
        # phone = request.POST.get('phone', '').strip()
        # email = request.POST.get('email').strip()
        # description = request.POST.get('description', '').strip()
        # show = request.POST.get('show', '').strip()
        # picture = request.POST.get('picture', '').strip()
        # category = request.POST.get('category', '').strip()
        # owner = request.POST.get('owner', '').strip()

        # first_name, last_name, phone)  # , email,
        form = ContactForm(request.POST)
        # description, show, picture, category, owner)

        # if form.is_valid():
        context = {"form": form}

        # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
        return render(
            request,
            'contact/create.html',
            context
        )
    # else:  # GET!
    context = {"form": ContactForm()}

    # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
    return render(
        request,
        'contact/create.html',
        context)
