from typing import Dict

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from cars.models.car_model import CarModel
from cars.models.punctation import Punctation


class PunctationCreateSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(write_only=True, min_value=1, max_value=5, required=True)
    car_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CarModel
        fields = ('car_id', 'rating', 'id')
        read_only_fields = ('id', )

    def create(self, validated_data: Dict):
        instance, _ = Punctation.objects.create(
            car_model=validated_data['car_id'],
            value=validated_data['rating']
        )

        return instance

    def validate_car_id(self, value):
        get_object_or_404(self.model, pk=value)
        return value