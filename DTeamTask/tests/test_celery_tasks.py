from django.test import TestCase
from news.tasks import create_new_news
from news.models import News


class NewsCeleryTest(TestCase):

    def test_create_new_news_function(self):
        celery_news = create_new_news()
        news = News.objects.all().first()
        self.assertEquals(news.title, celery_news)