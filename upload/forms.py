from django import forms
from .models import Album,Document

class AlbumForm(forms.ModelForm):
    class Meta:
        model	= Album
        fields	= [ "photo" ]

class DocumentForm(forms.ModelForm):
    class Meta:
        model	= Document
        fields	= [ "file" ]

