from rest_framework import routers
from core.api.viewsets import ShipmentViewSet


router = routers.DefaultRouter()
router.register(r'shipment', ShipmentViewSet)
