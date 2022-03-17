from django.db import models


class Brand(models.Model):
    # Vehicle brand name
    name = models.CharField(max_length=128, unique=True)
    # Vehicle origin ID
    origin_id = models.CharField(max_length=64)
    # From which integration entry comes
    source_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        # <Brand: Honda (nhtsa)>
        return f'{self.name} ({self.source_name})'
