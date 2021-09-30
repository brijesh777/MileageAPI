from django.urls import path
from .api import *
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('show', VechileAPI.as_view()),
    path('<int:unit>/<slug:date>', MileageAPI.as_view())
]
