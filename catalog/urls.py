from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),

    path('products/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', cache_page(90)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
]
