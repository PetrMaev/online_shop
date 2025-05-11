from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['title', ]
