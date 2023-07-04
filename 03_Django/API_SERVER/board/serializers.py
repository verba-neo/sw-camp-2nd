from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Article

User = get_user_model()



class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email',)

    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'user')



class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)

    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('pk', 'title', 'user')