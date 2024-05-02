from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsListView(ListView):
    model = Contact
