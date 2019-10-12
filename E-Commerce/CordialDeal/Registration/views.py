from .models import MyModel, Order
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.
def register(request):  # Index of a page
    products = MyModel.objects.all
    context = Order.objects.all()
    return render(request, 'home.html', {'products': products, 'contexts': context})


# Create your views here.

def general(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your account has been created Successfully! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    products = MyModel.objects.all
    return render(request, 'home.html', {'products': products})


@login_required
def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html', {})
