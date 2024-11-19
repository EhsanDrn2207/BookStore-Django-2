from rest_framework import serializers
from books.models import Book, Comment, Publisher, Category

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

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
    publisher = PublisherSerializer()
    category = CategorySerializer()
    comment = CommentSerializer(many=True, read_only=True)  

    class Meta:
        model = Book
        fields = ['id', 'user', 'title', 'description', 'author', 'cost', 'cover', 'publisher', 'translator', 'category', 'created_datetime', 'modified_datetime', 'comment']
