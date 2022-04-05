from django.shortcuts import render
from .models import Article

# Home page for articles.
def index(request):
    # Get all articles.
    return render(request, 'articles/index.html', {
        'articles': Article.objects.all(),
    })

# Detail page for an article.
def detail(request, article_id):
    # Get the article with the given id.
    return render(request, 'articles/detail.html', {
        'article_id': article_id,
        'article': Article.objects.get(id=article_id),
    })
