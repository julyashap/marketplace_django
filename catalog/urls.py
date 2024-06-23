from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('home/<int:pk>/', ProductDetailView.as_view(), name='product_item')
]
