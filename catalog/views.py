from django.http import HttpResponse
from django import forms
from django.views.generic import DetailView, ListView, FormView

from .models import Product, Category


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailVew(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CategoriesListVew(ListView):
    model = Category
    template_name = 'catalog/categories_list.html'
    context_object_name = 'categories'


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class ContactsView(FormView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = '/contacts/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        return HttpResponse(f'Спасибо {name}! Сообщение отправлено.')
