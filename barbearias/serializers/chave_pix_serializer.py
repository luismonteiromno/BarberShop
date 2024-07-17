from rest_framework import serializers

from ..models import ChavePix


class ChavePixSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ChavePix
        fields = '__all__'
