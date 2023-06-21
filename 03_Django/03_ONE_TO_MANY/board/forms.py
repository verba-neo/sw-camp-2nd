from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        min_length=2,
        max_length=100,
    )

    content = forms.CharField(
        min_length=2,
        widget=forms.Textarea(attrs={
          'class': 'my-text-area',
        })
    )
    
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        min_length=2,
        max_length=200,
    )

    class Meta:
        model = Comment
        fields = ('content', )
