from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json

# Create your views here.

@api_view(['POST'])
def Login(request):
    data = json.loads(request.body)
    password = data['password']
    username = data['username']
    userAuth = authenticate(username=username, password=password)
    if userAuth:
        user  = User.objects.get(username=username)
        token = Token.objects.get(user=user)
        return JsonResponse(token.key, safe=False)
    else:
        print('fail')
    return HttpResponse('woof')

@api_view(['POST'])
def Register(request):
    # data = json.loads(request.body)
    password = request.data['password']
    username = request.data['username']
    try:
        user = User.objects.create_user(username=username, password=password, email="k@gmail.com")
        token = Token.objects.create(user=user)
        user.save()
        print(token.key)
    except:
        user = None
    if user is not None:
        print('registered')
    else:
        print('fail')
    return HttpResponse('woof')