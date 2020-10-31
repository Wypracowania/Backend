from rest_framework import serializers
from .models import Bid, WriterImage
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

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterImage
        fields = ['image']

    def get_photo_url(self, image):
        request = self.context.get('request')
        photo_url = image.url
        return request.build_absolute_uri(photo_url)

class BidSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    order  = OrderSerializer()
    image  = ImageSerializer(read_only=True)

    class Meta:
        model = Bid
        fields = "__all__"
