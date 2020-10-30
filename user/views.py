from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.serializers import OrderSerializer
from rest_framework.decorators import api_view
from user.models import Order
from writer.models import Bid
from writer.serializers import BidSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
import stripe
# Create your views here.
stripe.api_key = 'sk_test_51H85zIGFoPYSSbM6SRULGQFrRbwm0DDQmEjHsrNUsWJN29ou60GbVa1hXuTvgbe7P6Z7oymrXHRG9r5AszUzXi9Y009VfmcAGj'

# Create your views here.

@api_view(['POST'])
def NewOrder(request):
    data = json.loads(request.body)
    username = data['username']
    document = data['document']
    category = data['category']
    topic    = data['topic']
    pages    = data['pages']
    deadline = data['deadline']
    instruct = data['instructions']

    user = User.objects.get(username=username)
    if user is not None:
        new_order = Order.objects.create(
            owner = user,
            document = document,
            category = category,
            topic = topic,
            pages = pages,
            deadline = deadline,
            instructions = instruct
        )
    if new_order:
        new_order.save()
        return JsonResponse({"id": new_order.id})
    return JsonResponse({"error": ":c"})

@api_view(['GET'])
def GetOrders(request, username):
    try:
        user = User.objects.get(username= username)
        user_orders = Order.objects.filter(owner = user)
    except:
        user_orders = None
    Serialized = OrderSerializer(user_orders, many=True)
    return Response(Serialized.data)

@api_view(['GET'])
def GetOrderDetail(request, id):
    Serialized = OrderSerializer(Order.objects.get(id = id))
    return Response(Serialized.data)

@api_view(['GET'])
def GetBids(request, id):
    order = Order.objects.get(id = id)
    Bids  = Bid.objects.filter(order=order)
    Serialized = BidSerializer(Bids, many=True)
    return Response(Serialized.data)

@api_view(['GET', 'POST'])
def Payment(request):
    intent = stripe.PaymentIntent.create(
    amount=1099,
    currency='pln',
    # Verify your integration in this guide by including this parameter
    metadata={'integration_check': 'accept_a_payment'},
    )
    print(intent['client_secret'])
    return Response({
        'clientSecret': intent['client_secret']
    })