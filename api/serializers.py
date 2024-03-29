from rest_framework import serializers

from recipes.models import Ingredient


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('title', 'dimension')
