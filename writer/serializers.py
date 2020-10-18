from rest_framework import serializers
from .models import Bid
from user.models import Order
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['topic']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class BidSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    order  = OrderSerializer()
    class Meta:
        model = Bid
        fields = "__all__"
