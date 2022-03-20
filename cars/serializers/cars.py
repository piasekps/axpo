from django.db.models import Avg
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from cars.exceptions import NotFoundError
from cars.integrations.nhtsa.client import NHTSAClient
from cars.models.brand import Brand
from cars.models.car_model import CarModel


class CarCreateSerilizer(serializers.ModelSerializer):
    make = serializers.CharField(write_only=True)
    model = serializers.CharField(write_only=True)

    class Meta:
        model = CarModel
        fields = ('make', 'model', 'id')
        read_only_fields = ('id', )

    def create(self, validated_data):
        # Get Data from external API
        client = NHTSAClient()
        car_models = client.get_models_by_name(validated_data['make'].upper())
        car_data = car_models[validated_data['model'].upper()]
        # Get car Brand or Create iif not exists
        brand, _ = Brand.objects.get_or_create(
            name=validated_data['make'],
            defaults={'origin_id': car_data['Make_ID'], 'source_name': client.name}
        )

        # Return car model or create new.
        car_model, _ = CarModel.objects.get_or_create(
            name=validated_data['model'],
            brand=brand,
            defaults={'origin_id': car_data['Model_ID']}
        )
        return car_model

    def validate(self, data):
        """Validate if model and car exist on external API."""
        validated_data = super().validate(data)

        client = NHTSAClient()
        try:
            # First validation check if Make exists
            car_models = client.get_models_by_name(validated_data['make'].upper())
        except NotFoundError:
            raise NotFound(f'Brand {validated_data["make"]} not found')

        if validated_data['model'].upper() not in car_models:
            # Second validation check for Car model
            raise NotFound(f'Can not find model {validated_data["model"]} for {validated_data["make"]}')

        return validated_data


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
