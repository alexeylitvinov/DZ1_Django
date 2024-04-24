from django.core.paginator import Paginator
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    """Отображение главной страницы и вывод 4 продуктов с возможностью постраничного вывода продуктов"""
    products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {'products': products}

    # latest_products = Product.objects.order_by('-id')[:5]
    # for product in latest_products:
    #     print(product)
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Отображение страницы Контакты и вывод в форму контактов данных из БД"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}, phone: {phone}, message: {message}')
    p = Contact.objects.all()
    return render(request, 'catalog/contacts.html',
                  {'country': p[0].country, 'inn': p[0].inn, 'address': p[0].address})


def product(request, pk):
    """Отображение страницы Продукт и вывод в форму подробной информации о продукте"""
    get_product = Product.objects.get(pk=pk)
    context = {'product': get_product}
    return render(request, 'catalog/product.html', context)
