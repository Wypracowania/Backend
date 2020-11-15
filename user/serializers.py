from rest_framework import serializers
from .models import ( 
    Order,
    Conversation,
    Message
)
from writer.models import Writer
from writer.serializers import UserSerializer
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name']
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'document',
            'category',
            'topic',
            'pages', 
            'deadline', 
            'instructions'
        ]


class ChatUserSerializer(serializers.RelatedField):
        def to_representation(self, value):
            username = value.username
            return username


class ChatWriterSerializer(serializers.ModelSerializer):
    writer = UserSerializer()

    class Meta:
        model = Writer
        fields = [
            'writer',
            'mini_photo'
        ]


class UnreadedMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            'unreaded_messages',
            'last_message'
        ]


class ConversationSerializer(serializers.ModelSerializer):
    writer = ChatWriterSerializer()
    customer = ChatUserSerializer(read_only=True)
    
    class Meta:
        model = Conversation
        fields = [
            'id',
            'writer',
            'customer',
            'unreaded_messages',
            'last_message',
            'last_sended'
        ]
        

class MessagesSerializer(serializers.ModelSerializer):
    # author = ChatUserSerializer(read_only=True)
    author = UserSerializer()
    
    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'created_at',
            'author'
        ]
