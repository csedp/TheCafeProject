from django.contrib import admin
from django.urls import path
from menu import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name= "home"),
    path("menu",views.menu, name= "menu")  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)