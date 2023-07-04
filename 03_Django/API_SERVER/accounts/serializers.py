from rest_framework import serializers
from django.contrib.auth import get_user_model

from board.models import Article

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('title', )

    article_set = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'article_set')