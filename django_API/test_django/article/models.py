from django.db import models


class Author(models.Model):
    name = models.CharField("Автор", max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Article(models.Model):
    title = models.CharField("Название", max_length=120)
    description = models.TextField("описание")
    body = models.TextField("текст")
    author = models.ForeignKey(Author, verbose_name="Автор", related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
