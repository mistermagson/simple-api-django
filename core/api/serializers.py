from rest_framework.serializers import ModelSerializer
from core.models import Shipment


class ShipmentSerializer(ModelSerializer):
    class Meta:
        model = Shipment
#        fields = ('id', 'tracking')
        fields = '__all__'
