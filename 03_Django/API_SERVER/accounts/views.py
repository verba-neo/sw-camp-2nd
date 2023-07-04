from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()


@api_view(['GET'])
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    serializer = UserSerializer(profile_user)
    
    return Response(serializer.data, status=201)


    