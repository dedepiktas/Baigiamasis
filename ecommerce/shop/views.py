from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse
from .models import Product, Category, Comment
from .forms import CommentForm

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

class ProductDetailView(DetailView, FormView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('shop:product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.product = self.get_object()
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(product=self.object)
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        return context

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Implement your cart logic here
    return redirect('shop:product_detail', pk=pk)
