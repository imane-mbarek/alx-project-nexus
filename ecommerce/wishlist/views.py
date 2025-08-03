from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Wishlist
from .serializers import WishlistSerializer, WishlistCreateSerializer
from cart.models import CartItem  # Import the Cart model from the cart app

class WishlistListView(generics.ListAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Return all wishlist items
        return Wishlist.objects.all()

class WishlistCreateView(generics.CreateAPIView):
    serializer_class = WishlistCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Allow anonymous users to add wishlist items without a user association
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

class WishlistDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Allow deletion of any wishlist item without user restriction
        return Wishlist.objects.all()

class MoveToCartView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Move the product from wishlist to cart without authentication
        wishlist_item = Wishlist.objects.filter(id=kwargs['pk']).first()

        if wishlist_item:
            # Check if the product is already in the cart
            if not CartItem.objects.filter(product=wishlist_item.product).exists():
                # Add the product to the cart without associating it with a user
                CartItem.objects.create(product=wishlist_item.product)
            
            # Remove the product from the wishlist
            wishlist_item.delete()
            return Response({'message': 'Product moved to cart'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Wishlist item not found'}, status=status.HTTP_404_NOT_FOUND)
