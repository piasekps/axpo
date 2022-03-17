from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Punctation(models.Model):
    # Connected Parent Model class
    car_model = models.ForeignKey('CarModel', null=False, on_delete=models.CASCADE, related_name='scoring')

    value = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
