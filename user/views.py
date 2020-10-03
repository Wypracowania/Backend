from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.serializers import OrderSerializer
from rest_framework.decorators import api_view
from user.models import Order
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def NewOrder(request):
    woof = Order.objects.get(id=1)
    serializer = OrderSerializer(woof)
    # if serializer.is_valid():
    #     serializer.save()
    return Response(serializer.data)
