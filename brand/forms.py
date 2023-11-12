from django import forms
from django.forms import widgets
from brand.models import *
from ckeditor.widgets import CKEditorWidget

class brand_form(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'brief_explamations',
            'descriptions',
            'logo_1th',
            'logo_2th',
            'logo_blured',
            'logo_slider',


        ]
        widgets = {
            'brief_explamations': forms.Textarea(attrs={ 'class':'form-control', 'placeholder': ' توضیحات کوتاه ', 'type':'text', 'cols':'40', 'rows':'22'  }),
            'descriptions': forms.CharField(widget=CKEditorWidget()),
            'logo_1th': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو اول ', 'type':'file', 'data-default-file':'لوگو اول را انتخاب کنید', 'data-max-file-size':'2M' }),
            'logo_2th': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو دوم ', 'type':'file', 'data-default-file':'لوگو دوم را انتخاب کنید', 'data-max-file-size':'2M' }),
            'logo_blured': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو بلور ', 'type':'file', 'data-default-file':'لوگو بلور را انتخاب کنید', 'data-max-file-size':'2M' }),
            'logo_slider': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو اسلایدر ', 'type':'file', 'data-default-file':'لوگو اسلایدر را انتخاب کنید', 'data-max-file-size':'2M' }),
        }

