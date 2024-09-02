from rest_framework import serializers

from .models import EmailAccess

class EmailAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAccess
        fields = ['email','expiry_date']
