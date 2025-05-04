from rest_framework import serializers
from .models import Computer, UserVerification, VPNStatus, VerificationTask

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'

class UserVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVerification
        fields = '__all__'

class VPNStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPNStatus
        fields = '__all__'

class VerificationTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationTask
        fields = '__all__'
