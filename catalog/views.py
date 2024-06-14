from django.shortcuts import render
from catalog.models import Product, Contact


def home(request):
    products = Product.objects.all()
    for i in range(5):
        print(products[i])

    return render(request, 'catalog/home.html')


def contacts(request):
    contact = Contact.objects.get(pk=1)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    context = {
        'object': contact
    }

    return render(request, 'catalog/contacts.html', context)


def product_item(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'object': product
    }

    return render(request, 'catalog/product_item.html', context)
