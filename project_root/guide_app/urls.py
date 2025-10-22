from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.mendic, name='mendic'),
    # path('maps-proxy', views.maps_proxy, name='maps_proxy'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)