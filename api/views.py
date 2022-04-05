from rest_framework.response import Response
from rest_framework.decorators import api_view
from article.models import Article
from .serializers import ArticleSerializer

# GET /api/articles/
@api_view(['GET'])
def getData(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

# POST /api/articles/
@api_view(['POST'])
def postData(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# PUT /api/articles/1/
@api_view(['PUT'])
def putData(request, pk):
    article = Article.objects.get(pk=pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    
# DELETE /api/articles/1/
@api_view(['DELETE'])
def deleteData(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return Response(status=204)

