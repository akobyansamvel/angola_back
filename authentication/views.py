from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @action(methods=['POST'], detail=False, url_path='login', permission_classes=[])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise ValidationError({'error': 'E-mail и пароль обязательны для входа'})

        user = authenticate(email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            response = Response({'accessToken': str(refresh.access_token)})
            response.set_cookie('refresh', str(refresh), httponly=True)
            return response
        else:
            raise AuthenticationFailed({'error': 'Неверный адрес электронной почты или пароль'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def get_user(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, url_path='logout', permission_classes=[IsAuthenticated])
    def logout(self, request):
        response = Response()
        response.delete_cookie('refresh')
        return response

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        if serializer.instance == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("Вы можете обновить только свой профиль")

    def perform_destroy(self, instance):
        if instance == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("Вы можете удалить только свой профиль")
