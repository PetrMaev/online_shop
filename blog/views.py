from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView, TemplateView
from django.urls import reverse, reverse_lazy

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)


class ArticleAllListView(ListView):
    model = Article
    template_name = 'blog/articles_list_all.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'preview', 'is_public']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview', 'is_public']
    template_name = 'blog/article_edit.html'

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:articles_list')


class ContactView(TemplateView):
    template_name = 'blog/contacts.html'
