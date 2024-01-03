
from django.utils import timezone
from django.db import models

# Create your models here.

# table contact

# id -> PRIMARY KEY - automatico


class Contact(models.Model):
    # max num of char, not null and not blank!!
    first_name = models.CharField(max_length=50)  # , null=False, blank=False)
    # , null=False, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    # category = models.ForeignKey(Category)
    # show = models.BooleanField()
    # owner = models.ForeignKey()
    # picture = models.ImageField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

# class Category(models.Model):
#    ...
