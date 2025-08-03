from django.urls import path
from .views import PaymentCreateView, PaymentDetailView, PaymentListView

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment-list'),   
    path('', PaymentCreateView.as_view(), name='payment-create'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]