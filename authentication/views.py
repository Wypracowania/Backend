from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import Group
import json

# Create your views here.

@api_view(['POST'])
def Login(request):
    data = request.data
    password = data['password']
    username = data['username']
    userAuth = authenticate(username=username, password=password)
    if userAuth:
        user  = User.objects.get(username=username)
        token = Token.objects.get(user=user)
        return Response({'token': token.key})
    else:
        return Response({'token': 'Nie udało się zalogować'})

@api_view(['POST'])
def Register(request):
    password = request.data['password']
    username = request.data['username']
    try:
        user  = User.objects.create_user(username=username, password=password, email="kk2k50@gmail.com")
        token = Token.objects.create(user=user)
        # Adding user group
        group = Group.objects.get(name='customer') 
        group.user_set.add(user)
        user.save()
    except:
        user = None
    if user is not None:
        return Response({'token': token.key})
    else:
        return Response({'token': 'Nie udało się zarejestrować'})