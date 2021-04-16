from celery import shared_task
from .models import News
import random
import string
from random_word import RandomWords

r = RandomWords()


@shared_task
def create_new_news():
    random_title = ' '.join([r.get_random_word() for _ in range(5)])
    random_content = ' '.join([r.get_random_word() for _ in range(70)])
    news = News.objects.create(title=random_title, content=random_content)
    return news.title