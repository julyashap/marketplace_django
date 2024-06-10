from django.shortcuts import render
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    for i in range(5):
        print(products[i])

    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')
