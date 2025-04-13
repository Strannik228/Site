from django.shortcuts import render
from .models import Dish, Category

def home(request):
    return render(request, 'main/home.html')

def menu(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    return render(request, 'main/menu.html', {'categories': categories, 'dishes': dishes})
