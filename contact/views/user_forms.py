from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from contact.forms import RegisterForm
from django.contrib.auth.models import User


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # VAL FEITA NO FORMS
            # new_user = form.save(commit=False)
            # email = new_user.email
            # user_email_exists = User.objects.filter(email=email)
            # if user_email_exists:
            #    raise Http404('CACETA')
            form.save()
            return redirect('contact:index')

        return render(request,
                      'contact/register.html',
                      context={"form": form})

    form = RegisterForm()
    context = {"form": form}
    return render(request,
                  'contact/register.html',
                  context)
