from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.serializers import (
    OrderSerializer,
    ConversationSerializer,
    UnreadedMessagesSerializer,
    MessagesSerializer
)
from rest_framework.decorators import api_view
from user.models import (
    Order,
    Conversation,
    Message
)
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
    username = request.data.get('username')
    document = request.data.get('document')
    category = request.data.get('category')
    topic    = request.data.get('topic')
    pages    = request.data.get('pages')
    deadline = request.data.get('deadline')
    instruct = request.data.get('instructions')

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
def GetAllOrders(request):
    user_orders = Order.objects.all()
    Serialized = OrderSerializer(user_orders, many=True)
    return Response(Serialized.data)

@api_view(['GET'])
def GetOrderDetail(request, id):
    Serialized = OrderSerializer(Order.objects.get(id = id))
    return Response(Serialized.data)

@api_view(['GET'])
def GetBids(request, username, id):
    owner = User.objects.get(username=username)
    order = Order.objects.get(id = id, owner=owner)
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

@api_view(['GET'])
def getConversation(request, username):
    customer = User.objects.get(username=username)
    conversations = Conversation.objects.filter(customer=customer)
    serialized = ConversationSerializer(conversations, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def check_unreaded_messages(request, username):
    customer = User.objects.get(username=username)
    conversations = Conversation.objects.filter(customer=customer)
    serialized = UnreadedMessagesSerializer(conversations, many=True)
    return Response(serialized.data)
    
@api_view(['GET'])
def check_for_message(request, username):
    customer = User.objects.get(username=username)
    conversations = Conversation.objects.filter(customer=customer)
    for x in conversations:
        if x.unreaded_messages():
            return JsonResponse({"new_message": True}, safe=False)
    return JsonResponse({"new_message": False}, safe=False)

@api_view(['GET'])
def get_messages(request, id):
    conversation = Conversation.objects.get(id=id)
    messages = Message.objects.filter(conversation=conversation)
    serialized = MessagesSerializer(messages, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def read_messages(request, id):
    conversation = Conversation.objects.get(id=id)
    messages = Message.objects.filter(conversation=conversation)
    for message in messages:
        if message.readed == False:
            message.readed = True
            message.save()
    return JsonResponse({"x": "xdd"}, safe=False)


@api_view(['POST'])
def create_message(request, id):
    text = request.data.get('text')
    username = request.data.get('username')
    author = User.objects.get(username=username)
    try:
        conversation = Conversation.objects.get(id=id)
        message = Message.objects.create(
            conversation = conversation,
            text = text,
            author = author
        )
        message.save()
        messages = Message.objects.filter(conversation=conversation)
        serialized = MessagesSerializer(messages, many=True)
        return Response(serialized.data)
    except:
        pass
    return JsonResponse({"error": "message was not delivered"})

