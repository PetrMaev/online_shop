from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Category


def home_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context=context)


def contacts_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо {name}! Сообщение отправлено.")
    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product_name': product.product_name,
        'description': product.description,
        'price': product.price,
    }
    return render(request, 'catalog/product_detail.html', context=context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context=context)


def categories_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'catalog/categories_list.html', context=context)
