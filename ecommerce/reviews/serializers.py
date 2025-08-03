from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at', 'updated_at', 'helpful_votes', 'is_approved']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'helpful_votes', 'is_approved']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']

class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class HelpfulVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['helpful_votes']