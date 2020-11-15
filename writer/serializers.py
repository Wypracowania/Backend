from rest_framework import serializers
from .models import (
    Bid,
    Writer, 
    Rating
)
from user.models import Order
from django.contrib.auth.models import User


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['topic']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class CustomerSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class CategoriesField(serializers.RelatedField):
    def to_representation(self, value):
        return value.category


class ReviewsSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = [
            'customer', 
            'rate', 
            'opinion'
        ]


class WriterSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    categories = CategoriesField(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = [
            'rate',
            'total_rates',
            'writer',
            'description',
            'categories',
            'photo',
            'mini_photo'
        ]
    

class BidSerializer(serializers.ModelSerializer):
    writer_details = WriterSerializer()
    order  = OrderSerializer()

    class Meta:
        model = Bid
        fields = "__all__"