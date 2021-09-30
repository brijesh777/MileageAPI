import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

import vechile
from .serializer import VechileSerializer, MileageSerializer
from .models import *


class VechileAPI(APIView):
    serializer_class = VechileSerializer

    def get_queryset(self):
        vechile_object = Vechile.objects.all()
        return vechile_object

    def get(self, request, *args, **kwargs):
        try:
            unit = request.query_params["unit"]
            if unit is not None:
                vechile_object = Vechile.objects.filter(unit=unit).first()
                serializer_class = VechileSerializer(vechile_object)
        except:
            vechile_object = self.get_queryset()
            serializer_class = VechileSerializer(vechile_object, many=True)
        return Response(serializer_class.data)

    def put(self, request, *args, **kwargs):
        unit = request.query_params["unit"]
        vechile_object = Vechile.objects.filter(unit=unit).first()

        data = request.data

        vechile_object.unit = data.get("unit", vechile_object.unit)
        vechile_object.mileage = data.get("mileage", vechile_object.mileage)
        vechile_object.manufacture = data.get("manufacture", vechile_object.manufacture)
        if data.get("status", vechile_object.status) == 'true':

            vechile_object.status = True
        else:
            vechile_object.status = False

        vechile_object.save()

        mileage_obj = vechile_Mileage.objects.create(
            day_mileage=int(vechile_object.mileage),
            unit=Vechile.objects.filter(unit=vechile_object.unit).first(),
            date=datetime.date.today())

        serializer_class = VechileSerializer(vechile_object)

        return Response(serializer_class.data)


class MileageAPI(APIView):
    serializer_class = MileageSerializer

    def get(self, request, *args, **kwargs):

            unit = kwargs.get('unit')
            date = kwargs.get('date')



            if unit and date is not None:

                mileage_object = vechile_Mileage.objects.filter(unit=unit, date=date).first()
                vechile_object = Vechile.objects.filter(unit=unit).first()

                distance = vechile_object.mileage - mileage_object.day_mileage


            return Response(distance)
