from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsSerializer
from .models import News
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.models import User


# API

class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsCreateAPIView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = {
            'title': request.data['title'],
            'content': request.data['content'],
            'author': request.user,
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            news = News.objects.create(**data)
            return Response(self.get_serializer(news).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Templates

class HomeView(TemplateView):
    template_name = 'home.html'


class NewsListView(ListView):
    queryset = News.objects.all()
    context_object_name = 'news_list'
    template_name = 'news/news_list.html'


class AuthorsListView(ListView):
    queryset = User.objects.all()
    context_object_name = 'authors'
    template_name = 'news/authors.html'