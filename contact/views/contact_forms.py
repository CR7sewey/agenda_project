from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpRequest, HttpResponse
from contact.forms import ContactForm
from django.urls import reverse

from contact.models import Contact

# Create your views here.

# PATH
# 1º -> url: .../contacts/create ; 2º -> views create (get) (render template create, action - create)
# 3º -> write some info, send (POST) ; 4º -> redirect to url: ... /contacts/{id}/update
# 5º views update (get) (render template create with the previous contact); 6 º -> new info; send, POST


def create(request):
    # url a carregar a view! buscar dentro do template a url
    form_action = reverse('contact:create')
    print(form_action)
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

        form = ContactForm(request.POST, request.FILES)  # FILES os arquicos

        # if form.is_valid():
        context = {"form": form, "form_action": form_action}

        if form.is_valid():  # true if all validations are passed!
            contact = form.save(commit=False)  # commit dont allow saving!
            # contact.show = False
            contact.save()  # save in database
            # template = f'contact/{contact.id}/detail/'
            # clean form, redireciona para o upate que por consequensia vai oara o views do update
            return redirect('contact:update', contact_id=contact.id)

        # id = contact.fields.get("id")
        # return redirect('contact:index')
        # return render(
        #    request,
        #    'contact/contact.html',
        #   {'contact': contact})
        # return redirect(template)

        return render(
            request,
            'contact/create.html',
            context)

    # else:  # GET! primeiro entra sempre aqui, pq o get tmb é para quando busca o template em si, ou qunado pagina atualizada etc
    context = {"form": ContactForm(), "form_action": form_action}
    # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
    return render(
        request,
        'contact/create.html',
        context)


def update(request, contact_id):
    form_action = reverse('contact:update', args=(contact_id,))
    actual_contact = get_object_or_404(  # buscar instancia de um objeto ja existente! para o forma ja ter os dados do contacto ja existente,
        Contact, pk=contact_id, show=True)
    # print(actual_contact.first_name)
    if request.method == 'POST':  # pq pode ser get a vir de la tmb!

        form = ContactForm(request.POST, request.FILES,
                           instance=actual_contact)

        # if form.is_valid():
        context = {"form": form, "form_action": form_action}

        if form.is_valid():  # true if all validations are passed!
            contact = form.save(commit=False)  # commit dont allow saving!
            # contact.show = False
            contact.save()  # save in database
            # template = f'contact/{contact.id}/detail/'
            # clean form, redireciona para o upate que por consequensia vai oara o views do update
            return redirect('contact:update', contact_id=contact.id)

        # id = contact.fields.get("id")
        # return redirect('contact:index')
        # return render(
        #    request,
        #    'contact/contact.html',
        #   {'contact': contact})
        # return redirect(template)
        return render(
            request,
            'contact/create.html',
            context)

    # else:  # GET! primeiro entra sempre aqui, pq o get tmb é para quando busca o template em si, ou qunado pagina atualizada etc
    context = {"form": ContactForm(
        instance=actual_contact), "form_action": form_action}
    # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
    return render(
        request,
        'contact/create.html',
        context)


def delete(request, contact_id):
    actual_contact = get_object_or_404(  # buscar instancia de um objeto ja existente! para o forma ja ter os dados do contacto ja existente,
        Contact, pk=contact_id, show=True)

    if request.method == 'POST':  # pq pode ser get a vir de la tmb!

        confirmation = request.POST.get(
            "confirmation", 'no').strip()  # from input (value)

        if confirmation == 'yes':  # value
            actual_contact.delete()
            return redirect('contact:index')

        return render(
            request,
            'contact/contact.html',
            {
                'contact': actual_contact,
                'confirmation': confirmation,
            }
        )

    # NUNCA ENTRA!
    # else:  # GET! primeiro entra sempre aqui, pq o get tmb é para quando busca o template em si, ou qunado pagina atualizada etc
    context = {"contact": actual_contact, 'confirmation': 'no'}
    # context = {"page_obj": page_obj, "site_title": 'Contacts - '}
    return render(
        request,
        'contact/contact.html',
        context)
