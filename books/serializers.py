# serializers.py
from rest_framework import serializers
from .models import Book, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_datetime', 'recommend', 'is_active']

class BookSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    category = CategorySerializer()
    comment = CommentSerializer(many=True,)  

    class Meta:
        model = Book
        fields = ['id', 'user', 'title', 'description', 'author', 'cost', 'cover', 'publisher', 'translator', 'category', 'created_datetime', 'modified_datetime', 'comment']
