from django import forms
from .models import Feed, Reaction


class FeedForm(forms.ModelForm):
    title = forms.CharField(
        min_length=2,
        max_length=100,
        label='글 제목',
        widget=forms.TextInput(attrs={
            'placeholder': '내용을 입력합시다.',
        }
        )
    )

    content = forms.CharField(
        min_length=2,
        widget=forms.Textarea(attrs={
            'placeholder': '잘 좀 써봅시다.',
        }),
        label='글 내용',
    )
    
    class Meta:
        model = Feed
        fields = ('title', 'content', )  # like_users


class ReactionForm(forms.ModelForm):

    content = forms.CharField(
        min_length=2,
        max_length=200,
    )

    class Meta:
        model = Reaction
        fields = ('content', )
