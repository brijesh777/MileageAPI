from rest_framework import serializers
from .models import *


class VechileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vechile
        fields = ['unit', 'mileage', 'manufacture', 'status']


class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model =vechile_Mileage
        fields = [ 'unit', 'day_mileage','date']