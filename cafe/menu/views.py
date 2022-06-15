from django.shortcuts import render
from .models import Menu, Category

# Create your views here.
def menu(request):
    data=Menu.objects.all().order_by('-id')
    return render(request, 'menu.html', {'data': data})

def index(request):
    return render(request, 'index.html')

# Product List According to Category
def category_product_list(request,cat_id):
	category=Category.objects.get(id=cat_id)
	data=Menu.objects.filter(category=category).order_by('-id')
	return render(request,'category_product_list.html',{
			'data':data,
			})