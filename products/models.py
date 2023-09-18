from django.db import models
from common.models import CommonModel


class Product(CommonModel):
    """Product Definiton"""

    ProductCategoryChoices = [
        ("Cosmetics", "cosmetic"),
        ("Clothes", "clothes"),
        ("Groceries", "grocery"),
        ("Others", "other"),
    ]

    name = models.CharField(max_length=280)
    description = models.CharField(
        max_length=350,
        null=True,
        blank=True,
    )

    category = models.CharField(
        max_length=20,
        choices=ProductCategoryChoices,
    )

    def __str__(self) -> str:
        return self.name
