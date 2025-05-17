from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductsListView, ProductDetailVew, CategoriesListVew, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailVew.as_view(), name='product_detail'),
    path('categories_list/', CategoriesListVew.as_view(), name='categories_list'),
]
