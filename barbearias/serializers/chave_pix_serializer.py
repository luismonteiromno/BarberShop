from rest_framework import serializers

from ..models import ChavePix


class ChavePixSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChavePix
        fields = '__all__'
