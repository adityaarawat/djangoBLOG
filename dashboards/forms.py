from django import forms
from blog.models import category,blog
class categoryAdd(forms.ModelForm):
    class Meta:
        model=category
        fields='__all__'


class BlogsAdd(forms.ModelForm):
    class Meta:
        model=blog
        fields=('title','category','featured_image','status','blog_body','short_description','is_featured')
