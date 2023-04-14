from django.db import models
from django.utils.timezone import now
from django_quill.fields import QuillField


# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    updated = models.DateTimeField(verbose_name='Дата обновления', auto_now_add=True)


    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text = QuillField(verbose_name='Текст новости')
    published = models.DateTimeField(verbose_name='Дата публикации', default=now)
    draft = models.BooleanField(verbose_name='Черновик', default=False)

    def __str__(self):
        return f"{self.title} от {self.published.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
