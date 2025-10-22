from django.shortcuts import render
from django.http import HttpResponse
import requests

YANDEX_MAPS_URL = "https://api-maps.yandex.ru/v3/?apikey=35fbf851-eea3-4819-bf08-558fcbb08e39&lang=ru_RU"

def mendic(request):
    return render(request, "main.html")

def registration(request):
    return render(request, "reg.html")

# def maps_proxy(request):
#     try:
#         response = requests.get(YANDEX_MAPS_URL)
#         response.raise_for_status()  # Проверяем статус ответа
        
#         # Возвращаем контент с правильным Content-Type
#         return HttpResponse(
#             response.content,
#             content_type=response.headers.get('Content-Type', 'application/javascript')
#         )
#     except requests.RequestException as e:
#         # В случае ошибки возвращаем пустой модуль
#         return HttpResponse(
#             "console.error('Yandex Maps API loading error');",
#             content_type="application/javascript"
#         )