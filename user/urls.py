from django.urls import path
from user.views import NewOrder

urlpatterns = [
    path('nowe-zamówienie', NewOrder),
]