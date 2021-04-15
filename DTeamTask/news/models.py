from django.db import models


class News(models.Model):
    title = models.CharField('Title', max_length=100, default='')
    content = models.TextField('Content', max_length=1000, default='')
    publication_date = models.DateField('Publication Date', auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'