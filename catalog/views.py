from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm
from .models import Category, Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'

    def test_func(self):
        product = self.get_object()
        return (
                product.owner == self.request.user or
                self.request.user.has_perm('catalog.can_unpublish_product')
        )

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для удаления этого продукта")

    def custom_permission_denied(request, exception=None):
        return HttpResponseForbidden(render(request, '403.html'))

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        return (
                product.owner == self.request.user or
                self.request.user.has_perm('catalog.delete_product')
        )

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для удаления этого продукта")

    def custom_permission_denied(request, exception=None):
        return HttpResponseForbidden(render(request, '403.html'))


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publish=True)


class ProductDetailVew(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductsAllListView(ListView):
    model = Product
    template_name = 'catalog/product_list_all.html'
    context_object_name = 'products'


class CategoriesListVew(ListView):
    model = Category
    template_name = 'catalog/categories_list.html'
    context_object_name = 'categories'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
