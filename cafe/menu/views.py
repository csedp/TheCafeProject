from django.shortcuts import render
from .models import Menu, Category

# Create your views here.
def menu(request):
    data=Menu.objects.all().order_by('-id')
    return render(request, 'menu.html', {'data': data})

def index(request):
    return render(request, 'index.html')

# Product List According to Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})