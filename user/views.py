from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.serializers import OrderSerializer
from rest_framework.decorators import api_view
from user.models import Order
from rest_framework.response import Response
import json
# Create your views here.

@api_view(['POST'])
def NewOrder(request):
    data = json.loads(request.body)
    document = data['document']
    category = data['category']
    topic    = data['topic']
    pages    = data['pages']
    deadline = data['deadline']
    instruct = data['instructions']
    new_order = Order.objects.create(
        document=document,
        category=category,
        topic=topic,
        pages=pages,
        deadline=deadline,
        instructions=instruct
    )
    if new_order:
        new_order.save()
        return JsonResponse({"Utworzono pomyślnie": "true"})
    return JsonResponse({"error": ":c"})

@api_view(['GET'])
def GetOrders(request):
    Serialized = OrderSerializer(Order.objects.all(), many=True)
    return Response(Serialized.data)

