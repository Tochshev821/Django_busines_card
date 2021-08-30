from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=100, default='')
    anons = models.CharField('Анонс', max_length=200, default='')
    full_text = models.TextField('Текст статьи')
    date = models.DateTimeField('Время и дата публикации')

    def __str__(self):
        return f'Новость: {self.title}'
    class Meta:
        verbose_name='Новость'

        verbose_name_plural='Новости'