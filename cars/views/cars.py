from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cars.models.car_model import CarModel
from cars.serializers.cars import CarCreateSerilizer, CarListSerializer
import logging as log


class CarsViewSet(ModelViewSet):
    queryset = CarModel.objects.select_related('brand')

    serializer_class_map = {
        'create': CarCreateSerilizer,
        'list': CarListSerializer,
    }

    def get_serializer_class(self):
        """Return the class to use for the serializer based on the HTTP method and action."""
        log.info('[Test] Action : %s', self.action)
        return self.serializer_class_map.get(self.action, CarCreateSerilizer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        brand = instance.brand

        instance.delete()
        if not CarModel.objects.filter(brand=brand).exists():
            brand.delete()

        return Response(status=status.HTTP_200_OK)
