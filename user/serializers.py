from rest_framework import serializers
from .models import Order
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name']
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'document', 'category', 'topic', 'pages', 'deadline', 'instructions']