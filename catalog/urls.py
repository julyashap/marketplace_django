from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('home/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
]
