from django.urls import path
from ninja import NinjaAPI
from .APIs.AuthAPI import router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

api = NinjaAPI()
api.add_router("", router)

urlpatterns = [
    # Auth route Access and refresh token, login
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_view"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),
    path('', api.urls),
]