from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name',
                  'phone',)  # , 'email', 'description',
        # 'show', 'picture', 'category', 'owner',)

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
