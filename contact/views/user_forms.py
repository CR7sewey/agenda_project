from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from contact.forms import RegisterForm


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
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
