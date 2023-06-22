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
        # fields = ('title', 'content')
        exclude = ('user', )


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        min_length=2,
        max_length=200,
    )

    class Meta:
        model = Comment
        # 아래 두개중 택 1
        fields = ('content', )
        # all 에서 빼는게 기본값
        # exclude = ('article', 'user',) 
