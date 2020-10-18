from django.urls import path
from writer.views import allOferts, Login, order, Register

urlpatterns = [
    path('oferty', allOferts, name='oferty'),
    path('login', Login, name='login'),
    path('rejestracja', Register, name='rejestracja'),
    path('zamowienie/<int:id>', order, name='zamowienie')
]