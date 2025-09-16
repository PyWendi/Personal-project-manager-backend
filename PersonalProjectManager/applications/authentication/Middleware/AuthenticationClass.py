from typing import Optional, Any

from django.http import HttpRequest
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class JWTAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        jwt_auth = JWTAuthentication()
        try:
            print("Inside jwtclass***************")
            print(token)
            validated_token = jwt_auth.get_validated_token(token)
            print("***************jwtclass***************")
            print(validated_token)
            user = jwt_auth.get_user(validated_token)
            return user
        except Exception:
            raise AuthenticationFailed("The token is invalid or expired")