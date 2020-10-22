from django.urls import path
from writer.views import allOferts, Login, order, Register, upload_file, get_writer_photo

urlpatterns = [
    path('oferty', allOferts, name='oferty'),
    path('login', Login, name='login'),
    path('rejestracja', Register, name='rejestracja'),
    path('zamowienie/<int:id>', order, name='zamowienie'),
    path('profil', upload_file, name='profile'),
    # username
    path('api/profile_photo/<str:pk>', get_writer_photo, name='profile_photo')
]