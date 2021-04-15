from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from news.serializers import *
from rest_framework import status
from django.contrib.auth.models import User
from .factories import *

client = APIClient()


class NewsViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.factory_news = NewsFactory()
        self.string = 'ded umer'
        User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        client.login(username='temporary', password='temporary')

    def test_get_all_news(self):
        response = client.get(reverse('api_news_list'))
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_news(self):
        response = client.get(reverse('api_news_detail', kwargs={'pk': self.factory_news.id}))
        news = News.objects.get(id=self.factory_news.id)
        serializer = NewsSerializer(news)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_news(self):
        response = client.patch(reverse('api_news_detail', kwargs={'pk': self.factory_news.id}),
                                data={'title': self.string, }, format='json')
        news = News.objects.get(id=self.factory_news.id)
        self.assertEqual(self.string, news.title)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_news(self):
        response = client.post(reverse('api_news_create'), {'title': self.string, 'content': self.string}, format='json')
        self.assertEqual(2, News.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_news(self):
        response = client.delete(reverse('api_news_detail', kwargs={'pk': self.factory_news.id}))
        self.assertEqual(0, News.objects.count())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
