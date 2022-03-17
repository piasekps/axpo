from django.db.models import Avg
from rest_framework import serializers

from cars.models.car_model import CarModel


class CarListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        model = CarModel
        fields = ('id', 'model', 'brand', 'avg_rating')
        read_only_fields = fields

    def get_brand(self, obj):
        return obj.brand.name

    def get_model(self, obj):
        return obj.name

    def get_avg_rating(self, obj):
        return obj.scoring.aggregate(Avg('value'))['value__avg']
