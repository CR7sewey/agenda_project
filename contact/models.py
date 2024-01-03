
from email.policy import default
from tabnanny import verbose
from django.utils import timezone
from django.db import models

# Create your models here.
# migrate if some change!!

# table contact

# id -> PRIMARY KEY - automatico


class Category(models.Model):
    # https://docs.djangoproject.com/pt-br/4.2/ref/models/options/
    class Meta:  # change name of Model in django admin
        verbose_name = "Category"  # https://www.youtube.com/watch?v=iIsLwz_vkzA
        verbose_name_plural = "Categories"

    name = models.CharField(default='name', max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


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
    # on_delete - quando apagar a cateogry tmb apagar o Contact (models.CASCADE)
    # ou outras cenas (meter nulo - SET_NULL)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    # owner = models.ForeignKey()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
