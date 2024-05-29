# passport/views.py
from rest_framework import viewsets
from .models import Passport
from .serializers import PassportSerializer

class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
