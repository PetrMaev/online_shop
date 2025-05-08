from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('categories_list/', views.categories_list, name='categories_list'),
]
