from rest_framework import serializers
from ..models import Cargo

class CargoSerializer(serializers.ModelSerializer):
    funcionarios_nesse_cargo = serializers.SerializerMethodField()
    
    def get_funcionarios_nesse_cargo(self, obj):
        return obj.funcionarios_com_esse_cargo
    
    class Meta:
        model = Cargo
        fields = '__all__'