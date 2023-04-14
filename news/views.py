from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from news.models import Article
from django.utils.timezone import now

class NewsListViews(ListView):
    model = Article
    paginate_by = 25

    queryset = model.objects\
        .filter(published__gte=now())\
        .filter(draft=False).all()


