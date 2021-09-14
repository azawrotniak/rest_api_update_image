from django.contrib import admin

from .models import Account, Image, Person


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'image',
    ]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'account',
    ]