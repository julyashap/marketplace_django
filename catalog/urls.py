from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('/<int:pk>', cache_page(ProductDetailView.as_view()), name='product_detail'),
    path('/create', ProductCreateView.as_view(), name='product_create'),
    path('/edit/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', ContactTemplateView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='create_blog'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
]
