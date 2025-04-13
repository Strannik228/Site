from django.contrib import admin
from .models import Dish, Category

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Category)

