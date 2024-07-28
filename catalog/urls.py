from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),

    path('products/<int:pk>', ProductListView.as_view(), name='product_list'),
    path('/<int:pk>', cache_page(90)(ProductDetailView.as_view()), name='product_detail'),
    path('/create', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('/edit/<int:pk>', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', ContactTemplateView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', never_cache(BlogCreateView.as_view()), name='create_blog'),
    path('blog/edit/<int:pk>', never_cache(BlogUpdateView.as_view()), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
]
