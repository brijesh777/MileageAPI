from django.urls import path
from .api import *


urlpatterns = [

    path('show', VechileAPI.as_view()),
    path('<int:unit>/<slug:date>', MileageAPI.as_view())
]
