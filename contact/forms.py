from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'class-a class-b',
                                      'placeholder': 'Write here'}  # renderiza classe no html!
                               ),
        help_text='Helpful text for user',
        label='First Name'
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
                  'category',)

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
