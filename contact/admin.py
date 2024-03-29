from django.contrib import admin
from contact import models
# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)
    ordering = ('id',)
    list_filter = ('created_data',)
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10  # numero de cenas por pagina
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name',
    list_editable = 'show',  # just to be easier to remove some of them
    list_display_links = 'id', 'phone'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    ordering = ('id',)
