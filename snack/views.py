from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Snack
from .serializers import SnackSerializer
from .permissions import OwnerOnly

class SnackListCreateView(ListCreateAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer
    permission_classes=[OwnerOnly]