from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductsListView(ListView):
    """
    Просмотр на странице всех объектов Продукт
    """
    model = Product

    def get_context_data(self, **kwargs):
        """
        Вывод на экран активной версии продукта если таковая имеется
        """
        context = super().get_context_data(**kwargs)
        for product in context['object_list']:
            product.active_version = product.version_set.filter(is_current=True).first()
        return context


class ProductDetailView(DetailView):
    """
    Детальный просмотр объекта Продукт
    """
    model = Product


class ProductCreateView(CreateView):
    """
    Формирование отображения страницы при создании объекта Продукт
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    """
    Формирование отображения страницы при обновлении объекта Продукт
    """
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    """
    Формирование отображения страницы при удалении объекта Продукт
    """
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsListView(ListView):
    """
    Просмотр на странице всех объектов Контакт
    """
    model = Contact
