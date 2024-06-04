from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Contact, Category
from catalog.services import get_category_from_cache


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

    def get_queryset(self):
        """
        Фильтрация объектов по признаку публикации
        """
        super().get_queryset().filter(publication=True)
        return get_category_from_cache(Product)


class ProductDetailView(DetailView):
    """
    Детальный просмотр объекта Продукт
    """
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Формирование отображения страницы при создании объекта Продукт
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = "/users/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Формирование отображения страницы при обновлении объекта Продукт
    """
    model = Product
    form_class = ProductForm
    login_url = "/users/login/"
    redirect_field_name = "redirect_to"

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_publication') and user.has_perm(
                'catalog.can_edit_description') and user.has_perm('catalog.can_edit_category'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Формирование отображения страницы при удалении объекта Продукт
    """
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = "/users/login/"
    redirect_field_name = "redirect_to"


class ContactsListView(ListView):
    """
    Просмотр на странице всех объектов Контакт
    """
    model = Contact


class CategoryListView(ListView):
    """
    Просмотр на странице всех объектов Категории
    """
    model = Category

    def get_queryset(self):
        return get_category_from_cache(Category)
