# passport/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Passport
from .serializers import PassportSerializer

@login_required
def passport_detail(request):
    passport = get_object_or_404(Passport, user=request.user)
    return render(request, 'passport/passport_detail.html', {'passport': passport})

@login_required
def passport_update(request):
    passport = get_object_or_404(Passport, user=request.user)
    if request.method == 'POST':
        form = PassportForm(request.POST, instance=passport)
        if form.is_valid():
            form.save()
            return redirect('passport_detail')
    else:
        form = PassportForm(instance=passport)
    return render(request, 'passport/passport_form.html', {'form': form})

class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Passport.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
