from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        session_key = self.request.session.session_key

        if not session_key:
            # Create a session key if it doesn't exist
            self.request.session.create()
            session_key = self.request.session.session_key

        if user.is_authenticated:
            return CartItem.objects.filter(user=user)
        else:
            # Return cart items for the current session
            return CartItem.objects.filter(session_key=session_key)

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        session_key = self.request.session.session_key

        if not session_key:
            # Create a session key if it doesn't exist
            self.request.session.create()
            session_key = self.request.session.session_key

        serializer.save(user=user, session_key=session_key)

    @action(detail=False, methods=['get'])
    def my_cart(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
