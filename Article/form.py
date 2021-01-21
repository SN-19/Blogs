from django import forms
from Article.models import Post
from tinymce.widgets import TinyMCE


class BlogForm(forms.ModelForm):

    class Meta:
        model=Post
        fields = ['description','content']
        widgets = {
            'name': TinyMCE(attrs={'cols': 80, 'rows': 30,'class': 'form-control'}),
        }

