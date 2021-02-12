from django import forms 
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'slug')


class CommentForm(forms.Form):
    body = forms.CharField(label='Comment', widget=forms.Textarea)





