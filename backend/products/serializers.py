from rest_framework import serializers
from products.models import CheongsamModel, TeasetModel

class CheongsamSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheongsamModel
        fields = '__all__'

class TeasetSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeasetModel
        fields = '__all__'
