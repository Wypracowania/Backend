from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from user.models import Order
from django.shortcuts import redirect
from .forms import LoginForm, RegisterForm, WriterImageForm
from django.contrib.auth import authenticate, login as auth_login, logout
from .decorators import writer_required
from .models import (
    Bid, 
    Writer, 
    Rating
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    # ImageSerializer, 
    WriterSerializer,
    ReviewsSerializer
)
# Create your views here.

@writer_required(allowed_roles=['writer'])
def allOferts(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }
    return render(request, 'oferts.html', context)

def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('oferty')
            else:
                return HttpResponse('Nie udało się zalogować')
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})

def Register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = User.objects.create(username=username)
            user.set_password(password)
            group = Group.objects.get(name='writer') 
            group.user_set.add(user)
            if user:
                user.save()
                writer = Writer.objects.create(writer=user)
                writer.save()
                auth_login(request, user)
                return redirect('oferty')
            else:
                return HttpResponse('Nie udało się zarejestrować')
    else:
        form = RegisterForm()
    return render(request, 'rejestracja.html', {"form": form})

def order(request, id):
    order = Order.objects.get(id=id)
    try:
        writer = Writer.objects.get(writer=request.user)
        exist = Bid.objects.get(order=order, writer_details=writer)
    except:
        writer = None
        exist = None
    if exist is None:
        writer = Writer.objects.get(writer=request.user)
        bid = Bid.objects.create(order=order, message="Wykonam to zlecenie", price=120, writer_details=writer)
        bid.save()
        return HttpResponse('Oferta została złożona')
    else:
        return HttpResponse('Błąd, już złożyłeś/aś ofertę pod tym zleceniem')

def upload_file(request):
    if request.method == 'POST':
        form = WriterImageForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['image']
            user = request.user
            writer = Writer.objects.get(writer=user)
            writer.photo = file
            writer.save()
            return HttpResponse('Dodano zdjecie pomyslnie')
    else:
        form = WriterImageForm()
    return render(request, 'upload.html', {'form': form})

# @api_view(['GET'])
# def get_writer_photo(request, pk):
#     try:
#         writer = User.objects.get(username=pk)
#         writer_image = WriterImage.objects.get(writer=writer)
#     except:
#         writer = None
#         writer_image = None
#     serialized = ImageSerializer(writer_image, context={"request": request})
#     return Response(serialized.data)

@api_view(['GET'])
def get_writer_detail(request, pk):
    writer_detail = Writer.objects.get(id=pk)
    serialized = WriterSerializer(writer_detail)
    return Response(serialized.data)

@api_view(['GET'])
def get_reviews(request, pk):
    writer = User.objects.get(id=pk)
    worker = Writer.objects.get(writer=writer)
    rating = Rating.objects.filter(worker=worker)
    serialized = ReviewsSerializer(rating, many=True)
    return Response(serialized.data)