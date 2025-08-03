from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product  # Assuming you have a Product model

User = get_user_model()

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    helpful_votes = models.PositiveIntegerField(default=0)
    is_approved = models.BooleanField(default=False)  # For moderation

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"Review by {username} for {self.product.name}"

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

    def mark_as_helpful(self):
        self.helpful_votes += 1
        self.save()
