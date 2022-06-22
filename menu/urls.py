import imp
from django.contrib import admin
from django.urls import path
from menu import views
from .views import CustomLoginView,RegisterView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name= "home"),
    path("home",views.index, name= "home"),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
    path("menu",views.menu, name= "menu"),
    path("about",views.about, name= "about"),
    path("category",views.category_list, name= "category"),
    path('category-menu-list/<int:cat_id>',views.category_menu_list,name='category-menu-list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)