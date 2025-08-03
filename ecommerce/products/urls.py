from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductListCreateView, ProductDetailView, ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
