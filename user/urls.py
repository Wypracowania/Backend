from django.urls import path
from user.views import (
    NewOrder,
    GetOrders,
    GetOrderDetail,
    GetBids,
    Payment,
    GetAllOrders
)

urlpatterns = [
    path('nowe-zamowienie', NewOrder),
    path('order/<int:id>/', GetOrderDetail),
    path('bids/<int:id>/', GetBids),
    path('all/<str:username>/', GetOrders),
    path('all/', GetAllOrders),
    path('payment', Payment)
]