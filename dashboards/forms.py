from django import forms
from blog.models import category
class categoryAdd(forms.ModelForm):
    class Meta:
        model=category
        fields='__all__'