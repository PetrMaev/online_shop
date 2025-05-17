from django.urls import path
from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    ContactView, ArticleAllListView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', ArticleListView.as_view(), name='articles_list'),
    path('blogs/articles_list_all/', ArticleAllListView.as_view(), name='articles_list_all'),
    path('blogs/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('blogs/new/', ArticleCreateView.as_view(), name='article_create'),
    path('blogs/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('blogs/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('blogs/contacts/', ContactView.as_view(), name='contacts'),
]