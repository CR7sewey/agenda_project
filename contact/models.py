
from email.policy import default
from django.utils import timezone
from django.db import models

# Create your models here.
# migrate if some change!!

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
    show = models.BooleanField(default=True)
    # not necessary to put an image
    # in media a pictures folder and a year and month folder are created
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    # owner = models.ForeignKey()
    # category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    ...
