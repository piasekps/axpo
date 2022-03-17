from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cars.serializers.populars import PopularListSerialziers
from cars.models.car_model import CarModel


class PopularsViewSet(ModelViewSet):
    serializer_class = PopularListSerialziers
    queryset = CarModel.objects.all()
    ordering_fields = ('rates_number', )
    ordering = ('rates_number')
