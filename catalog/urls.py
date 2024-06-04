from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.views import ProductsListView, ProductDetailView, ContactsListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', never_cache(ProductsListView.as_view()), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsListView.as_view(), name='contacts_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
]
