from django.urls import path
from authentication.views import Login, Register

urlpatterns = [
    path('login', Login),
    path('rejestracja', Register),
]