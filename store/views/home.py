from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')

def get(self, request):
    products = None
    categories = Category.get_all_categories()

