from django.urls import path

from catalog.apps import CatalogConfig

from .views import (CategoriesListVew, ContactsView, ProductCreateView,
                    ProductDeleteView, ProductDetailVew, ProductsListView,
                    ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="home"),
    path("catalog/new/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("catalog/contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/product_detail/<int:pk>/", ProductDetailVew.as_view(),name="product_detail"),
    path("catalog/categories_list/", CategoriesListVew.as_view(), name="categories_list"),
]
