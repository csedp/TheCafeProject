from django.shortcuts import render,redirect
from .models import Menu, Category
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
# Imports for Reordering Feature

from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class CustomLoginView(LoginView):
    template_name="login.html"
    fields="__all__"
    redirect_authenticated_user= True
    def get_success_url(self) -> str:
        return reverse_lazy('home')

class RegisterView(FormView):
    template_name="register.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).get(*args, **kwargs)

# Create your views here.
def menu(request):
    context={}
    if request.user.is_authenticated:
        context['p']="Logout"
    else:
        context['p']="Sign-in"
    data=Menu.objects.all().order_by('-id')
    context['data']=data
    return render(request, 'menu.html', context)

def index(request):
    if request.user.is_authenticated:
        context={"data":"Logout"}
    else:
        context={"data":"Sign-in"}
    return render(request, 'index.html',context)


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
