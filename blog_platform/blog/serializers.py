from rest_framework import serializers
from .models import BlogPost, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = BlogPost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
