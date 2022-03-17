from django.db import models


class CarModel(models.Model):
    # Model name
    name = models.CharField(max_length=128)
    # Vehicle model origin ID
    origin_id = models.CharField(max_length=64)
    # Connected parent model
    brand = models.ForeignKey('Brand', null=False, on_delete=models.CASCADE, related_name='models')

    def __str__(self) -> str:
        # <CarModel: Civic>
        return self.name
