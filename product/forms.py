from django import forms
from django.forms import widgets
from .models import *
from ckeditor.widgets import CKEditorWidget

class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'poster',
            'review',


        ]
        widgets = {
            'poster': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو ', 'type':'file', 'data-default-file':'عکس محصول را انتخاب کنید', 'data-max-file-size':'2M' }),
            'review': forms.CharField(widget=CKEditorWidget())
        }

class ProductImage_form(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'image',


        ]
        widgets = {
            'image': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو ', 'type':'file', 'data-default-file':'عکس بلاگ را انتخاب کنید', 'data-max-file-size':'2M' }),
        }