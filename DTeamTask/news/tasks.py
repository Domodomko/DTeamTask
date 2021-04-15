from celery import shared_task
from .models import News
import random
import string


@shared_task
def create_new_news():
    random_title = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    random_content = ''.join([random.choice(string.ascii_letters) for _ in range(100)])
    news = News.objects.create(title=random_title, content=random_content)
    return news.title