from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        min_length=2,
        max_length=200,
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
