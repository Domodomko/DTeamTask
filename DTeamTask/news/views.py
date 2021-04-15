from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsSerializer
from .models import News


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsCreateView(generics.CreateAPIView):
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
