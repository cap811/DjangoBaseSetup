from rest_framework import serializers
from article.models import Article

# Article Serializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # Create a new article
        def create(self, validated_data):
            return Article.objects.create(**validated_data)
        # Update an article
        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance
        # Delete an article
        def delete(self, instance):
            instance.delete()
            return instance
