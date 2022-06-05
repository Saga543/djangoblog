from django import forms
from .models import Post

'''
Klasa dziedziczy po klasie frameworka Django, odpowiada za zamieszczanie postów
'''
class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znaków')

    class Meta:
        model = Post
        fields = ['title','text']