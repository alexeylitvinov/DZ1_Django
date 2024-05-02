from django.urls import path

from catalog.views import ProductsListView, ProductDetailView, ContactsListView

urlpatterns = [
    path('', ProductsListView.as_view()),
    path('contacts/', ContactsListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
