from django import forms
from .models import Feed, Reaction


class FeedForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField(
        min_length=2,
        widget=forms.Textarea()
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
