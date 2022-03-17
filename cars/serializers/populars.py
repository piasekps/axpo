from rest_framework import serializers

from cars.models.car_model import CarModel


class PopularListSerialziers(serializers.ModelSerializer):
    make = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = CarModel
        fields = ('id', 'make', 'model', 'rates_number')
        read_only_fields = fields

    def get_make(self, obj) -> str:
        return obj.brand.name

    def get_model(self, obj) -> str:
        return obj.name

    def get_rates_number(self, obj) -> int:
        return obj.scoring.count()
