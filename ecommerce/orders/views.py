from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer, OrderCancelSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user

    def get_queryset(self):
        # Return all orders for unauthenticated users or filter by user if authenticated
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.filter(user__isnull=True)

    def perform_create(self, serializer):
        # Save with user if authenticated, otherwise None
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Allow retrieving any order
        return Order.objects.all()

class OrderCancelView(generics.UpdateAPIView):
    serializer_class = OrderCancelSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Return orders for authenticated users or none for anonymous
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.none()

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.cancel():
            return Response({'status': 'Order cancelled'}, status=status.HTTP_200_OK)
        return Response({'error': 'Order cannot be cancelled'}, status=status.HTTP_400_BAD_REQUEST)
