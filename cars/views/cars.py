from rest_framework.viewsets import ModelViewSet

from cars.models.car_model import CarModel
from cars.serializers.cars import CarListSerializer
import logging as log


class CarsViewSet(ModelViewSet):
    queryset = CarModel.objects.select_related('brand')

    serializer_class_map = {
        'list': CarListSerializer,
    }
    def get_serializer_class(self):
        """Return the class to use for the serializer based on the HTTP method and action."""
        log.info('[Test] Action : %s', self.action)
        return self.serializer_class_map.get(self.action, CarListSerializer)
