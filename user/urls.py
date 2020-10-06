from django.urls import path
from user.views import NewOrder, GetOrders

urlpatterns = [
    path('nowe-zamowienie', NewOrder),
    path('all', GetOrders)
]