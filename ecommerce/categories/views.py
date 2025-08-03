from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminUserOrReadOnly
from rest_framework import generics, permissions, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by("-created_at")
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  
