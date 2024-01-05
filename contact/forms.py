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
                  'phone',)  # , 'email', 'description',
        # 'show', 'picture', 'category', 'owner',)

        # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
        # campo a ser renderizado! ex forms.PasswordInput()
        # criar novo widget!
        # widgets = {'first_name': forms.TextInput(
        #    attrs={'class': 'class-a class-b',
        #           'placeholder': 'Write here'}  # renderiza classe no html!
        # )}

    def clean(self):  # sobrescrever metodo
        # cleaned_data = self.cleaned_data  # data before added to database

        self.add_error(
            'first_name',  # or first_name for ex - atrelar a um campo
            ValidationError('Error 1:', code='invalid')
        )

        self.add_error(
            'first_name',  # or first_name for ex - atrelar a um campo
            ValidationError('Error 2:', code='invalid')
        )
