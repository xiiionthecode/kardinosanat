from django import forms
from django.forms import widgets
from category.models import *
from ckeditor.widgets import CKEditorWidget

class ProductCategory_form(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = [
            'vector',
        ]

        widgets = {
            'vector': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' وکتور دسته بندی ', 'type':'file', 'data-default-file':'وکتور دسته بندی را انتخاب کنید', 'data-max-file-size':'2M' }),
        }


class ProductCategorySubset_form(forms.ModelForm):
    class Meta:
        model = ProductCategorySubset
        fields = [
            'vector',
        ]

        widgets = {
            'vector': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' وکتور دسته بندی ', 'type':'file', 'data-default-file':'وکتور دسته بندی را انتخاب کنید', 'data-max-file-size':'2M' }),
        }

