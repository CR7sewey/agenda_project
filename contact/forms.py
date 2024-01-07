from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'class-a class-b',
                                      'placeholder': 'Write here'}  # renderiza classe no html!
                               ),
        help_text='Helpful text for user',
        label='First Name'
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',  # restirct the type of input
            }
        )
    )

    # criar campo aqui sem ser no models!
    # qualquer = forms.CharField(
    #    widget=forms.TextInput(attrs={'class': 'class-a class-b',
    #                                 'placeholder': 'Write here'}  # renderiza classe no html!
    #                          ),
    #   help_text='Helpful text for user',
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #    'placeholder': 'Write here'
        # })  # atualizar o wideget que ja estava no campo

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name',
                  'phone', 'email', 'description',
                  'category', 'picture',)

        # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
        # campo a ser renderizado! ex forms.PasswordInput()
        # criar novo widget!
        # widgets = {'first_name': forms.TextInput(
        #    attrs={'class': 'class-a class-b',
        #           'placeholder': 'Write here'}  # renderiza classe no html!
        # )}

    def clean(self):  # sobrescrever metodo, used to validate fields!
        cleaned_data = self.cleaned_data  # data before added to database

        # self.add_error(
        #   'first_name',  # or first_name for ex - atrelar a um campo
        #   ValidationError('Error 1:', code='invalid')
        # )

        # self.add_error(
        #    'first_name',  # or first_name for ex - atrelar a um campo
        #    ValidationError('Error 2:', code='invalid')
        # )

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            self.add_error('first_name',
                           ValidationError('First name must be different from Last name', code='invalid'))
            self.add_error('last_name',
                           ValidationError('First name must be different from Last name', code='invalid'))

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(  # or raise (o problema do raise é que dps nao deixa ver os restantes erros que possam haver!!)
                'first_name',  # or first_name for ex - atrelar a um campo
                ValidationError('Add error', code='invalid')
            )

        return first_name


class RegisterForm(UserCreationForm):
    # SIMILAR TO MODELS
    first_name = forms.CharField(
        widget=forms.TextInput(),
        label='First Name',
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput(),
        label='Last Name',
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='Email',
        required=True
    )

    username = forms.CharField(
        widget=forms.TextInput(),
        label='Username',
        required=True
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password confirmation',
        required=True
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email',
                  'username', 'password1', 'password2')

    def clean(self):

        # NOTA:
        # O DJANGO AUTOMAITCAMENTE JA VALIDA
        # PASS iguais e simples e tal
        # Username ja existente
        # ainda nao valida se o email ja existe!!

        cleaned_data = self.cleaned_data  # data before added to database

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:  # p campo password ja valida isto !!
            self.add_error('password2',
                           ValidationError('Passoword doesn\'t match :(',
                                           code='invalid'))

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check if email exists
        if User.objects.filter(email=email).exists():
            self.add_error('email',
                           ValidationError('Email already registered!',
                                           code='invalid'))
        return email

    '''
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            self.add_error(  # or raise (o problema do raise é que dps nao deixa ver os restantes erros que possam haver!!)
                'first_name',  # or first_name for ex - atrelar a um campo
                ValidationError(
                    'Please, introduce your first name', code='invalid')
            )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            self.add_error(  # or raise (o problema do raise é que dps nao deixa ver os restantes erros que possam haver!!)
                'last_name',  # or first_name for ex - atrelar a um campo
                ValidationError(
                    'Please, introduce your last name', code='invalid')
            )

        return last_name'''


'''
class AuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(),
        label='Username',
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password',)

    def clean(self):

        cleaned_data = self.cleaned_data  # data before added to database

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        # p campo password ja valida isto !!
        if User.objects.filter(username=username).get('password') != password:
            self.add_error('password',
                           ValidationError('Passoword doesn\'t match with this username :(',
                                           code='invalid'))

        return super().clean()

    def clean_username(self):
        username = self.cleaned_data.get('email')
        # check if email exists
        if not User.objects.filter(username=username).exists():
            self.add_error('username',
                           ValidationError('Username does not exists!',
                                           code='invalid'))
        return username
'''
