from django.shortcuts import render
from .models import MenuAttribute
# Create your views here.
def menu_list(request):
    data=MenuAttribute.objects.all().order_by('-id')
    return render(request,'index.html',{'data':data})
