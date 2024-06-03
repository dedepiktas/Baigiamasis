from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Comment  # Ensure models are imported and used
from .forms import CommentForm

def store(request):
    all_products = Product.objects.all()
    context = {'my_products': all_products}
    return render(request, 'store/store.html', context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'category': category, 'products': products})

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    comments = product.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
            return redirect('product_detail', product_slug=product.slug)
    else:
        form = CommentForm()

    return render(request, 'store/product-info.html', {'product': product, 'comments': comments, 'form': form})
