from django.shortcuts import render
from rest_framework import generics
from .models import Computer, UserVerification, VPNStatus, VerificationTask
from .serializers import ComputerSerializer, UserVerificationSerializer, VPNStatusSerializer, VerificationTaskSerializer

# Create your views here.

class ComputerListView(generics.ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class UserVerificationListView(generics.ListAPIView):
    queryset = UserVerification.objects.all()
    serializer_class = UserVerificationSerializer

class VPNStatusListView(generics.ListAPIView):
    queryset = VPNStatus.objects.all()
    serializer_class = VPNStatusSerializer

class VerificationTaskListView(generics.ListAPIView):
    queryset = VerificationTask.objects.all()
    serializer_class = VerificationTaskSerializer
