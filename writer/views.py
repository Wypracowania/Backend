from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from user.models import Order
from django.shortcuts import redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login as auth_login
from .decorators import writer_required
from .models import Bid
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
                return HttpResponse('xD')
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
            user = User.objects.create(username=username, password=password)
            group = Group.objects.get(name='writer') 
            group.user_set.add(user)
            if user:
                user.save()
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
        exist = Bid.objects.get(offer=order, writer=request.user)
    except:
        exist = None
    if exist is None:
        bid = Bid.objects.create(offer=order, message="Wykonam to zlecenie", price=120, writer=request.user)
        bid.save()
        return HttpResponse('Oferta została złożona')
    else:
        return HttpResponse('Błąd, już złożyłeś ofertę pod tym zleceniem')
