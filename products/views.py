from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from products.forms import ProductForm
from products.models import Products


class ProductCreateView(CreateView):
    template_name = 'products/create_product.html'
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('home')

class ProductListView(ListView):
    template_name = 'products/products_list_view.html'
    model = Products
    context_object_name = 'all_products'
