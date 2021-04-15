import factory
from news.models import News
from faker import Faker

faker = Faker()


class NewsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = News

    title = faker.pystr(max_chars=100)
    content = faker.pystr(max_chars=1000)