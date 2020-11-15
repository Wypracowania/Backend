from django.urls import path
from user.views import (
    NewOrder,
    GetOrders,
    GetOrderDetail,
    GetBids,
    Payment,
    GetAllOrders,
    getConversation,
    check_unreaded_messages,
    get_messages,
    create_message,
    read_messages,
    check_for_message
)

urlpatterns = [
    path('nowe-zamowienie', NewOrder),
    path('order/<int:id>/', GetOrderDetail),
    path('bids/<str:username>/<int:id>/', GetBids),
    path('all/<str:username>/', GetOrders),
    path('all/', GetAllOrders),
    path('payment', Payment),
    path('get-conversations/<str:username>', getConversation),
    # user ID
    path('check-unreaded-messages/<str:username>', check_unreaded_messages),
    path('check-for-message/<str:username>', check_for_message),
    # conversation ID
    path('get-messages/<int:id>', get_messages),
    # conversation ID
    path('create-message/<int:id>', create_message),
    path('read-messages/<int:id>', read_messages)
]