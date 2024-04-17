from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    """Отображение главной страницы и вывод в консоль последних 5 продуктов при любом GET запросе"""
    latest_products = Product.objects.order_by('-id')[:5]
    for product in latest_products:
        print(product)
    return render(request, 'catalog/home.html')


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
