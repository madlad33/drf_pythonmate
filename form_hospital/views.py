from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ShiftSerializer
from .models import Shift
# Create your views here.

class ShiftViewSet(viewsets.ModelViewSet):
    """Viewset for the respective user"""
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


    def get_queryset(self):
        """Return objects for the current aUthenticated users only!"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)


class ShiftAllViewSet(viewsets.ModelViewSet):
    """Viewset for displaying all the shifts"""
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    http_method_names = ['get',]

