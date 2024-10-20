from django.urls import path
from django.views.decorators.cache import never_cache
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create_blog'),
    path('edit/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
]
