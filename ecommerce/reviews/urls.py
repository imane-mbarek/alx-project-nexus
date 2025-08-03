from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, HelpfulVoteView

urlpatterns = [
    path('product/<int:product_id>/', ReviewListView.as_view(), name='review-list'),
    path('', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('<int:pk>/helpful/', HelpfulVoteView.as_view(), name='review-helpful'),
]