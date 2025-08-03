from django.urls import path
from .views import WishlistListView, WishlistCreateView, WishlistDeleteView, MoveToCartView

urlpatterns = [
    path('', WishlistListView.as_view(), name='wishlist-list'),
    path('', WishlistCreateView.as_view(), name='wishlist-create'),
    path('<int:pk>/', WishlistDeleteView.as_view(), name='wishlist-delete'),
    path('<int:pk>/move-to-cart/', MoveToCartView.as_view(), name='wishlist-move-to-cart'),
]