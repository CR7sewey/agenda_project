from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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
            return redirect('contact:login')

        return render(request,
                      'contact/register.html',
                      context={"form": form})

    form = RegisterForm()
    context = {"form": form}
    return render(request,
                  'contact/register.html',
                  context)


def login_view(request):
    form = AuthenticationForm(request)  # feito automaticamnte as validacoes
    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login sucessful')
            return redirect('contact:index')
        messages.error(request, 'Login unsucessful')
        return render(request,
                      'contact/login.html',
                      context={"form": form})

    # form = AuthForm()
    context = {"form": form}
    return render(request,
                  'contact/login.html',
                  context)


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:user_update')
