from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):

    messages.info(request, 'Introduce a new user')
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
            messages.success(request, 'User registered!')
            return redirect('contact:index')

        return render(request,
                      'contact/register.html',
                      context={"form": form})

    form = RegisterForm()
    context = {"form": form}
    return render(request,
                  'contact/register.html',
                  context)
