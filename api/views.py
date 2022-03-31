from rest_framework.response import Response
from rest_framework.decorators import api_view
from article.models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def getData(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
