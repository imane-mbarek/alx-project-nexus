from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from rest_framework.authtoken.models import Token
from .serializers import (
    RegisterSerializer, LoginSerializer, UserProfileSerializer, ResetPasswordSerializer
)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user  # Retrieve the authenticated user
        login(request, user)  # Log the user in
        token, created = Token.objects.get_or_create(user=user)  # Generate or retrieve token

        return Response({"token": token.key, "message": "Login successful"}, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(CustomUser, email=serializer.validated_data['email'])
        token = default_token_generator.make_token(user)
        reset_link = f"http://yourdomain.com/reset-password/{user.pk}/{token}/"
        send_mail(
            subject="Password Reset",
            message=f"Reset your password using the following link: {reset_link}",
            from_email="noreply@yourdomain.com",
            recipient_list=[user.email]
        )
        return Response({"message": "Password reset link sent"}, status=status.HTTP_200_OK)


