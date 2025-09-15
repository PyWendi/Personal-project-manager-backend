from django.urls import path
from .APIs.api import api

urlpatterns = [
    path('', api.urls),
]