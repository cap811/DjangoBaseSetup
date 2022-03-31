from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    return render(request, 'articles/index.html', {
        'articles': Article.objects.all(),
    })

def detail(request, article_id):
    return render(request, 'articles/detail.html', {
        'article_id': article_id,
        'article': Article.objects.get(id=article_id),
    })


