from django.contrib import admin

# Register your models here.
# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/ == #

from django.contrib import admin
from .models import Album,Document

class AlbumAdmin(admin.ModelAdmin):
    list_display	= [ "id", "photo" ]

class DocumentAdmin(admin.ModelAdmin):
    list_display	= [ "id", "file" ]


admin.site.register(Album,AlbumAdmin)
admin.site.register(Document,DocumentAdmin)
