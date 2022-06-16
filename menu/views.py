from django.shortcuts import render
from .models import Menu, Category

# Create your views here.
def menu(request):
    data=Menu.objects.all().order_by('-id')
    return render(request, 'menu.html', {'data': data})

def index(request):
    return render(request, 'index.html')


def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})

# Product List According to Category
def category_menu_list(request,cat_id):
	cat=Category.objects.get(id=cat_id)
	data=Menu.objects.filter(category=cat).order_by('-id')
	return render(request,'category_menu_list.html',{
			'data':data,
			})
