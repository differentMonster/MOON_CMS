from rest_framework import serializers
from products.models import CheongsamModels, TeasetModels

class CheongsamAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = CheongsamModels
        fields = '__all__'


class TeasetAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = TeasetModels
        fields = '__all__'
