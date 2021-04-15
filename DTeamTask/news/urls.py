from django.urls import path
from . import views

urlpatterns = [
    # API
    path('api/news/', views.NewsListAPIView.as_view(), name='api_news_list'),
    path('api/news/<int:pk>', views.NewsDetailAPIView.as_view(), name='api_news_detail'),
    path('api/news_create/', views.NewsCreateAPIView.as_view(), name='api_news_create'),
    # Templates
    path('home/', views.HomeView.as_view(), name='home'),
    path('news/', views.NewsListView.as_view(), name='news_list')
]