from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    data=Menu.objects.all().order_by('-id')
    return render(request, 'menu.html', {'data': data})