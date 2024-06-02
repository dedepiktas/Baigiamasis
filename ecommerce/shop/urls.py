from django.urls import path
from .views import ProductListView, ProductDetailView, HomePageView, add_to_cart, CategoryDetailView

app_name = 'shop'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),  # Add this line
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
]
