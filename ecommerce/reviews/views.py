from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer, ReviewCreateSerializer, ReviewUpdateSerializer, HelpfulVoteSerializer

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product_id=product_id, is_approved=True)

class ReviewCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save()  # No user since authentication is removed

class ReviewUpdateView(generics.UpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Review.objects.all()

class ReviewDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Review.objects.all()

class HelpfulVoteView(generics.UpdateAPIView):
    serializer_class = HelpfulVoteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Review.objects.all()

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        review.helpful_votes += 1
        review.save()
        return Response({'helpful_votes': review.helpful_votes}, status=status.HTTP_200_OK)
