from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    description = serializers.CharField()
    category = serializers.ChoiceField(
        choices=Product.ProductCategoryChoices,
    )

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
