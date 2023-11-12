from django import forms
from django.forms import widgets
from blog.models import Blog, BlogTag
from ckeditor.widgets import CKEditorWidget

class blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'description',
            'poster',
            'second_poster',
            'article_text',


        ]
        widgets = {
            'description': forms.Textarea(attrs={ 'class':'form-control', 'placeholder': ' توضیخات کوتاه ', 'type':'text', 'cols':'40', 'rows':'7'  }),
            'poster': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو ', 'type':'file', 'data-default-file':'عکس بلاگ را انتخاب کنید', 'data-max-file-size':'2M' }),
            'second_poster': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو ', 'type':'file', 'data-default-file':'عکس بلاگ را انتخاب کنید', 'data-max-file-size':'2M' }),
            'article_text': forms.CharField(widget=CKEditorWidget())
        }

