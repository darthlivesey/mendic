from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

YANDEX_MAPS_URL = "https://api-maps.yandex.ru/v3/?apikey=35fbf851-eea3-4819-bf08-558fcbb08e39&lang=ru_RU"

def mendic(request):
    return render(request, "main.html")

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'Регистрация прошла успешно!')
            login(request, user)
            return redirect('mendic')
        else:
            return render(request, 'reg.html', {'form': form})
    else:  # GET request
        form = RegisterForm()
        return render(request, 'reg.html', {'form': form})