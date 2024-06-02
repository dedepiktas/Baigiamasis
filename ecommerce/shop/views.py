# shop/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView  # Add these imports
from .models import Product, Category

class HomePageView(TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['new_products'] = Product.objects.order_by('-id')[:4]  # Display 4 newest products
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
