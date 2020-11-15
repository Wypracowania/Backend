from django.contrib import admin
from user.models import (
    Order,
    OrderInfo,
    Conversation,
    Message
)
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderInfo)
admin.site.register(Conversation)
admin.site.register(Message)