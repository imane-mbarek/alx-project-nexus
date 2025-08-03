from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("all/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]
